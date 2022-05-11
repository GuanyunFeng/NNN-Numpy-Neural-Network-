from turtle import forward
import numpy as np

class SGD():
    def __init(self, lr, momentum=0, weight_decay=0, dampening = 0):
        self.lr = lr
        self.momentum = momentum
        self.weight_decay = weight_decay
        self.dampening = dampening
        self.flag = True #第一轮为True,后续迭代均为False
        self.accumulate_momentum = 0
    
    def update(self, weight, grad):
        if self.weight_decay:
            grad = weight*self.weight_decay + grad
        if self.momentum:
            if self.flag:
                self.accumulate_m = grad
            else:
                self.accumulate_m = self.momentum*self.accumulate_m+ (1-self.dampening)*weight
                grad = self.accumulate_m
        weight -= self.lr* grad


class Adagrad():
    def __init(self, lr, weight_decay = 0):
        self.lr = lr
        self.weight_decay = weight_decay
        self.flag = True #第一轮为True,后续迭代均为False
    
    def update(self, weight, grad):
        if self.weight_decay:
            grad = weight*self.weight_decay + grad
        if self.flag:
            self.stat_sum = np.zeros_like(grad)
        self.stat_sum += grad**2
        weight -= self.lr*grad/(self.stat_sum**0.5 + 1e-10)


class RMSprop():
    def __init(self, lr):
        self.lr = lr
    
    def get_eta(self, grad):
        return self.lr*grad

class Adam():
    def __init(self, lr):
        self.lr = lr
    
    def get_eta(self, grad):
        return self.lr*grad