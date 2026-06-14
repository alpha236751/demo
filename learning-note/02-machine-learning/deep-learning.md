# 第一章 深度学习概述
## 1.1 深度学习简介
深度学习作为机器学习的一个分支，专注于使用多层神经网络来建模和解决问题
## 1.2 深度学习特点
- 使用多层神经网络，能够自动提取数据的多层次特征。
- 适合处理非结构化数据，如图像、音频、文本等。
- 依赖大量数据和计算资源，训练时间较长。
- 模型复杂，通常被视为“黑箱”，解释性较差。

# 第二章 神经网络基础
## 2.1 神经网络的构成

- 人工神经网络（ANN）
- 神经网络（NN）


## 2.2 激活函数
### 2.2.1 激活函数作用
激活函数是连接感知机和神经网络的桥梁，在神经网络中起着至关重要的作用。

如果没有激活函数，整个神经网络就等效于单层线性变换，不论如何加深层数，总是存在与之等效的“无隐藏层的神经网络”。激活函数必须是**非线性**函数，也正是激活函数的存在为神经网络引入了非线性，使得神经网络能够学习和表示复杂的非线性关系。

### 2.2.2 阶跃函数 Binary step
$$
f(x) =
\begin{cases} 
0, & x < 0 \\
1, & x \geq 0
\end{cases}, \quad f'(x) = 0
$$

### 2.2.3 sigmoid函数
$$
f(x) = \frac{1}{1 + e^{-x}}
$$

$$
f'(x) = \frac{1}{1 + e^{-x}} \left( 1 - \frac{1}{1 + e^{-x}} \right) = f(x) \left( 1 - f(x) \right)
$$

Sigmoid（也叫 Logistic 函数）是平滑的、可微的，能将任意输入映射到区间(0,1)。常用于二分类的输出层。但因其涉及指数运算，计算量相对较高。

Sigmoid 的输入在[-6,6]之外时，其输出值变化很小，可能导致信息丢失。

Sigmoid 的输出并非以 0 为中心，其输出值均>0，导致后续层的输入始终为正，可能影响后续梯度更新方向。

Sigmoid 的导数范围为(0,0.25)，梯度较小。当输入在[-6,6]之外时，导数接近 0，此时网络参数的更新将会极其缓慢。使用 Sigmoid 作为激活函数，可能出现梯度消失（在逐层反向传播时，梯度会呈指数级衰减）。

### 2.2.4 Tanh函数
$$
f(x) = \frac{1 - e^{-2x}}{1 + e^{-2x}}
$$

$$
f'(x) = 1 - \left( \frac{1 - e^{-2x}}{1 + e^{-2x}} \right)^2 = 1 - f^2(x)
$$

Tanh（双曲正切）将输入映射到区间(-1,1)。其关于原点中心对称。常用在隐藏层。

输入在[-3,3]之外时，Tanh的输出值变化很小，此时其导数接近0。

Tanh的输出以0为中心，且其梯度相较于Sigmoid更大，收敛速度相对更快。但同样也存在梯度消失现象。

### 2.2.5 ReLU函数
$$
f(x) = \max(0, x) =
\begin{cases} 
0, & x \leq 0 \\
x, & x > 0 
\end{cases}
$$

$$
f'(x) =
\begin{cases} 
0, & x \leq 0 \\
1, & x > 0 
\end{cases}
$$

ReLU（Rectified Linear Unit，修正线性单元）会将小于 0 的输入转换为 0，大于等于 0 的输入则保持不变。ReLU 定义简单，计算量小。常用于隐藏层。

ReLU 作为激活函数不存在梯度消失。当输入小于 0 时，ReLU 的输出为 0，这意味着在神经网络中，ReLU 激活的节点只有部分是“活跃”的，这种稀疏性有助于减少计算量和提高模型的效率。

当神经元的输入持续为负数时，ReLU 的输出始终为 0。这意味着神经元可能永远不会被激活，从而导致“神经元死亡”问题。这会影响模型的学习能力，特别是如果大量的神经元都变成了“神经元死亡”。为解决此问题，可使用 Leaky ReLU 来代替 ReLU 作为激活函数。

$$
\text{Leaky ReLU}(x) = 
\begin{cases} 
\alpha x, & x \leq 0 \\
x, & x > 0 
\end{cases}
$$

其中 \(\alpha\) 是一个很小的常数（在负数区域引入一个小的斜率来解决“神经元死亡”问题）。

### 2.2.6 Softmax函数
$$
y_k = \frac{e^{x_k}}{\sum_{i=1}^n e^{x_i}}, \quad k = 1 \sim n
$$

$$
\frac{\partial y_k}{\partial x_i} = 
\begin{cases} 
y_k(1 - y_i), & k = i \\ 
-y_k y_i, & k \neq i 
\end{cases}
$$

Softmax 将一个任意的实数向量转换为一个概率分布，确保输出值的总和为 1，是二分类激活函数 Sigmoid 在多分类上的推广。Softmax 常用于多分类问题的输出层，用来表示类别的预测概率。

Softmax 会放大输入中较大的值，使得最大输入值对应的输出概率较大，其他较小的值会被压缩。即在类别之间起到了一定的区分作用。

### 2.2.7 其他激活函数
1. **Identity** 恒等函数
$$ f(x) = x, \quad f'(x) = 1 $$

2. **Leaky ReLU**
$$ f(x) = 
\begin{cases} 
\alpha x, & x \leq 0 \\ 
x, & x > 0 
\end{cases}, \quad f'(x) = 
\begin{cases} 
\alpha, & x \leq 0 \\ 
1, & x > 0 
\end{cases} $$

3. **PReLU**
$$ f(x) = 
\begin{cases} 
\alpha x, & x \leq 0 \\ 
x, & x > 0 
\end{cases}, \quad f'(x) = 
\begin{cases} 
\alpha, & x \leq 0 \\ 
1, & x > 0 
\end{cases} $$
这里 \(\alpha\) 是一个可训练的参数，而非固定的常数。

4. **RReLU**
$$ f(x) = 
\begin{cases} 
\alpha x, & x \leq 0 \\ 
x, & x > 0 
\end{cases}, \quad f'(x) = 
\begin{cases} 
\alpha, & x \leq 0 \\ 
1, & x > 0 
\end{cases} $$
这里 \(\alpha\) 是一个在训练时从一个均匀分布中随机选择的参数

5. **ELU**
$$ f(x) = 
\begin{cases} 
a(e^x - 1), & x \leq 0 \\
x, & x > 0
\end{cases}, \quad f'(x) = 
\begin{cases} 
ae^x, & x \leq 0 \\
1, & x > 0
\end{cases} $$

6. **Swish** (SiLU)
$$ f(x) = \frac{x}{1 + e^{-x}}, \quad f'(x) = \frac{1 + e^{-x} + xe^{-x}}{(1 + e^{-x})^2} $$

7. **Softplus**
$$ f(x) = \ln(1 + e^x), \quad f'(x) = \frac{1}{1 + e^{-x}} $$

### 2.2.8 激活函数的选择
1）隐藏层

- 首选 ReLU，如果效果不好可尝试 Leaky ReLU 等。
- Sigmoid 在隐藏层易导致梯度消失，应尽量避免。
- Tanh 的输出均值为 0，对中心化数据更友好，但仍可能引发梯度消失，仅适用于浅层网络。

2）输出层

- 二分类选择 Sigmoid。
- 多分类选择 Softmax。
- 回归默认选择 Identity。

## 2.3 简单神经网络
```python
# 初始化神经网络
def init_network():
    network = {}
    network['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    network['b1'] = np.array([0.1, 0.2, 0.3])
    network['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    network['b2'] = np.array([0.1, 0.2])
    network['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    network['b3'] = np.array([0.1, 0.2])
    
    return network
# 前向传播
def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)
    
    return y

# 测试
network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)
```

# 第三章 神经网络的学习
## 3.1 损失函数
### 3.1.1 常见损失函数
1. 均方误差MSE (mean squared error)
   $$ L = \frac{1}{n} \sum_{i=1}^n (y_i - t_i)^2 $$
2. 交叉熵损失函数CEE (cross entropy error)
   $$ L = -\frac{1}{n} \sum_{i=1}^n t_i \log y_i $$
   其中，log 表示自然对数，\( y_i \) 表示神经网络的输出，\( t_i \) 表示正确解标签；而且，\( t_i \) 中只有正确解标签对应的值为 1，其它均为 0（one-hot 表示）。

### 3.1.2 分类任务损失函数
1. 二分类BCE
    二分类任务常用二元交叉熵损失函数（Binary Cross-Entropy Loss）。
    $$ L = -\frac{1}{n} \sum_{i=1}^n (y_i \log \hat{y}_i + (1 - y_i) \log (1 - \hat{y}_i)) $$
    其中：
    - \( y_i \) 为真实值（通常为 0 或 1）
    - \( \hat{y}_i \) 为预测值（表示样本 \( i \) 为 1 的概率）
2. 多分类CCE
    多分类任务常用多类交叉熵损失函数（Categorical Cross-Entropy Loss）。它是对每个类别的预测概率与真实标签之间差异的加权平均。

    \[ L = -\frac{1}{n} \sum_{i=1}^n \sum_{c=1}^c y_{i,c} \log \hat{y}_{i,c} \]

    其中：

    - C 是类别数
    - \( y_{i,c} \) 为真实值（表示 \( y_i \) 是否为类别 c，通常为 0 或 1）
    - \( \hat{y}_{i,c} \) 为预测值（表示样本 i 为类别 c 的概率）

### 3.1.3 回归任务损失函数
1. MAE
2. MSE
3. Smooth L1
    $$ \text{Smooth L1} = 
    \begin{cases} 
    \frac{1}{2}(y_i - \hat{y}_i)^2, & |y_i - \hat{y}_i| < 1 \\ 
    |y_i - \hat{y}_i| - \frac{1}{2}, & |y_i - \hat{y}_i| \geq 1 
    \end{cases} $$

## 3.2 数值微分
### 3.2.1 导数和数值微分
$$ f'(x) = \frac{df(x)}{dx} = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h} $$
在这里，我们以 \( x \) 为中心，计算它两边各发生微小变化后的差分，可以避免只计算单向增大时的误差。这种方法称为 **中心差分**。

另外，取微小值 \( h \) 时不能太小，这会导致计算机浮点数表示的精度不够，出现舍入误差。

### 3.2.2 偏导数
### 3.2.3 梯度

## 3.3 神经网络梯度计算
$$ W = 
\begin{pmatrix}
W_{11} & W_{12} & W_{13} \\
W_{21} & W_{22} & W_{23}
\end{pmatrix} $$

$$ \frac{\partial L}{\partial W} = 
\begin{pmatrix}
\frac{\partial L}{\partial W_{11}} & \frac{\partial L}{\partial W_{12}} & \frac{\partial L}{\partial W_{13}} \\
\frac{\partial L}{\partial W_{21}} & \frac{\partial L}{\partial W_{22}} & \frac{\partial L}{\partial W_{23}}
\end{pmatrix} $$

**数值微分计算梯度**
```python
import numpy as np

def softmax(x):
    if x.ndim == 2:
        x = x - np.max(x, axis=1, keepdims=True) # 溢出对策 保持维度不变
        return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True) 
    x = x - np.max(x) # 溢出对策
    return np.exp(x) / np.sum(np.exp(x))

def cross_entropy_error(y, t):
    if y.ndim ==1 :
        y = y.reshape(1, -1)
        t = t.reshape(1, -1)

    # 如果t是one-hot向量，则转换为正确标签的索引
    if t.size == y.size:
        t = t.argmax(axis=1)
    n = y.shape[0]
    return -np.sum(np.log(y[np.arange(n), t] + 1e-7)) / n   

def _numerical_gradient(f, x):
    h = 1e-4  # 0.0001
    grad = np.zeros_like(x)
    # 遍历x的每一个维度(特征)
    for i in range(x.size):
        tmp_val = x[i]
        x[i] = tmp_val + h 
        fxh1 = f(x)  # f(x + h)
        x[i] = tmp_val - h
        fxh2 = f(x)  # f(x - h)

        grad[i] = (fxh1 - fxh2) / (2 * h)

        x[i] = tmp_val  # 值复原

    return grad 
def numerical_gradient(f, X):
    if X.ndim == 1:  # 如果X是一维向量
        return _numerical_gradient(f, X)
    else:
        grad = np.zeros_like(X)
        for i, x in enumerate(X): # i是索引，x是X中的每一条数据 
            grad[i] = _numerical_gradient(f, x)
        return grad
    
class simpleNet:
    def __init__(self):
        self.W = np.random.rand(2, 3)  # 权重初始化
    def forward(self, x):
        return np.dot(x, self.W)  # 前向传播
    def loss(self, x, t):
        z = self.forward(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)
        return loss

if __name__ == '__main__':
    x = np.array([0.6, 0.9])
    t = np.array([0, 0, 1])  # 正确标签

    net = simpleNet()
    
    f = lambda w: net.loss(x,t)
    gradw = numerical_gradient(f, net.W)

    print(gradw)
```
## 3.4 随机梯度下降法SGD
### 3.4.1 梯度下降法
求函数最小值代码
```python
import numpy as np
import matplotlib.pyplot as plt

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)
    for i in range(x.size):
        tmp_val = x[i]
        x[i] = tmp_val + h
        fxh1 = f(x)
        x[i] = tmp_val - h
        fxh2 = f(x)
        grad[i] = (fxh1 - fxh2)/(2*h)
        x[i] = tmp_val
    return grad
def gradient_descent(f, x, lr=0.1, num_iter=100):
    x_history = []

    for i in range(num_iter):
        x_history.append(x.copy())
        grad = numerical_gradient(f, x)
        x -= lr * grad
    return np.array(x_history)

def f(x):
    return x[0]**2 + x[1]**2

x_init = np.array([-3.0, 4.0])
x_history = gradient_descent(f, x_init)
print(x_history[-1]) # 最终解
plt.plot(x_history[:, 0], x_history[:, 1], '-or')
plt.show()
```

### 3.4.2 模型训练相关概念
1. Epoch （轮数，时代、纪元）
   模型遍历完整个数据集的过程
2. Batch （批次）
   每次训练时输入的样本数量
3. Iteration （迭代）
   完成一个Batch的训练过程

### 3.4.3 SGD
随机梯度下降法SGD(Stochastic Gradient Descent)，在神经网络中指每次从训练数据中随机选择一个小批量数据，然后用梯度下降法迭代多个轮次。
具体过程如下：
1. 随机选择一个小批量数据
2. 计算梯度
3. 更新权重
4. 重复迭代

## 3.5 手写数字识别 微分计算梯度实现
计算量很大，所需训练时间较长。
此代码中的超参数并不是最优的，运行时没有让模型训练到最优解。

```python
import numpy as np
def softmax(x):
    x -= np.max(x, axis=1, keepdims=True)
    return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
def cross_entropy_error(y, t):
    if t.ndim == y.ndim and t.shape[1] == y.shape[1]:  # 判断是否为 one‑hot
        t = t.argmax(axis=1)
    n = y.shape[0]
    return -np.sum(np.log(y[np.arange(n), t] + 1e-7)) / n  
def numerical_gradient(f, X):
    h = 1e-4
    if X.ndim == 1:
        grad = np.zeros_like(X)
        for i in range(X.size):
            tmp_val = X[i]
            X[i] = tmp_val + h
            fxh1 = f(X)
            X[i] = tmp_val - h
            fxh2 = f(X)
            grad[i] = (fxh1 - fxh2)/(2*h)
            X[i] = tmp_val
    else:
        grad = np.zeros_like(X)
        for i, x in enumerate(X):
            for j in range(x.size):     
                tmp_val = x[j]
                x[j] = tmp_val + h
                fxh1 = f(X)
                x[j] = tmp_val - h
                fxh2 = f(X)
                grad[i][j] = (fxh1 - fxh2)/(2*h)
                x[j] = tmp_val
    return grad

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init_std=0.01):
        self.params = {}
        self.params['w1'] = np.random.randn(input_size, hidden_size) * weight_init_std
        self.params['b1'] = np.zeros(hidden_size)
        self.params['w2'] = np.random.randn(hidden_size, output_size) * weight_init_std
        self.params['b2'] = np.zeros(output_size)
    def forward(self, X):
        W1,W2 = self.params['w1'], self.params['w2']
        b1,b2 = self.params['b1'], self.params['b2']
        a1 = X @ W1 + b1
        z1 = sigmoid(a1)
        a2 = z1 @ W2 + b2
        y = softmax(a2)
        return y
    def loss(self, X, t):
        y = self.forward(X)
        return cross_entropy_error(y, t)
    def accuracy(self, X, t):
        y = self.forward(X)
        y = np.argmax(y, axis=1)
        return np.mean(y == t)
    def gradient(self, X, t):
        loss_f = lambda w: self.loss(X, t)
        grad = {}
        grad['w1'] = numerical_gradient(loss_f, self.params['w1'])
        grad['b1'] = numerical_gradient(loss_f, self.params['b1'])
        grad['w2'] = numerical_gradient(loss_f, self.params['w2'])
        grad['b2'] = numerical_gradient(loss_f, self.params['b2'])
        return grad

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
dataset = datasets.load_digits()
X_train, X_test, y_train, y_test = train_test_split(dataset.data, dataset.target, test_size=0.2, random_state=42)
scaler = MinMaxScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

network = TwoLayerNet(64, 20, 10)

learning_rate = 0.2
batch_size = 100
num_epochs = 20
train_size = X_train.shape[0]
iter_per_epoch = np.ceil(train_size / batch_size) # ceil 向上取整
iters = int(iter_per_epoch * num_epochs)

train_loss_list = []
train_acc_list = []
test_acc_list = []

for i in range(iters):
    batch_mask = np.random.choice(train_size, batch_size)
    X_batch = X_train[batch_mask]
    y_batch = y_train[batch_mask]
    grad = network.gradient(X_batch, y_batch)
    for key in grad:
        network.params[key] -= learning_rate * grad[key]
    if i % iter_per_epoch == 0:
        loss = network.loss(X_train, y_train)
        train_loss_list.append(loss)
        train_acc = network.accuracy(X_train, y_train)
        train_acc_list.append(train_acc)
        test_acc = network.accuracy(X_test, y_test)
        test_acc_list.append(test_acc)

import matplotlib.pyplot as plt
fig, ax = plt.subplots(1,2 , figsize=(12, 4))
x = np.arange(len(train_acc_list))
ax[0].plot(x, train_acc_list, label='train acc')
ax[0].plot(x, test_acc_list, label='test acc')
ax[0].set_xlabel('epoch')
ax[0].set_ylabel('accuracy')
ax[0].legend()
b = np.arange(len(train_loss_list))
ax[1].plot(b, train_loss_list, label='train loss')
ax[1].set_xlabel('epoch')
ax[1].set_ylabel('loss')
ax[1].legend()
plt.show()
```

# 第四章 反向传播算法 BP算法 (Back propagation)
## 4.1 计算图
## 4.2 链式法则
## 4.3 反向传播
### 4.3.1 加法节点
保持上游不变
### 4.3.2 乘法节点
将上游的值乘以输入的翻转

## 4.4 激活层的反向传播和实现
### 4.4.1 ReLU

ReLU（Rectified Linear Unit）函数的定义为：

$$
f(x) = \max(0, x) =
\begin{cases} 
0, & x \leq 0 \\
x, & x > 0 
\end{cases}
$$

其导数为：

$$
f'(x) =
\begin{cases} 
0, & x \leq 0 \\
1, & x > 0 
\end{cases}
$$
```python
# ReLU层
class ReLU:
    def __init__(self):
        self.mask = None
    def forward(self, X):
        self.mask = (X <= 0)
        y = X.copy()
        y[self.mask] = 0
        return y
    def backward(self, dout):
        dx = dout.copy()
        dx[self.mask] = 0
        return dx
```

### 4.4.2 Sigmoid   

Sigmoid 函数定义为：

$$
f(x) = \frac{1}{1 + e^{-x}}
$$

其导数推导过程如下：

$$
f'(x) = -\left(\frac{1}{1 + e^{-x}}\right)^2 \cdot e^{-x} \cdot (-1) = \frac{e^{-x}}{(1 + e^{-x})^2}
$$

进一步化简为：

$$
f'(x) = \frac{1}{1 + e^{-x}} \left(1 - \frac{1}{1 + e^{-x}}\right)
$$

即：

$$
f'(x) = f(x) \bigl(1 - f(x)\bigr)
$$
```python
# Sigmoid层
class Sigmoid:
    def __init__(self):
        self.y = None
    def forward(self, X):
        y = 1 / (1 + np.exp(-X))
        self.y = y
        return y
    def backward(self, dout):
        return dout * self.y * (1.0 - self.y) 
```

## 4.5 Affine层 (仿射层，全连接层)
全连接层(Fully Connected Layer， Dense Layer)
仿射变换(Affine Transformation)

考虑 \( N \) 个数据一起进行正向传播的情况，写成矩阵计算形式：

$$
Y = XW + B
$$

 \( X \) 是 \( N \times m \) 的矩阵，\( m \) 就是 Affine 层输入神经元的个数
 \( W \) 是 \( m \times n \) 的权重矩阵，\( n \) 就是 Affine 层输出神经元的个数。

根据矩阵求导的运算法则，可以得到损失函数 \( L \) 关于 \( X \)、\( W \) 的偏导数：

$$
\frac{\partial L}{\partial X} = \frac{\partial L}{\partial Y} \cdot W^T
$$

$$
\frac{\partial L}{\partial W} = X^T \cdot \frac{\partial L}{\partial Y}
$$
```python
# Affine层
class Affine:
    def __init__(self, W, b):
        self.W = W
        self.b = b
        self.X = None
        self.X_shape = None
        self.dW = None
        self.db = None
    def forward(self, X):
        self.X_shape = X.shape
        self.X = X.reshape(X.shape[0], -1)
        y = np.dot(X, self.W) + self.b
        return y
    def backward(self, dout):
        dX = np.dot(dout, self.W.T)
        dX = dX.reshape(*self.X_shape)
        self.dW = np.dot(self.X.T, dout)
        self.db = np.sum(dout, axis=0)
        return dX 
```

## 4.6 输出层
在输出层，我们一般使用 Softmax 作为激活函数。

对于 Softmax 函数：

$$
y_k = \frac{e^{x_k}}{\sum_{i=1}^n e^{x_i}}, \quad k = 1 \sim n
$$

其偏导数为：

$$
\frac{\partial y_k}{\partial x_i} = 
\begin{cases} 
y_k(1 - y_i), & k = i \\ 
-y_k y_i, & k \neq i 
\end{cases}
$$

而对于输出层，一般会直接将结果代入损失函数的计算。对于我们之前介绍的分类问题，这里选择交叉熵误差（Cross Entropy Error）作为损失函数，就可以得到一个 **Softmax-with-Loss 层**，它包含了 Softmax 和 Cross Entropy Loss 两部分。

最终反向传播的梯度，对分类还是回归问题，都是**预测值与真实值的差**。

## 4.7 手写数字识别 反向传播实现
```python
import numpy as np
from common.layers import ReLU, Affine, SoftmaxwithLoss
from collections import OrderedDict

class TwoLayerNet:
    def __init__(self, input_size, hidden_size, output_size, weight_init=0.01):
        self.params = {} # 权重参数
        self.params['W1'] = np.random.randn(input_size, hidden_size) * weight_init
        self.params['b1'] = np.zeros(hidden_size)
        self.params['W2'] = np.random.randn(hidden_size, output_size) * weight_init
        self.params['b2'] = np.zeros(output_size)
        self.layers = OrderedDict() # 层
        self.layers['Affine1'] = Affine(self.params['W1'], self.params['b1'])
        self.layers['ReLU1'] = ReLU()
        self.layers['Affine2'] = Affine(self.params['W2'], self.params['b2'])
        # 单独定义最后一层
        self.last_layer = SoftmaxwithLoss()

    def forward(self, X):
        for layer in self.layers.values():
            X = layer.forward(X)
        return X
    def loss(self, X, t):
        y = self.forward(X)
        loss_value = self.last_layer.forward(y, t)
        return loss_value
    def accuracy(self, X, t):
        y = self.forward(X)
        y = np.argmax(y, axis=1)
        accuracy = np.sum(y == t) / y.shape[0]
        return accuracy
    def gradient(self, X, t):
        self.loss(X, t)
        dout = 1
        dout = self.last_layer.backward(dout)
        layers = list(self.layers.values())
        layers.reverse() # 反转层的顺序
        for layer in layers:
            dout = layer.backward(dout)
        grads = {}
        grads['W1'] = self.layers['Affine1'].dW
        grads['b1'] = self.layers['Affine1'].db
        grads['W2'] = self.layers['Affine2'].dW
        grads['b2'] = self.layers['Affine2'].db
        return grads

import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.preprocessing import MinMaxScaler
data = datasets.load_digits()


X_train, X_test, y_train, y_test = train_test_split(data.data, data.target, test_size=0.2, random_state=42)
sclaer = MinMaxScaler()
X_train = sclaer.fit_transform(X_train)
X_test = sclaer.transform(X_test)


net = TwoLayerNet(input_size=64, hidden_size=50, output_size=10)

learning_rate = 0.2
batch_size = 100
num_epochs = 50
train_size = X_train.shape[0]
iter_per_epoch = int(np.ceil(train_size / batch_size))
iters = iter_per_epoch * num_epochs

train_loss_list = []
test_acc_list = []
train_acc_list = []

for i in range(iters):
    batch_mask = np.random.choice(train_size, batch_size)
    X_batch = X_train[batch_mask]
    t_batch = y_train[batch_mask]
    grad = net.gradient(X_batch, t_batch)
    for key in net.params:
        net.params[key] -= learning_rate * grad[key]
    loss = net.loss(X_batch, t_batch)
    train_loss_list.append(loss)
    if i % iter_per_epoch == (iter_per_epoch - 1):
        test_acc = net.accuracy(X_test, y_test)
        train_acc = net.accuracy(X_train, y_train)
        test_acc_list.append(test_acc)
        train_acc_list.append(train_acc)

x = np.arange(len(train_acc_list))
plt.plot(x, train_acc_list, label='train acc')
plt.plot(x, test_acc_list, label='test acc')
plt.legend()
plt.show()
```

# 第五章 学习的技巧
## 5.1 深度神经网络及其问题
### 5.1.1 深度学习
### 5.1.2 梯度消失和梯度爆炸
当反向传播进行很多层的时候，每一层都乘以一个系数，当这个梯度小于1时，越往前传，梯度会越小，导致梯度消失，反之，当这个梯度大于1时，越往前传，梯度会越大，导致梯度爆炸。
## 5.2 更新参数方法的优化
### 5.2.1 SGD的缺点
SGD 有以下问题：

- 局部最优解：陷入局部最优，尤其在非凸函数中，难以找到全局最优解。
- 鞍点：陷入鞍点，梯度为 0，导致训练停滞。
- 收敛速度慢：高维或非凸函数中，收敛速度较慢。
- 学习率选择：学习率过大导致震荡或不收敛，过小则收敛速度慢。
### 5.2.2 Momentum动量法
而 Momentum（动量法）会保存历史梯度并给予一定的权重，使其也参与到参数更新中：

$$v = \alpha v - \eta \nabla$$

$$W = W + v$$

- $v$: 历史（负）梯度的加权和  
- $\alpha$: 历史梯度的权重  
- $\nabla$: 当前梯度，即 $\frac{\partial L}{\partial w}$  
- $\eta$: 学习率

### 5.2.3 学习率衰减

1. 等间隔衰减
   每隔固定的训练周期（epoch），学习率按一定的比例下降，也称为“步长衰减”。例如，使学习率每隔 20 epoch 衰减为之前的 0.7：
2. 指定间隔衰减
   在指定的 epoch, 让学习率按照一定的系数衰减。例如, 使学习率在 epoch 达到 [10,50,200] 时衰减为之前的 0.7:
3. 指数衰减
   学习率按照指数函数 $f(x) = a^x$，$a < 1$ 进行衰减。例如，使学习率以 0.99 为底数，  
epoch 为指数衰减：

### 5.2.4 AdaGrad

AdaGrad (Adaptive Gradient, 自适应梯度) 会为每个参数适当地调整学习率，并且随着学习的进行，学习率会逐渐减小。

$$h = h + \nabla^2$$

$$W = W - \eta \frac{1}{\sqrt{h}} \nabla$$

- $h$: 历史梯度的平方和  
- $\nabla^2$: 梯度平方的平方和，即 $\frac{\partial L}{\partial W}$，这里的 $\nabla^2$ 表示对应矩阵元素的乘法。  

使用 AdaGrad 时，学习越深入，更新的幅度就越小。如果无止境地学习，更新量就会变为 0，完全不再更新。

### 5.2.5 RMSProp
RMSProp（Root Mean Square Propagation，均方根传播）是在 AdaGrad 基础上的改进，它并非将过去所有梯度一视同仁的相加，而是逐渐遗忘过去的梯度，采用指数移动加权平均，呈指数地减小过去梯度的尺度。

$$h = \alpha h + (1 - \alpha) \nabla^2$$

$$W = W - \eta \frac{1}{\sqrt{h}} \nabla$$

- $h$: 历史梯度平方和的指数移动加权平均  
- $\alpha$: 权重

### 5.2.6 Adam
Adam（Adaptive Moment Estimation，自适应矩估计）融合了 Momentum 和 AdaGrad 的方法。

$$v = \alpha_1 v + (1 - \alpha_1) \nabla$$

$$h = \alpha_2 h + (1 - \alpha_2) \nabla^2$$

$$\hat{v} = \frac{v}{1 - \alpha_1^t}$$

$$\hat{h} = \frac{h}{1 - \alpha_2^t}$$

$$W = W - \eta \frac{\hat{v}}{\sqrt{h}}$$

- $\eta$：学习率
- $\alpha_1$、$\alpha_2$：一次动量系数和二次动量系数
- $t$：迭代次数，从 1 开始

### 5.2.7 代码展示
```python
import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict # 有序字典
from common.optimizer import *

def f(x,y):
    return x**2/20 + y**2
def fgrad(x,y):
    return  x/10, 2*y

init_pos = (-7.0, 2.0)
params = {}
grads = {}
id = 1
optimizers = OrderedDict()

optimizers['sgd'] = SGD(lr=0.9)
optimizers['momentum'] = Momentum(lr=0.1, momentum=0.85)
optimizers['adagrad'] = AdaGrad(lr=1.5)
optimizers['adam'] = Adam(lr=0.5 , alpha1=0.5)

for key in optimizers.keys():
    optimizer = optimizers[key]
    x_list = []
    y_list = []
    params['x'], params['y'] = init_pos[0], init_pos[1]
    for i in range(30):
        x_list.append(params['x'])
        y_list.append(params['y'])
        grads['x'], grads['y'] = fgrad(params['x'], params['y'])
        optimizer.update(params, grads)
    x = np.arange(-10, 10, 0.01)
    y = np.arange(-5, 5, 0.01)
    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    Z[Z > 7] = 0
    plt.subplot(2, 2, id)
    id += 1
    plt.contour(X, Y, Z)
    plt.plot(x_list, y_list,'r-', label=key)
    plt.plot(0,0,'+')
    plt.legend()
    plt.xlim(-10, 10)
    plt.ylim(-5, 5)
plt.show()
```

## 5.3 参数初始化
### 5.3.1 常数初始化
所有权重参数初始化为一个常数，即  

$$W = k \cdot J$$

这里 $J$ 为全 1 矩阵，$k$ 为初始化的常数。  

注意：将权重初始值设为 0 将无法正确进行学习。严格地说，不能将权重初始值设成一  
样的值。因为这意味着反向传播时权重全部都会进行相同的更新，被更新为相同的值（对称  
的值）。这使得神经网络拥有许多不同的权重的意义丧失了。为了防止“**权重均一化**”（瓦  
解权重的对称结构），必须随机生成初始值。

### 5.3.2 秩初始化
权重参数初始化为单位矩阵

### 5.3.3 正态分布初始化
权重参数按指定均值 $\mu$ 与标准差 $\sigma$ 正态分布初始化。因为不能直接将权重初始化为相同的常数，所以需要对参数进行随机初始化。最常见的随机分布就是 **正态分布**（也叫 **高斯分布**），记作 $X \sim N(\mu, \sigma^2)$。

其概率密度函数为：

$$f(x) = \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$

### 5.3.4 均匀分布初始化

权重参数在指定区间内均匀分布初始化。均匀分布一般记作 $X \sim U(a, b)$。

其概率密度函数为：

$$f(x) = \frac{1}{b-a}, \quad a < x < b$$

$$f(x) = 0, \quad x \leq a \quad \text{or} \quad x \geq b$$

### 5.3.5 Xavier 初始化（Glorot 初始化）

Xavier 初始化根据输入和输出的神经元数量调整权重的初始范围，确保每一层的输出方差与输入方差相近。

Xavier 正态分布初始化：均值为 0，标准差为 $\sqrt{\frac{2}{n_{in} + n_{out}}}$ 的正态分布。

Xavier 均匀分布初始化：区间 $\left[-\sqrt{\frac{6}{n_{in} + n_{out}}}, \sqrt{\frac{6}{n_{in} + n_{out}}}\right]$ 内均匀分布。

其中 $n_{in}$ 表示输入数，$n_{out}$ 表示输出数。

Xavier 初始化参数适用于 **Sigmoid** 和 **Tanh** 等激活函数，能有效缓解梯度消失或爆炸问题。

### 5.3.6 He 初始化 (Kaiming 初始化)

He 初始化根据输入的神经元数量调整权重的初始范围。

He 正态分布初始化：均值为 0，标准差为 $\sqrt{\frac{2}{n_{in}}}$ 的正态分布。

He 均匀分布初始化：区间 $\left[-\sqrt{\frac{6}{n_{in}}}, \sqrt{\frac{6}{n_{in}}}\right]$ 内均匀分布。

其中 $n_{in}$ 表示输入数。

He 初始化参数主要适用于 **ReLU** 及其变体（如 Leaky ReLU）激活函数。

## 5.4 正则化
凡是能抑制模型过拟合的方法，都可以被称为正则化方法。
### 5.4.1 Batch Normalization 批量标准化
Batch Normalization 最重要的目的，其实是调整各层的激活值分布使其拥有适当的广度，  
BN 层通常放在线性层（全连接层/卷积层）之后，激活函数之前。它有着以下优点：  

- 可以使学习快速进行（允许更高的学习率）  
- 不那么依赖初始值（对于初始值不用那么神经质）  
- 抑制过拟合（降低 Dropout 等的必要性）  

Batch Normalization 会先对数据进行标准化，再对数据进行缩放和平移：  

均值：  
\[\mu = \frac{1}{n} \sum x\]  

方差：  
\[\sigma^2 = \frac{1}{n} \sum (x - \mu)^2\]  

标准化：  
\[\hat{x} = \frac{x - \mu}{\sqrt{\sigma^2 + \epsilon}} \quad (\epsilon \text{为一个微小值，防止分母为 } 0)\]  

缩放平移：  
\[y = \gamma \hat{x} + \beta\]  

- \(\gamma\)：系数，可通过学习调整  
- \(\beta\)：偏置，可通过学习调整

### 5.4.2 权值衰减

通过在学习的过程中对大的权重进行“惩罚”，可以有效地抑制过拟合，这种方法被称为 **权值衰减**。因为很多过拟合产生的原因，就是权重参数取值过大。

一般会对损失函数加上一个权重范数，最常见的就是 L2 范数的平方：

$$L' = L + \frac{1}{2} \lambda \cdot \|W\|^2$$

- $\|W\|$：表示权重 $W = (w_1, w_2, \dots, w_n)$ 的 L2 范数，即 $\sqrt{w_1^2 + w_2^2 + \dots + w_n^2}$

- $\lambda$：控制正则化强度的超参数。

惩罚项 $\frac{1}{2} \lambda \cdot \|W\|^2$ 求导之后得到 $\lambda W$，所以在求权重梯度时，需要为之前误差反向传播的结果，再加上 $\lambda W$。

### 5.4.3 Dropout 随机失活

Dropout（随机失活，暂退法）是一种在学习的过程中随机关闭神经元的方法。

训练时以概率 $p$ 随机关闭神经元，迫使网络不依赖特定神经元，增强鲁棒性，同时未被关闭的神经元的输出值以 $\frac{1}{(1-p)}$ 的比例进行缩放，以保持期望值不变；而测试时通常不使用 Dropout，即所有神经元保持激活状态并且不进行缩放。

Dropout 会有隐式集成的效果（每次迭代训练不同的子网络，测试时近似集成效果）。

Dropout 在全连接层和卷积层均适用，尤其对大规模网络效果显著。Dropout 通常放在激活函数之后，线性层（全连接层/卷积层）之前。

# 第六章 Pytorch简介
## 6.1 什么是Pytorch
PyTorch 是facebook开发的一个开源的 Python 机器学习库，基于 Torch 库（一个有大量机器学习算法支持的科学计算框架，有着与 Numpy 类似的张量（Tensor）操作，采用的编程语言是 Lua），底层由 C++实现，应用于人工智能领域，如计算机视觉和自然语言处理。

PyTorch 主要有两大特征：

- 类似于 NumPy 的张量计算，能在 GPU 或 MPS 等硬件加速器上加速。
- 基于带自动微分系统的深度神经网络。

PyTorch 官网：https://pytorch.org/。

另外一个谷歌开发的Tensorflow更偏向工程应用，比较难上手一些

## 6.2 Pytorch安装
## 6.3 张量创建
### 6.3.1 基本张量创建
1. 指定内容创建张量
```python
tensor1 = torch.tensor(10)
tensor2 = torch.tensor(np.array([1, 2, 3]))
```
2. 指定形状创建张量
大写Tensor创建默认数据类型为float32，不能指定标量创建
```python
tensor1 = torch.Tensor(3,2,4)
tensor2 = torch.Tensor([10])
```
3. 指定数据类型创建张量
```python
tensor1 = torch.tensor(10, dtype=torch.int64)
tensor2 = torch.LongTensor([1, 2, 3])
```
### 6.3.2 指定区间创建张量
1. arange 按步长创建张量
```python
tensor1 = torch.arange(10)
tensor2 = torch.arange(10, 20, 2)
```
2. linspace 按元素数量创建张量
```python
tensor1 = torch.linspace(0, 8, 5)
```
3. logspace 按指数创建张量
```python
tensor2 = torch.logspace(0, 8, 5, 2)
```
### 6.3.3 按数值填充张量
- torch.zeros(size)创建指定形状的全 0 张量
- torch.ones(size)创建指定形状的全 1 张量
- torch.full(size, value)创建指定形状的按指定值填充的张量
- torch.empty(size)创建指定形状的未初始化的张量
- torch.zeros_like(input)创建与给定张量形状相同的全 0 张量
- torch.ones_like(input)创建与给定张量形状相同的全 1 张量
- torch.full_like(input, value)创建与给定张量形状相同的按指定值填充的张量
- torch.empty_like(input)创建与给定张量形状相同的未初始化的张量
- torch.eye(n,[m])创建单位矩阵

### 6.3.4 随机数创建张量
- torch.rand(size) 创建在[0,1)上均匀分布的，指定形状的张量
- torch.randint(low, high, size) 创建在[low,high)上均匀分布的，指定形状的张量
- torch.randn(size) 创建标准正态分布的，指定形状的张量
- torch.normal(mean, std, size) 创建自定义正态分布的，指定形状的张量
- torch.rand_like(input) 创建在[0,1)上均匀分布的，与给定张量形状相同的张量
- torch.randint_like(input, low, high) 创建在[low,high)上均匀分布的，与给定张量形状相同的张量
- torch.randn_like(input) 创建标准正态分布的，与给定张量形状相同的张量
- torch.randperm(n) 创建一个从0到n-1的随机排列张量
- torch.random.initial_seed() 获取当前随机数种子
- torch.manual_seed(seed) 设置随机数种子

## 6.4 张量转换
### 6.4.1 张量类型转换
```python
tensor1 = tensor1.type(torch.float32)
tensor2 = tensor2.float()
```
### 6.4.2 ndarray转换
```python
array1 = tensor1.numpy() # 将张量转换为ndarray 共享内存
tensor2 = torch.from_numpy(array2) # 将ndarray转换为张量 共享内存
tensor3 = torch.tensor(array3) # 将ndarray转换为张量 不共享内存
```
### 6.4.3 标量转换
```python
tensor1 = torch.tensor(10)
scalar1 = tensor1.item() # 将标量张量转换为Python标量 仅限一个元素
```

## 6.5 张量运算
### 6.5.1 基本运算
1. 四则运算

- +、-、*、/加减乘除

- add()、sub()、mul()、div()加减乘除，不改变原数据

- add_()、sub_()、mul_()、div_()加减乘除、修改原数据

2. 取负
- -、neg()、neg_() 

3. 求幂
- **、pow()、pow_() 

4. 求平方根
- sqrt()、sqrt_() 

5. 以e为底的指数
- exp()、exp_() 

6. 以e为底的对数
- log()、log_() 

### 6.5.2 哈达玛积运算
使用*或mul()实现两个形状相同的张量之间对位相乘

### 6.5.3 矩阵乘法
- mm()严格用于二维矩阵相乘
- @ 和 matmul() 支持多维张量，最后两个维度做矩阵乘法，其他维度按哈达玛积运算

## 6.6 张量运算函数
- sum()求和  
- mean()求均值  
- max()/min()求最大/最小值及其索引  
- argmax()/argmin()求最大值/最小值的索引  
- std()求标准差  
- unique()去重  
- sort()排序

## 6.7 张量索引
### 6.7.1 简单张量索引
```python
print(tensor1[0,2,1])
```
### 6.7.2 范围索引
```python
print(tensor1[:,2])
```
### 6.7.3 列表索引
```python
print(tensor1[[0,1],[2,3]]) # 1对1
print(tensor1[[[0],[1]],[2,3]]) # 1对多
``` 
### 6.7.4 布尔索引
```python
mask = (tensor1 > 2) # 所有大于2的元素
mask = (tensor1[:,2] > 2) # 第3列大于2的元素
```
## 6.8 张量形状操作
### 6.8.1 交换维度
- .T 维度翻转
- .mT 交换最后两个维度
- transpose()交换两个维度
- permute()重新排列维度
### 6.8.2 调整形状
- reshape()调整形状
- view()需要内存连续，共享内存
### 6.8.3 增加或删除维度
- unsqueeze()增加维度 ，在指定维度上增加一个长度为1的维度
- squeeze()删除维度 ，删除长度为1的维度

## 6.9 张量拼接
- torch.cat()拼接张量 ，在指定维度上拼接 其他维度需要相同
- torch.stack()拼接张量 ，在新维度上拼接 其他维度需要相同

## 6.10 自动微分模块
自动微分的关键就是记录节点的数据与运算。数据记录在张量的 data 属性中，计算记录在张量的 grad_fn 属性中。

计算图根据搭建方式可分为静态图和动态图，PyTorch 是动态图机制，在计算的过程中逐步搭建计算图，同时对每个 Tensor 都存储 grad_fn 供自动微分使用。

若设置张量参数 requires_grad=True，则 PyTorch 会追踪所有基于该张量的操作，并在反向传播时计算其梯度。依赖于叶子节点的节点，requires_grad 默认为 True。当计算到根节点后，在根节点调用 backward() 方法即可反向传播计算图中所有节点的梯度。

非叶子节点的梯度在反向传播之后会被释放掉（除非设置参数 retain_grad=True）。而叶子节点的梯度在反向传播之后会保留（累积）。通常需要使用 optimizer.zero_grad() 清零参数的梯度。

有时我们希望将某些计算移动到计算图之外，可以使用 Tensor.detach() 返回一个新的变量，该变量与原变量具有相同的值，但丢失计算图中如何计算原变量的信息。换句话说，梯度不会在该变量处继续向下传播。

Tensor.data相比Tensor.detach()的区别在于，Tensor.data不会被计算图追踪，安全性更低

## 6.11 线性回归案例
```python
import torch
import matplotlib.pyplot as plt
from torch import nn, optim 
from torch.utils.data import TensorDataset, DataLoader

X = torch.randn(100, 1)
w = torch.tensor([2.5])
b = torch.tensor([5.2])
noise = torch.randn(100, 1) * 0.1
y = X * w + b + noise
dataset = TensorDataset(X, y)
dataloader = DataLoader(dataset, batch_size=10, shuffle=True) # 批量大小为10，每个epoch随机打乱数据

model = nn.Linear(1, 1)
loss = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=0.01)
loss_list = []

epoch = 100
for e in range(epoch):
    total_loss = 0
    for x_train , y_train in dataloader:
        y_pred = model(x_train)
        loss_value = loss(y_pred, y_train)
        total_loss += loss_value.detach() * len(x_train)

        loss_value.backward()
        optimizer.step()
        optimizer.zero_grad()
    loss_list.append(total_loss / len(dataset))

print(model.weight)
print(model.bias)

fig, ax = plt.subplots(1,2,figsize=(10, 4))
ax[0].plot(loss_list)
ax[0].set_title('loss')
ax[0].set_xlabel('epoch')
ax[0].set_ylabel('loss')
ax[1].scatter(X,y)
y_pred = model.weight.item() * X + model.bias.item()
ax[1].plot(X,y_pred,color='red')
plt.show()
```

# 第七章 用Pytorch进行深度学习
## 7.1 激活函数
### 7.1.1 Sigmoid函数
```python
import torch
import matplotlib.pyplot as plt

x = torch.linspace(-10, 10, 1000, requires_grad=True)
y = torch.sigmoid(x)

fig, ax = plt.subplots(1,2,figsize=(10, 4))
ax[0].plot(x.detach(), y.detach(), color='purple')
ax[0].set_title('sigmoid')
ax[0].axhline(0.5, color='grey', linestyle='--')
ax[0].axhline(1, color='grey', linestyle='--')
ax[0].spines['top'].set_visible(False)
ax[0].spines['right'].set_visible(False)
ax[0].spines['left'].set_position('zero')
ax[0].spines['bottom'].set_position('zero')

y.sum().backward()

ax[1].plot(x.detach(), x.grad, color='purple')
ax[1].set_title('sigmoid derivative')
ax[1].spines['top'].set_visible(False)
ax[1].spines['right'].set_visible(False)
ax[1].spines['left'].set_position('zero')
ax[1].spines['bottom'].set_position('zero')

plt.show()
```
### 7.1.2 Tanh函数

### 7.1.3 ReLU函数  

### 7.1.4 Softmax函数

## 7.2 参数初始化和正则化
### 7.2.1 全连接层(nn.Linear)
```python
import torch

linear = nn.Linear(2, 3)
```
### 7.2.2 常数初始化
```python
linear = nn.Linear(5, 2)
nn.init.ones_(linear.weight)
nn.init.zeros_(linear.bias)
nn.init.constant_(linear.bias, 100)
```
### 7.2.3 秩初始化
```python
nn.init.eye_(linear.weight)
```
### 7.2.4 正态分布初始化
```python
nn.init.normal_(linear.weight , mean=0, std=0.1)
```
### 7.2.5 均匀分布初始化
```python
nn.init.uniform_(linear.weight, a=-1, b=1)
```
### 7.2.6 Xavier初始化 Sigmoid/Tanh
```python
nn.init.xavier_normal_(linear.weight)
nn.init.xavier_uniform_(linear.weight)
```
### 7.2.7 Kaiming初始化 Relu
```python
nn.init.kaiming_normal_(linear.weight)
nn.init.kaiming_uniform_(linear.weight)
```
### 7.2.8 Dropout随机失活
```python
dropout = nn.Dropout(p=0.5) # 以概率0.5随机失活神经元
```

## 7.3 搭建神经网络
### 7.3.1 自定义模型
在神经网络框架中，由多个层组成的组件称之为 **模块（Module）**。

在 PyTorch 中模型就是一个 Module，各网络层、模块也是 Module。Module 是所有神经网络的基类。

在定义一个 Module 时，我们需要继承 `torch.nn.Module` 并主要实现两个方法：
- `__init__`：定义网络各层的结构，并初始化参数。
- `forward`：根据输入进行前向传播，并返回输出。计算其输出关于输入的梯度，可通过其反向传播函数进行访问（通常自动发生）。`forward` 方法是每次调用的具体实现。
```python
class MyModel(nn.Module):
    def __init__(self):
        super().__init__() # 继承父类的初始化方法
        self.linear1 = nn.Linear(3, 4)
        nn.init.xavier_normal_(self.linear1.weight) 
        self.linear2 = nn.Linear(4, 4)
        nn.init.kaiming_normal_(self.linear2.weight)
        self.linear3 = nn.Linear(4, 2)
    def forward(self, x):
        x = self.linear1(x)
        x = torch.tanh(x)
        x = self.linear2(x)
        x = torch.relu(x)
        x = self.linear3(x)
        x = torch.softmax(x, dim=1)
        return x

x = torch.randn(10 , 3)
model = MyModel()
y = model(x)

# 查看模型参数
for param in model.named_parameters():
    print(param)
print(model.state_dict())
```

### 7.3.2 查看模型结构和参数数量
```python
from torchinfo import summary
summary(model, (10, 3))
```

补充模型设备选择
```python
device = 'cuda' if torch.cuda.is_available() else 'cpu'

x = torch.randn(10 , 3 , device=device)
model = MyModel().to(device)
y = model(x)
```

### 7.3.3 使用Sequential构建模型
```python
import torch
import torch.nn as nn
from torchinfo import summary

x = torch.randn(10 , 3)
model = nn.Sequential(
    nn.Linear(3, 4),
    nn.Tanh(),
    nn.Linear(4, 4),
    nn.ReLU(),
    nn.Linear(4, 2),
    nn.Softmax(dim=1)
)

# 参数初始化函数
def init_params(layers):
    if isinstance(layers, nn.Linear):
        nn.init.xavier_uniform_(layers.weight)
        nn.init.zeros_(layers.bias)

model.apply(init_params)

y = model(x)
print(y)

summary(model, (10, 3))
```

## 7.4 损失函数
### 7.4.1 分类任务损失函数
1. 二分类任务损失函数BCE
    二分类任务常用二元交叉熵损失函数，其公式如下：

    $$
    L = -\frac{1}{n}\sum_{i=1}^{n} \left( y_i \log \hat{y}_i + (1 - y_i)\log(1 - \hat{y}_i) \right)
    $$

    其中：
    - $y_i$ 为真实值（通常为 0 或 1）
    - $\hat{y}_i$ 为预测值（表示样本 $i$ 为 1 的概率）
    
2. 多分类任务损失函数CCE
    多分类任务常用多类交叉熵损失函数，它是对每个类别的预测概率与真实标签之间差异的加权平均。

    $$
    L = -\frac{1}{n}\sum_{i=1}^{n}\sum_{c=1}^{C} y_{i,c}\log\hat{y}_{i,c}
    $$

    其中：
    - $C$ 是类别数
    - $y_{i,c}$ 为真实值（表示 $y_i$ 是否为类别 $c$，通常为 0 或 1）
    - $\hat{y}_{i,c}$ 为预测值（表示样本 $i$ 为类别 $c$ 的概率）

### 7.4.2 回归任务损失函数

1. MAE L1loss
2. MSE L2loss
3. SmoothL1

## 7.5 参数更新方法
### 7.5.1 Momentum
```python
import torch
import numpy as np
import matplotlib.pyplot as plt

def f(X):
    return 0.05 * X[0] ** 2 + X[1] ** 2

def g(X, optimizer, iters):
    X_arr = X.clone().detach() # tensor
    for i in range(iters):
        y = f(X)
        y.backward()
        optimizer.step()
        optimizer.zero_grad()

        X_arr = np.vstack((X_arr, X.clone().detach())) # tensor堆叠为nparray
    return X_arr

X = torch.tensor([-7.0, 2.0], requires_grad=True)
lr = 0.01
iters = 500

# SGD
X_clone = X.clone().detach().requires_grad_(True) # tensor
sgd = torch.optim.SGD([X_clone],lr = lr)  # list
X_arr1 = g(X_clone, sgd, iters)

# momentum
X_clone = X.clone().detach().requires_grad_(True)
momentum = torch.optim.SGD([X_clone],lr = lr, momentum=0.9) 
X_arr2 = g(X_clone, momentum, iters)

plt.plot(X_arr1[:,0], X_arr1[:,1], 'r', label='SGD')
plt.plot(X_arr2[:,0], X_arr2[:,1], 'b', label='momentum')
x1, x2 = np.meshgrid(np.linspace(-7, 7, 100), np.linspace(-2, 2, 100)) # 将这两个一维数组转换为二维网格坐标矩阵
y_grid = 0.05 * x1**2 +  x2**2
plt.contour(x1, x2, y_grid, levels=15) 
plt.legend()
plt.show()
```

### 7.5.2 学习率衰减
1. 等间隔衰减
   例如，每 100 次迭代将学习率衰减为之前的0.7倍
```python
import torch
import numpy as np
import matplotlib.pyplot as plt
from torch.optim.lr_scheduler import StepLR # 等间隔衰减

def f(X):
    return 0.05 * X[0] ** 2 + X[1] ** 2

X = torch.tensor([-7.0, 2.0], requires_grad=True)
lr = 0.9
iters = 500
sgd = torch.optim.SGD([X], lr=lr)
lr_scheduler = StepLR(sgd, step_size=20, gamma=0.7) # 学习率衰减器

X_arr = X.clone().detach() # tensor
lr_list = []
for i in range(iters):
    y = f(X)
    y.backward()
    sgd.step() # 更新参数
    sgd.zero_grad()
    X_arr = np.vstack((X_arr, X.clone().detach())) # tensor堆叠为nparray
    lr_list.append(sgd.param_groups[0]['lr'])
    lr_scheduler.step() # 更新学习率

fig, ax = plt.subplots(1,2,figsize=(12, 4))
x1, x2 = np.meshgrid(np.linspace(-7, 7, 100), np.linspace(-2, 2, 100)) # 将这两个一维数组转换为二维网格坐标矩阵
y_grid = 0.05 * x1**2 +  x2**2
ax[0].contour(x1, x2, y_grid, levels=15) 
ax[0].plot(X_arr[:, 0], X_arr[:, 1], 'r')
ax[1].plot(lr_list)
plt.show()
```
2. 指定间隔衰减
```python
from torch.optim.lr_scheduler import MultiStepLR 
lr_scheduler = MultiStepLR(sgd, milestones=[10,50,200], gamma=0.7)
lr_scheduler.step()
```
3. 指数衰减
```python
from torch.optim.lr_scheduler import ExponentialLR 
lr_scheduler = ExponentialLR(sgd, gamma=0.99)
lr_scheduler.step()
```

### 7.5.3 Adagrad(Adaptive Gradient)
以历史梯度的平方和的倒根号作为衰减因子
```python
from torch.optim import Adagrad
adagrad = Adagrad([X_clone],lr = lr) 
```
### 7.5.4 RMSprop
RMSprop(Root Mean Square Propagation, 均方根传播),adagrad的改进，采取历史梯度和当前梯度的权重和，逐渐遗忘过去的梯度
```python
from torch.optim import RMSprop
rmsprop = RMSprop([X_clone],lr = lr, alpha=0.9) 
```
### 7.5.5 Adam
Adam(Adamaptive Moment Estimation), 适应矩估计，结合了Momentum和RMSprop的优点
```python
from torch.optim import Adam
adam = Adam([X_clone],lr = lr, betas=(0.9, 0.999)) 
```
工程上常用AdamW

## 7.6 房价预测
```python
import torch
import pandas as pd
import torch.nn as nn
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer # 列转换器
from sklearn.impute import SimpleImputer # 缺失值填充器
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.pipeline import Pipeline # 管道 将多个数据处理步骤和模型封装成一个整体
from torch.utils.data import DataLoader, TensorDataset # 数据加载器 张量数据集

def load_data():
    data = pd.read_csv('./data/house_prices.csv')
    data.drop('Id', axis=1, inplace=True)
    X = data.drop(columns=['SalePrice'])
    y = data['SalePrice'] 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    num_features = X.select_dtypes(include=['number']).columns
    cat_features = X.select_dtypes(include=['str']).columns
    num_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='mean')), # 缺失值填充器
        ('std', StandardScaler()) # 标准化
    ])
    cat_transformer = Pipeline([
        ('imputer', SimpleImputer(strategy='constant', fill_value='NaN')), # 缺失值填充器
        ('onehot', OneHotEncoder(handle_unknown='ignore')) # 独热编码  忽略未知类别
    ])
    transformers = ColumnTransformer([
        ('num', num_transformer, num_features),
        ('cat', cat_transformer, cat_features)
    ])
    X_train = transformers.fit_transform(X_train) # 默认返回稀疏矩阵
    X_test = transformers.transform(X_test)
    # 稀疏矩阵转稠密矩阵转DataFrame
    X_train = pd.DataFrame(X_train.toarray(), columns=transformers.get_feature_names_out()) 
    X_test = pd.DataFrame(X_test.toarray(), columns=transformers.get_feature_names_out()) 
    train_dataset = TensorDataset(torch.tensor(X_train.values).float(), torch.tensor(y_train.values).float())
    test_dataset = TensorDataset(torch.tensor(X_test.values).float(), torch.tensor(y_test.values).float())
    return train_dataset, test_dataset, X_train.shape[1]

train_dataset, test_dataset, feature_dim = load_data()
model = nn.Sequential(
    nn.Linear(feature_dim, 128),
    nn.BatchNorm1d(128),
    nn.ReLU(),
    nn.Dropout(0.2),
    nn.Linear(128, 1),
)
mse = nn.MSELoss()

def log_rmses(y,t):
    y = torch.clamp(y,1,float('inf')) # 将y的值限制在[0,正无穷]之间
    return torch.sqrt(mse(torch.log(y),torch.log(t)))

def train(model, train_data, test_data, lr, epoch_num, batch_size, device):
    def init_model(layer):
        if isinstance(layer, nn.Linear):
            nn.init.xavier_normal_(layer.weight)    
    model.apply(init_model)
    model = model.to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    train_losslist = []
    test_losslist = []

    for epoch in range(epoch_num):
        model.train() # 切换到训练模式
        train_loader = DataLoader(train_data, batch_size=batch_size, shuffle=True)
        train_loss_sum = 0.0

        for id, (x, y) in enumerate(train_loader):
            x = x.to(device)
            y = y.to(device)
            y_pred = model(x)
            loss_val = log_rmses(y_pred.squeeze(), y) # 降维
            loss_val.backward()
            optimizer.step()
            optimizer.zero_grad()
            train_loss_sum += loss_val.item()*x.shape[0]
        train_losslist.append(train_loss_sum/len(train_data))

        model.eval() # 切换到评估模式
        test_loader = DataLoader(test_data, batch_size=batch_size)
        test_loss_sum = 0.0
        with torch.no_grad(): # 禁用梯度计算
            for id, (x, y) in enumerate(test_loader):
                x = x.to(device)
                y = y.to(device)
                y_pred = model(x)
                loss_val = log_rmses(y_pred.squeeze(), y) # 降维
                test_loss_sum += loss_val.item()*x.shape[0]
        test_losslist.append(test_loss_sum/len(test_data))
        print(f"Epoch: {epoch}, Train Loss: {train_loss_sum/len(train_data):.4f}, Test Loss: {test_loss_sum/len(test_data):.4f}")
    return train_losslist, test_losslist

device = 'cuda' if torch.cuda.is_available() else 'cpu'
lr = 0.1
epoch_num = 200
batch_size = 64

train_losslist, test_losslist = train(model, train_dataset, test_dataset, lr, epoch_num, batch_size, device)

plt.plot(train_losslist, label='Train', color='blue')
plt.plot(test_losslist, label='Test', color='red')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.show()
```

# 第八章 卷积神经网络 CNN
## 8.1 CNN概述 Convolutional Neural Network
## 8.2 卷积层 Convolution
### 8.2.1 卷积运算
对于输入数据，卷积运算以一定间隔滑动卷积核的窗口并应用。将各个位置上卷积核的元素和输入的对应元素相乘，然后再求和（也称为乘积累加运算、矩阵的内积）。

在CNN中，卷积核的参数对应之前的权重。

### 8.2.2 填充 Padding
在卷积层中，填充（Padding）是指在输入数据的边界添加零值，以保持卷积核的大小不变。

### 8.2.3 步幅 Stride
在卷积层中，步幅（Stride）是指卷积核滑动的步长。默认步幅为1，即每次滑动一个像素。

假设输入数据形状为 $(H, W)$，卷积核大小为 $(FH, FW)$，填充为 $P$，步幅为 $S$，输出数据形状为 $(OH, OW)$，可得：

$$
OH = \frac{H + 2P - FH}{S} + 1
$$

$$
OW = \frac{W + 2P - FW}{S} + 1
$$

例如，对于形状为 $(4,4)$ 的输入数据应用幅度为 $1$ 的填充，并应用步幅为 $3$，卷积核大小为 $(3,3)$ 的卷积运算：

$$
OH = OW = \frac{4 + 2 - 3}{3} + 1 = 2
$$

得到形状为 $(2,2)$ 的输出数据。

当输出大小无法除尽时，PyTorch 卷积层会自动向下取整，输出整数尺寸，舍弃无法覆盖完整卷积核的输入部分。

### 8.2.4 三维数据的卷积运算

1. 输入特征图 Channel
    维度：$\boldsymbol{(C, H, W)}$
    - $C$：输入特征通道数
    - $H$：输入特征图高度
    - $W$：输入特征图宽度

2. 卷积核（权重） Filter
    维度：$\boldsymbol{(FN, C, FH, FW)}$
    - $FN$：卷积核数量（决定输出通道数）
    - $C$：卷积核特征通道数，必须与输入特征通道数一致
    - $FH、FW$：单个卷积核的高、宽

3. 卷积中间结果 Output
    输入与卷积核做卷积运算后，得到未加偏置的特征图：
    维度：$\boldsymbol{(FN, OH, OW)}$
    - $OH、OW$：输出特征图的高度、宽度

4. 偏置项
    维度：$\boldsymbol{(FN, 1, 1)}$
    利用张量广播机制，为单个输出通道内所有像素位置统一加上同一个偏置值。

5. 最终输出特征图
    维度：$\boldsymbol{(FN, OH, OW)}$

$$
\boldsymbol{输入(C,H,W)} \circledast \boldsymbol{卷积核(FN,C,FH,FW)} \implies \boldsymbol{卷积中间结果(FN,OH,OW)} \xrightarrow{+\boldsymbol{偏置(FN,1,1)}} \boldsymbol{输出(FN,OH,OW)}
$$

### 8.2.5 API
```python
import torch
import matplotlib.pyplot as plt

img = plt.imread("./data/duck.jpg") # (1000, 1000, 3)
input = torch.tensor(img).permute(2, 0, 1).float()  # (3, 1000, 1000)

conv = torch.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=9, stride=3, padding=0, bias=False)
output = conv(input)

output = torch.clamp(output.int(), min=0, max=255).permute(1, 2, 0).numpy()
plt.imshow(output)
plt.show()
```

## 8.3 池化层 Pooling
池化层缩小长、宽方向上的空间来进行降维，能够缩减模型的大小并提高计算速度。
有Max池化、Average池化
与卷积层不同，池化层不改变特征通道数，只改变特征图的尺寸。
```python
import torch
import matplotlib.pyplot as plt
img = plt.imread("./data/duck.jpg") # (1000, 1000, 3)
input = torch.tensor(img).permute(2, 0, 1).float()  # (3, 1000, 1000)

conv = torch.nn.Conv2d(in_channels=3, out_channels=3, kernel_size=9, stride=3, padding=0, bias=False)
output = conv(input)
print(output.shape)

pool = torch.nn.MaxPool2d(kernel_size=6, stride=6, padding=1)  # 6*6的池化层，步长为6，填充为1
output2 = pool(output)
print(output2.shape)

output = torch.clamp(output.int(), min=0, max=255).permute(1, 2, 0).numpy()
output2 = torch.clamp(output2.int(), min=0, max=255).permute(1, 2, 0).numpy()
fig, ax = plt.subplots(1,2, figsize=(10,5))
ax[0].imshow(output)
ax[1].imshow(output2)
ax[0].set_title("Convolution")
ax[1].set_title("Max Pooling")
plt.show()
```

## 8.4 深度卷积神经网络
1. AlexNet
2. VGG
3. GoogleNet
4. ResNet

## 8.5 服装分类案例
```python
import torch
import pandas as pd
import torch.nn as nn
import matplotlib.pyplot as plt
from torch.utils.data import DataLoader,TensorDataset
# 加载数据集
fashion_train = pd.read_csv("./data/fashion-mnist_train.csv")
fashion_test = pd.read_csv("./data/fashion-mnist_test.csv")
# 数据预处理
x_train = torch.tensor(fashion_train.drop(columns=["label"]).values.reshape(-1, 1, 28, 28)).float()
y_train = torch.tensor(fashion_train["label"]).long()
x_test = torch.tensor(fashion_test.drop(columns=["label"]).values.reshape(-1, 1, 28, 28)).float()
y_test = torch.tensor(fashion_test["label"]).long()
train_dataset = TensorDataset(x_train, y_train)
test_dataset = TensorDataset(x_test, y_test)
# 模型定义
model = nn.Sequential(
    nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5, stride=1, padding=2),
    nn.Sigmoid(),
    nn.MaxPool2d(kernel_size=2, stride=2, padding=0),

    nn.Conv2d(in_channels=6, out_channels=16, kernel_size=5, stride=1, padding=0),
    nn.Sigmoid(),
    nn.MaxPool2d(kernel_size=2, stride=2, padding=0),

    nn.Flatten(), 

    nn.Linear(400, 120),
    nn.Sigmoid(),

    nn.Linear(120, 84),
    nn.Sigmoid(),

    nn.Linear(84, 10),
)
# 训练函数
def train(model, train_dataset, test_dataset, lr, epochs, batch_size, device):
    def init_weights(layer):
        if isinstance(layer, nn.Linear) or isinstance(layer, nn.Conv2d):
            nn.init.xavier_uniform_(layer.weight)

    model.apply(init_weights)
    model.to(device)
    loss = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=lr)

    for epoch in range(epochs):
        model.train()
        dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
        train_loss = 0.0
        train_correct = 0
        for batch_idx, (x,y) in enumerate(dataloader):
            x = x.to(device)
            y = y.to(device)
            output = model(x)
            loss_value = loss(output, y) 
            loss_value.backward()
            optimizer.step()
            optimizer.zero_grad()

            train_loss += loss_value.item() * x.shape[0] # 累计批次损失
            pred = output.argmax(dim=1) # 取批次预测类别
            train_correct += (pred == y).sum().item() # 累计批次正确预测数量

            print(f"\r Epoch: {epoch+1:0>2} [{'=' * int((batch_idx+1) / len(dataloader)*50) }]", end="")
        this_loss = train_loss / len(train_dataset) # 本轮损失
        train_acc = train_correct / len(train_dataset) # 本轮准确率
        
        model.eval()
        test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)
        test_correct = 0
        with torch.no_grad():
            for x,y in test_loader:
                x = x.to(device)
                y = y.to(device)
                output = model(x)
                pred = output.argmax(dim=1) # 取批次预测类别
                test_correct += (pred == y).sum().item() # 累计批次正确预测数量
        this_test_acc = test_correct / len(test_dataset) # 本轮测试准确率

        print(f"train_loss: {this_loss:.4f}, train_acc: {train_acc:.4f}, test_acc: {this_test_acc:.4f}")
# 训练模型
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
lr = 0.01
epochs = 20
batch_size = 256
train(model, train_dataset, test_dataset, lr, epochs, batch_size, device)
# 测试
plt.imshow(x_test[99,0], cmap="gray" )
plt.show()
print(y_test[99] )
output = model(x_test[99].unsqueeze(0).to(device))
y_pred = output.argmax(dim=1)
print(y_pred)
```

# 第九章 循环神经网络
## 9.1 自然语言处理概述 NLP
Natural Language Processing, NLP 自然语言处理，让计算机能够理解和生成人类的语言

### 9.1.1 同义词词典
同义词归到同一类别中，根据关系构建层级树状图
### 9.1.2 计数
收集文本数据，构建语料库(corpus)
统计词频，分词，词关联ID，词向量化
所有词向量(word vector)汇总起来，形成一个共现矩阵(cooccurrence matrix)
### 9.1.3 推理
在已知上下文前提下，推测当前位置应该是什么词

## 9.2 词嵌入层
### 9.2.1 什么是词嵌入层




