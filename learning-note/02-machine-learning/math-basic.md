# 第一章 高等数学 Higher Mathematics

## 1.1 导数 Derivative

### 1.1.1 基本概念

- **导数 (Derivative)**：函数在某一点附近的变化率，描述函数值随自变量变化的快慢。
  $$
  f'(x_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x) - f(x_0)}{\Delta x}
  $$

- **几何意义**：导数 $f'(x_0)$ 等于曲线 $y = f(x)$ 在点 $(x_0, f(x_0))$ 处切线的斜率。

- **物理意义**：若 $f(t)$ 表示位移，则 $f'(t)$ 表示瞬时速度；若 $f'(t)$ 是速度，则 $f''(t)$ 是加速度。

### 1.1.2 常见函数的导数

| 函数 $f(x)$ | 导数 $f'(x)$ |
|---|---|
| $C$（常数） | $0$ |
| $x^n$ | $n x^{n-1}$ |
| $e^x$ | $e^x$ |
| $\ln x$ | $\frac{1}{x}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |

### 1.1.3 求导法则

- **四则运算**：
  - $(u \pm v)' = u' \pm v'$
  - $(uv)' = u'v + uv'$
  - $\left(\frac{u}{v}\right)' = \frac{u'v - uv'}{v^2}$

- **链式法则 (Chain Rule)**：若 $y = f(g(x))$，则
  $$
  \frac{dy}{dx} = f'(g(x)) \cdot g'(x)
  $$

- **直观理解**：链式法则将复合函数的求导拆解为"外层求导 × 内层求导"。在神经网络的反向传播中，链式法则是最核心的数学工具——梯度从输出层逐层向前传递，每一层都是链式法则的一次应用。

---

## 1.2 偏导与梯度 Partial Derivative & Gradient

### 1.2.1 偏导数 Partial Derivative

- **偏导 (Partial Derivative)**：多元函数沿某一坐标轴方向的变化率——求导时只对一个自变量求导，其余自变量视作常量。
  $$
  \frac{\partial f}{\partial x}(x_0, y_0) = \lim_{\Delta x \to 0} \frac{f(x_0 + \Delta x, y_0) - f(x_0, y_0)}{\Delta x}
  $$

- **记号**：对 $x$ 的偏导记为 $\frac{\partial f}{\partial x}$ 或 $f_x$。

### 1.2.2 方向导数 Directional Derivative

- **方向导数 (Directional Derivative)**：多元函数沿任意单位向量指定方向的变化率。偏导数是方向导数沿坐标轴方向的特殊情况。
  $$
  \frac{\partial f}{\partial l}(x_0, y_0) = f_x(x_0, y_0)\cos\alpha + f_y(x_0, y_0)\cos\beta
  $$
  其中 $f_x(x_0, y_0)$、$f_y(x_0, y_0)$ 表示点 $(x_0, y_0)$ 处 $f$ 对 $x$、$y$ 的偏导数；$\cos\alpha$、$\cos\beta$ 是方向 $l$ 的方向余弦，即 $l$ 方向的单位方向向量可以表示为：
  $$
  l_0 = (\cos\alpha, \cos\beta)
  $$

### 1.2.3 梯度 Gradient

- **梯度 (Gradient)**：函数在某点上升最快的方向，同时附带变化快慢的大小。梯度是一个**向量**，由各偏导数组成：
  $$
  \nabla f(x_0, y_0) = \left( \frac{\partial f}{\partial x}(x_0, y_0),\; \frac{\partial f}{\partial y}(x_0, y_0) \right)
  $$

- **方向导数与梯度的关系**：方向导数 = 梯度 · 单位方向向量，即：
  $$
  \frac{\partial f}{\partial l} = \nabla f \cdot l_0 = \|\nabla f\| \cdot \|l_0\| \cdot \cos\theta
  $$
  当 $l_0$ 与 $\nabla f$ 同向（$\cos\theta = 1$）时方向导数最大 → 梯度指向函数**上升最快**的方向；反向时下降最快。

- **直观理解**：想象你站在一座山上——梯度指向最陡的上坡方向，梯度的模长告诉你那个方向有多陡。机器学习中，梯度下降法正是**沿着负梯度方向**一步步走向函数的最小值。

```python
import numpy as np

# 函数 f(x, y) = x² + y² 在某点的梯度
def f(x, y):
    return x**2 + y**2

def gradient(x, y):
    return np.array([2*x, 2*y])  # ∇f = (∂f/∂x, ∂f/∂y)

x0, y0 = 3.0, 4.0
grad = gradient(x0, y0)
print(f"点 ({x0}, {y0}) 处的梯度: {grad}")
print(f"梯度方向 (上升最快): ({grad[0]:.1f}, {grad[1]:.1f})")
print(f"负梯度方向 (下降最快): ({-grad[0]:.1f}, {-grad[1]:.1f})")
print(f"梯度模长 (变化速率): {np.linalg.norm(grad):.1f}")

# 验证：沿梯度方向走一小步，函数值的变化
step = 0.1
direction = grad / np.linalg.norm(grad)  # 单位梯度方向
new_x, new_y = x0 + step * direction[0], y0 + step * direction[1]
print(f"\n沿梯度方向走 {step}:")
print(f"  f({x0}, {y0}) = {f(x0, y0)}")
print(f"  f({new_x:.2f}, {new_y:.2f}) = {f(new_x, new_y):.2f} (上升)")
```

# 第二章 线性代数 Linear Algebra

## 2.1 标量与向量 Scalar & Vector

### 2.1.1 基本概念

- **标量 (Scalar)**：单个数值，无方向。例如温度 30°C、价格 50 元、学习率 0.01。
- **向量 (Vector)**：由一组有序数值组成的量，既有大小又有方向。可以看作 $n$ 维空间中的一个点或带方向的箭头。
  $$
  x = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n \end{pmatrix} \in \mathbb{R}^n
  $$

- **机器学习中的理解**：一个 $n$ 维向量可以表示一个样本的 $n$ 个特征。例如，一套房子的面积、卧室数、房龄就是一个 3 维特征向量。

### 2.1.2 向量运算

| 运算 | 记号/代码 | 说明 |
|---|---|---|
| **转置** | `x.T` | 列向量 → 行向量，或反之 |
| **加法** | `x + y` | 对应元素相加，需同维度 |
| **标量乘** | `c * x` | 标量与每个元素相乘（缩放） |
| **内积** | `x @ y` 或 `np.dot(x, y)` | 对应元素乘积之和，结果为**标量** |

**1. 向量转置**：列向量转置结果为行向量。
$$
x = \begin{pmatrix} 2 \\ 5 \\ 8 \end{pmatrix}, \quad
x^T = \begin{pmatrix} 2 & 5 & 8 \end{pmatrix}
$$

**2. 向量加法**：对应元素相加。
$$
\begin{pmatrix} 2 \\ 5 \\ 8 \end{pmatrix} + \begin{pmatrix} 1 \\ 3 \\ 7 \end{pmatrix} = \begin{pmatrix} 3 \\ 8 \\ 15 \end{pmatrix}
$$

**3. 标量与向量相乘**：标量与每个元素相乘，相当于缩放向量的长度。
$$
3 \times \begin{pmatrix} 2 \\ 5 \\ 8 \end{pmatrix} = \begin{pmatrix} 6 \\ 15 \\ 24 \end{pmatrix}
$$

**4. 向量内积 (Dot Product)**：两向量对应元素乘积之和，结果为标量。
$$
\langle x, y \rangle = \left\langle \begin{pmatrix} 2 \\ 5 \\ 8 \end{pmatrix}, \begin{pmatrix} 1 \\ 3 \\ 7 \end{pmatrix} \right\rangle = 2 \times 1 + 5 \times 3 + 8 \times 7 = 2 + 15 + 56 = 73
$$

**内积的几何意义**：$\langle x, y \rangle = \|x\| \cdot \|y\| \cdot \cos\theta$，由此可以计算两向量之间的夹角：
$$
\cos\theta = \frac{\langle x, y \rangle}{\|x\| \cdot \|y\|} = \frac{\langle x, y \rangle}{\sqrt{\langle x, x \rangle} \sqrt{\langle y, y \rangle}}
$$

> **注意**：内积为 0 $\iff$ 两向量正交（垂直）；内积为正值 → 夹角小于 90°（方向大致相同）；内积为负值 → 夹角大于 90°（方向大致相反）。这在**注意力机制 (Attention)** 中至关重要——Query 和 Key 的内积衡量二者的"匹配程度"。

---

### 2.1.3 向量范数 Norm

- **范数 (Norm)**：衡量向量"长度"或"大小"的函数，满足非负性、齐次性、三角不等式。

对于向量 $x = (x_1, x_2, \dots, x_n)$，**p-范数（$L_p$ 范数）**：
$$
\|x\|_p = \left( \sum_{i=1}^n |x_i|^p \right)^{\frac{1}{p}}
$$

| 范数 | 定义 | 直观 | 用途 |
|---|---|---|---|
| $L_0$ | 非零元素个数 | 稀疏度计数 | 稀疏表示（NP难，用 $L_1$ 近似） |
| $L_1$ | $\sum \mid x_i\mid$ | 曼哈顿距离（走直角） | L1 正则化 (Lasso)，产生稀疏解 |
| $L_2$ | $\sqrt{\sum x_i^2}$ | 欧几里得距离（直线距离） | L2 正则化 (Ridge)，防止过拟合 |
| $L_\infty$ | $\max \mid x_i\mid$ | Chebyshev 距离 | 控制最大误差 |

**1. $L_0$ 范数（0-范数，非零元素计数）**

- **定义**：$\|x\|_0 = \text{card}\{ i \mid x_i \ne 0 \}$
- **注意**：严格来说 $L_0$ 不满足范数的齐次性（$\|\lambda x\|_0 = \|x\|_0, \lambda \ne 0$），所以它不是真正的范数，只是习惯叫法。优化 $L_0$ 范数是 NP 难问题，实际中常用 $L_1$ 范数来近似求解稀疏问题。

**2. $L_1$ 范数（1-范数，曼哈顿范数）**

- **定义**：$\|x\|_1 = \sum_{i=1}^n |x_i|$
- **直观理解**：在二维平面上，相当于"走直角"的曼哈顿距离。
- **特点**：会让解变得**稀疏**（很多元素变成 0），常用于 L1 正则化（如 Lasso 回归）；对异常值的鲁棒性比 $L_2$ 范数强。

**3. $L_2$ 范数（2-范数，欧几里得范数）**

- **定义**：$\|x\|_2 = \sqrt{\sum_{i=1}^n x_i^2}$
- **直观理解**：向量到原点的直线距离，最符合日常直觉的"长度"。
- **特点**：最常用的范数；平方形式会放大大数值的影响，对异常值敏感；常用于 L2 正则化（如 Ridge 回归），防止过拟合。

**4. $L_\infty$ 范数（无穷范数，最大范数）**

- **定义**：$\|x\|_\infty = \max\{ |x_1|, |x_2|, \dots, |x_n| \}$
- **直观理解**：只关注向量中绝对值最大的分量。
- **特点**：常用于控制最大误差和鲁棒优化。

```python
import numpy as np

x = np.array([1, -2, 3, -4])

# L0范数（非零元素个数）
l0 = np.count_nonzero(x)
print(f"L0范数: {l0}")

# L1范数
l1 = np.linalg.norm(x, ord=1)
print(f"L1范数: {l1}")

# L2范数
l2 = np.linalg.norm(x, ord=2)
print(f"L2范数: {l2}")

# L∞范数
linf = np.linalg.norm(x, ord=np.inf)
print(f"L∞范数: {linf}")
```

---

## 2.2 矩阵 Matrix

### 2.2.1 基本概念

- **矩阵 (Matrix)**：由 $m \times n$ 个数排成的矩形阵列。$A \in \mathbb{R}^{m \times n}$ 表示 $m$ 行 $n$ 列的矩阵。
  $$
  A = \begin{bmatrix}
  a_{11} & a_{12} & \dots & a_{1n} \\
  a_{21} & a_{22} & \dots & a_{2n} \\
  \vdots & \vdots & \ddots & \vdots \\
  a_{m1} & a_{m2} & \dots & a_{mn}
  \end{bmatrix}
  $$

- **特殊矩阵**：

| 类型 | 定义 | 示例 |
|---|---|---|
| **方阵** | $m = n$ 的矩阵 | $A \in \mathbb{R}^{n \times n}$ |
| **对角矩阵** | 仅主对角线元素非零 | $\text{diag}(1, 2, 3)$ |
| **单位矩阵** $I$ | 对角全为 1 的对角矩阵 | $I_3 = \text{diag}(1,1,1)$ |

- **机器学习中的理解**：一个矩阵可以表示一个**数据集**——每行是一个样本，每列是一个特征。例如 1000 张 28×28 的图片可以表示为 $1000 \times 784$ 的矩阵。矩阵也可以表示**线性变换**——将输入向量映射到输出向量。

### 2.2.2 矩阵运算

| 运算 | 记号/代码 | 说明 |
|---|---|---|
| **转置** | `A.T` | 行列互换，$(A^T)_{ij} = A_{ji}$ |
| **加法** | `A + B` | 对应元素相加，需同形状 |
| **标量乘** | `c * A` | 每个元素乘以标量 |
| **哈达玛积** | `A * B` | 对应元素相乘，需同形状 |
| **矩阵乘法** | `A @ B` 或 `A.dot(B)` | 前行乘后列，$A_{m \times n} B_{n \times p} = C_{m \times p}$ |
| **求逆** | `np.linalg.inv(A)` | $A A^{-1} = I$，仅限可逆方阵 |
| **伪逆** | `np.linalg.pinv(A)` | 对非方阵或奇异矩阵求广义逆 |
| **向量化** | `A.flatten()` | 将矩阵展平为一维向量 |
| **克罗内克积** | `np.kron(A, B)` | $A \otimes B$，也称直积或张量积 |

> **注意**：`*` 在 NumPy 中表示**逐元素相乘 (Hadamard积)**，而非矩阵乘法。矩阵乘法必须用 `@` 或 `np.dot()`。这是初学者最常犯的错误之一。

**矩阵乘法的维度匹配规则**：$A_{m \times n} \cdot B_{n \times p} = C_{m \times p}$
- $A$ 的列数必须等于 $B$ 的行数（中间的 $n$ 必须匹配）。
- 结果矩阵的形状由外侧维度决定：$m$ 行 $p$ 列。
- 每个元素 $C_{ij} = \sum_{k=1}^n A_{ik} \cdot B_{kj}$（$A$ 第 $i$ 行与 $B$ 第 $j$ 列的内积）。

### 2.2.3 张量 Tensor

- **张量 (Tensor)**：三维及以上的多维数组，是标量（0 维）、向量（1 维）、矩阵（2 维）向更高维度的推广。
  - 标量 → 0-D tensor：`shape = ()`
  - 向量 → 1-D tensor：`shape = (n,)`
  - 矩阵 → 2-D tensor：`shape = (m, n)`
  - 高维张量 → 3-D+ tensor：`shape = (d1, d2, d3, ...)`

- **典型应用**：一批彩色图像表示为 4D 张量 `(batch, height, width, channels)`，例如 32 张 224×224 RGB 图像 → `shape = (32, 224, 224, 3)`。

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

# 转置
print("A.T:\n", A.T)

# 哈达玛积 (逐元素相乘)
print("A * B:\n", A * B)

# 矩阵乘法
print("A @ B:\n", A @ B)

# 矩阵求逆
A_inv = np.linalg.inv(A)
print("A的逆:\n", A_inv)
print("验证 A @ A_inv = I:\n", A @ A_inv)

# 伪逆（适用于非方阵）
C = np.array([[1, 2, 3],
              [4, 5, 6]])
C_pinv = np.linalg.pinv(C)
print("C的伪逆 shape:", C_pinv.shape)

# 向量化
print("A.flatten():", A.flatten())

# 克罗内克积
print("kron(A, B):\n", np.kron(A, B))
```

---

## 2.3 矩阵求导 Matrix Calculus

- **本质**：矩阵求导就是函数对变元的每个元素逐个求偏导，然后按原变元的形状排列成向量或矩阵。这样做的目的是让求导结果与变元**形状一致**，便于在梯度下降中直接做减法：$\theta \leftarrow \theta - \eta \nabla_\theta f$。

### 2.3.1 梯度向量 Gradient Vector

对于实向量变元 $\boldsymbol{x} \in \mathbb{R}^m$，实标量函数 $f(\boldsymbol{x})$ 的梯度向量为 $m \times 1$ 的列向量（与 $\boldsymbol{x}$ 形状相同）：

$$
\nabla_{\boldsymbol{x}} f(\boldsymbol{x}) = \frac{\partial f(\boldsymbol{x})}{\partial \boldsymbol{x}} = \begin{bmatrix}
\frac{\partial f(\boldsymbol{x})}{\partial x_1}, &
\frac{\partial f(\boldsymbol{x})}{\partial x_2}, &
\ldots, &
\frac{\partial f(\boldsymbol{x})}{\partial x_m}
\end{bmatrix}^T
$$

### 2.3.2 梯度矩阵 Gradient Matrix

对于矩阵变元 $\boldsymbol{X} \in \mathbb{R}^{m \times n}$，可以类似地得到 $f(\boldsymbol{X})$ 的梯度矩阵（与 $\boldsymbol{X}$ 形状相同）：

$$
\nabla_{\boldsymbol{X}} f(\boldsymbol{X}) = \frac{\partial f(\boldsymbol{X})}{\partial \boldsymbol{X}} = 
\begin{bmatrix}
\frac{\partial f(\boldsymbol{X})}{\partial x_{11}} & \dots & \frac{\partial f(\boldsymbol{X})}{\partial x_{1n}} \\
\vdots & \ddots & \vdots \\
\frac{\partial f(\boldsymbol{X})}{\partial x_{m1}} & \dots & \frac{\partial f(\boldsymbol{X})}{\partial x_{mn}}
\end{bmatrix} \in \mathbb{R}^{m \times n}
$$

### 2.3.3 黑塞矩阵 Hessian Matrix

$f(\boldsymbol{x})$ 的二阶偏导构成的矩阵被称为**黑塞矩阵 (Hessian Matrix)**——它是一个 $n \times n$ 的对称方阵，描述了梯度的变化率（即函数的曲率）：

$$
\boldsymbol{H}(\boldsymbol{x}) = \nabla^2 f(\boldsymbol{x}) = \left[ \frac{\partial^2 f}{\partial x_i \partial x_j} \right]_{n \times n}
$$

- 在**牛顿法**中，Hessian 矩阵用于二阶优化，收敛速度比梯度下降更快但计算代价更高。
- 在深度学习中，Hessian 的特征值分布与训练的稳定性和收敛速度密切相关。

### 2.3.4 常用矩阵求导公式

| $f(\boldsymbol{x})$ | $\nabla_{\boldsymbol{x}} f$ |
|---|---|
| $\boldsymbol{a}^T \boldsymbol{x}$ | $\boldsymbol{a}$ |
| $\boldsymbol{x}^T \boldsymbol{x}$（即 $\|\boldsymbol{x}\|_2^2$） | $2\boldsymbol{x}$ |
| $\boldsymbol{x}^T A \boldsymbol{x}$（$A$ 对称） | $2A\boldsymbol{x}$ |
| $\|\boldsymbol{x}\|_2$ | $\frac{\boldsymbol{x}}{\|\boldsymbol{x}\|_2}$ |

```python
import numpy as np

# np.gradient：对「等间隔采样序列」求导（一维函数曲线）
# 例：y = t²，在 t = [0,1,2,3,4] 采样
t = np.array([0, 1, 2, 3, 4])
y = t ** 2
dy_dt = np.gradient(y, t)  # 传入坐标 t，求 dy/dt
print("\n一维函数 y=t² 的离散导数:")
print("t:     ", t)
print("dy/dt: ", dy_dt)
print("理论导数 2t:", 2*t)

# np.gradient 对矩阵：分别对每行和每列求梯度
X = np.array([[1, 2, 3],
              [4, 6, 8]])
g_row, g_col = np.gradient(X)
print(f"\n矩阵 X:\n{X}")
print(f"沿行方向梯度 (axis=0，即每列的变化率):\n{g_row}")
print(f"沿列方向梯度 (axis=1，即每行的变化率):\n{g_col}")
```

# 第三章 概率论 Probability Theory

## 3.1 概率 Probability

### 3.1.1 基本概念

- **样本空间 (Sample Space)** $\Omega$：随机试验所有可能结果的集合。
- **事件 (Event)** $A \subseteq \Omega$：样本空间的子集，即我们关心的某些结果的集合。
- **概率 (Probability)** $P(A)$：对事件 $A$ 发生可能性大小的度量，满足以下三条公理：
  1. **非负性**：$P(A) \geq 0$
  2. **规范性**：$P(\Omega) = 1$
  3. **可列可加性**：若 $A_1, A_2, \dots$ 两两互不相容，则 $P\left(\bigcup_{i=1}^{\infty} A_i\right) = \sum_{i=1}^{\infty} P(A_i)$

### 3.1.2 条件概率 Conditional Probability

- **定义**：在事件 $B$ 已发生的条件下，事件 $A$ 发生的概率：
  $$
  P(A \mid B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) > 0
  $$

- **乘法公式**：由条件概率定义直接推出：
  $$
  P(A \cap B) = P(A \mid B) \cdot P(B) = P(B \mid A) \cdot P(A)
  $$

### 3.1.3 独立性 Independence

- **定义**：若 $P(A \cap B) = P(A) \cdot P(B)$，则称事件 $A$ 与 $B$ **相互独立**。
- **等价条件**：当 $P(B) > 0$ 时，$A$ 与 $B$ 独立 $\iff$ $P(A \mid B) = P(A)$
- **直观理解**：$B$ 的发生与否不影响 $A$ 的发生概率。

### 3.1.4 全概率公式 Law of Total Probability

- 若 $B_1, B_2, \dots, B_n$ 构成样本空间 $\Omega$ 的一个**划分**（两两互斥且并集为 $\Omega$），则对任意事件 $A$：
  $$
  P(A) = \sum_{i=1}^{n} P(A \mid B_i) \cdot P(B_i)
  $$

- **直观理解**：把 $A$ 的概率按不同的"原因" $B_i$ 拆开分别计算再求和。"分而治之"的思想。

---

## 3.2 概率分布 Probability Distribution

### 3.2.1 随机变量 Random Variable

- **随机变量 (Random Variable)**：将样本空间中的结果映射到实数的函数 $X: \Omega \to \mathbb{R}$。
- **离散随机变量**：取值有限个或可列无限个。
- **连续随机变量**：取值充满某个区间，不可逐个列举。

### 3.2.2 概率质量函数与概率密度函数

| | 离散型 | 连续型 |
|---|---|---|
| **函数名** | 概率质量函数 PMF | 概率密度函数 PDF |
| **记号** | $p(x) = P(X = x)$ | $f(x)$，其中 $f(x) \geq 0$ |
| **求概率** | 直接取值：$P(X = x_i) = p(x_i)$ | 积分求面积：$P(a < X < b) = \int_a^b f(x)\,dx$ |
| **归一化** | $\sum_x p(x) = 1$ | $\int_{-\infty}^{+\infty} f(x)\,dx = 1$ |

> **注意**：连续型随机变量在**单点**处的概率为 0，即 $P(X = a) = 0$。密度值 $f(x)$ 本身**不是概率**，只是概率的"浓度"。

### 3.2.3 累积分布函数 CDF

- **定义**：$F(x) = P(X \leq x)$，对离散和连续型均适用。
- **性质**：
  - 单调不减：$x_1 < x_2 \implies F(x_1) \leq F(x_2)$
  - $F(-\infty) = 0,\quad F(+\infty) = 1$
  - 对连续型：$f(x) = F'(x)$，即 PDF 是 CDF 的导数。

### 3.2.4 常见分布

**1. 伯努利分布 Bernoulli Distribution**（离散）

- 描述单次"成功/失败"试验。$X \sim \text{Bernoulli}(p)$
- PMF：$P(X=1) = p,\quad P(X=0) = 1-p$
- 期望 $E[X] = p$，方差 $\text{Var}(X) = p(1-p)$

**2. 二项分布 Binomial Distribution**（离散）

- $n$ 次独立伯努利试验中成功的次数。$X \sim B(n, p)$
- PMF：$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$
- 期望 $E[X] = np$，方差 $\text{Var}(X) = np(1-p)$

**3. 高斯分布（正态分布）Gaussian (Normal) Distribution**（连续）

- 自然界中最常见的分布。$X \sim \mathcal{N}(\mu, \sigma^2)$
- PDF：
  $$
  f(x) = \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left( -\frac{(x-\mu)^2}{2\sigma^2} \right)
  $$
- $\mu$ 为均值（分布中心），$\sigma$ 为标准差（分布宽度）。
- **68-95-99.7 法则**：约 68% 的数据落在 $\mu \pm \sigma$，约 95% 落在 $\mu \pm 2\sigma$，约 99.7% 落在 $\mu \pm 3\sigma$。

**4. 均匀分布 Uniform Distribution**（连续）

- 在区间 $[a, b]$ 上每一点密度相同。$X \sim U(a, b)$
- PDF：$f(x) = \frac{1}{b-a},\; x \in [a, b]$
- 期望 $E[X] = \frac{a+b}{2}$，方差 $\text{Var}(X) = \frac{(b-a)^2}{12}$

### 3.2.5 期望与方差 Expectation & Variance

- **期望 (Expectation)**：随机变量取值的"加权平均"，权重为概率。
  - 离散：$E[X] = \sum_x x \cdot p(x)$
  - 连续：$E[X] = \int_{-\infty}^{+\infty} x \cdot f(x)\,dx$
  - 线性性质：$E[aX + bY] = aE[X] + bE[Y]$（**无条件成立**）

- **方差 (Variance)**：衡量随机变量围绕期望的离散程度。
  $$
  \text{Var}(X) = E\left[(X - E[X])^2\right] = E[X^2] - (E[X])^2
  $$
  - $\text{Var}(aX + b) = a^2 \text{Var}(X)$（常数 $b$ 的方差为 0，平移不改变离散度）

- **标准差 (Standard Deviation)**：$\sigma_X = \sqrt{\text{Var}(X)}$，与原始数据同量纲。

```python
import numpy as np

# 生成各种分布的样本
np.random.seed(42)

# 二项分布 B(n=10, p=0.5)
binom_samples = np.random.binomial(n=10, p=0.5, size=10000)

# 正态分布 N(μ=0, σ²=1)
normal_samples = np.random.normal(loc=0, scale=1, size=10000)

# 均匀分布 U(0, 1)
uniform_samples = np.random.uniform(low=0, high=1, size=10000)

# 期望与方差
print(f"正态样本: 均值={normal_samples.mean():.3f}, 方差={normal_samples.var():.3f}")
```

---

## 3.3 贝叶斯定理 Bayes' Theorem

### 3.3.1 定理公式

- 由条件概率定义 $P(A \mid B) = \frac{P(A \cap B)}{P(B)}$ 及其对称形式 $P(B \mid A) = \frac{P(A \cap B)}{P(A)}$，消去 $P(A \cap B)$ 得：

$$
P(A \mid B) = \frac{P(B \mid A) \cdot P(A)}{P(B)}
$$

- 结合全概率公式展开分母 $P(B) = \sum_i P(B \mid A_i) P(A_i)$：
  $$
  P(A_i \mid B) = \frac{P(B \mid A_i) \cdot P(A_i)}{\sum_j P(B \mid A_j) \cdot P(A_j)}
  $$

### 3.3.2 各项术语

| 术语 | 记号 | 含义 |
|---|---|---|
| **先验概率 Prior** | $P(A)$ | 在观测到任何数据之前，对 $A$ 发生概率的初始信念 |
| **似然 Likelihood** | $P(B \mid A)$ | 在 $A$ 成立的条件下，观测到数据 $B$ 的可能性 |
| **证据 Evidence** | $P(B)$ | 数据 $B$ 出现的总概率（归一化常数） |
| **后验概率 Posterior** | $P(A \mid B)$ | 观测到数据 $B$ 之后，对 $A$ 发生概率的更新信念 |

- **核心思想**：
  $$
  \text{后验} \propto \text{似然} \times \text{先验}
  $$
  即通过观测到的数据，不断**更新**我们对未知量的信念——这是贝叶斯推断的基石。

### 3.3.3 直观例子：疾病检测

- 某种疾病发病率为 1%（先验 $P(D) = 0.01$）
- 检测准确率：真有病时阳性率 99%（似然 $P(+ \mid D) = 0.99$），没病时假阳性率 5%（$P(+ \mid \neg D) = 0.05$）
- 问：检测呈阳性时，真正有病的概率是多少？

**计算**：
$$
P(D \mid +) = \frac{P(+ \mid D) \cdot P(D)}{P(+ \mid D)P(D) + P(+ \mid \neg D)P(\neg D)} = \frac{0.99 \times 0.01}{0.99 \times 0.01 + 0.05 \times 0.99} = \frac{0.0099}{0.0099 + 0.0495} \approx 16.7\%
$$

> **启示**：即使检测准确率很高，由于疾病本身很罕见，阳性结果也仅有约 16.7% 的概率意味着真正患病。这体现了**基础概率（先验）不可忽视**——贝叶斯定理的核心价值正在于此。

---

## 3.4 似然函数和极大似然估计 Likelihood & MLE

### 3.4.1 似然函数 Likelihood Function

- **定义**：给定观测数据 $\mathcal{D} = \{x_1, x_2, \dots, x_n\}$，似然函数是**未知参数 $\theta$ 的函数**，定义为在参数 $\theta$ 下观测到这些数据的概率（或密度）：
  $$
  \mathcal{L}(\theta \mid \mathcal{D}) = P(\mathcal{D} \mid \theta) = \prod_{i=1}^{n} p(x_i \mid \theta)
  $$
  其中乘法成立的前提是样本 **i.i.d.**（独立同分布）。

- **似然 vs 概率**：
  - 概率 $P(\mathcal{D} \mid \theta)$：参数固定，数据可变 → "给定参数，数据出现的可能性"
  - 似然 $\mathcal{L}(\theta \mid \mathcal{D})$：数据固定，参数可变 → "给定数据，哪个参数更合理"

### 3.4.2 极大似然估计 Maximum Likelihood Estimation (MLE)

- **思想**：选择使观测数据出现概率**最大**的参数值作为估计：
  $$
  \hat{\theta}_{\text{MLE}} = \arg\max_{\theta} \mathcal{L}(\theta \mid \mathcal{D})
  $$

- **对数似然 Log-Likelihood**：由于连乘在数值上容易下溢且求导不便，实际中通常最大化**对数似然**：
  $$
  \ell(\theta) = \log \mathcal{L}(\theta \mid \mathcal{D}) = \sum_{i=1}^{n} \log p(x_i \mid \theta)
  $$
  $\log$ 是单调递增函数，最大化 $\mathcal{L}$ 等价于最大化 $\ell$。

- **求解步骤**：
  1. 写出似然函数 $\mathcal{L}(\theta)$ 或对数似然 $\ell(\theta)$
  2. 对 $\theta$ 求导，令导数为 0：$\frac{\partial \ell}{\partial \theta} = 0$
  3. 解出 $\hat{\theta}_{\text{MLE}}$，验证是否为最大值

### 3.4.3 例子：高斯分布的 MLE

- 数据 $\mathcal{D} = \{x_1, \dots, x_n\}$ 独立采样自 $\mathcal{N}(\mu, \sigma^2)$，求 $\mu$ 和 $\sigma^2$ 的 MLE。

- 似然函数：
  $$
  \mathcal{L}(\mu, \sigma^2) = \prod_{i=1}^{n} \frac{1}{\sqrt{2\pi\sigma^2}} \exp\left( -\frac{(x_i - \mu)^2}{2\sigma^2} \right)
  $$

- 对数似然：
  $$
  \ell(\mu, \sigma^2) = -\frac{n}{2}\log(2\pi) - \frac{n}{2}\log(\sigma^2) - \frac{1}{2\sigma^2}\sum_{i=1}^{n}(x_i - \mu)^2
  $$

- 分别对 $\mu$ 和 $\sigma^2$ 求偏导并令其为 0，解得：
  $$
  \hat{\mu}_{\text{MLE}} = \frac{1}{n}\sum_{i=1}^{n} x_i \quad (\text{样本均值})
  $$
  $$
  \hat{\sigma}^2_{\text{MLE}} = \frac{1}{n}\sum_{i=1}^{n} (x_i - \hat{\mu})^2 \quad (\text{样本方差，注意分母是 } n \text{ 而非 } n-1)
  $$

> **注意**：MLE 对方差的估计是**有偏的**（分母为 $n$），而样本方差常用无偏估计（分母 $n-1$，即贝塞尔校正）。但当 $n$ 很大时两者差异可忽略。

```python
import numpy as np
from scipy import stats

# 从 N(μ=5, σ=2) 中采样
np.random.seed(42)
data = np.random.normal(loc=5, scale=2, size=1000)

# MLE 估计：μ̂ = 样本均值，σ̂² = 有偏样本方差
mu_mle = np.mean(data)
sigma2_mle = np.mean((data - mu_mle)**2)   # 分母为 n
sigma2_unbiased = np.var(data, ddof=1)      # 分母为 n-1，无偏估计

print(f"MLE 均值 μ̂:       {mu_mle:.3f}  (真实 μ=5)")
print(f"MLE 方差 σ̂²:      {sigma2_mle:.3f}  (真实 σ²=4, 有偏)")
print(f"无偏方差 σ̂²_unb:  {sigma2_unbiased:.3f}  (真实 σ²=4, 无偏)")

# 也可用 scipy 直接拟合
mu_fit, sigma_fit = stats.norm.fit(data)
print(f"scipy拟合: μ={mu_fit:.3f}, σ={sigma_fit:.3f}")
```

### 3.4.4 MLE 与贝叶斯估计的联系

- **MLE**：只考虑似然，视参数为固定但未知的常数 → $\hat{\theta} = \arg\max_\theta P(\mathcal{D} \mid \theta)$
- **最大后验估计 MAP**：在 MLE 基础上引入先验 $P(\theta)$ → $\hat{\theta} = \arg\max_\theta P(\mathcal{D} \mid \theta) P(\theta)$
- 当先验为**均匀分布**（即对所有 $\theta$ 一视同仁）时，MAP 退化为 MLE。因此 MLE 可以看作 MAP 在无信息先验下的特例。