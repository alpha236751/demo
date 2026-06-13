# 阶跃函数
# def step_function0(x):
#     if x > 0:
#         return 1
#     else:
#         return 0
    
# 阶跃函数的矢量化实现
import numpy as np
def step_function(x):
    return np.array(x > 0, dtype=int)

# sigmoid函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# tanh函数
def tanh(x):
    return np.tanh(x)

# Relu函数
def relu(x):
    return np.maximum(0, x)

# softmax函数
def softmax0(x):
    return np.exp(x) / np.sum(np.exp(x))
def softmax(x):
    if x.ndim == 2:
        x = x - np.max(x, axis=1, keepdims=True) # 溢出对策 保持维度不变
        return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True) 
    x = x - np.max(x) # 溢出对策
    return np.exp(x) / np.sum(np.exp(x))

# 恒等函数
def identity_function(x):
    return x

# MSE损失函数
def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)

# 交叉熵损失函数
def cross_entropy_error(y, t):
    # 如果t是one-hot向量，则转换为正确标签的索引
    if t.size == y.size:
        t = t.argmax(axis=1)
    n = y.shape[0]
    return -np.sum(np.log(y[np.arange(n), t] + 1e-7)) / n       



if __name__ == '__main__':
    x = np.array([-1.0, 1.0, 2.0])
    print(step_function(x))
    print(sigmoid(x))
    print(tanh(x))
    print(relu(x))
