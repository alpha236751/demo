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

### 2.3.1 One-Hot编码
1. 词袋模型(Bag of Words) 
一句话对应一个向量
2. 序列编码(Sequence Encoding) 
一句话对应一个二维矩阵 

缺点：
- 维度灾难
- 没有语义相似性
- OOV

一些改进算法：
- TF-IDF 考虑词频和逆文档频率，对词进行加权，而不是单纯的0和1
  

### 2.3.2 语义化词向量
为每个词生成一个具有语义的稠密向量

1. Word2Vec概述
基于分布假设，即一个词的含义由它周围的词决定。通过学习词与上下文之间的关系，自动为每个词生成一个语义化的向量表示。
强调每个词视为一个独立的、不可分割的最小单元
- CBOW(Continuous Bag of Words)
输入上下文，输出目标词，不关注语序
- Skip-gram(Skip Gram)
输入目标词，输出上下文

一些改进算法：
- fastText：缓解了OOV问题，更能捕捉到词的语义信息

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
代表模型————ELMo(Embeddings from Language Models)

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

# 第五章 Seq2Seq 模型
## 5.1 概述
传统自然语言处理任务以静态输出为主，如文本分类、情感分析、命名实体识别、序列标注等
然而现实中许多应用需要动态生成新序列，如机器翻译、文本摘要、对话系统、问答系统等。


