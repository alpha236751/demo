## 一、先从整体上理解 RAG

RAG 的核心不是“向量数据库 + 大模型”，而是一套完整的**知识构建、证据检索、答案生成和持续评测优化系统**。

从整体上，可以把 RAG 分成四个部分：

```text
RAG
├── 1. 离线知识库构建
│   ├── 文档解析
│   ├── 数据清洗
│   ├── Chunk 切分
│   ├── Metadata
│   ├── Embedding
│   └── 向量数据库
│
├── 2. 在线检索问答
│   ├── Query 处理
│   ├── Query Rewrite
│   ├── Dense / Sparse Retrieval
│   ├── RRF
│   ├── Reranker
│   ├── Context 构造
│   └── LLM Generation
│
├── 3. 安全与结果控制
│   ├── Citation
│   ├── 拒答
│   ├── 权限过滤
│   └── 结构校验
│
└── 4. 评测与持续优化
    ├── Ground Truth
    ├── Recall@K
    ├── MRR
    ├── RAGAS
    ├── Bad Case
    └── Regression Test
```

面试时介绍一个 RAG 项目，也建议按照这四层来讲，而不是一个技术点一个技术点零散介绍。

一句话概括：

> RAG 首先把企业知识处理成可检索的数据，然后根据用户问题找到正确证据，再让大模型基于证据生成答案，最后通过评测和 Bad Case 持续优化整个链路。

---

## 二、第一部分：离线知识库怎么构建

这一部分解决的问题是：

> **怎么把 PDF、Word、指南、说明书等原始资料，变成可以被 RAG 正确检索的数据。**

整体链路：

```text
原始文档
   ↓
文档解析
   ↓
数据清洗
   ↓
结构识别
   ↓
Chunk
   ↓
Metadata
   ↓
Embedding
   ↓
Milvus
```

### 1. 文档解析

#### 面试题：扫描版 PDF 怎么处理？

扫描版 PDF 没有文本层，本质上是一张张图片，因此需要：

```text
扫描 PDF
 ↓
OCR / 文档视觉模型
 ↓
版面分析
 ↓
文本恢复
 ↓
章节结构恢复
```

#### 面试题：表格怎么处理？

不能把 Cell 单独拆出来。

例如：

| 药品  | 肾功能不全 | 肝功能不全 |
| --- | ----- | ----- |
| 药物A | 慎用    | 禁用    |

如果拆成：

```text
慎用
禁用
```

就失去了具体语义。

更合理的是保留成 Markdown，或者转换成：

```text
药物A：
肾功能不全患者慎用；
肝功能不全患者禁用。
```

---

### 2. 数据清洗

解析结束以后，一般还要清洗：

* 页眉页脚
* 页码
* 重复标题
* 多余换行
* 乱码
* OCR 错字
* 重复内容
* 目录内容

#### 面试题：为什么数据清洗这么重要？

因为 RAG 存在明显的“垃圾进，垃圾出”。

如果原始 Chunk 就是错的：

> Embedding 模型、Reranker 和 LLM 再好也没有办法恢复原文不存在的信息。

所以一个真实 RAG 项目，数据质量往往比换大模型更重要。

---

### 3. Chunk 切分

#### 面试题：为什么需要 Chunk？

因为完整文档通常太长，而且用户问题只对应其中一部分。

例如一本 100 页的指南：

```text
整本指南
 ↓
Chunk 1
Chunk 2
Chunk 3
...
Chunk 500
```

检索时只需要找到真正相关的几个 Chunk。

#### 面试题：Chunk 怎么切？

最简单的是固定长度：

```text
500 Token
Overlap 50 Token
```

但实际业务更推荐结构化切分：

```text
文档
 ↓
一级标题
 ↓
二级标题
 ↓
段落
 ↓
句子
 ↓
Chunk
```

优先保证：

> 一个 Chunk 尽量表达一个完整语义。

#### 面试题：Chunk 越小越好吗？

不是。

Chunk 太小：

* 上下文容易丢失
* 答案可能被拆开
* 一个完整规则可能跨多个 Chunk

Chunk 太大：

* 噪声增加
* Embedding 语义不集中
* Context Token 增加

所以需要通过评测确定。

#### 面试题：Chunk Size 怎么确定？

不能说：

> 我感觉 500 比较合适。

应该说：

> 我们会在固定测试集上，对 300、500、800 等不同 Chunk Size 做实验，然后比较 Recall@K、Context Precision 和最终回答效果，最终选择效果和性能比较均衡的配置。

---

### 4. Overlap

Overlap 是为了避免：

```text
Chunk 1：
肾功能不全患者使用该药时……

Chunk 2：
应根据 eGFR 调整剂量……
```

一句完整含义被从中间截断。

所以两个 Chunk 之间可以保留一部分重叠。

但 overlap 也不能太大，否则：

* 重复 Chunk 增多
* 检索结果重复
* Token 浪费

---

### 5. Metadata

除了正文，一般还会保存：

```json
{
  "chunk_id": "chunk_1001",
  "document_id": "doc_001",
  "title": "高血压临床指南",
  "chapter": "药物治疗",
  "version": "2025",
  "document_type": "guideline",
  "effective_date": "2025-01-01"
}
```

#### 面试题：Metadata 有什么作用？

一方面用于 Citation。

另一方面用于 Metadata Filter。

比如用户明确问：

> 2025 年高血压指南怎么规定？

就可以先：

```text
version = 2025
document_type = guideline
```

然后再做语义搜索。

这比在所有历史版本里直接做向量搜索更可靠。

---

### 6. Embedding

Embedding 的作用是：

```text
文本
 ↓
Embedding Model
 ↓
高维向量
```

例如：

```text
血压一直很高怎么办？
```

和：

```text
高血压患者治疗方案
```

关键词不同，但是语义相近。

Embedding 就是为了捕捉这种语义关系。

#### 面试题：Embedding 模型怎么选择？

主要看：

* 中文效果
* 业务领域效果
* 输入长度
* 向量维度
* 推理速度
* 部署资源
* 最终 Recall

不要只看排行榜。

最终还是：

> 用自己的评测集验证。

---

### 7. Milvus

Embedding 后的数据写入向量数据库。

典型结构：

```text
chunk_id
embedding
document_id
metadata
```

#### 面试题：为什么需要 Milvus？

因为数据量大以后，不可能让一个 Query 向量和所有向量逐个计算。

比如：

```text
100 万 Chunk
```

需要使用 ANN：

> Approximate Nearest Neighbor。

通过索引快速找到相似向量。

#### 面试题：HNSW 是什么？

可以简单理解：

> 把向量构建成多层图结构，查询时沿着图快速接近目标区域，而不是遍历所有向量。

常见参数：

```text
M
efConstruction
efSearch
```

通常：

```text
efSearch ↑
Recall ↑
Latency ↑
```

所以本质上还是效果与性能的平衡。

---

## 三、第二部分：用户提问以后，在线检索怎么跑

这一部分解决：

> **用户提出问题以后，系统怎么从几十万甚至几百万 Chunk 中找到真正有用的证据。**

整体流程：

```text
Query
 ↓
Query Processing
 ↓
实体归一化
 ↓
Query Rewrite
 ↓
Dense + Sparse
 ↓
RRF
 ↓
Candidate Top-N
 ↓
Reranker
 ↓
Top-K
 ↓
Context
 ↓
LLM
```

---

### 1. Query Processing

真实用户的问题可能是：

```text
这个呢？
老人可以吗？
二甲呢？
血压一直高咋办？
```

不能永远直接 Embedding。

因此前面经常需要做：

* 实体归一化
* Query Rewrite
* 多轮上下文补全
* 权限识别

---

### 2. 实体归一化

例如：

```text
二甲
二甲双胍
Metformin
盐酸二甲双胍
```

本质上可能指向一个药物实体。

统一之后：

```text
二甲
 ↓
盐酸二甲双胍
```

能够提升检索稳定性。

---

### 3. Query Rewrite

多轮对话：

```text
用户：
二甲双胍有哪些注意事项？

用户：
肾功能不全呢？
```

第二句话直接检索信息不足。

Rewrite 后：

```text
肾功能不全患者使用二甲双胍有哪些注意事项？
```

#### 面试题：Query Rewrite 会不会改错？

会。

所以一种比较稳妥的方案是：

```text
Original Query
      +
Rewrite Query
      ↓
分别召回
      ↓
Fusion
```

保留原 Query，避免 Rewrite 改变用户原始意图以后整个检索失败。

---

### 4. Dense Retrieval

Dense Retrieval 就是：

```text
Query
 ↓
Embedding
 ↓
Query Vector
 ↓
Milvus
 ↓
Top-N
```

优势：

> 擅长语义相关性。

比如：

```text
血压一直很高
```

也能找到：

```text
高血压治疗方案
```

---

### 5. Sparse Retrieval

Sparse Retrieval 更擅长：

* 专业术语
* 药品名称
* 数字
* ICD 编码
* 特定型号
* 专有名词

所以 Dense 和 Sparse 是互补的。

---

### 6. 为什么需要混合召回？

可以理解成：

```text
Dense
→ 解决“意思差不多”

Sparse
→ 解决“关键词必须准确”
```

所以：

```text
              Query
                │
       ┌────────┴────────┐
       │                 │
     Dense             Sparse
       │                 │
     Top-N             Top-N
       └────────┬────────┘
                ↓
               RRF
```

---

### 7. RRF

Dense 和 Sparse 的 Score 不能简单直接相加。

例如：

```text
Dense Score = 0.82
Sparse Score = 13.5
```

两个分数尺度完全不同。

所以可以使用 RRF，根据排名进行融合：

```text
RRF(d) = Σ 1 / (k + rank(d))
```

面试不一定要求推公式。

理解：

> 如果一个 Chunk 在 Dense 和 Sparse 两边排名都比较高，那么它融合后的排名也会比较高。

---

### 8. Candidate Top-N

召回阶段目标：

> 尽量别漏掉正确证据。

所以可以先取：

```text
Top-20
Top-30
Top-50
```

但这些不会全部给 LLM。

因为里面还会有很多“看起来相关，但实际上不是最佳答案”的 Chunk。

所以还需要 Reranker。

---

### 9. Reranker

Retriever 解决：

> **找没找到。**

Reranker 解决：

> **找到以后，谁最相关。**

例如 Retriever Top-30：

```text
1   普通相关
2   普通相关
...
18  正确证据
```

说明正确证据已经召回。

但是最终只给 LLM Top-5。

所以需要重新排序。

Cross-Encoder：

```text
Query + Chunk
      ↓
Reranker
      ↓
Relevance Score
```

最后得到：

```text
Top-5 Evidence
```

#### 为什么重排成本高，计算量大？
因为召回所用到的文档相似度向量是固定的，是已经计算好的，而重排会根据问题的不同对文档有不同的侧重点，不能一开始就算好，要重新计算。

---

### 10. 为什么排序问题会影响结果？

这是非常关键的一点。

例如正确证据：

```text
Retriever Top-30：
Rank 18
```

说明：

> Retriever 找到了。

但 Rerank 后：

```text
Rank 12
```

系统最终只取：

```text
Top-5
```

于是：

> LLM 根本看不到这条正确证据。

所以出现：

```text
找到了
≠
最终模型看到了
```

这就是 Ranking Problem。

一句话记：

> **Retrieval 负责有没有，Ranking 负责靠不靠前。**

---

### 11. Bi-Encoder 和 Cross-Encoder

Bi-Encoder：

```text
Query → Vector
Document → Vector
        ↓
Similarity
```

优点：

> 快。

适合百万级召回。

Cross-Encoder：

```text
Query + Document
       ↓
      Model
       ↓
Relevance Score
```

优点：

> 准。

缺点：

> 慢。

所以：

```text
Bi-Encoder → 召回
Cross-Encoder → 精排
```

---

### 12. Parent-Child Chunk

检索时需要：

> 小 Chunk，语义精准。

生成时需要：

> 大一些的上下文，信息完整。

所以可以：

```text
Child Chunk
 ↓
检索命中
 ↓
parent_id
 ↓
Parent Section
 ↓
提供给 LLM
```

可以记：

> **小块负责找得准，大块负责看得全。**

---

### 13. Context 构造

最终不是简单：

```text
Top-5 拼起来
```

而可以进一步：

```text
Top-K
 ↓
去重
 ↓
父章节补充
 ↓
排序
 ↓
控制 Token
 ↓
Context
```

这里如果做不好，同样会影响 LLM。

例如：

* 重复 Chunk 太多
* 多版本内容冲突
* 正确证据被截断
* Context 太长

都会影响答案。

---

### 14. LLM Generation

这时候 LLM 的任务不是：

> 自己回答问题。

而是：

```text
理解 Query
+
理解 Evidence
+
根据 Evidence 组织答案
```

因此 Prompt 一般明确：

```text
只能基于 Context 回答
证据不足必须拒答
不能自行补充事实
关键结论需要 Citation
```

---

### 15. Citation

Citation 最好不要完全让 LLM 自己生成。

每个 Chunk 本身已经有：

```text
chunk_id
document_id
document_name
chapter
version
```

给 LLM：

```text
[chunk_001]
内容......

[chunk_002]
内容......
```

然后要求它：

> 只能引用当前 Context 中存在的 Chunk。

生成之后再次校验：

```text
LLM Citation
 ↓
ID 是否存在
 ↓
是否属于本次 Top-K
 ↓
通过 / 拒绝
```

---

### 16. 拒答机制

如果 Retrieval 结果非常差：

```text
Top-K Score 很低
```

或者：

```text
没有足够 Evidence
```

就不能让模型硬答。

应该：

```text
证据不足
 ↓
拒答
```

例如：

> 当前知识库中没有检索到足够依据，暂时无法回答该问题。

这也是降低幻觉的重要机制。


---

## 四、第三部分：RAG 到底怎么评测和优化

这一部分是面试最容易被深挖的地方。

核心思路：

> **不要只看最后回答对不对，而是把整个 RAG 链路拆开评测。**

整体：

```text
Ground Truth
      ↓
Retrieval Evaluation
      ↓
Ranking Evaluation
      ↓
Generation Evaluation
      ↓
Bad Case
      ↓
针对性优化
      ↓
Regression Test
```

---

### 1. Ground Truth

Ground Truth：

> 人工提前标注的正确结果。

RAG 里面最重要的两个：

#### Ground Truth Answer

标准答案。

#### Ground Truth Evidence

标准答案对应的正确证据。

例如：

```text
Query：
肾功能不全患者使用二甲双胍有什么注意事项？

Ground Truth Answer：
标准答案……

Ground Truth Evidence：
chunk_1024
《二甲双胍说明书》
4.2 节
```

所以：

> Ground Truth Answer 用来判断“答案对不对”。

> Ground Truth Evidence 用来判断“证据找没找到”。

---

### 2. Recall@K

例如测试集：

```text
100 个 Query
```

其中 91 个 Query：

```text
Ground Truth Evidence
进入 Retriever Top-5
```

那么：

```text
Recall@5 = 91 / 100 = 0.91
```

简单记：

> **Recall 看正确证据漏没漏。**

---

### 3. Precision@K

例如 Top-5：

```text
相关
相关
无关
相关
无关
```

Precision 关注：

> 检索结果里面有多少真正有用。

所以：

```text
Recall
→ 找全

Precision
→ 找准
```

---

### 4. MRR

MRR 主要看：

> 第一个正确证据排名多靠前。

例如：

```text
Query A → Rank 1 → 1

Query B → Rank 2 → 1/2

Query C → Rank 4 → 1/4
```

最后求平均。

所以：

```text
Recall → 有没有

MRR → 排得靠不靠前
```

---

### 5. 为什么 Recall 很高，答案还是可能不好？

因为：

```text
Retriever Top-30
正确证据存在
```

只能说明：

> 找到了。

后面还可能：

```text
Reranker 排错
Context 构造错误
LLM 理解错误
LLM 幻觉
引用错误
```

所以不能单独用 Recall 评价整个 RAG。

---

### 6. RAGAS 常见四个指标

#### Context Recall

标准答案需要的信息：

> 有没有召回来。

#### Context Precision

召回出来的信息：

> 有没有大量噪声。

#### Faithfulness

LLM 的答案：

> 是否忠实于 Context。

#### Answer Relevancy

答案：

> 有没有真正回答用户的问题。

一句话记忆：

```text
Context Recall
→ 漏没漏

Context Precision
→ 乱不乱

Faithfulness
→ 瞎没瞎编

Answer Relevancy
→ 答没答到点上
```

---

### 7. Bad Case 怎么分类

建议统一按照链路分类：

```text
Bad Case
├── 数据问题
├── Chunk 问题
├── Query 问题
├── Retrieval 问题
├── Ranking 问题
└── Generation 问题
```

#### 数据问题

例如：

* PDF 解析错误
* OCR 错误
* 表格丢失
* 文档版本错误

#### Chunk 问题

例如：

* 答案跨 Chunk
* Chunk 太小
* Chunk 太大
* 标题丢失

#### Query 问题

例如：

* 用户使用简称
* Query 太短
* 多轮指代
* Rewrite 改错

#### Retrieval 问题

判断标准：

```text
Ground Truth Evidence
没有进入 Candidate Top-N
```

说明 Retriever 没找到。

#### Ranking 问题

判断：

```text
Retriever Top-30
有 Ground Truth Evidence

Reranker Top-5
没有
```

说明：

> 找到了，但是排序排错了。

#### Generation 问题

判断：

```text
Ground Truth Evidence
已经进入最终 Context

但是答案仍然错误
```

这时候重点看：

* Prompt
* LLM
* Context
* 上下文冲突
* 幻觉

---

### 8. 回答错误时怎么排查

这是很重要的一道面试题。

可以固定按照这个顺序：

```text
① 原始文档有没有答案？
          ↓
② 文档解析是否正确？
          ↓
③ 正确内容有没有被切进 Chunk？
          ↓
④ Query Rewrite 是否正确？
          ↓
⑤ Ground Truth Evidence 有没有进入 Top-N？
          ↓
⑥ Rerank 后有没有进入 Top-K？
          ↓
⑦ Context 是否完整？
          ↓
⑧ LLM 是否正确使用 Evidence？
          ↓
⑨ Citation 是否正确？
```

这个回答比：

> 我会继续调 Prompt。

要成熟很多。

---

### 9. 怎么优化 RAG

不要回答：

> 换更大的模型。

而应该根据问题在哪一层进行优化。

```text
数据层
→ 解析、清洗、版本

Chunk 层
→ Size、Overlap、语义切分、Parent-Child

Query 层
→ Rewrite、实体归一化、Expansion

Retrieval 层
→ Embedding、Hybrid Search、Metadata Filter

Ranking 层
→ RRF、Reranker、Top-K

Generation 层
→ Context、Prompt、LLM、Citation、拒答
```

核心：

> **先定位，再优化。**

---

### 10. 线上反馈怎么形成闭环

```text
用户点踩
 ↓
记录 Query
 ↓
保存 Retrieval Result
 ↓
保存 Rerank Result
 ↓
保存 Context
 ↓
保存 Answer
 ↓
人工分析
 ↓
Bad Case Dataset
 ↓
优化
 ↓
Regression Test
```

这样线上问题才能真正转化成系统优化数据。

---

## 五、面试时最终应该形成的一套回答逻辑

如果面试官问：

> 你们 RAG 是怎么做的？

不要一上来：

> 我们用了 Milvus、BGE-M3、BGE-Reranker……

更好的回答顺序是：

### 第一层：先说整体架构

> 我们整个 RAG 分成离线知识库建设和在线检索问答两部分，同时配套一套分层评测和 Bad Case 优化机制。

### 第二层：讲离线知识库

> 离线侧先对原始文档做解析和清洗，然后按照标题、章节、段落和表格结构进行语义切分，同时维护文档来源、章节、版本、权限等 Metadata。之后使用 Embedding 模型向量化，并写入 Milvus 建立索引。

### 第三层：讲在线检索

> 用户 Query 进来以后，我们先做实体归一化和 Query Rewrite，然后进行 Dense 和 Sparse 双路召回，通过 RRF 做结果融合，再使用 Reranker 对候选结果精排，最终选择 Top-K Evidence 构建 Context。

### 第四层：讲生成与安全

> LLM 被要求严格根据检索证据回答，同时返回 Citation。如果检索证据不足，就进入拒答流程，而不是让模型使用自身知识强行生成答案。

### 第五层：讲评测

> 评测方面我们会把检索和生成拆开。检索主要看 Recall@K、MRR，生成侧关注 Faithfulness、Answer Relevancy 和引用准确性。每个 Bad Case 会进一步定位到数据、Chunk、Query、Retrieval、Ranking 或 Generation 层，然后针对性优化。

最终整套 RAG 可以记成一条主线：

```text
文档
 ↓
解析
 ↓
清洗
 ↓
Chunk
 ↓
Metadata
 ↓
Embedding
 ↓
Milvus
 ↓
────────────────
 ↓
Query
 ↓
Rewrite
 ↓
Dense + Sparse
 ↓
RRF
 ↓
Top-N
 ↓
Reranker
 ↓
Top-K
 ↓
Context
 ↓
LLM
 ↓
Citation / Reject
 ↓
────────────────
 ↓
Ground Truth
 ↓
Recall / MRR / RAGAS
 ↓
Bad Case
 ↓
定位问题
 ↓
优化
```

面试时最重要的不是把每一个技术名词都背下来，而是始终知道：

> **当前这个问题属于 RAG 的哪一层。**

比如：

```text
答案压根没找到
→ Retrieval

找到了但是没进最终 Context
→ Ranking

证据已经给模型了但是回答还错
→ Generation

不同版本指南互相冲突
→ Metadata / Version

引用不存在
→ Citation Validation

Recall 很低
→ Query / Chunk / Embedding / Retrieval

Recall 很高但最终效果不好
→ Ranking / Context / Generation
```

真正成熟的 RAG 项目，核心不是“用了多少模型”，而是：

> **能够通过 Ground Truth 和分层评测，知道问题到底发生在哪一层，然后针对这一层做优化。**
