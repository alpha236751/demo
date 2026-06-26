# 第一章 机器学习概述

## 1.1 AI、ML和DL
- **人工智能**（Artificial Intelligence）：人工智能是一门让机器表现出类似人类智能行为的学科，旨在使机器能够执行诸如推理、学习、规划、决策和语言理解等任务。
- **机器学习**（Machine Learning）：机器学习是人工智能的一个子领域，强调通过数据训练模型，使其在没有明确编程规则的情况下，学会从数据中识别模式并做出预测或决策。
- **深度学习**（Deep Learning）：深度学习是机器学习的一个子领域，主要关注使用多层神经网络（深度神经网络）来从大量数据中提取特征和进行复杂任务处理。

## 1.2 基本术语

- 数据集(Data Set)
- 样本(Sample)
- 特征(Feature)
- 特征向量(Feature Vector)
- 标签(Lable)
- 模型(Model)
- 参数(Parameter):模型通过训练学习到的值
- 超参数(Hyper Parameter):用户设置的值，不能通过训练主动学习

# 第二章 机器学习基本理论

## 2.1 机器学习三要素

- 模型model
- 策略strategy:模型的评价标准
- 算法algorithm:模型的具体实现

## 2.2 方法分类(待补充)

- 有监督学习:有标签
  - 线性模型
    - 线性回归
    - lasso回归
    - 岭回归
    - 线性判别
    - 逻辑回归
  - KNN
  - 决策树
  - 朴素贝叶斯
  - 支持向量机 SVM
  - 神经网络
  - 集成学习
    - boosting
    - bagging
- 无监督学习:无标签
  - 聚类
    - K-means
    - 高斯混合聚类
    - 密度聚类
    - 层次聚类
    - 谱聚类
  - 降维
    - 主成分分析
    - 奇异值分解 SVD
    - t-SNE
    - 自编码器
- 半监督学习:混合
  - 半监督SVM
  - 图半监督学习
  - 生成模型
  - 协同训练
- 强化学习:在动态交互中产生最优数据
  - 动态规划
  - 蒙特卡洛树搜索
  - Q学习
  - 策略梯度算法
  - 模仿学习

## 2.3 建模流程

- 收集数据
- 数据清洗
- 特征工程
- 选择算法
- 模型训练
- 模型评估
- 模型优化
- 模型部署
  
## 2.4 特征工程(Feature Engineering)

### 2.4.1 什么是特征工程

将原始数据转换为可以更好表示问题的特征格式，帮助模型更好理解和学习数据中的规律

### 2.4.2 特征工程方法(待补充)

- 特征选择 
  - 过滤法 基于统计指标（如卡方、互信息）独立评价特征，不涉及学习器。
  - 包裹法 用学习器表现直接评价特征子集
  - 嵌入法 学习器内部自动进行特征选择（如Lasso、决策树特征重要性）
- 特征转换
  - 归一化
  - 标准化
  - 对数变换
  - 类别编码(独热编码、标签编码、目标编码、频率编码)
- 特征构造
  - 交互特征
  - 统计特征
  - 日期和时间特征
- 特征降维
  - 主成分分析(PCA)
  - 线性判别分析(LDA)
  - s-SNE(t分布随机近邻嵌入)
  - 自编码器

### 2.4.3 特征工程常用方法

- **低方差过滤法** 方差低表示特征基本一致，对预测影响不大，应过滤

```python
import numpy as np
# 特征选择 低方差过滤
from sklearn.feature_selection import VarianceThreshold  

vt = VarianceThreshold(0.01) # 过滤方差小于0.01的特征
X_filtered = vt.fit_transform(X)
```

- **相关系数法** 计算特征与目标变量的相关性，保留相关性高的
  - 皮尔逊相关系数(pearson)
  - 斯皮尔曼相关系数(spearman)

```python
import pandas as pd

# 计算每一个特征与标签的相关性 pandas对象内置方法
print(X.corrwith(y, method="pearson"))
```

- **主成分分析**(PCA) 将高维数据投影到低维空间 与单纯选择不同 要先提取出本质特征

```python
# 降维 PCA主成分分析
from sklearn.decomposition import PCA

pca = PCA(n_components=4) # 保留4个维度 若为小数表示保留对应比例维度
X_pca = pca.fit_transform(X)
```

## 2.5 模型评估和模型选择
模型选择时的评估，使用训练集 和 验证集 可以调整验证集，修改模型 
注意和测试集的区分

### 2.5.1 损失函数 loss function

- 0-1 损失函数
$$
L(Y, f(X)) = 
\begin{cases}
1, & Y \neq f(X) \\
0, & Y = f(X)
\end{cases}
$$

---

- 平方损失函数
$$
L(Y, f(X)) = (Y - f(X))^2
$$

---

- 绝对损失函数
$$
L(Y, f(X)) = |Y - f(X)|
$$

---

- 对数似然损失函数 适合概率分布函数
$$
L(Y, P(Y|X)) = -\log P(Y|X)
$$

### 2.5.2 经验误差emp

- 训练误差也叫**经验误差empirical error**、经验风险empirical risk
  $$R_{\text{emp}}(f) = \frac{1}{m} \sum_{i=1}^m L\big(y_i, f(x_i)\big)$$
- 类似的，在测试数据集上的误差，称为测试误差或**泛化误差generalization error**
- **经验风险最小化emperical risk minimizatio**n就是取经验风险最小的模型

### 2.5.3 欠拟合与过拟合fit

- **欠拟合**underfitting
  - 模型复杂度不足
  - 特征不足
  - 训练不充分
  - 正则化过强
- **过拟合**overfitting
  - 模型复杂度过高
  - 训练过长
  - 训练数据不足
  - 特征过多
```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression # 线性回归模型
from sklearn.preprocessing import PolynomialFeatures # 多项式
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 数据集
X = np.linspace(-3,3,300).reshape(-1,1)
y = np.sin(X) + np.random.uniform(-0.5,0.5,300).reshape(-1,1)
train_X, test_X, train_y, test_y = train_test_split(X,y,test_size=0.2)
model1 = LinearRegression()
model2 = LinearRegression()
model3 = LinearRegression()

# 欠拟合
x_train1 = train_X
x_test1 = test_X
model1.fit(x_train1,train_y)
# print(model1.coef_)
# print(model1.intercept_)

train_loss1 = mean_squared_error(train_y,model1.predict(x_train1))
test_loss1 = mean_squared_error(test_y,model1.predict(x_test1))

# 恰好拟合
poly5 = PolynomialFeatures(degree=5)
x_train2 = poly5.fit_transform(train_X)
x_test2 = poly5.transform(test_X)
model2.fit(x_train2,train_y)
# print(model2.coef_)
# print(model2.intercept_)

train_loss2 = mean_squared_error(train_y,model2.predict(x_train2))
test_loss2 = mean_squared_error(test_y,model2.predict(x_test2))

# 过拟合
poly20 = PolynomialFeatures(degree=20)
x_train3 = poly20.fit_transform(train_X)
x_test3 = poly20.transform(test_X)
model3.fit(x_train3,train_y)
# print(model3.coef_)
# print(model3.intercept_)

train_loss3 = mean_squared_error(train_y,model3.predict(x_train3))
test_loss3 = mean_squared_error(test_y,model3.predict(x_test3))

# 绘图
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(1, 3, figsize=(15,4))
ax[0].scatter(X,y,c="y")
ax[1].scatter(X,y,c="y")
ax[2].scatter(X,y,c="y")

ax[0].plot(X,model1.predict(X),"r")
ax[0].set_title("欠拟合 (线性回归)")
ax[0].text(-3,1.3,f"训练误差：{train_loss1:.4f}")
ax[0].text(-3,1,f"测试误差：{test_loss1:.4f}")

ax[1].plot(X,model2.predict(poly5.transform(X)),    "r")
ax[1].set_title("拟合适中 (5阶多项式)")
ax[1].text(-3,1.3,f"训练误差：{train_loss2:.4f}")
ax[1].text(-3,1,f"测试误差：{test_loss2:.4f}")

ax[2].plot(X,model3.predict(poly20.transform(X)),"r")
ax[2].set_title("过拟合 (20阶多项式)")
ax[2].text(-3,1.3,f"训练误差：{train_loss3:.4f}")
ax[2].text(-3,1,f"测试误差：{test_loss3:.4f}")

plt.show()
```

### 2.5.4 正则化Regularization

在损失函数中添加额外项来惩罚过大参数，限制模型复杂度，防止过拟合，提升模型泛化能力

1. **L1正则化(Lasso 回归)**
   $$Loss_{L1} = 原Loss + \lambda \sum_{i=1}^{k} |\omega_i|$$
2. **L2正则化(Ridge 回归)**
   $$Loss_{L2} = 原Loss + \lambda \sum_{i=1}^{k} \omega_i^2$$

> $\lambda$是正则化系数，控制正则化强度，太大可能会导致模型太简单欠拟合，太小可能导致模型复杂度升高过拟合

```python
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, Lasso, Ridge
from sklearn.preprocessing import PolynomialFeatures # 多项式
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# 数据集
X = np.linspace(-3,3,300).reshape(-1,1)
y = np.sin(X) + np.random.uniform(-0.5,0.5,300).reshape(-1,1)
train_X, test_X, train_y, test_y = train_test_split(X,y,test_size=0.2)

poly20 = PolynomialFeatures(degree=20)
x_train = poly20.fit_transform(train_X)
x_test = poly20.transform(test_X)

linear = LinearRegression()
lasso = Lasso(alpha=0.01)
ridge = Ridge(alpha=1)

# 不加正则化
linear.fit(x_train,train_y)
test_loss1 = mean_squared_error(test_y,linear.predict(x_test))

# lasso
lasso.fit(x_train,train_y)
test_loss2 = mean_squared_error(test_y,lasso.predict(x_test))

# ridge
ridge.fit(x_train,train_y)
test_loss3 = mean_squared_error(test_y,ridge.predict(x_test))

# 绘图
plt.rcParams['font.sans-serif'] = ['KaiTi']
plt.rcParams['axes.unicode_minus'] = False

fig, ax = plt.subplots(2, 3, figsize=(15,8))
ax[0,0].scatter(X,y,c="y")
ax[0,1].scatter(X,y,c="y")
ax[0,2].scatter(X,y,c="y")

ax[0,0].plot(X,linear.predict(poly20.transform(X)),"r")
ax[0,0].set_title("过拟合 (20阶多项式) ")
ax[0,0].text(-3,1.3,f"测试误差：{test_loss1:.4f}")
ax[1,0].bar(np.arange(21), linear.coef_.reshape(-1))

ax[0,1].plot(X,lasso.predict(poly20.transform(X)),"r")
ax[0,1].set_title("lasso正则化 ")
ax[0,1].text(-3,1.3,f"测试误差：{test_loss2:.4f}")
ax[1,1].bar(np.arange(21), lasso.coef_.reshape(-1))

ax[0,2].plot(X,ridge.predict(poly20.transform(X)),"r")
ax[0,2].set_title("ridge回归 ")
ax[0,2].text(-3,1.3,f"测试误差：{test_loss3:.4f}")
ax[1,2].bar(np.arange(21), ridge.coef_.reshape(-1))

plt.show()
```

### 2.5.5 交叉验证(Cross-Validation)

在选择模型时评估模型泛化能力，调优超参数

1. **简单交叉验证**(Hold-Out Validation)
   普通划分训练集和验证集，没有实际交叉
2. **k折交叉验证**(k-Fold Cross-Validation)
   将数据分为k个子集，k-1折用于训练，1折用于验证，重复k次，选平均指标
3. **留一交叉验证**(Leave-One-Out, LOO)
   极致的k折交叉验证，仅保留一个样本作为验证集，重复此过程直到所有样本都被验证过一次，适用于小数据集

## 2.6 模型求解
增加了正则化项的损失函数最小化，称为**结构风险最小化（Structural Risk Minimization, SRM）**。

$$
\min \frac{1}{n} \left( \sum_{i=1}^n L(y_i, f(x_i)) \right) + \lambda J(\theta)
$$
### 2.6.1 解析法
通过严格数学公式推导，求得模型模型损失函数结构风险最小化的解析解
仅适用于那些目标函数可导的简单的模型
- 线性回归：“最小二乘法”
$$Loss_{MSE} = \frac{1}{n} (X\beta - y)^T (X\beta - y)$$

$$\nabla Loss_{MSE} = \frac{2}{n} X^T (X\beta - y) = 0$$

$$\beta = (X^T X)^{-1} X^T y$$
- 线性回归：L2正则化
$$Loss_{L2} = \frac{1}{n} (X\beta - y)^T (X\beta - y) + \frac{1}{n} \lambda \beta^T \beta$$

$$\nabla Loss_{L2} = \frac{2}{n} X^T (X\beta - y) + \frac{2}{n} \lambda \beta = 0$$

$$\beta = (X^T X + \lambda I)^{-1} X^T y$$

### 2.6.2 梯度下降法gradient descent
$$
\theta_{k+1} = \theta_k - \alpha \cdot \nabla L(\theta_k)
$$
1. 分类
- 批量梯度下降(batch gradient descent, BGD)
  每次迭代使用全部训练数据计算梯度
- 随机梯度下降(stochastic gradient descent, SGD)
  每次迭代随机选取一个样本计算梯度
- 小批量梯度下降(Mini-batch gradient descent, MBGD)
  每次迭代使用一小批样本计算梯度
2. 应用
- L1正则化
- L2正则化
  
### 2.6.3 牛顿法和拟牛顿法(待补充)

## 2.7 模型评价指标

### 2.7.1 回归模型评价指标

- **平均绝对误差MAE**
$$MAE = \frac{1}{n}\sum_{i=1}^{n}|f(x_i)-y_i|$$
- **均方误差MSE**
$$MSE = \frac{1}{n}\sum_{i=1}^{n}\big(f(x_i)-y_i\big)^2$$
- **均方根误差RMSE**
$$RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}\big(f(x_i)-y_i\big)^2}$$
- **决定系数$R^2$**
$$R^2 = 1-\frac{\sum_{i=1}^{n}\big(f(x_i)-y_i\big)^2}{\sum_{i=1}^{n}\big(y_i-\bar{y}\big)^2}$$

### 2.7.2 分类模型评价指标

1. **混淆矩阵**(confusion matrix)

| 真实值\预测值 | 正例 | 负例 |
| ---- | ---- | ---- |
| 正例 | 真正例（True Positive, TP） | 假负例（False Negative, FN） |
| 负例 | 假正例（False Positive, FP） | 真负例（True Negative, TN） |
```python
import pandas as pd
from sklearn.metrics import confusion_matrix

label = ["猫", "狗"]  # 标签
y_true = ["猫", "猫", "猫", "猫", "猫", "猫", "狗", "狗", "狗", "狗"]  # 真实值
y_pred = ["猫", "猫", "狗", "猫", "猫", "猫", "猫", "猫", "狗", "狗"]  # 预测值

matrix = confusion_matrix(y_true, y_pred, labels=label) # 生成矩阵
print(pd.DataFrame(matrix, columns=label, index=label)) # 格式化矩阵
```

2. **准确率**(accuracy) 正确预测的比例 
$$Accuracy = \frac{TP+TN}{TP+TN+FP+FN}$$
```python
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_true, y_pred)
print(accuracy)
```

1. **精确率**(precision) 预测为正例的样本中实际正例的比例 关心假阳性
$$Precision = \frac{TP}{TP+FP}$$
```python
from sklearn.metrics import precision_score

precision = precision_score(y_true, y_pred, pos_label="猫")
print(precision)
```

4. **召回率**(recall) 实际为正例的样本中预测为正例的比例 关心假阴性
$$Recall = \frac{TP}{TP+FN}$$
```python
from sklearn.metrics import recall_score

recall = recall_score(y_true, y_pred, pos_label="猫")
print(recall)
```

5. **F1分数** 精确率和召回率的调和平均
$$F1 Score = \frac{2 \times Precision \times Recall}{Precision + Recall}$$
```python
from sklearn.metrics import f1_score

f1 = f1_score(y_true, y_pred, pos_label="猫")
print(f1)
```
  
> sklearn里有分类任务评估报告
> from sklearn.metrics import classification_report
> report = classification_report(y_true, y_pred, labels=label, target_names=None)

6. **ROC曲线**
- **真正例率(TPR)**：实际为正例，被预测为正例的比例，即召回率。
$$TPR = \frac{TP}{\text{实际正例数}} = \frac{TP}{TP+FN}$$

- **假正例率(FPR)**：实际为负例，被预测为正例的比例。
$$FPR = \frac{FP}{\text{实际负例数}} = \frac{FP}{FP+TN}$$

- **阈值(Threshold)**：根据阈值将概率转换为类别标签。

ROC 曲线（Receiver Operating Characteristic Curve，受试者工作特征）是评估二分类模型性能的工具，以假正例率（FPR）为横轴，以真正例率（TPR）为纵轴，展示不同阈值下模型的表现。绘制 ROC 曲线时，从高到低调整阈值，计算每个阈值的 TPR 和 FPR 并绘制所有阈值的点，形成 ROC 曲线。

7. **AUC**

AUC值代表ROC曲线下的面积，越大代表模型分类能力越强，0.5表示接近随机猜测，1表示完美模型

```python
from sklearn.metrics import roc_auc_score
roc_auc = roc_auc_score(y_test, y_pred_proba) # y_pred_proba 是正例的标签概率
print(roc_auc)
```

# 第三章 KNN算法 K Nearest Neighbors

## 3.1 KNN介绍
**K近邻算法**（K-Nearest Neighbors，KNN）是一种基本的分类与回归方法，属于监督学习算法。其核心思想是通过计算给定样本与数据集中所有样本的距离，找到距离最近的K个样本，然后根据这K个样本的类别或值来预测当前样本的类别或值。
### 3.1.1 工作原理
- 计算距离
- 选择K个近邻
- 投票或平均：
  - 分类任务：取最大值的类别
  - 回归任务：取平均值

### 3.1.2 特点
- K值：K值过小容易过拟合，K值过大容易欠拟合

> 计算量大，对噪声敏感，简单直观易于实现

### 3.1.3 代码实现

1. 分类
k可以取20以内的奇数，这样不用设置权重，只根据数量判定类别
```python
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

X = np.array([[2,1],[3,1],[1,4],[2,6]])
y = np.array([0,0,1,1])
knn = KNeighborsClassifier(2) # weights = 'distance' 设置k个近邻的距离权重
knn.fit(X,y)
x = np.array([[4,9]])
x_pred = knn.predict(x)
print(x_pred)

fig,ax = plt.subplots()
ax.axis('equal')
ax.scatter(X[:,0],X[:,1],c=y,vmin=0,vmax=1)
ax.scatter(x[:,0],x[:,1],c=x_pred,vmin=0,vmax=1)
plt.show()
```
2. 回归
```python
from sklearn.neighbors import KNeighborsRegressor

X = [[2,1],[3,1],[1,4],[2,6]]
y = [1,2,3,4]
knn = KNeighborsRegressor(2) # weights = 'distance' 设置权重
knn.fit(X,y)
x = [[4,9]]
x_pred = knn.predict(x)
print(x_pred)
```
## 3.2 常见距离度量方法

- **闵可夫斯基距离**是一种用于度量多维空间中两点间距离的通用方法，点$x(x_1,\dots,x_n)$和$y(y_1,\dots,y_n)$之间的闵可夫斯基距离：
$$
d(x,y)=\left(\sum_{i=1}^n \left(|x_i-y_i|\right)^p\right)^{\frac1p}
$$
$p$越小，对多个维度的差异更敏感；$p$越大，更关注最大维度的差异。

通过调整参数$p$，闵可夫斯基距离可以退化为以下经典距离：
- **曼哈顿距离：$p=1$**
$$d(x,y)=\sum_{i=1}^n |x_i-y_i|$$
- **欧氏距离：$p=2$**
$$d(x,y)=\sqrt{\sum_{i=1}^n (x_i-y_i)^2}$$
- **切比雪夫距离：$p=\infty$**
$$d(x,y)=\max\left(|x_i-y_i|\right)$$

## 3.3 归一化与标准化
### 3.3.1 归一化
将原始数据线性等比例缩放至固定区间 $[x_{min},x_{max}]$，工程常用区间：$\boldsymbol{[0,1]}$ 或 $\boldsymbol{[-1,1]}$
- 缩放到 $[0,1]$ 公式：
$$
x' = \frac{x-x_{min}}{x_{max}-x_{min}}
$$
- 缩放到 $[-1,1]$ 公式：
$$
x' = 2\times\frac{x-x_{min}}{x_{max}-x_{min}} -1
$$
> $x_{max}$：该特征样本最大值；$x_{min}$：该特征样本最小值
```python
from sklearn.preprocessing import MinMaxScaler

X = [[2, 1], [3, 1], [1, 4], [2, 6]]

X_scaled = MinMaxScaler((-1,1)).fit_transform(X) # 默认范围(0,1)
print(X_scaled)
```

### 3.3.2 标准化

将数据缩放为均值0、标准差1的标准分布，变换公式：
$$x' = \frac{x-\mu}{\sigma}$$
原始数据平均值：$\boldsymbol{\mu = \dfrac{\sum_{i=1}^{n}x_i}{n}}$
原始数据总体标准差：$\boldsymbol{\sigma = \sqrt{\dfrac{\sum_{i=1}^{n}(x_i-\mu)^2}{n}}}$
```python
from sklearn.preprocessing import StandardScaler
X = [[2, 1], [3, 1], [1, 4], [2, 6]]

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```
## 3.4 心脏病案例
```python
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

# 加载Heart Disease，设定为Dataframe格式
heart = fetch_openml(name="heart-disease", version=1, as_frame=True)
df = heart.data

# 数据集划分
x = df.iloc[:,:-1]
y = df["target"]
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

# 特征工程
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer # 对不同的特征做批量转换

columnTransformer = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), ["age", "restecg", "chol", "thalach", "oldpeak", "ca"]),
        # drop='first'：丢弃第一列，消除多重共线性
        ("category", OneHotEncoder(drop='first'), ["cp", "restecg", "slope", "thal"]),
        ("binary", "passthrough", ["sex", "fbs", "exang"])
    ]
)
x_train = columnTransformer.fit_transform(x_train)
x_test = columnTransformer.transform(x_test)

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train, y_train)
score = knn.score(x_test, y_test)

# 保存模型
import joblib
joblib.dump(knn, "knn_model.pkl")
# 加载模型
knn_loaded = joblib.load("knn_model.pkl")
# 测试
pred = knn_loaded.predict(x_test[4:5])
print(pred, y_test.iloc[4])
```
## 3.5 模型评估和超参数调优
### 3.5.1 网格搜索（Grid Search）
**网格搜索**（Grid Search）是一种系统化的超参数调优方法，通过遍历预定义的超参数组合，找到使模型性能最优的参数配置。通过自动化调参避免手动试错，提高效率。

网格搜索通常嵌套交叉验证，与交叉验证结合以提高调参的可靠性：
- **外层循环**：遍历参数网格中的每个参数组合。
- **内层循环**：对每个参数组合使用交叉验证评估模型性能。

### 3.5.2 心脏病案例超参数调优
```python
from sklearn.model_selection import GridSearchCV

# 设置网格参数
param_grid = {'n_neighbors': np.arange(1, 11)}
# 创建网格搜索器，cv=5：使用5折交叉验证
grid_search = GridSearchCV(knn, param_grid, cv=5)
grid_search.fit(x_train, y_train)

results = pd.DataFrame(grid_search.cv_results_)
# print(results)
print(grid_search.best_estimator_) # 输出最佳模型
print(grid_search.best_score_) # 最佳模型的CV平均分
```

# 第四章 线性回归 Linear Regression
## 4.1 线性回归简介
### 4.1.1 什么是线性回归
$$y=\beta_0+\beta_1 x_1+\beta_2 x_2+\cdots+\beta_n x_n$$
### 4.1.2 代码使用
```python
from sklearn.linear_model import LinearRegression

X = [[5], [8], [10], [12], [15], [3], [7], [9], [14], [6]]
y = [55, 65, 70, 75, 85, 50, 60, 72, 80, 58]

model = LinearRegression()
model.fit(X, y)
print(model.coef_)
print(model.intercept_)

x_test = [[11]]
y_pred = model.predict(x_test)
print(y_pred)
```

## 4.2 线性回归求解
### 4.2.1 损失函数
- **均方误差MSE**
  若误差服从正态分布，则均方误差对应极大似然估计，是最优损失函数
  假设因变量$y$与自变量$x$的关系为$y_i = \boldsymbol{\beta}^T \boldsymbol{x}_i + \epsilon_i$，$\epsilon_i$为误差项。
  当误差独立且具有相同分布，并且都服从正态分布时：
  $$
  p(\epsilon_i) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left(-\frac{\epsilon_i^2}{2\sigma^2}\right)
  $$
  将$y_i$与$x_i$代入：
  $$
  p(y_i|\boldsymbol{x}_i; \boldsymbol{\beta}) = \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left(-\frac{(y_i - \boldsymbol{\beta}^T \boldsymbol{x}_i)^2}{2\sigma^2}\right)
  $$
  似然函数：
  $$
  L(\boldsymbol{\beta}) = \prod_{i=1}^n p(y_i|\boldsymbol{x}_i; \boldsymbol{\beta})
  = \prod_{i=1}^n \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left(-\frac{(y_i - \boldsymbol{\beta}^T \boldsymbol{x}_i)^2}{2\sigma^2}\right)
  $$
  对数似然函数：
  $$
  \begin{align*}
  \ln L(\boldsymbol{\beta}) &= \ln \prod_{i=1}^n \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left(-\frac{(y_i - \boldsymbol{\beta}^T \boldsymbol{x}_i)^2}{2\sigma^2}\right) \\
  &= -n\ln\sqrt{2\pi}\sigma - \frac{1}{2\sigma^2}\sum_{i=1}^n \big(y_i - \boldsymbol{\beta}^T \boldsymbol{x}_i\big)^2
  \end{align*}
  $$
  为使似然函数最大，需求解$\displaystyle \frac{1}{2\sigma^2}\sum_{i=1}^n(y_i - \boldsymbol{\beta}^T \boldsymbol{x}_i)^2 = \frac{1}{2\sigma^2}\sum_{i=1}^n\big(y_i - f(\boldsymbol{x}_i)\big)^2$的最小值，发现其与均方误差直接相关。
  即**最大化对数似然函数等价于最小化均方误差**。
- **平均绝对误差MAE**

### 4.2.2 一元线性回归解析解
对MSE分别以各个参数为自变量求偏导，令两个偏导等于0，两个方程两个未知数，联立求解
$$
f(x_i) = \beta_0 + \beta_1 x_i
$$

$$
MSE = \frac{1}{n} \sum_{i=1}^n (\beta_0 + \beta_1 x_i - y_i)^2
$$
### 4.2.3 正规方程法(解析法)
$$
\begin{aligned}
MSE &= \frac{1}{n} \sum_{i=1}^n (f(x_i) - y_i)^2 \\
&= \frac{1}{n} \sum_{i=1}^n \left( (\beta_0 + \beta_1 x_{i1} + \beta_2 x_{i2} + \cdots + \beta_m x_{im}) - y_i \right)^2 \\
&= \frac{1}{n} \sum_{i=1}^n (\beta^T x_i - y_i)^2 \\
&= \frac{1}{n} \|X\beta - y\|_2^2 \\
&= \frac{1}{n} (X\beta - y)^T (X\beta - y)
\end{aligned}
$$
$X: n \times (m+1)$ 的矩阵，包含一个全 1 的列

$$
X = 
\begin{bmatrix}
1 & x_{11} & x_{12} & \cdots & x_{1m} \\
1 & x_{21} & x_{22} & \cdots & x_{2m} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_{n1} & x_{n2} & \cdots & x_{nm}
\end{bmatrix}
$$

$\beta: (m+1) \times 1$ 的参数向量（包含截距项 $\beta_0$）

$$
\beta = 
\begin{bmatrix}
\beta_0 \\
\beta_1 \\
\vdots \\
\beta_m
\end{bmatrix}
$$

$y: n \times 1$ 的因变量向量

对 $\beta$ 求偏导

$$
\begin{aligned}
\frac{\partial MSE}{\partial \beta} &= \frac{\partial}{\partial \beta} \left( \frac{1}{n} (X\beta - y)^T (X\beta - y) \right) \\
&= \frac{2}{n} X^T (X\beta - y)
\end{aligned}
$$

当 $X^T X$ 为满秩矩阵或正定矩阵时，令偏导等于 0

$$
\frac{2}{n} X^T X \beta - \frac{2}{n} X^T y = 0
$$

$$
X^T X \beta = X^T y
$$

$$
\beta = (X^T X)^{-1} X^T y
$$

正规方程法适用于特征数量较少的情况。当特征数量较大时，计算逆矩阵的复杂度会显著增加，此时梯度下降法更为适用。

### 4.2.4 梯度下降法
假设目标函数为 $J(\beta)$，其中 $\beta$ 是模型参数。梯度下降的更新公式为：

$$
\beta_{t+1} = \beta_t - \alpha \cdot \nabla J(\beta_t)
$$

$\alpha$：学习率（Learning Rate），用于控制步长

$\nabla J(\beta_t)$：目标函数在 $\beta_t$ 处的梯度（偏导数组成的向量）
$$
J(\beta) = \frac{1}{n} \|X\beta - y\|_2^2
$$

$$
\nabla J(\beta) = \frac{2}{n} X^T (X\beta - y)
$$
```python
from sklearn.linear_model import SGDRegressor
import numpy as np
x = np.array([[5], [8], [10], [12], [15], [3], [7], [9], [14], [6]])
y = np.array([55, 65, 70, 75, 85, 50, 60, 72, 80, 58])

model = SGDRegressor(
    penalty=None, # 惩罚项 正则化项
    loss="squared_error", # 损失函数
    max_iter=1000, # 最大迭代次数
    eta0=0.01, # 学习率
    learning_rate="constant", # 学习率策略
    tol=1e-3, # 停止迭代条件
)
model.fit(x, y)
print(model.coef_, model.intercept_)
```

# 第五章 逻辑回归 Logistic Regression
## 5.1 逻辑回归简介
### 5.1.1 什么是逻辑回归
逻辑回归主要用于解决分类问题，尤其是二分类问题
逻辑回归通过将线性回归输出映射到$[0,1]$区间上，来表示某个类别的概率
常用的映射函数是 sigmoid 函数：

$$
f(x) = \frac{1}{1+e^{-x}}
$$

其导数：

$$
f'(x) = f(x)(1-f(x))
$$
逻辑回归结果可表示为：
$$
P(y = 1 \mid x) = \frac{1}{1 + e^{-(\beta_0 + \beta_1 x_1 + \beta_2 x_2 + \cdots + \beta_n x_n)}}
$$

### 5.1.2 逻辑回归损失函数
逻辑回归的损失函数通常使用对数损失（Log Loss），也称为二元交叉熵损失（Binary Cross-Entropy Loss），用于衡量模型输出的概率分布与真实标签之间的差距。逻辑回归的损失函数来源于最大似然估计（MLE）。

$P(Y|X; \beta)$ 表示给定输入特征 $x$ 和模型参数 $\beta$ 时，因变量 $y$ 发生的概率：

$$
P(y = 1|x; \beta) = \frac{1}{1 + e^{-(\beta^T x)}}
$$

$$
P(y = 0|x; \beta) = 1 - P(y = 1|x; \beta) = 1 - \frac{1}{1 + e^{-(\beta^T x)}}
$$

整合：

$$
P(y|x; \beta) = P(y = 1|x; \beta)^y (1 - P(y = 1|x; \beta))^{1-y}
$$

$$
= \left( \frac{1}{1 + e^{-(\beta^T x)}} \right)^y \left( 1 - \frac{1}{1 + e^{-(\beta^T x)}} \right)^{1-y}
$$

似然函数 $L(\beta)$ 表示已知 $y$ 的结果，此时模型参数为 $\beta$ 的概率：

对于 1 个样本：

$$
L(\beta) = P(y|x; \beta) = P(y = 1|x; \beta)^y (1 - P(y = 1|x; \beta))^{1-y}
$$

对于 n 个样本：

$$
L(\beta) = \prod_{i=1}^n P(y_i|x_i; \beta) = \prod_{i=1}^n P(y_i = 1|x_i; \beta)^{y_i} (1 - P(y_i = 1|x_i; \beta))^{1-y_i}
$$

取对数似然：

$$
\log L(\beta) = \sum_{i=1}^n \left( y_i \log P(y_i = 1 | x_i; \beta) + (1 - y_i) \log (1 - P(y_i = 1 | x_i; \beta)) \right)
$$

拟合的过程就是求解似然函数的最大值，为了方便优化，令损失函数

$$
\begin{aligned}
Loss &= -\frac{1}{n} \log L(\beta) \\
&= -\frac{1}{n} \sum_{i=1}^n \left( y_i \log P(y_i = 1 | x_i; \beta) + (1 - y_i) \log (1 - P(y_i = 1 | x_i; \beta)) \right)
\end{aligned}
$$

### 5.1.3 损失函数求梯度
略
### 5.1.4 API使用
```python
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression

heart = fetch_openml(name="heart-disease", version=1, as_frame=True)
df = heart.data
X = df.drop("target", axis=1)
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

columnTransformer = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), ["age", "restecg", "chol", "thalach", "oldpeak", "ca"]),
        # drop='first'：丢弃第一列，消除多重共线性
        ("category", OneHotEncoder(drop='first'), ["cp", "restecg", "slope", "thal"]),
        ("binary", "passthrough", ["sex", "fbs", "exang"])
    ]
)
X_train = columnTransformer.fit_transform(X_train)
X_test = columnTransformer.transform(X_test)

model = LogisticRegression()
model.fit(X_train, y_train)
print("训练集得分：", model.score(X_train, y_train))
print("测试集得分：", model.score(X_test, y_test))
```

## 5.2 多分类任务
### 5.2.1 一对多OVR One-vs-Rest
把每一个类单独拿出算其作为正类的二分类概率
```python
from sklearn.multiclass import OneVsRestClassifier
from sklearn.model_selection import LogisticRegression

model_ovr = OneVsRestClassifier(LogisticRegression())
```

### 5.2.2 Softmax回归 (多项逻辑回归)
若有 $C$ 个类别，模型将输出 $C$ 个分数。

对于类别 $c$，

$$
P(y = c \mid x) = \frac{e^{\beta_c^T x}}{\sum_{j=1}^c e^{\beta_j^T x}}
$$

损失函数

$$
Loss = -\frac{1}{n} \sum_{i=1}^n \sum_{c=1}^C I(y_i = c) \log P(y_i = c \mid x_i)
$$

其中 $I(y_i = c)$ 为示性函数，当 $y_i = c$ 时值为 $1$，反之值为 $0$。
```python
from sklearn.model_selection import LogisticRegression

model_softmax = LogisticRegression(
    multi_class='multinomial' # 多项式回归(softmax)
)
```
## 5.3 手写数字识别案例
```python
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.linear_model import LogisticRegression
import pandas as pd
import matplotlib.pyplot as plt

X = datasets.load_digits().data
y = datasets.load_digits().target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(max_iter=500)
model.fit(X_train, y_train)
accuracy = model.score(X_test, y_test)
print(f"Accuracy: {accuracy:.2f}")

test = X_test_scaled[0].reshape(1, -1)
print(f"Predicted: {model.predict(test)[0]}, Actual: {y_test[0]}, probability: {model.predict_proba(test)[0]}")
plt.imshow(X_test[0].reshape(8, 8), cmap='gray')
plt.show()
```

# 第六章 感知机 Perceptron
## 6.1 感知机的概念
感知机（Perceptron）是机器学习中最基础的线性二分类模型，由 Frank Rosenblatt 在 1957 年提出。可以把它理解为一个模拟神经元工作的简单数学模型——它接收多个输入信号，分别乘以对应的权重并求和，再加上偏置，最后通过一个阶跃函数来决定输出 +1 或 -1（或 0/1）

## 6.2 简单逻辑电路
1. 与门 AND gate
2. 与非门 NAND gate
3. 或门 OR gate
## 6.3 感知机实现
```python
import numpy as np

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    tmp = (w @ x) + b
    if tmp <= 0 :
        return 0
    else:        
        return 1

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5])
    b = 0.7
    tmp = (w @ x) + b
    if tmp <= 0 :
        return 0
    else:        
        return 1 

def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.2
    tmp = (w @ x) + b
    if tmp <= 0 :
        return 0
    else:        
        return 1
```

## 6.4 感知机的局限
感知机只能解决**线性可分问题**（例如 AND、OR 函数），但对经典的**非线性问题** XOR（异或） 无能为力。

## 6.5 多层感知机
```python
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y
```

# 第七章 其他监督学习算法
## 7.1 朴素贝叶斯算法 naive Bayes
### 7.1.1 朴素贝叶斯法简介
朴素贝叶斯法的核心是贝叶斯定理：

$$
P(Y|X) = \frac{P(X|Y)P(Y)}{P(X)}
$$

- $P(Y|X)$: 后验概率，给定特征 $X$ 时类 $Y$ 的概率。
- $P(X|Y)$: 条件概率，类 $Y$ 包含特征 $X$ 的概率。
- $P(Y)$: 先验概率，类 $Y$ 的概率。
- $P(X)$: 特征 $X$ 的概率。

朴素贝叶斯假设所有特征相互独立，这使得我们无需考虑特征之间复杂的依赖关系，极大简化了条件概率的计算：

$$
P(X_1, X_2, ..., X_n|Y) = P(X_1|Y) \cdot P(X_2|Y) \cdot ... \cdot P(X_n|Y) = \prod_{j=1}^n P(X_j|Y)
$$

### 7.1.2 极大似然估计
先验概率 $P(Y = C_k)$（$Y$ 为类 $C_k$）的极大似然估计：

$$
P(Y = C_k) = \frac{\sum_{i=1}^N I(y_i = C_k)}{N}, \quad k = 1, 2, \dots, K
$$

条件概率 $P(X_j = a_{jl} \mid Y = C_k)$（$Y$ 为类 $C_k$ 时第 $j$ 个特征 $X_j$ 为 $a_{jl}$）的极大似然估计：

$$
P(X_j = a_{jl} \mid Y = C_k) = \frac{\sum_{i=1}^N I(x_{ji} = a_{jl}, y_i = C_k)}{\sum_{i=1}^N I(y_i = C_k)}
$$

$$
j = 1, 2, \dots, n; \quad l = 1, 2, \dots, L; \quad k = 1, 2, \dots, K
$$

其中 $I$ 为示性函数，取值为 1 或 0。

### 7.1.3 贝叶斯估计
使用极大似然估计可能会出现所要估计的概率值为 0 的情况，这会影响到后验概率的计算结果，使分类产生偏差。  
解决方法是将贝叶斯估计。

先验概率的贝叶斯估计：

$$
P_{\lambda}(Y = C_k) = \frac{\sum_{i=1}^N I(y_i = C_k) + \lambda}{N + K\lambda}, \quad k = 1, 2, \dots, K
$$

条件概率的贝叶斯估计：

$$
P_{\lambda}(X_j = a_{jl} \mid Y = C_k) = \frac{\sum_{i=1}^N I(x_{ji} = a_{jl}, y_i = C_k) + \lambda}{\sum_{i=1}^N I(y_i = C_k) + L\lambda}
$$

$$
j = 1, 2, \dots, n; \quad l = 1, 2, \dots, L; \quad k = 1, 2, \dots, K
$$

式中 $\lambda \geq 0$，当 $\lambda = 0$ 时就是极大似然估计，常取 $\lambda = 1$，这时称为拉普拉斯平滑。

### 7.1.4 学习和分类过程
学习时，计算先验概率：

$$
P(Y = C_k), \quad k = 1, 2, ..., K
$$

和条件概率：

$$
P(X_j = a_{jl} \mid Y = C_k), \quad j = 1, 2, ..., n; \quad l = 1, 2, ..., L; \quad k = 1, 2, ..., K
$$

分类时，根据给定的实例 $x = (x_1, x_2, ..., x_n)$ 计算后验概率：

$$
P(Y = C_k) \prod_{j=1}^n P(X_j = x_j \mid Y = C_k), \quad k = 1, 2, ..., K
$$

并确定实例 $x$ 属于哪一个类别：

$$
y = \arg\max_{C_k} P(Y = C_k) \prod_{j=1}^n P(X_j = x_j \mid Y = C_k), \quad k = 1, 2, ..., K
$$

## 7.2 决策树 Decision Tree
### 7.2.1 决策树简介
决策树适用于需要规则化、可解释性和快速决策的场景，尤其在数据特征明确、样本量适中的情况下表现良好。在复杂任务中，它常作为基础模型，与集成学习结合（如随机森林、梯度提升树）以提升性能。
### 7.2.2 决策树工作过程
1. 特征选择
   选择最优特征，使得子集在当前条件下得到最好的划分。
2. 决策树生成
   迭代划分，直到所有训练数据被基本正确分类
3. 决策树剪枝
   
### 7.2.3 特征选择与决策树生成
1. **信息熵** Entropy
信息熵（Entropy）是表示随机变量不确定性的度量，设 $X$ 是一个取有限个值的离散随机变量，其概率分布为：
$$
P(X = x_i) = p_i, \quad i = 1, 2, \dots, n
$$
随机变量 $X$ 的熵定义为：
$$
H(X) = -\sum_{i=1}^n p_i \log p_i
$$
若 $p_i = 0$，则定义 $0 \log 0 = 0$。通常式中对数以 2 或 e 为底。
在 $n = 2$ 的情况下，假设 $X$ 的概率分布为：
$$
P(X = 1) = p, \quad P(X = 0) = 1 - p
$$
则 $X$ 的信息熵为：
$$
H(X) = -p \cdot \log p - (1 - p) \cdot \log (1 - p)
$$
熵只依赖于 $X$ 的分布，与 $X$ 的取值无关。熵越大，随机变量的不确定性就越大。
设有随机变量 $(X, Y)$，其联合概率分布为：
$$
P(X = x_i, Y = y_j) = p_{ij}, \quad i = 1, 2, \dots, n; \quad j = 1, 2, \dots, m
$$
条件熵 $H(Y|X)$ 表示在已知随机变量 $X$ 的条件下，随机变量 $Y$ 仍然保留的不确定性：
$$
H(Y|X) = \sum_{i=1}^n P(X = x_i) \, H(Y|X = x_i)
$$
2. **信息增益**与ID3
决策树学习应用信息增益（Information Gain）准则选择特征，给定训练集数据 $D$ 和特征 $A$，熵 $H(D)$ 表示对数据集进行分类的不确定性，条件熵 $H(D|A)$ 表示在特征 $A$ 给定条件下对数据集 $D$ 进行分类的不确定性。两者之差即信息增益：
$$g(D, A) = H(D) - H(D|A)$$
3. **信息增益率**与C4.5
使用信息增益划分训练数据集的特征，会倾向于选择取值较多的特征。而使用信息增益率（Information Gain Ratio）可以对这一问题进行校正，这是特征选择的另一个准则。
特征 \( A \) 对训练数据集 \( D \) 的信息增益率 \( g_R(D, A) \) 定义为信息增益 \( g(D, A) \) 与训练数据集 \( D \) 关于特征 \( A \) 的值的熵 \( H_A(D) \) 之比：
$$g_R(D, A) = \frac{g(D, A)}{H_A(D)}$$
其中 \( H_A(D) = -\sum_{i=1}^n \frac{|D_i|}{|D|} \log_2 \frac{|D_i|}{|D|} \)，\( n \) 是特征 \( A \) 的取值个数。
4. **基尼系数**与CART
有 \( K \) 个类，样本属于第 \( k \) 类的概率为 \( p_k \)，则概率分布的基尼指数：
$$Gini(p) = \sum_{k=1}^K p_k (1 - p_k) = 1 - \sum_{k=1}^K p_k^2$$
对于给定的样本集合 \( D \)，其基尼指数：
$$Gini(D) = 1 - \sum_{k=1}^K \left( \frac{|C_k|}{|D|} \right)^2$$
这里 \( C_k \) 是 \( D \) 中属于第 \( k \) 类的样本子集，\( K \) 是类的个数。
如果样本集合 \( D \) 根据特征 \( A \) 是否取某一可能值 \( a \) 被划分为两个子集 \( D_1, D_2 \)，则在特征 \( A \) 的条件下，集合 \( D \) 的基尼指数：
$$Gini(D, A) = \frac{|D_1|}{|D|} Gini(D_1) + \frac{|D_2|}{|D|} Gini(D_2)$$
基尼指数 \( Gini(D) \) 表示集合 \( D \) 的不确定性，基尼指数 \( Gini(D, A) \) 表示经 \( A = a \) 划分后集合 \( D \) 的不确定性。基尼指数越大样本集合的不确定性也越大，这与信息熵相似。
CART 决策树是一棵二叉树，根据基尼指数生成决策树，对训练数据集 \( D \) 的每个特征 \( A \) 的每一个可能的取值 \( a \)，计算 \( A = a \) 时的基尼指数，选择基尼指数最小的特征及其对应的切分点作为最优特征与最优切分点，并生成两个子节点，将训练数据集依特征分配到两个子节点中。重复上述过程，直到节点中样本数小于阈值、或样本集的基尼指数小于阈值、或没有更多特征。
5. CART回归树
对应空间上的划分
最终区域的平均值作为目标值
由此生成的回归树称为**最小二乘回归树**

### 7.2.4 剪枝 Pruning
可以分为**预剪枝**(pre-pruning)和**后剪枝**(post-pruning)
预剪枝
**预剪枝**是在决策树生成过程中，通过设置一些限制条件提前停止树的生长，避免过度分裂。常见的停止条件有：限制最大树深度、限制每个节点最小样本数、限制最小的误差减少量、限制最大叶节点数量等。但过于严格的停止条件可能导致欠拟合，并且可能难以确定最佳阈值，需要多次尝试。
**后剪枝**是在决策树完全生成之后，基于某种评估准则从底部向上逐步判断是否移除分支。常见的后剪枝方法有代价复杂度剪枝（Cost-Complexity Pruning，CCP）和减少误差剪枝（Reduced Error Pruning，REP）等。

## 7.3 支持向量机 SVM
### 7.3.1 支持向量机简介
支持向量机（Support Vector Machines，SVM）是一种二分类模型。其核心目标是寻找一个**“间隔最大”的超平面**将不同类别的数据点分隔开。这个超平面在二维空间中是一条直线，在三维空间中是一个平面，在更高维空间中则是一个超平面。
分类：线性可分支持向量机、线性支持向量机、非线性支持向量机

### 7.3.2 线性可分支持向量机-硬间隔
1. 硬间隔
当训练样本线性可分时，此时可以通过最大化硬间隔来学习线性可分支持向量机。硬间隔是指超平面能够将不同类的样本完全划分开。距离超平面最近的几个样本点称为支持向量，它们直接决定超平面的位置和方向，只要支持向量不变，超平面就不会变。
在样本空间中，超平面可表示为  
$$
w^T x + b = 0
$$  
其中 \( w = (w_1, w_2, \dots, w_n) \) 为法向量，决定了超平面的方向；\( b \) 为位移项，决定了超平面与原点之间的距离。将超平面记为 \( (w, b) \)
相应的分类函数称为线性可分支持向量机：  
$$
f(x) = \text{sign}(w^T x + b)
$$

2. 间隔与最大间隔
\( x' \) 为超平面上一点，\( w^T x' + b = 0 \)，样本空间中任一点 \( x \) 到超平面 \( (w, b) \) 的距离为：
$$
r = \left| \frac{w^T (x - x')}{\|w\|} \right| = \frac{|w^T x + b|}{\|w\|}
$$
记每个样本点 \(x_i\) 的类别为 \(y_i\)，该样本点的函数间隔 \(\hat{y}_i = y_i(w^T x + b)\)，表示分类预测的正确性及确信度，若超平面 \((w, b)\) 能将样本正确分类，则有
$$\begin{cases} 
w^T x_i + b > 0, & y_i = +1 \\ 
w^T x_i + b < 0, & y_i = -1 
\end{cases}$$
此时有
$$y_i(w^T x_i + b) = |w^T x_i + b| > 0$$
$$\hat{y}_i = \frac{|w^T x_i + b|}{||w||} = \frac{y_i(w^T x_i + b)}{||w||} = \frac{\hat{y}_i}{||w||}$$
我们注意到对 \(w, b\) 进行缩放变换 \(w \to \lambda w, b \to \lambda b\) 时，不会改变超平面，也不会改变 \(r\) 的值，但函数间隔 \(\hat{y}_i = y_i(w^T x_i + b)\) 会随着缩放 \(w\) 和 \(b\) 而发生变化。也就是说可以通过缩放 \(w\) 和 \(b\) 来任意缩放函数间隔 \(\hat{y}_i\) 而不改变 \(r_i\)。
因此令支持向量到超平面的函数间隔 \(\hat{y}_i = 1\)，此时支持向量到超平面的距离 \(r_i = \frac{\hat{y}_i}{||w||} = \frac{1}{||w||}\)。两个异类支持向量到超平面的距离之和 \(\gamma = \frac{2}{||w||}\)，\(\gamma\) 被称为“间隔”。
欲找到具有最大间隔的超平面，也就是求在约束 \( y_i(w^T x_i + b) \geq 1 \) 下最大的 \( y_i \)：
$$\max_{w,b} \frac{2}{\|w\|}$$
s.t. \( y_i(w^T x_i + b) \geq 1 \)
等价于：
$$\min_{w,b} \frac{\|w\|^2}{2}$$
s.t. \( y_i(w^T x_i + b) \geq 1 \)
s.t. 为 Subject to，意为约束。
上式就是支持向量机的基本型。对上式使用拉格朗日乘子法得到其对偶问题，从对偶问题中解出拉格朗日乘子，进而解出 \( w, b \)，即可得到具有最大间隔的超平面。

### 7.3.3 线性支持向量机-软间隔
线性不可分意味着某些样本点 \((x_i, y_i)\) 不能满足约束条件 \(y_i(w^T x_i + b) \geq 1\)。为解决这个问题，可以对每个样本点引进一个松弛变量 \(\xi_i \geq 0\)，使得函数间隔加上松弛变量 \(\geq 1\)。这时约束条件变为：

$$y_i(w^T x_i + b) \geq 1 - \xi_i$$

同时为了在最大化间隔的时候使不满足约束的样本尽可能少，目标函数中引入对误分类的惩罚：

$$\frac{\|w\|^2}{2} + C \sum_{i=1}^n \xi_i$$

这里 \(C > 0\) 为惩罚系数，\(C\) 值越大对误分类的惩罚越大。

线性不可分的线性支持向量机的学习问题可表示如下：

$$\min_{w, b, \xi} \frac{\|w\|^2}{2} + C \sum_{i=1}^n \xi_i$$

s.t. 

$$y_i(w^T x_i + b) \geq 1 - \xi_i$$

### 7.3.4 非线性支持向量机-核函数
通过**核函数**将数据从原始空间映射到高维特征空间，使得数据在高维特征空间线性可分，将原本的非线性问题转换为线性问题。使用核技巧学习非线性支持向量机，等价于隐式地在高维特征空间中学习线性支持向量机。

## 7.4 集成学习 Ensemble Learning
**集成学习**（Ensemble Learning）通过某种策略组合多个个体学习器的预测结果来提高整体的预测能力。只包含同种类型的个体学习器的集成称为同质集成，例如决策树集成中全是决策树，同质集成中的个体学习器亦称基学习器，相应的学习算法称为基学习算法。包含不同类型的个体学习器的集成称为异质集成，例如同时包含决策树和神经网络。

集成学习有三大经典方法：**Boosting**、**Bagging** 和 **Stacking**。

**Boosting**（提升方法）按顺序训练模型，每个模型关注前一个模型的错误，通过加权调整来优化整体预测。如 AdaBoost 通过给错分的样本更大的权重，逐步改进；梯度提升树用梯度下降法优化损失函数；XGBoost 和 LightGBM 是高效的梯度提升树变种。Boosting 主要关注于**降低偏差**。

**Bagging**（Bootstrap Aggregating，自助聚合）从原始数据集中通过有放回的对样本采样生成多个子数据集，分别训练多个独立模型，最后通过投票（分类）或平均（回归）得到结果。**随机森林**则是在 Bagging 基础上随机选择特征子集训练每棵树。Bagging 主要关注于降低方差。

**Stacking**（堆叠）训练多个不同类型的个体学习器，之后使用一个元模型综合多个个体学习器的预测。灵活性强，能结合多种模型的优势。

### 7.4.1 AdaBoost
对于分类问题而言，给定一个训练样本集，求比较粗糙的分类规则（弱分类器）要比求精确的分类规则（强分类器）容易的多。Boosting 就是从弱学习算法出发，反复学习，得到一系列弱分类器，然后组合这些弱分类器构成一个强分类器。**AdaBoost** 通常使用**单层决策树**作为基学习器，单层决策树也被称为决策树桩（Decision Stump）。

大多数 Boosting 都是改变训练数据的概率分布（权重分布），针对不同的训练数据分布调用弱学习算法学习一系列弱分类器。AdaBoost（Adaptive Boosting，自适应提升）的做法是提高被前一轮弱分类器错误分类的样本的权重，降低被正确分类的样本的权重。这样一来后一轮弱学习器会更加关注那些没有被正确分类的数据。同时采用加权多数表决的方法，加大分类误差率小的弱分类器的权重，减小分类误差率大的弱分类器的权重。

### 7.4.2 随机森林
随机森林是 Bagging 的一个变体，在以决策树为基学习器构建 Bagging 集成的基础上，进一步在决策树训练过程中引入了随机属性选择。

具体来说，传统决策树在选择划分特征时是在当前节点的特征集合（假定有 \(d\) 个特征）中选择最优特征。而在随机森林中，基决策树的每个节点先从该节点的特征集合中随机选择一个包含 \(k\) 个特征的子集，然后再从这个子集中选择一个最优特征用于划分。参数 \(k\) 控制着随机性的引入程度，若 \(k = d\)，则基决策树的生成与传统决策树相同；若 \(k = \lfloor \frac{n}{d} \rfloor\)，则随机选择一个属性用于划分。一般推荐 \(k = \log_2 d\)。

随机森林简单易实现，但在很多任务中都展现出了强大性能，被誉为“代表集成学习技术水平的方法”。Bagging 中基学习器的多样性仅来自于样本扰动，而随机森林中基学习器的多样性不仅来自样本扰动，还来自特征扰动，这就使得最终集成的泛化性能可通过基学习器之间差异度的增加而进一步提升。

# 第八章 无监督学习
## 8.1 聚类 clustering
### 8.1.1 聚类简介
聚类（Clustering）旨在将数据集中的样本分成若干个簇，使得同一个簇内的对象彼此相似，不同簇间的对象差异较大。聚类是一种无监督学习算法，不需要预先标记数据的标签，完全依赖数据本身内在结构和特征来进行分组，最终簇所对应的概念语义需由使用者来把握和命名。

聚类的核心是“物以类聚”，具体通过以下步骤实现：

- 定义相似性：选择一个度量标准（如欧氏距离，余弦相似度）来衡量对象之间的相似性或距离。

- 分组：根据相似性将对象分配到不同的簇中。

- 优化：通过迭代或直接计算，调整簇的划分，使簇内相似性最大化，簇间差异最大化。

### 8.1.2 常见聚类算法
1. K均值聚类
K 均值聚类（K-means）是基于样本集合划分的聚类方法，将样本集合划分为 \( k \) 个子集构成 \( k \) 个簇，将 \( n \) 个样本分到 \( k \) 个簇中，每个样本到其所属簇的中心的距离最小。每个样本只能属于一个簇，所以 K 均值聚类是硬聚类。
- 初始化，随机选择 \( k \) 个样本点作为初始簇中心。
- 对样本进行聚类，计算每个样本到各个簇中心的距离，将每个样本分到与其最近的簇，构成聚类结果。
- 计算聚类结果中每个簇中所有样本的均值，作为新的簇中心。
- 使用新的簇中心重复上述过程，直到收敛或符合停止条件（例如划分不再改变）。

2. 层次聚类
层次聚类（Hierarchical Clustering）假设簇之间存在层次结构，将样本聚到层次化的簇中。层次聚类有自下而上的聚合方法和自上而下的分裂方法。因为每个样本只属于一个簇，所以层次聚类属于硬聚类。
聚合聚类：开始将每个样本各自分到一个簇，之后将相距最近的两个簇合并，如此往复直至满足停止条件（例如达到预设的簇的个数、每个簇只包含一个样本、簇内样本相似性达到某个阈值等）。
分裂聚类：开始将整个数据集视作一个整体，之后根据某种距离或相似性度量，选择一个现有的簇将其分裂成两个簇，使分裂后子簇内相似性高，子簇间差异大，如此往复直至满足停止条件。

3. 密度聚类
密度聚类（Density-Based Clustering）假设聚类结构能通过样本分布的紧密程度确定。
通常情况下，密度聚类算法从样本密度的角度来考察样本之间的可连接性，并基于可连接样本不断扩展簇以获得最终聚类效果。
**DBSCAN** 是一种著名的密度聚类算法，基于邻域参数来刻画样本分布的紧密程度。对于给定数据集 \( D = \{x_1, x_2, ..., x_m\} \)，定义下列概念：
- \(\varepsilon\)-邻域：对于 \(x_i \in D\)，其 \(\varepsilon\)-邻域包含样本集 \(D\) 中与 \(x_i\) 的距离不大于 \(\varepsilon\) 的样本。
- 核心对象：若 \(x_i\) 的 \(\varepsilon\)-邻域至少包含 \(MinPts\) 个对象，则 \(x_i\) 是一个核心对象。
- 密度直达：若 \(x_j\) 在 \(x_i\) 的 \(\varepsilon\)-邻域中，且 \(x_i\) 是核心对象，则称 \(x_j\) 由 \(x_i\) 密度直达。
- 密度可达：对 \(x_i\) 和 \(x_j\)，若存在样本序列 \(p_1, p_2, ..., p_n\)，其中 \(p_1 = x_i\)，\(p_n = x_j\)，且 \(p_{i+1}\) 由 \(p_i\) 密度直达，则称 \(x_j\) 由 \(x_i\) 密度可达。
- 密度相连：对 \(x_i\) 和 \(x_j\)，存在 \(x_k\) 使得 \(x_i\) 和 \(x_j\) 均由 \(x_k\) 密度可达，则称 \(x_j\) 与 \(x_i\) 密度相连。
- 噪声点：不属于任何簇的点，既不是核心对象也不在核心对象邻域内。  
基于这些概念，DBSCAN 将簇定义为由密度可达关系导出的最大密度相连样本集合。
DBSCAN 先根据邻域参数（ε、MinPts）找出所有核心对象，再以任一核心对象为出发点找出由其密度可达的样本生成一个簇，直到所有核心对象均被访问为止。

### 8.1.3 API
```python
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

X, _ = make_blobs(n_samples=300, centers=3, cluster_std=1)

kmeans = KMeans(n_clusters=3)
kmeans.fit(X)
centers = kmeans.cluster_centers_ # 获取聚类中心
y_pred = kmeans.predict(X) # 获取每个样本所属的聚类标签

fig, ax = plt.subplots(2, 1, figsize=(12, 6))
ax[0].scatter(X[:, 0], X[:, 1], c='grey', label='original data')
ax[0].set_title('Original Data')
ax[0].legend()
ax[1].scatter(X[:, 0], X[:, 1], c=y_pred, cmap='viridis', label='clustered data')
ax[1].scatter(centers[:, 0], centers[:, 1], c='red', s=200, label='centroids')
ax[1].set_title('KMeans Clustering')
ax[1].legend()
plt.show()
```

### 8.1.4 聚类模型评估
1. 轮廓系数
2. 簇内平方和
3. 肘部法
4. CH指数
## 8.2 降维 decompose
### 8.2.1 奇异值分解 SVD
### 8.2.2 主成分分析
