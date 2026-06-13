import numpy as np
# 数值微分求导，x是一个标量 一元函数
def numerical_diff(f, x):
    h = 1e-4  # 0.0001
    return (f(x + h) - f(x - h)) / (2 * h)

# 数值微分求梯度，x是一个向量 多元函数
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