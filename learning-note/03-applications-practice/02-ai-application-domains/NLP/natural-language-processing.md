# 第一章 NLP概述
## 1.1 定义
NLP（Natural Language Processing），自然语言处理，是指计算机与人类自然语言进行交互

## 1.2 常见任务
### 1.2.1 文本分类
### 1.2.2 序列标注
序列标注是指对输入序列中的每个元素进行分类，例如将每个单词标注为名词、动词、形容词等。
BIO 标注：Begin, Inside, Outside
Begin: 开始一个实体
Inside: 继续一个实体
Outside: 不是实体
### 1.2.3 文本生成
### 1.2.4 信息抽取
### 1.2.5 文本转换

## 1.3 技术演进
### 1.3.1 规则系统阶段
人工编写语言规则
### 1.3.2 统计方法阶段
基于统计方法对大量文本数据进行概率建模
- n-gram 假设每个词只与前n-1个词相关 分词相关
- HMM(隐马尔可夫模型)
### 1.3.3 机器学习阶段
引入机器学习算法
特征工程是关键环节
### 1.3.4 深度学习阶段
- RNN(Recurrent Neural Network,循环神经网络)
- LSTM(Long Short-Term Memory,长短期记忆)
- GRU(Gated Recurrent Unit,门控循环神经网络)
- Transformer(注意力机制)

# 第二章 文本表示
## 2.1 概述
文本表示是将自然语言转化为计算机可以理解的数值形式，是NLP任务的基础步骤

传统词袋模型BoW(Bag of Words)忽略语序，将整个文本编码为一个向量
现代NLP逐渐引入更精细和表达能力更强的文本表示方法

## 2.2 分词
分词(Tokenization)将原始文本切分为若干具有独立语义的最小单元(token)
### 2.2.1 英文分词
- 词级分词(Word-level)
- 字符级分词(Character-level)
- 子词分词(Subword-level)

分词算法：BPE(Byte Pair Encoding) 

### 2.2.2 中文分词
- 字符级分词(Character-level)
- 词级分词(Word-level) 需要构建词典
- 子词分词(Subword-level) 无需人工词典

### 2.2.3 分词工具
- 基于词典：jieba、 HanLP
- 基于子词：Hugging Face Tokenizers、SentencePiece、tiktoken等

jieba分词
- 精确模式 cut lcut
- 全模式 列出所有可能的分词结果 cut_all=True
- 搜索引擎模式 对长词进一步切分
- 自定义词典 load_userdict('userdict.txt')
每一行一个词，词 词频 词性

## 2.3 词表示(Word Representation)
词表(Vocabulary)具有双向映射关系，将token映射为整数索引，将索数映射为token

### 2.3.1 词袋模型
1. 词袋模型(Bag of Words) 
一句话对应一个向量 只考虑词频，不考虑词的顺序和上下文
2. 序列编码(Sequence Encoding) 
一句话对应一个二维矩阵 

缺点：
- 维度灾难
- 没有语义相似性
- OOV (Out-of Vocabulary) 未登录词

一些词袋模型：
- TF-IDF 考虑词频和逆文档频率，对词进行加权，而不是单纯的0和1
- BM25 TF-IDF的改进版本
  

### 2.3.2 语义化词向量
为每个词生成一个具有语义的稠密向量

1. Word2Vec概述
基于**分布假设**，即一个词的含义由它周围的词决定。通过学习词与上下文之间的关系，自动为每个词生成一个语义化的向量表示。
强调每个词视为一个独立的、不可分割的最小单元
- CBOW(Continuous Bag of Words)
输入上下文，输出目标词，不关注语序
- Skip-gram(Skip Gram)
输入目标词，输出上下文

一些改进算法：
- fastText：缓解了OOV问题，更能捕捉到词的语义信息

缺点：这些向量是静态的，即一个词在任何语境下都对应同一个向量

2. Word2Vec原理
先独热编码，再输入到神经网络中
两层神经网络，两层线性变换，最后softmax计算损失函数，通过反向传播更新参数，优化模型。
取第一层的参数作为词向量表示。

3. 获取Word2Vec词向量
gensim 加载和训练词向量的工具

- 使用他人发布的词向量 https://github.com/Embedding/Chinese-Word-Vectors
```python
from gensim.models import KeyedVectors

model = KeyedVectors.load_word2vec_format('data/sgns.weibo.word')

print(model.vector_size) # 查看词向量维度
print(len(model.index_to_key)) # 查看词向量数量
print(model['你好']) # 查看词向量
print(model.similarity('北京', '上海')) # 查看词向量相似度
print(model.most_similar('北京', topn=10)) # 查看与北京最相似的10个词
print(model.most_similar(positive=['男人', '女孩'], negative=['男孩']))
```

- 自行训练
```python
from gensim.models import Word2Vec, KeyedVectors
import pandas as pd
import jieba

df = pd.read_csv('data/online_shopping_10_cats.csv').dropna()

sentences = [[token for token in jieba.lcut(sentence) if token.strip() != ''] for sentence in df['review']]
model = Word2Vec(
    sentences=sentences, # 文本列表
    vector_size=100, # 词向量维度
    window=5, # 窗口大小
    min_count=2, # 最小词频
    sg=1, # 1表示skip-gram模型，0表示cbow模型
    workers=4 # 并行线程数
)   

model.wv.save_word2vec_format('data/word2vec.model')
model = KeyedVectors.load_word2vec_format('data/word2vec.model')
```
4. Word2Vec词向量应用
训练好的词向量常用于初始化下游NLP任务的嵌入层

嵌入层的初始化
- 随机初始化
- 使用预训练的词向量初始化
```python
from torch import nn
from gensim.models import KeyedVectors
import torch
import jieba

wv = KeyedVectors.load_word2vec_format('data/word2vec.model')

id2token = ['<UNK>'] + wv.index_to_key
token2id = {token:i for i,token in enumerate(id2token)}

num_embeddings = len(id2token)
embedding_dim = wv.vector_size
embedding_matrix = torch.randn(num_embeddings, embedding_dim)
# unk被随机初始化，其他单词的embedding从wv中获取
for i,word in enumerate(id2token):
    if word in wv:
        embedding_matrix[i] = torch.tensor(wv[word])

embedding = nn.Embedding.from_pretrained(embedding_matrix)

text = '你好，我是张三'
tokens = jieba.lcut(text)
input_ids = [token2id[token] for token in tokens]
input_tensor = torch.tensor(input_ids)
embedding(input_tensor).shape
```

### 2.3.3 上下文相关词表示(Contextual Word Representation)
静态词向量语义固定，无法根据上下文变化而变化。
代表模型：
- ELMo 首次实现上下文相关的词嵌入。它使用双向LSTM读取整个句子，为每个词生成一个融合了其前后文信息的动态向量
- BERT 采用双向的Transformer编码器，通过掩码语言模型（MLM） 等任务进行预训练，能生成真正融合上下文的动态词向量
- GPT 则采用单向（从左到右）的Transformer解码器，专注于生成式任务

# 第三章 传统序列模型

## 3.1 RNN
### 3.1.1 概述
逐个读取句子中的每个词，在每一步中根据当前词和之前上下文信息，不断更新对句子的理解

### 3.1.2 基础结构

### 3.1.3 多层结构
每一层的输出序列作为下一层的输入，顶层RNN的输出作为最终的结果

### 3.1.4 双向结构
同时使用两层RNN，正向和反向，将正向和反向的输出结合起来，作为最终的结果。
通常是直接拼接，也可以求平均或求和

### 3.1.5 多层+双向结构

### 3.1.6 API
```python
nn.RNN(
    input_size=3,  # 输入维度
    hidden_size=4,  # 隐藏层维度
    num_layers=2,  # 隐藏层数
    nonlinearity='tanh', # 激活函数
    bias=True,  # 是否添加偏置项
    batch_first=True,  # 是否将批次维度放在第一个位置
    dropout=0.0,  # dropout概率
    bidirectional=True,  # 是否使用双向RNN
    device=None,  # 设备类型
    dtype=None,  # 数据类型
)
# inputs = (input, hx)
# input = (N, L, H)
# hx = (num_layers, N, H)
# outputs = (output, hn)
# output = (N, L, H)
# hn = (num_layers, N, H)

input = torch.randn(2, 4, 3)
output, hn = rnn(input)
print(output.shape) # (2, 4, 8)
print(hn.shape) # (4, 2, 4)
```

### 3.1.7 存在问题
尽管循环神经网络（RNN）在处理序列数据时具有天然优势，但它在实际应用中面临一个非常严重的问题：长期依赖建模困难。这指的是：在训练过程中，当序列的长度超过RNN的处理能力时，RNN会忘记之前的信息

根本原因：梯度消失或爆炸

RNN 在计算梯度时，由链式法则，出现大量连乘，导致早期的梯度非常容易消失或爆炸。

## 3.2 LSTM
### 3.2.1 概述
LSTM（Long Short-Term Memory）长短期记忆网络

### 3.2.2 基础结构
引入记忆单元(Memory Cell)

LSTM（长短期记忆网络）通过三个精心设计的“门”结构，配合**细胞状态**（\( C_t \)）和**隐藏状态**（\( h_t \)），来解决传统RNN的长期依赖问题。三个门协同工作，就像一个智能的“信息筛选与传递系统”。

以下是三个门的详细介绍、计算公式及核心作用：

1. **遗忘门**（Forget Gate）—— “选择性遗忘”
    遗忘门决定上一时刻的细胞状态 \( C_{t-1} \) 中有多少信息需要被丢弃。它通过查看当前输入 \( x_t \) 和上一时刻的隐藏状态 \( h_{t-1} \)，为每个维度输出一个 0~1 之间的数。

    - **计算公式**：\( f_t = \sigma(W_f \cdot [h_{t-1}, x_t] + b_f) \)
    - **核心作用**：控制长期记忆的保留程度。当 \( f_t \) 趋近于 0 时，表示“完全忘记”旧信息；趋近于 1 时，表示“完全保留”旧信息。


2. **输入门**（Input Gate）—— “选择性记忆”
    输入门决定当前时刻的输入 \( x_t \) 中哪些新信息需要被存入细胞状态。它由两部分组成：

    - **Sigmoid层（输入门层）**：决定哪些维度需要被更新（\( i_t \)）。
    - **Tanh层（候选细胞状态）**：创建一个新的候选值向量（\( \tilde{C}_t \)），表示当前步潜在的新信息。
    - **计算公式**：
    - \( i_t = \sigma(W_i \cdot [h_{t-1}, x_t] + b_i) \) （更新权重）
    - \( \tilde{C}_t = \tanh(W_C \cdot [h_{t-1}, x_t] + b_C) \) （候选信息）
    - **核心作用**：将“旧记忆”和“新候选”结合，更新细胞状态。

    > **细胞状态更新公式**：\( C_t = f_t \odot C_{t-1} + i_t \odot \tilde{C}_t \)
    > （其中 \( \odot \) 表示逐元素相乘，旧状态乘以遗忘门，加上新候选乘以输入门，完成状态更新。）



3. **输出门**（Output Gate）—— “选择性输出”
    输出门决定当前时刻的细胞状态 \( C_t \) 中有多少信息需要输出给隐藏状态 \( h_t \)，进而影响后续网络或最终预测结果。

    - **计算公式**：
    - \( o_t = \sigma(W_o \cdot [h_{t-1}, x_t] + b_o) \) （输出权重）
    - \( h_t = o_t \odot \tanh(C_t) \) （将细胞状态缩放至 -1~1 后，再按输出门筛选）
    - **核心作用**：控制对外暴露的记忆量。并不是所有内部记忆都适合当前输出，输出门根据当前任务需求，提取最相关的部分作为隐藏状态。
  
梯度传播变成多个f_t连乘的结果，遗忘门取值小于1，但通常较接近1，因为遗忘门倾向于“记得多，忘得少”。


### 3.2.3 多层结构

在多层LSTM中，每一层的输出隐藏状态作为下一层的输入，每一层维护独立的记忆单元

### 3.2.4 双向结构

每个时间步，LSTM都有正向和反向的输出，将正向和反向的输出结合起来，作为最终的结果。通常是直接拼接，也可以求平均或求和。

### 3.2.5 多层双向结构

### 3.2.6 API

proj_size：投影维度，用于将隐藏状态映射到指定维度。
```python
from torch

lstm = torch.nn.LSTM(input_size=3, hidden_size=4, num_layers=2)
output, (hn, cn) = lstm(input, (h0, c0))
```


### 3.2.7 存在问题

- 难以并行计算
    LSTM的时间步具有强依赖性，每个时间步的计算依赖于上一个时间步的输出，导致无法大规模并行加速
- 参数量大
    LSTM的参数量较大，需要训练的参数更多，导致训练时间更长，内存占用更大
- 长期依赖建模仍然有限
    虽然LSTM缓解了梯度消失问题，但并不能完全消除 

## 3.3 GRU
### 3.3.1 概述
GRU（Gated Recurrent Unit）门控循环神经网络，进一步简化了LSTM结构，降低计算成本。

### 3.3.2 基础结构
- 取消了LSTM中独立的记忆单元，只保留隐藏状态
- 通过**更新门**和**重置门**，控制信息流动


GRU（门控循环单元）的核心计算公式总结如下。设 \( x_t \) 为当前输入，\( h_{t-1} \) 为上一时刻隐藏状态，\( \odot \) 表示逐元素相乘，\( \sigma \) 为 Sigmoid 函数，\( \tanh \) 为双曲正切函数。

**1. 更新门（Update Gate）**
控制保留多少旧信息以及吸收多少新信息。
\[
z_t = \sigma(W_z x_t + U_z h_{t-1} + b_z)
\]

**2. 重置门（Reset Gate）**
控制忽略多少过去的历史信息。
\[
r_t = \sigma(W_r x_t + U_r h_{t-1} + b_r)
\]

**3. 候选隐藏状态（Candidate Hidden State）**
利用重置门对历史信息进行过滤后，结合当前输入生成新的候选值。
\[
\tilde{h}_t = \tanh(W_h x_t + U_h (r_t \odot h_{t-1}) + b_h)
\]

**4. 最终隐藏状态（Final Hidden State）**
通过更新门在旧状态与新候选状态之间进行线性插值（此处采用主流深度学习框架如 PyTorch 的惯例，\( z_t \) 越接近 1 代表更新越多）。
\[
h_t = (1 - z_t) \odot h_{t-1} + z_t \odot \tilde{h}_t
\]

---

**简要直观解读：**

- **重置门 \( r_t \)**：若为 0，则完全丢弃之前的隐藏状态，相当于从当前输入“重新开始”。
- **更新门 \( z_t \)**：若为 1，则几乎完全忽略旧状态，直接使用新候选状态；若为 0，则几乎完全保留旧状态，跳过当前输入。

> **注**：部分原始论文中更新门的插值形式可能写作 \( h_t = z_t \odot h_{t-1} + (1 - z_t) \odot \tilde{h}_t \)，这仅是 \( z_t \) 定义域取反的差异，数学本质完全等价，实际使用时以具体框架实现为准。


### 3.3.3 多层 双向

### 3.3.4 API

# 第四章 Seq2Seq 模型
## 4.1 概述
传统自然语言处理任务以**静态输出**为主，如文本分类、情感分析、命名实体识别、序列标注等
然而现实中许多应用需要**动态**生成新序列，如机器翻译、文本摘要、对话系统、问答系统等。

传统序列模型缺点：
输出与输入等长 对联式的输出 一个时间步一个隐藏状态输出 


## 4.2 基础结构
Seq2Seq 模型由一个编码器-解码器架构组成
- 编码器（Encoder）：负责提取输入序列语义信息，并将其压缩为一个固定长度的上下文向量(context vector)
- 解码器（Decoder）：基于该向量，逐步生成目标序列

### 4.2.1 编码器
编码器主要由一个循环神经网络(RNN/LSTM/GRU)构成
最后的隐藏状态作为上下文向量(context vector)，传递给解码器，作为指导后续序列生成

双向结构对编码器提升有限 因为编码器只取最后一个时间步的隐藏状态作为输出
但多层结构可以帮助编码器提取更深的语义特征  

### 4.2.2 解码器
解码器也主要由一个循环神经网络(RNN/LSTM/GRU)构成
在生成开始时，把**上下文向量**作为**初始隐藏状态**，**特殊起始标记**作为**第一个时间步输入**，用来预测第一个token
(Autoregressive Generation，**自回归生成**)随后，在每个时间步，模型根据前一刻的隐藏状态和当前时间步的输入，预测当前的输出
直到生成一个特殊结束标记，表示句子生成完成

两个特殊标记`<sos>`和`<eos>` 在训练时 就应该构建

## 4.3 模型训练和推理

### 4.3.1 训练
- 数据准备 目标序列 要标注起点和终点
- 前向传播 
  - 编码器 接收源语言序列 编码为上下文向量(context vector)
  - 解码器 推理使用自回归生成方式 训练使用 teacher forcing 方法 每个时间步输入不是上一个时间步输出，而是真实的前一个token
- 计算损失 每个时间步的输出 与 词表每一个词 对应 多分类任务 使用CrossEntropyLoss
- 反向传播 

### 4.3.2 推理
- 编码器 
- 解码器 
  - 自回归生成 
  - 词选择策略 
    - 贪心解码Greedy Decoding   每一步都选概率最高的        局部最优 生成不够多样
    - 束搜索Beam Search         每一步保留多个候选词序列    计算开销大

## 4.4 案例
collate_fn 整理函数 在构建数据集时使用
`from torch.nn.utils.rnn import pad_sequence` 用于pad填充
padding_idx=0 用于embedding 将索引 0 对应的向量永远输出为 0，并且在反向传播时，自动将该索引对应的梯度强制置为 0。
ignore_index 用于损失函数 指定一个目标值，该值在计算损失时会被忽略，不参与损失计算，因此不会对输入梯度产生贡献
NLTK 英文分词 提供评估指标

DataLoader 产出：
inputs(batch,L_cn) L_cn中文序列长度 每批都可能不一样 V_cn中文词表大小
targets(batch,L_en) L_en英文序列长度 V_en英文词表大小
编码器：
1. embedding : inputs(batch,L_cn)  -> (barch, L_cn, cn_embedding_dim)
2. GRU : (batch, L_cn, cn_embedding_dim) + h_0 -> output(batch, L_cn, hiddene) h_n(layers, batch, hiddene)
teacherforcing：
decoder_inputs(batch, L_en-1) 去掉尾部的 <eos>
decoder_targets(batch, L_en-1) 去掉头部的 <sos>
decoder_h0(layer, batch, hiddene)由编码器输出升维得到 layer是1
解码层：
训练：以上下文向量作为初始隐状态 教师强制输入正确输入
1. embedding:decoder_inputs(batch, L_en-1) -> (batch, L_en-1, en_embedding_dim)
2. GRU(batch,L_en-1,embedding_dim) + h0(layer,batch,hiddene) -> output(batch,L_en-1,hiddend) + hn(layer,batch,hiddend)
3. Linear(batch,L_en-1,hiddend) -> (batch, L_en-1, V_en)
预测：以上下文向量作为初始隐状态，自回归循环 起点 <sos>
1. Embedding(batch,1) -> (batch,1,en_embedding_dim)
2. GRU input(batch,1,embedding) + h0(layer,batch,hiddene) -> output(batch,1,hiddend) + hn(layer,batch,hiddend)
3. Linear (batch,1,hiddend) -> (batch, 1, V_en)
4. argmax(batch, 1, V_en) -> (batch,1) next_token_ids

## 4.5 存在问题
- 定长向量表示语义 容易导致信息在压缩过程中丢失
- 始终基于同一个上下文向量进行生成 缺乏动态感知 无法选择性关注输入序列的不同部分 

# 第五章 Attention机制
## 5.1 概述
生成目标序列每一步时，不再依赖于一个静态的上下文向量，而是根据当前解码状态，动态地从编码器各时间步选取最相关信息
## 5.2 工作原理
### 5.2.1 相关性计算
在目标序列生成的每一步，解码器都会计算**当前时间步的隐藏状态**与编码器**各个时间步输出**之间的相关性。这些相关性衡量了源句中每个位置对当前生成内容的重要程度，从而决定模型应将多少注意力分配给不同的源位置。
相关性的计算依赖于特定的函数，通常被称为**注意力评分函数**（attention scoring function）
### 5.2.2 注意力权重计算
所有源位置的注意力评分，经**Softmax**归一化为概率分布，作为注意力权重
### 5.2.3 上下文向量计算
对编码器每个时间步隐藏状态 与 注意力权重 **加权求和** ，得到动态上下文向量，表示当前时间步源句的关键信息
### 5.2.4 解码信息融合
上下文向量 与 解码器当前时间步隐藏状态 拼接，通过**线性变换和softmax**生成当前时间步 目标词的概率分布

## 5.3 注意力评分函数
### 5.3.1 点积评分（Dot）
编码器每个时间步 与 解码器当前时间步 隐藏状态 的 点积
两个向量方向越一致，点击就越大，相关性越强，给予注意力越多
> 要求 编码器隐藏状态 和 解码器隐藏状态 向量维度hidden_size相等
### 5.3.2 通用点积评分（General）
在点积评分的基础上，引入**可学习**的权重矩阵W，对编码器隐藏状态进行**线性变换**
增强了模型对编码器输出的适应能力，提升了注意力表达能力
### 5.3.3 拼接评分（Concat）
将编码器每个时间步隐藏状态和解码器隐藏状态**拼接为长向量**，经**线性变换**和**非线性激活**，最后再用一个**向量投影**(还是一个矩阵的线性变换)，得到最终打分值

## 5.4 实战案例

## 5.5 存在问题
- 计算过程无法并行 RNN时间步之间存在强依赖关系，必须顺序执行
- 长期依赖问题没有根除 对于长序列 仍然会有梯度消失和梯度爆炸

# 第六章 Transformer
## 6.1 模型结构
### 6.1.1 核心思想
注意力机制不仅是信息提取的工具，其本质是在每一个目标位置上，显式建模该位置与源序列**各位置之间的依赖关系**。

### 6.1.2 整体结构
Transformer 的编码器和解码器模块分别由多个结构相同的层堆叠而成。
通过层层堆叠，模型能够逐步提取更深层次的语义特征，从而增强对复杂语言现象的建模能力。
标准的 Transformer 模型通常包含 6 个编码器层和 6 个解码器层。

### 6.2.3 编码器
#### 6.2.3.1 概述
    Transformer 的编码器用于理解输入序列的语义信息，并生成每个 token 的上下文表示，为解码器生成目标序列提供基础。
    编码器由多个结构相同的**编码器层**（Encoder Layer）堆叠而成。
    每个 Encoder Layer 的主要任务都是对其输入序列进行上下文建模，使每个位置的表示都能融合来自整个序列的全局信息。
    每个 Encoder Layer 都包含两个子层（sublayer），分别是**自注意力子层**（Self-Attention Sublayer）和**前馈神经网络子层**（Feed-Forward Sublayer）。
#### 6.2.3.2 自注意力层
自注意力机制（Self-Attention）是 Transformer 编码器的核心结构之一，它的作用是在序列内部建立各位置之间的依赖关系，使模型能够为每个位置生成融合全局信息的表示。

计算过程：
$$
\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
$$
  
1. 生成Query、Key、Value向量
    自注意力机制的第一步，是将输入序列中的每个位置表示映射为三个不同的向量，分别是查询（Query）、键（Key）和值（Value）。

    这些向量的作用如下：
    Query：表示当前词的用于发起注意力匹配的向量；
    Key：表示序列中每个位置的内容标识，用于与 Query 进行匹配；
    Value：表示该位置携带的信息，用于加权汇总得到新的表示。

    自注意力的核心思想是：每个位置用自身的 Query 向量，与整个序列中所有位置的 Key 向量进行相关性计算，从而得到注意力权重，并据此对对应的 Value 向量加权汇总，形成新的表示。

    每个向量均由自己的可学习的权重矩阵与原始向量相乘得到，论文矩阵维度（512，64）

2. 计算位置相关性
    评分函数采用**向量点积**形式。由于在高维空间中，点积的数值可能过大，会影响 softmax 的稳定性，因此在实际计算中对结果进行了缩放。最终的评分函数为：
    $$
    score(i,j)=\frac{q_i \cdot k_j}{\sqrt{d_k}}
    $$
    其中$d_k$是 key 向量的维度，用于缩放点积的幅度。不缩放会影响softmax结果
    评分函数分数越大，表示第 i 个位置越应该关注第 j 个位置的信息。

3. 计算注意力权重
    在得到每个位置与所有位置之间的相关性评分(L, L)后，模型会使用 softmax 函数进行归一化(L, L)，确保每个位置对所有位置的关注程度之和为 1，从而形成一个有效的加权分布。

4. 加权求和
    最后，模型会根据注意力权重(L, L)对所有位置的 Value 向量(L, E)进行加权求和，得到每个位置融合全局信息后的新表示(L, E)。

多头自注意力机制：

Transformer 引入了多头注意力机制（Multi-Head Attention）。其核心思想是通过多组独立的 Query、Key、Value 投影，让不同注意力头分别专注于不同的语义关系，最后将各头的输出拼接后乘以权重矩阵维度变成nmodel。

1. 分别计算各头注意力
   单独一个头的qkv维度是 nmodel/nhead
2. 合并多头注意力
   按最后一个维度拼接，乘以权重矩阵 得到与输入维度一致的输出(为了进行残差连接)

> 原始论文使用八头注意力

#### 6.2.3.3 前馈神经网络层
前馈神经网络（Feed-Forward Network，简称 FFN）是 Transformer 编码器中每个子层的重要组成部分，紧接在多头注意力子层之后。它通过对每个位置的表示进行逐位置、非线性的特征变换，进一步提升模型对复杂语义的建模能力。

一个标准的 FFN 子层包含两个线性变换和一个非线性激活函数，中间通常使用 ReLU 激活。其计算公式如下：
$$
FFN(x) = Linear_2(ReLU(Linear_1(x))) = W_2 \cdot ReLU(W_1x + b_1) + b_2
$$

原始论文中 中间**放大维度**为初始维度的4倍(2048)
最终输出维度与输入维度保持一致(为了进行残差连接)

#### 6.2.3.4 残差连接和层归一化
在 Transformer 的每个编码器层中，每个子层，包括自注意力子层和前馈神经网络子层，其输出都要经过**残差连接**（Residual Connection）和**层归一化**（Layer Normalization）处理。
这两者是深层神经网络中常用的结构，用于缓解模型训练中的**梯度消失**、**收敛困难**等问题，对于 Transformer 能够堆叠多层至关重要。
1. 残差连接
    残差连接（Residual Connection，也称“跳跃连接”或“捷径连接”）最初在计算机视觉领域被提出，用于缓解深层神经网络中的梯度消失问题。其核心思想是：
    将子层的输入直接与其输出相加，形成一条跨越子层的“捷径”，其数学形式为：
    $$y = x + SubLayer(x)$$

2. 层归一化
    每个子层在残差连接之后都会进行**层归一化**（Layer Normalization，简称 LayerNorm）。
    它的主要作用是对输入序列中每个 token 的所有特征分布标准化（某个 token 的表示可能在不同维度上有较大数值差异）

> 批归一化 对一个批次内的所有样本的单个特征进行标准化处理 主要用于CNN，图像batch稳定
> 层归一化 对一个样本的所有特征进行标准化处理 主要用于NLP，契合每个token单独处理的自注意力机制

#### 6.2.3.5 位置编码
Transformer 引入了一个关键机制——**位置编码**（Positional Encoding）。该机制**为每个词引入一个表示其位置信息的向量，并将其与对应的词向量相加**，作为模型输入的一部分。这样一来，模型在处理每个词时，既能获取词义信息，也能感知其在句子中的位置乃至**相对位置**，从而具备对基本语序的理解能力。

原始论文使用**正弦-余弦位置编码**

### 6.2.4 解码器
Transformer 解码器的主要功能是：
根据编码器的输出，逐步生成目标序列中的每一个词。
其生成方式采用自回归机制（autoregressive）：每一步的输入由此前已生成的所有词组成，模型将输出一个与当前输入长度相同的序列表示。
我们只取最后一个位置的输出，作为当前步的预测结果。这一过程会不断重复，直到生成特殊的结束标记 `<eos>`，表示序列生成完成。

每个Decoder Layer都包含三个子层，分别是**Masked自注意力子层**、**编码器-解码器注意力子层**（Encoder-Decoder Attention）和**前馈神经网络子层**（Feed-Forward Network）。

#### 6.2.4.1 Masked自注意力子层
由于 Transformer 不具备像 RNN 那样的隐藏状态传递机制，无法在序列生成过程中保留上下文信息，因此在生成每一个词时，必须将此前已生成的所有词作为输入，通过自注意力机制重新建模上下文关系，以预测下一个词。

解码器在自注意力机制中引入了**遮盖机制**（Mask）。该机制会在计算注意力时，**阻止模型访问当前位置之后的词**，只允许它依赖自身及前文的信息。这样，即使在并行训练时，模型也只能像逐词生成一样“看见”它应该看到的内容，从而保持训练与推理阶段的一致性。

Mask 机制的实现非常简单：只需将注意力得分矩阵中当前位置对其后续位置的评分设置为 $-\infty$

#### 6.2.4.2 编码器-解码器注意力子层
该子层的主要作用是：建模当前解码位置与源语言序列中各位置之间的依赖关系，帮助模型在生成目标词时有效地参考输入内容，相当于Seq2Seq模型中的注意力机制。

编码器-解码器注意力的核心机制与前面讲过的自注意力机制完全一致，区别仅在于：
Query 来自解码器当前的输入表示，即当前生成状态；
Key 和 Value 来自编码器的输出表示，即整个源序列的上下文。

也就是说，当前生成位置使用自己的 Query，去“询问”编码器输出中的哪些位置最相关。注意力机制会根据 Query 与所有 Key 的相似度，为每个源位置分配一个权重，然后用这些权重对 Value 进行加权求和，得到当前生成词所需的上下文信息。

#### 6.2.4.3 小结
- Masked 自注意力子层：
负责建模目标序列内部的上下文关系。通过引入遮盖机制（Mask），限制训练时每个位置只能关注它前面的词，从而在结构上模拟逐词生成，防止信息泄露。

- 编码器-解码器注意力子层：
负责建模目标序列与源序列之间的依赖关系。该机制允许解码器根据当前生成状态动态聚焦源语言中的关键信息，实现跨序列的信息对齐。

- 前馈神经网络子层：
对每个位置的表示进行独立的非线性变换，增强模型的表达能力，与编码器中的结构一致。

为了确保训练稳定，每个子层之后都配有**残差连接**与**层归一化**（LayerNorm），与编码器的设计保持一致，便于模型堆叠和优化。

此外，解码器同样采用了**位置编码**来注入顺序信息；输出端则通过线性变换和Softmax层将隐藏表示映射为词表概率分布，从而逐步生成目标序列。

在输出阶段，解码器最后会通过一个**线性层+Softmax**将隐藏表示映射为**词表上的概率分布**，逐步生成完整的目标句子。

整体来看，Transformer 解码器通过合理设计的多层结构与注意力机制，既保持了训练效率，又满足了生成任务的因果约束，是现代自然语言生成模型的核心组件之一。

## 6.2 API使用
### 6.2.1 概述
PyTorch 提供了对 Transformer 的官方实现，该模块封装了完整的编码器-解码器结构，可直接应用于机器翻译、文本生成等典型的序列建模任务。

### 6.2.2 核心类
- nn.Transformer
封装了完整的 Transformer 架构，由**编码器和解码器**组成。作为顶层接口，适用于需要同时使用编码器和解码器的任务，如机器翻译。支持用户通过参数自定义层数、注意力头数、隐藏维度等模型结构。

- nn.TransformerEncoder
实现了 Transformer **编码器结构**，由多个编码器层堆叠而成，用于将输入序列编码为上下文相关的表示。

- nn.TransformerDncoder
实现了 Transformer **解码器结构**，由多个解码器层堆叠而成，用于基于编码结果逐步生成目标序列。

- nn.TransformerEncoderLayer
实现了**单个编码器层**结构，包含一个多头自注意力子层和一个前馈神经网络子层，两者均带有残差连接和 LayerNorm。

- nn.TransformerDecoderLayer
实现了**单个解码器层**结构，包含自注意力、编码器-解码器注意力、前馈子层，同样配有残差连接和 LayerNorm。

### 6.2.3 Transformer构造参数
```py
transformer = torch.nn.Transformer(
    d_model=512,                # 嵌入维度
    nhead=8,                    # 多头注意力头数
    num_encoder_layers=6,       # 编码器层数
    num_decoder_layers=6,       # 解码器层数
    dim_feedforward=2048,       # 前馈网络（FFN）的隐藏层维度
    dropout=0.1,                # 各子层（注意力、FFN）后的随机失活
    activation='relu',          # FFN 的激活函数，可选 'relu' 或 'gelu'
    custom_encoder=None,        # 自定义编码器（覆盖默认编码器）
    custom_decoder=None,        # 自定义解码器（覆盖默认解码器）
    layer_norm_eps=1e-05,       # LayerNorm 中的 epsilon，防止除零
    batch_first=False,          # 输入形状是否为 (batch, seq, feature)（若 False 则为 (seq, batch, feature)）
    norm_first=False,           # 是否在子层前先做 LayerNorm（Pre-Norm），若 False 则在子层后做（Post-Norm）
    bias=True,                  # 是否在线性层中使用偏置项
    device=None,                # 模型运行的设备（CPU/GPU）
    dtype=None                  # 模型参数的数据类型 默认torch.float
)
```

### 6.2.4 Transformer.forward
封装完整前向传播逻辑，编码器+解码器，训练时使用
```py
output = transformer(
    # 编码器输入序列（源语言嵌入），(batch, src_len，d_model)
    # embedding和position_encoding要自己做
    src=src_emb, 
    # 解码器输入序列（目标语言嵌入），(batch, tgt_len)  右移一位的目标序列                    
    tgt=tgt_emb,    
    # 源序列的填充掩码，标记 padding 位置（True 表示忽略），形状 (batch, src_len)                 
    src_key_padding_mask=src_pad_mask,  
    # 目标序列的填充掩码，标记 padding 位置（True 表示忽略），形状 (batch, tgt_len)
    # 用于左侧pad填充
    tgt_key_padding_mask=tgt_pad_mask,  
    # 目标序列的masked自注意力掩码，(tgt_len, tgt_len)
    tgt_mask=tgt_mask,               
    # 编码器输出（memory）的填充掩码，用于编解码器交叉注意力，通常与 src_key_padding_mask 相同
    memory_key_padding_mask=src_pad_mask  
)
```

### 6.2.5 Transformer.encoder
```py
transformer = nn.Transformer(
    d_model=512, 
    nhead=8,
    num_encoder_layers=6, 
    num_decoder_layers=6,
    batch_first=True
)

memory = transformer.encoder(
    src=src_emb,
    src_key_padding_mask=src_pad_mask
)
```

### 6.2.6 Transformer.dncoder
```py
from torch import nn

# 初始化 Transformer
transformer = nn.Transformer(
    d_model=512, nhead=8,
    num_encoder_layers=6, num_decoder_layers=6,
    batch_first=True
)

# 调用编码器
memory = transformer.encoder(
    src=src_emb,
    src_key_padding_mask=src_pad_mask
)

# 调用解码器（逐步生成）
output = transformer.decoder(
    tgt=tgt_emb,
    memory=memory,
    tgt_mask=tgt_mask,
    tgt_key_padding_mask=tgt_pad_mask,
    memory_key_padding_mask=src_pad_mask
)

```

# 第七章 预训练模型
## 7.1 概述
针对每个具体任务单独训练模型，依赖大量人工标注，语言知识难以复用。

所以出现 “预训练” + “微调” 范式

## 7.2 分类
- 解码器(Decoder-only)          GPT     2018.6      OpenAI
- 编码器(Encoder-only)          BERT    2018.10     Google
- 编解码器(Encoder-Decoder)     T5      2019.10     Google

## 7.3 主流模型
### 7.3.1 GPT
#### 7.3.1.1 模型结构
1. 输入嵌入层
   - Text Embedding
   - Position Embedding 
   位置编码使用可学习的位置嵌入，每个位置对应一个可训练的向量
   每个token最终表示词嵌入与位置嵌入的向量和 维度768

2. 解码器 
   12个相同的解码器层
   掩码多头自注意力层 12头
   前馈网络

3. 输出层
   根据任务不同，输出接入不同任务头
   - Text Prediction 文本预测
    用于下一个词的生成 输出是词表大小的概率分布
   - Task Classifier 任务分类器
    用于微调阶段，适配具体的下游任务

#### 7.3.1.2 预训练
    在无监督文本上进行自监督学习，根据已观察到的前文上下文，预测当前词位置应出现的词

#### 7.3.1.3 微调
    使用有监督数据对模型进一步训练，保留预训练语言建模能力，利用标注数据对模型进行端到端优化，实现知识迁移
  - 添加任务输出层 将GPT隐藏状态映射为下游任务标签类别
  - 统一输入格式设计 “起始符 + 任务特定文本 + 分隔符 + 任务特定文本 + 终止符”

### 7.3.2 BERT
#### 7.3.2.1 模型结构
BERT-base   12层    168维   12头    0.11B
BERT-large  24层    1024维  16头    0.13B
1. 输入表示层
   - Token Embedding 
   - Position Embedding
   - Segment Embedding 用于区分句子对中的两个句子，分别用一个可学习的向量表示
2. 编码器
3. 输出层
    根据下游任务不同接不同 任务输出头
      - Token-Level 命名实体识别
      - Sequence-Level 文本分类、句子对分类
#### 7.3.2.2 预训练
- 掩码语言模型 MLM 
     学习词级语义 随机遮盖15%token 0.8Mask 0.1随机词 0.1原词
- 下一句预测 NSP
     学习句子关系 判断第二句是否是第一句的真实后续句

在预训练时同时优化MLM和NSP，NSP根据CLS句首token计算损失，MLM根据Mask token计算损失

#### 7.3.2.3 微调
- 句子对
- 单句
- 问答 抽取式问答
- 序列标注

### 7.3.3 T5
1. 预训练
随机遮盖，以遮盖词作为目标序列
2. 微调
任务分类前缀+输入序列 用于多任务微调
目标序列

# 第八章 Hugging Face
Hugging Face Hub 托管和分享模型、数据集和应用
Librayies 预训练工具库 
- Datasets 加载和处理数据集
- Tokenizers 将文本转换位模型输入
- Transformers

## 8.1 预训练模型的加载和使用
### 8.1.1 模型加载
1. AutoModel类 用于自动下载和加载模型 只加载主干结构 没有输出层
```python
from transformers import AutoModel
# .cache/huggingface/hub/modelname/snapshots/xxx/config.json+模型参数文件
model = AutoModel.from_pretrained("")
```
2. AutoModelForXXX 类 自动添加适配任务的输出层
### 8.1.2 模型输入输出
看文档 或 forward方法