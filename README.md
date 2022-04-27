# NpNN-Numpy-Neural-Network

## 前言
本系列主要是为了巩固自己对深度学习的理解，而我个人对于繁杂的数学公式理解速度远慢于去阅读代码，因此选择使用numpy来从零构建神经网络。本仓库在实现的过程中完全不注重性能，底层直接使用numpy而非c++。在实现的过程中也会就一些问题展开讨论，希望能帮助到新接触到深度学习的小伙伴。

## 神经网络的构成
在使用numpy实现神经网络首先需要了解神经网络的组件,主要的组件包括层、激活函数、损失函数、优化器。
### 层
神经网络的基本数据结构是层(layer)。层是一个数据处理模块，将一个或多个输入张量转换为一个或多个输出张量。大多数的层是有权重的，神经网络训练的过程也就是权重迭代更新的过程。常见的层结构包括[全连接层](https://github.com/GuanyunFeng/NpNN-Numpy-Neural-Network/blob/main/Dense.md)、卷积层、池化层、循环层等等。还有一些特殊的层，例如Dropout层，Batch Norm层。

### 激活函数
激活函数主要的作用是去线性化，让神经网络能拟合更复杂的函数。本仓库中实现了relu、tanh、sigmoid、softmax。
### 损失函数
神经网络的目标是最小化损失函数, 损失函数的作用在于度量预测值和真实值之间的差异。常用的损失函数有均方误差、交叉熵等等。
### 优化器