import numpy as np

class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr
    # 参数和梯度均为字典
    def update(self, params, grads):
        for key in params.keys():
            params[key] -= self.lr * grads[key]

class Momentum:
    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None # 历史梯度
    def update(self, params, grads):
        if self.v is None: # 初始化历史梯度
            self.v = {}
            for key in params.keys():
                self.v[key] = np.zeros_like(params[key])

        for key in params.keys():
            self.v[key] = self.momentum * self.v[key] - self.lr * grads[key]
            params[key] += self.v[key]

class AdaGrad:
    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None # 历史梯度的平方和
    def update(self, params, grads):
        if self.h is None: # 初始化历史梯度的平方和
            self.h = {}
            for key in params.keys():
                self.h[key] = np.zeros_like(params[key])
        for key in params.keys():
            self.h[key] += grads[key] ** 2
            params[key] -= self.lr * grads[key] / np.sqrt(self.h[key] + 1e-7)

class RMSProp:
    def __init__(self, lr=0.01, decay=0.99):
        self.lr = lr
        self.decay = decay
        self.h = None # 历史梯度的平方和
    def update(self, params, grads):
        if self.h is None: # 初始化历史梯度的平方和
            self.h = {}
            for key in params.keys():
                self.h[key] = np.zeros_like(params[key])
        for key in params.keys():
            self.h[key] *= self.decay
            self.h[key] += ( 1 - self.decay) * (grads[key] ** 2)
            params[key] -= self.lr * grads[key] / np.sqrt(self.h[key] + 1e-7) 

class Adam: 
    def __init__(self, lr=0.01, alpha1=0.9, alpha2=0.999):
        self.lr = lr
        self.alpha1 = alpha1
        self.alpha2 = alpha2
        self.v = None # 历史梯度
        self.h = None # 历史梯度的平方和
        self.t = 0 # 迭代次数
    def update(self, params, grads):
        if self.v is None: # 初始化历史梯度
            self.v = {}
            self.h = {}
            for key in params.keys():
                self.v[key] = np.zeros_like(params[key])
                self.h[key] = np.zeros_like(params[key])
        self.t += 1
        lr_t = self.lr * np.sqrt(1 - self.alpha2 ** self.t) / (1 - self.alpha1 ** self.t)
        for key in params.keys():
            self.v[key] += (1 - self.alpha1) * (grads[key] - self.v[key])
            self.h[key] += (1 - self.alpha2) * (grads[key] ** 2 - self.h[key])
            params[key] -= lr_t * self.v[key] / np.sqrt(self.h[key] + 1e-7)
           