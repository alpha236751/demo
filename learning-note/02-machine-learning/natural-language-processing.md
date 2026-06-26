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


