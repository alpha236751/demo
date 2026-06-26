from common.functions import softmax, cross_entropy_error
import numpy as np
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
        
# SoftmaxwithLoss层
class SoftmaxwithLoss:
    def __init__(self):
        self.y = None
        self.t = None
        self.loss = None
    def forward(self, X, t):
        self.y = softmax(X)
        self.t = t
        self.loss = cross_entropy_error(self.y, self.t)
        return self.loss
    def backward(self, dout=1):
        n = self.t.shape[0]
        # 如果是独热编码 直接计算梯度
        if self.t.size == self.y.size:
            dx = (self.y - self.t) 
        else:
            dx = self.y.copy()
            dx[np.arange(n), self.t] -= 1
        return dx/n
    