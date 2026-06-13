# 第一章 概率论的基本概念
## 1.1 随机试验
### 1.1.1 随机试验定义
> 满足下述三条特征的试验称为随机试验\(E\)：
> 1. 可在相同条件下重复进行；
> 2. 试验结果不止一个，所有结果预先明确；
> 3. 每次试验仅出现一个结果，试验前无法预知具体结果。

## 1.2 样本空间、随机事件
### 1.2.1 样本空间与样本点
- 随机试验\(E\)所有可能结果组成的集合称为样本空间，记作\(S\)
- 样本空间中的单个元素称为样本点

### 1.2.2 随机事件相关定义
> 样本空间\(S\)的子集称为随机事件，简称事件。
- 基本事件：由单个样本点构成的事件
- 必然事件：样本空间\(S\)本身，每次试验必然发生
- 不可能事件：空集\(\emptyset\)，每次试验均不发生

### 1.2.3 事件间运算与关系
- 包含：\(A\subset B\)，\(A\)发生则\(B\)必发生；\(A=B \iff A\subset B,B\subset A\)
- 和事件：\(A\cup B\)，\(A,B\)至少一个发生；\(\bigcup_{k=1}^n A_k\)为有限和，\(\bigcup_{k=1}^\infty A_k\)为可列和
- 积事件：\(A\cap B\)（简写\(AB\)），\(A,B\)同时发生；\(\bigcap_{k=1}^n A_k,\bigcap_{k=1}^\infty A_k\)
- 差事件：\(A-B\)，\(A\)发生\(B\)不发生，\(A-B=A\overline{B}\)
- 互斥：\(AB=\emptyset\)，\(A,B\)不能同时发生
- 对立：\(A\cup B=S,AB=\emptyset\)，\(B=\overline{A}\)

### 1.2.4 事件运算性质
- 交换律：\(A\cup B=B\cup A,AB=BA\)
- 结合律：\((A\cup B)\cup C=A\cup(B\cup C),(AB)C=A(BC)\)
- 分配律：\(A(B\cup C)=AB\cup AC,A\cup(BC)=(A\cup B)(A\cup C)\)
- 德摩根律：\(\overline{A\cup B}=\overline{A}\overline{B},\overline{AB}=\overline{A}\cup\overline{B}\)，推广\(\overline{\bigcup A_k}=\bigcap\overline{A_k},\overline{\bigcap A_k}=\bigcup\overline{A_k}\)

## 1.3 频率与概率
### 1.3.1 频率定义
> 在\(n\)次重复试验中，事件\(A\)发生次数\(n_A\)，频率\(f_n(A)=\frac{n_A}{n}\)
- 频率性质：
  - \(0\le f_n(A)\le1\)
  - \(f_n(S)=1\)
  - \(A_1,\dots,A_k\)两两互斥：\(f_n(\bigcup_{i=1}^k A_i)=\sum_{i=1}^k f_n(A_i)\)

### 1.3.2 概率公理化定义
> 设\(S\)为样本空间，对任意事件\(A\)，实值函数\(P(A)\)满足：
> 1. 非负性：\(P(A)\ge0\)
> 2. 规范性：\(P(S)=1\)
> 3. 可列可加性：\(A_1,A_2,\dots\)两两互斥，\(P(\bigcup_{i=1}^\infty A_i)=\sum_{i=1}^\infty P(A_i)\)，称\(P(A)\)为事件\(A\)概率。

### 1.3.3 概率基本性质
- \(P(\emptyset)=0\)
- 有限可加：\(A_1\dots A_n\)两两互斥，\(P(\bigcup_{i=1}^n A_i)=\sum_{i=1}^n P(A_i)\)
- \(A\subset B\Rightarrow P(B-A)=P(B)-P(A),P(A)\le P(B)\)
- 对任意\(A\)：\(P(\overline{A})=1-P(A)\)
- 加法公式：\(P(A\cup B)=P(A)+P(B)-P(AB)\)，推广\(P(A\cup B\cup C)=P(A)+P(B)+P(C)-P(AB)-P(AC)-P(BC)+P(ABC)\)

## 1.4 等可能概型（古典概型）
### 1.4.1 古典概型定义
> 试验满足：样本空间含有限个样本点；各基本事件发生可能性相等，称为古典概型。
- 计算公式：\(P(A)=\frac{A包含基本事件数}{S中基本事件总数}=\frac{n_A}{n}\)

## 1.5 条件概率
### 1.5.1 条件概率定义
> \(P(B)>0\)时，\(P(A|B)=\frac{P(AB)}{P(B)}\)为\(B\)发生条件下\(A\)的条件概率
- 条件概率满足概率三条公理与全部概率性质

### 1.5.2 乘法公式
- \(P(B)>0,P(AB)=P(B)P(A|B)\)
- 推广：\(P(A_1A_2\dots A_{n-1})>0,P(A_1A_2\dots A_n)=P(A_1)P(A_2|A_1)P(A_3|A_1A_2)\dots P(A_n|A_1\dots A_{n-1})\)

### 1.5.3 全概率公式
- 划分定义：\(B_1,\dots,B_n\subset S\)，两两互斥，\(\bigcup_{i=1}^n B_i=S\)，称\(\{B_i\}\)为\(S\)一个划分
- 全概率：\(\forall A\subset S,P(A)=\sum_{i=1}^n P(B_i)P(A|B_i)\)

### 1.5.4 贝叶斯公式
- \(P(A)>0,P(B_i)>0\)，\(P(B_j|A)=\frac{P(B_j)P(A|B_j)}{\sum_{i=1}^n P(B_i)P(A|B_i)}\)

## 1.6 独立性
### 1.6.1 两事件独立
> \(P(AB)=P(A)P(B)\)，称\(A,B\)相互独立
- \(A,B\)独立\(\iff A,\overline{B}\)；\(\overline{A},B\)；\(\overline{A},\overline{B}\)均相互独立
- \(P(A)>0,A,B\)独立\(\iff P(B|A)=P(B)\)

### 1.6.2 多事件独立
- 三事件\(A,B,C\)相互独立：
  $$
  \begin{cases}
  P(AB)=P(A)P(B)\\
  P(AC)=P(A)P(C)\\
  P(BC)=P(B)P(C)\\
  P(ABC)=P(A)P(B)P(C)
  \end{cases}
  $$
- \(n\)事件相互独立：任意\(k(2\le k\le n)\)个事件积的概率等于各事件概率乘积

# 第二章 随机变量及其分布
## 2.1 随机变量
### 2.1.1 随机变量定义
> 设\(S\)为样本空间，实值单值函数\(X=X(e),e\in S\)称为随机变量。

## 2.2 离散型随机变量及其分布律
### 2.2.1 分布律
> 离散型随机变量全部取值\(x_k\)，\(P(X=x_k)=p_k,k=1,2\dots\)为分布律
- 性质：\(p_k\ge0,\sum_{k=1}^\infty p_k=1\)

### 2.2.2 常见离散分布
#### 0-1分布
- 取值\(0,1\)，\(P(X=1)=p,P(X=0)=1-p,0<p<1\)

#### 二项分布\(X\sim B(n,p)\)
- \(P(X=k)=\binom{n}{k}p^k(1-p)^{n-k},k=0,1,\dots,n,0<p<1\)
- \(n=1\)退化为0-1分布

#### 泊松分布\(X\sim P(\lambda)\)
- \(P(X=k)=\frac{\lambda^k e^{-\lambda}}{k!},k=0,1\dots,\lambda>0\)
- 泊松近似：\(n\)大\(p\)小，\(np=\lambda\)，\(\binom{n}{k}p^k(1-p)^{n-k}\approx\frac{\lambda^k e^{-\lambda}}{k!}\)

## 2.3 随机变量的分布函数
### 2.3.1 分布函数定义
> \(F(x)=P(X\le x),x\in\mathbb R\)，称\(F(x)\)为\(X\)分布函数
- 性质：
  - 单调不减：\(x_1<x_2\Rightarrow F(x_1)\le F(x_2)\)
  - 有界：\(0\le F(x)\le1,\lim_{x\to-\infty}F(x)=0,\lim_{x\to+\infty}F(x)=1\)
  - 右连续：\(\lim_{x\to x_0^+}F(x)=F(x_0)\)
- 概率公式：\(P(a<X\le b)=F(b)-F(a),P(X=a)=F(a)-F(a^-)\)

## 2.4 连续型随机变量及其概率密度
### 2.4.1 概率密度定义
> 若存在非负可积函数\(f(x)\)，\(F(x)=\int_{-\infty}^x f(t)\mathrm dt\)，称\(X\)连续型，\(f(x)\)为概率密度。
- 密度性质：
  - \(f(x)\ge0,\int_{-\infty}^{+\infty}f(x)\mathrm dx=1\)
  - \(P(a<X\le b)=\int_a^b f(x)\mathrm dx\)
  - \(f(x)\)在连续点：\(F'(x)=f(x)\)
  - 连续型单点概率：\(P(X=a)=0\)

### 2.4.2 常用连续分布
#### 均匀分布\(X\sim U(a,b)\)
$$
f(x)=
\begin{cases}
\frac1{b-a},&a<x<b\\
0,&\text{其他}
\end{cases}
$$
$$
F(x)=
\begin{cases}
0,&x<a\\
\frac{x-a}{b-a},&a\le x<b\\
1,&x\ge b
\end{cases}
$$

#### 指数分布
$$
f(x)=
\begin{cases}
\lambda e^{-\lambda x},&x>0,\lambda>0\\
0,&x\le0
\end{cases}
$$
$$
F(x)=
\begin{cases}
1-e^{-\lambda x},&x>0\\
0,&x\le0
\end{cases}
$$
- 无记忆性：\(P(X>s+t|X>s)=P(X>t),s,t>0\)

#### 正态分布\(X\sim N(\mu,\sigma^2),\sigma>0\)
$$
f(x)=\frac1{\sqrt{2\pi}\sigma}\exp\left\{-\frac{(x-\mu)^2}{2\sigma^2}\right\},x\in\mathbb R
$$
- 标准正态\(Z\sim N(0,1)\)，\(\varphi(x)=\frac1{\sqrt{2\pi}}e^{-\frac{x^2}2},\Phi(x)=\int_{-\infty}^x\varphi(t)\mathrm dt\)
- 标准化：\(Z=\frac{X-\mu}{\sigma}\sim N(0,1),F(x)=\Phi\left(\frac{x-\mu}{\sigma}\right)\)
- \(\Phi(-x)=1-\Phi(x)\)

## 2.5 随机变量的函数的分布
### 2.5.1 离散型
- 由\(X\)分布律，逐一代入\(Y=g(X)\)取值合并相同项得\(Y\)分布律

### 2.5.2 连续型
- 已知\(X\)密度\(f_X(x)\)，\(Y=g(X)\)单调可导，反函数\(x=h(y)\)
$$
f_Y(y)=
\begin{cases}
f_X[h(y)]|h'(y)|,&\alpha<y<\beta\\
0,&\text{其他}
\end{cases}
$$

# 第三章 多维随机变量及其分布
## 3.1 二维随机变量
### 3.1.1 联合分布函数
> \(F(x,y)=P(X\le x,Y\le y),(x,y)\in\mathbb R^2\)，二维联合分布函数
- 性质：
  - 对\(x,y\)单调不减；\(0\le F(x,y)\le1\)
  - \(\lim_{x\to-\infty}F=\lim_{y\to-\infty}F=\lim_{x,y\to-\infty}F=0,\lim_{x,y\to+\infty}F=1\)
  - 分别关于\(x,y\)右连续
  - \(P(x_1<X\le x_2,y_1<Y\le y_2)=F(x_2,y_2)-F(x_2,y_1)-F(x_1,y_2)+F(x_1,y_1)\)

### 3.1.2 边缘分布
- \(F_X(x)=\lim_{y\to+\infty}F(x,y),F_Y(y)=\lim_{x\to+\infty}F(x,y)\)

## 3.2 二维离散型随机变量
### 3.2.1 联合分布律
> \(P(X=x_i,Y=y_j)=p_{ij},i,j=1,2\dots,\sum_i\sum_j p_{ij}=1,p_{ij}\ge0\)
- 边缘分布律：\(p_{i\cdot}=\sum_j p_{ij}=P(X=x_i),p_{\cdot j}=\sum_i p_{ij}=P(Y=y_j)\)

## 3.3 二维连续型随机变量
### 3.3.1 联合概率密度
> \(F(x,y)=\int_{-\infty}^x\int_{-\infty}^y f(u,v)\mathrm du\mathrm dv\)，\(f(x,y)\)为联合密度
- 性质：
  - \(f(x,y)\ge0,\iint_{\mathbb R^2}f(x,y)\mathrm dx\mathrm dy=1\)
  - \(P((X,Y)\in D)=\iint_D f(x,y)\mathrm dx\mathrm dy\)
  - \(f\)连续处：\(\frac{\partial^2 F}{\partial x\partial y}=f(x,y)\)
- 边缘密度：
$$
f_X(x)=\int_{-\infty}^{+\infty}f(x,y)\mathrm dy,\quad f_Y(y)=\int_{-\infty}^{+\infty}f(x,y)\mathrm dx
$$

### 3.3.2 二维均匀分布
$$
f(x,y)=
\begin{cases}
\frac1{A},&(x,y)\in D\\
0,&\text{其他}
\end{cases}
$$
\(A\)为区域\(D\)面积

### 3.3.3 二维正态\(N(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\rho)\)
$$
\begin{aligned}
f(x,y)=&\frac1{2\pi\sigma_1\sigma_2\sqrt{1-\rho^2}}\exp\left\{-\frac1{2(1-\rho^2)}\left[\left(\frac{x-\mu_1}{\sigma_1}\right)^2\right.\right.\\
&\left.\left.-2\rho\frac{x-\mu_1}{\sigma_1}\frac{y-\mu_2}{\sigma_2}+\left(\frac{y-\mu_2}{\sigma_2}\right)^2\right]\right\}
\end{aligned}
$$
- 边缘：\(X\sim N(\mu_1,\sigma_1^2),Y\sim N(\mu_2,\sigma_2^2)\)

## 3.4 条件分布
### 3.4.1 离散条件分布
- \(P(Y=y_j|X=x_i)=\frac{p_{ij}}{p_{i\cdot}},p_{i\cdot}>0\)
- \(P(X=x_i|Y=y_j)=\frac{p_{ij}}{p_{\cdot j}},p_{\cdot j}>0\)

### 3.4.2 连续条件密度
$$
f_{Y|X}(y|x)=\frac{f(x,y)}{f_X(x)},f_X(x)>0,\quad f_{X|Y}(x|y)=\frac{f(x,y)}{f_Y(y)},f_Y(y)>0
$$

## 3.5 相互独立的随机变量
### 3.5.1 独立判定
> \(F(x,y)=F_X(x)F_Y(y),\forall x,y\)，则\(X,Y\)相互独立
- 离散：\(p_{ij}=p_{i\cdot}p_{\cdot j},\forall i,j\)
- 连续：\(f(x,y)=f_X(x)f_Y(y)\)几乎处处成立
- 二维正态：\(\rho=0\iff X,Y\)独立

## 3.6 两个随机变量函数的分布
### 3.6.1 \(Z=X+Y\)
$$
f_Z(z)=\int_{-\infty}^{+\infty}f_X(z-y,y)\mathrm dy=\int_{-\infty}^{+\infty}f(x,z-x)\mathrm dx
$$
- 独立卷积：\(f_Z=f_X*f_Y=\int_{-\infty}^{+\infty}f_X(x)f_Y(z-x)\mathrm dx\)

### 3.6.2 \(M=\max(X,Y),N=\min(X,Y)\)（独立）
$$
F_M(z)=F_X(z)F_Y(z),\quad F_N(z)=1-[1-F_X(z)][1-F_Y(z)]
$$

# 第四章 随机变量的数字特征
## 4.1 数学期望
### 4.1.1 定义
> 离散：\(E(X)=\sum_{k=1}^\infty x_k p_k\)，级数绝对收敛；
> 连续：\(E(X)=\int_{-\infty}^{+\infty}x f(x)\mathrm dx\)，反常积分绝对收敛。

### 4.1.2 随机变量函数期望
- 离散\(Y=g(X)\)：\(E(Y)=\sum g(x_k)p_k\)
- 连续\(Y=g(X)\)：\(E(Y)=\int_{-\infty}^{+\infty}g(x)f(x)\mathrm dx\)
- 二维\(Z=g(X,Y)\)：
$$
E(Z)=
\begin{cases}
\sum_i\sum_j g(x_i,y_j)p_{ij}&\text{离散}\\
\iint g(x,y)f(x,y)\mathrm dx\mathrm dy&\text{连续}
\end{cases}
$$

### 4.1.3 期望性质
- \(E(C)=C,C\)常数；\(E(CX)=CE(X)\)
- \(E(X+Y)=E(X)+E(Y)\)；\(X,Y\)独立\(\Rightarrow E(XY)=E(X)E(Y)\)

## 4.2 方差
### 4.2.1 定义
> \(D(X)=\mathrm{Var}(X)=E\left\{[X-E(X)]^2\right\}\)，标准差\(\sigma(X)=\sqrt{D(X)}\)
- 计算公式：\(D(X)=E(X^2)-[E(X)]^2\)

### 4.2.2 方差性质
- \(D(C)=0,D(CX)=C^2D(X),D(X+C)=D(X)\)
- \(X,Y\)独立：\(D(X\pm Y)=D(X)+D(Y)\)
- \(D(X)=0\iff P(X=C)=1\)

### 4.2.3 常用分布期望方差
- 0-1：\(E=p,D=p(1-p)\)
- \(B(n,p)\)：\(E=np,D=np(1-p)\)
- \(P(\lambda)\)：\(E=\lambda,D=\lambda\)
- \(U(a,b)\)：\(E=\frac{a+b}2,D=\frac{(b-a)^2}{12}\)
- 指数\(\lambda\)：\(E=\frac1\lambda,D=\frac1{\lambda^2}\)
- \(N(\mu,\sigma^2)\)：\(E=\mu,D=\sigma^2\)

## 4.3 协方差与相关系数
### 4.3.1 协方差
> \(\mathrm{Cov}(X,Y)=E\{[X-E(X)][Y-E(Y)]\}=E(XY)-E(X)E(Y)\)
- 性质：
  - \(\mathrm{Cov}(X,Y)=\mathrm{Cov}(Y,X)\)
  - \(\mathrm{Cov}(aX,bY)=ab\mathrm{Cov}(X,Y)\)
  - \(\mathrm{Cov}(X_1+X_2,Y)=\mathrm{Cov}(X_1,Y)+\mathrm{Cov}(X_2,Y)\)
- \(D(X+Y)=D(X)+D(Y)+2\mathrm{Cov}(X,Y)\)

### 4.3.2 相关系数
$$
\rho_{XY}=\frac{\mathrm{Cov}(X,Y)}{\sqrt{D(X)}\sqrt{D(Y)}},D(X),D(Y)>0
$$
- 性质：\(|\rho_{XY}|\le1\)
- \(|\rho|=1\iff\exists a,b,P(Y=a+bX)=1\)
- \(\rho_{XY}=0\)称\(X,Y\)不相关；独立必不相关，反之不成立；二维正态独立\(\iff\rho=0\)

## 4.4 矩、协方差矩阵
### 4.4.1 矩定义
- \(k\)阶原点矩：\(E(X^k)\)；\(k\)阶中心矩：\(E\{[X-E(X)]^k\}\)
- \(k+l\)阶混合原点矩：\(E(X^kY^l)\)；混合中心矩：\(E\{[X-E(X)]^k[Y-E(Y)]^l\}\)

### 4.4.2 协方差矩阵
二维：
$$
\boldsymbol C=
\begin{pmatrix}
c_{11}&c_{12}\\
c_{21}&c_{22}
\end{pmatrix},
c_{11}=D(X),c_{22}=D(Y),c_{12}=c_{21}=\mathrm{Cov}(X,Y)
$$

# 第五章 大数定律及中心极限定理
## 5.1 大数定律
### 5.1.1 切比雪夫不等式
$$
P(|X-E(X)|\ge\varepsilon)\le\frac{D(X)}{\varepsilon^2},\forall\varepsilon>0
$$

### 5.1.2 切比雪夫大数定律
- \(X_1,X_2\dots\)两两不相关，\(D(X_k)\le C\)有界，则\(\forall\varepsilon>0\)
$$
\lim_{n\to\infty}P\left(\left|\frac1n\sum_{k=1}^n X_k-\frac1n\sum_{k=1}^n E(X_k)\right|<\varepsilon\right)=1
$$

### 5.1.3 伯努利大数定律
- \(n_A\sim B(n,p)\)：\(\lim_{n\to\infty}P\left(\left|\frac{n_A}n-p\right|<\varepsilon\right)=1\)

### 5.1.4 辛钦大数定律
- \(X_i\)独立同分布，\(E(X_i)=\mu\)存在：
$$
\lim_{n\to\infty}P\left(\left|\frac1n\sum_{k=1}^n X_k-\mu\right|<\varepsilon\right)=1
$$

## 5.2 中心极限定理
### 5.2.1 独立同分布中心极限（林-莱）
- \(X_i\)独立同分布，\(E=\mu,D=\sigma^2>0\)
$$
\lim_{n\to\infty}P\left(\frac{\sum_{k=1}^n X_k-n\mu}{\sqrt{n}\sigma}\le x\right)=\Phi(x)
$$

### 5.2.2 棣莫弗-拉普拉斯
- \(X\sim B(n,p)\)：
$$
\lim_{n\to\infty}P\left(\frac{X-np}{\sqrt{np(1-p)}}\le x\right)=\Phi(x)
$$

# 第六章 样本及抽样分布
## 6.1 随机样本
### 6.1.1 总体与样本
> 研究对象全部取值为总体\(X\)；\(X_1,\dots,X_n\)独立同\(X\)分布，称简单随机样本。
- 样本联合分布：\(F^*(x_1\dots x_n)=\prod_{i=1}^n F(x_i)\)；密度\(f^*=\prod f(x_i)\)

### 6.1.2 统计量
> 不含未知参数的样本函数\(g(X_1\dots X_n)\)称为统计量。
- 常用统计量：
  - 样本均值：\(\overline X=\frac1n\sum_{i=1}^n X_i\)
  - 样本方差：\(S^2=\frac1{n-1}\sum_{i=1}^n(X_i-\overline X)^2\)
  - 样本标准差：\(S=\sqrt{S^2}\)
  - \(k\)阶原点矩：\(A_k=\frac1n\sum X_i^k\)；\(k\)阶中心矩：\(B_k=\frac1n\sum(X_i-\overline X)^k\)

## 6.2 抽样分布
### 6.2.1 \(\chi^2\)分布
- \(X_1\dots X_n\stackrel{\text{iid}}{\sim}N(0,1)\)，\(\chi^2=\sum_{i=1}^n X_i^2\sim\chi^2(n)\)，\(n\)自由度
- 性质：\(E(\chi^2)=n,D(\chi^2)=2n\)；可加：\(\chi_1^2(n_1)+\chi_2^2(n_2)\sim\chi^2(n_1+n_2)\)

### 6.2.2 \(t\)分布
- \(X\sim N(0,1),Y\sim\chi^2(n)\)独立，\(t=\frac X{\sqrt{Y/n}}\sim t(n)\)
- \(n\to\infty,t(n)\xrightarrow{\text{渐近}}N(0,1)\)

### 6.2.3 \(F\)分布
- \(U\sim\chi^2(n_1),V\sim\chi^2(n_2)\)独立，\(F=\frac{U/n_1}{V/n_2}\sim F(n_1,n_2)\)，\(F^{-1}\sim F(n_2,n_1)\)

### 6.2.4 正态总体常用抽样结论
- \(X\sim N(\mu,\sigma^2)\)，\(\overline X\sim N(\mu,\sigma^2/n)\)，\(\frac{(n-1)S^2}{\sigma^2}\sim\chi^2(n-1)\)，\(\overline X\)与\(S^2\)独立
- \(\frac{\overline X-\mu}{S/\sqrt{n}}\sim t(n-1)\)

# 第七章 参数估计
## 7.1 点估计
### 7.1.1 矩估计
> 以样本\(k\)阶矩\(A_k\)替换总体\(k\)阶矩\(\mu_k=E(X^k)\)，解方程得参数矩估计量。

### 7.1.2 最大似然估计
- 似然函数：离散\(L(\theta)=\prod_{i=1}^n p(x_i;\theta)\)；连续\(L(\theta)=\prod_{i=1}^n f(x_i;\theta)\)
- \(\hat\theta=\mathop{\arg\max}_{\theta}L(\theta)\)；对数似然\(\ln L(\theta)\)，求导\(\frac{\mathrm d\ln L}{\mathrm d\theta}=0\)解MLE

## 7.2 估计量评选标准
### 7.2.1 无偏性
> \(E(\hat\theta)=\theta,\forall\theta\)，\(\hat\theta\)为\(\theta\)无偏估计
- \(\overline X\)是\(\mu\)无偏，\(S^2\)是\(\sigma^2\)无偏，样本二阶中心矩\(B_2\)非无偏

### 7.2.2 有效性
- \(\hat\theta_1,\hat\theta_2\)均无偏，\(D(\hat\theta_1)<D(\hat\theta_2)\)则\(\hat\theta_1\)更有效

### 7.2.3 相合性
- \(n\to\infty,\hat\theta\xrightarrow{P}\theta\)，称\(\hat\theta\)为相合估计

## 7.3 区间估计
### 7.3.1 置信区间定义
> \(P(\underline\theta<\theta<\overline\theta)=1-\alpha\)，\(1-\alpha\)置信水平，\((\underline\theta,\overline\theta)\)置信区间

### 7.3.2 正态总体均值与方差置信区间
#### \(\sigma^2\)已知，\(\mu\)：\(\left(\overline X\pm z_{\alpha/2}\frac{\sigma}{\sqrt n}\right)\)
#### \(\sigma^2\)未知，\(\mu\)：\(\left(\overline X\pm t_{\alpha/2}(n-1)\frac{S}{\sqrt n}\right)\)
#### \(\mu\)未知，\(\sigma^2\)：\(\left(\frac{(n-1)S^2}{\chi^2_{\alpha/2}(n-1)},\frac{(n-1)S^2}{\chi^2_{1-\alpha/2}(n-1)}\right)\)

# 第八章 假设检验
## 8.1 假设检验基本概念
### 8.1.1 原假设与备择假设
- 原假设\(H_0\)：待检验的假设，备择假设\(H_1\)：与原假设对立的假设。
- 双侧假设：\(H_0:\mu=\mu_0,\ H_1:\mu\neq\mu_0\)
- 单侧假设：\(H_0:\mu\le\mu_0,H_1:\mu>\mu_0\)；\(H_0:\mu\ge\mu_0,H_1:\mu<\mu_0\)

### 8.1.2 两类错误
> 第一类错误（弃真错误）：\(H_0\)成立时拒绝\(H_0\)；第二类错误（取伪错误）：\(H_0\)不成立时接受\(H_0\)。
- \(\alpha=P\{\text{拒}H_0|H_0\text{真}\}\)为显著性水平，预先限定第一类错误概率。

### 8.1.3 显著性检验与拒绝域
- 检验统计量：依托样本构造、用于判定假设的随机变量。
- 拒绝域：样本观测值落入则拒绝\(H_0\)的统计量取值集合。
- 显著性检验：固定\(\alpha\)、只控制第一类错误概率的假设检验。

## 8.2 正态总体均值的假设检验
### 8.2.1 \(\sigma^2\)已知，Z检验
- 检验统计量：
$$
Z=\frac{\bar{X}-\mu_0}{\sigma/\sqrt{n}}\sim N(0,1)
$$
- 双侧拒绝域：\(|Z|\ge z_{\alpha/2}\)

### 8.2.2 \(\sigma^2\)未知，t检验
- 检验统计量：
$$
t=\frac{\bar{X}-\mu_0}{S/\sqrt{n}}\sim t(n-1)
$$
- 双侧拒绝域：\(|t|\ge t_{\alpha/2}(n-1)\)

### 8.2.3 两正态总体均值差检验
- \(\sigma_1^2,\sigma_2^2\)已知：
$$
Z=\frac{\bar{X}-\bar{Y}-\delta}{\sqrt{\frac{\sigma_1^2}{n_1}+\frac{\sigma_2^2}{n_2}}}\sim N(0,1)
$$
- \(\sigma_1^2=\sigma_2^2=\sigma^2\)未知：
$$
t=\frac{\bar{X}-\bar{Y}-\delta}{S_p\sqrt{\frac1{n_1}+\frac1{n_2}}},\quad S_p^2=\frac{(n_1-1)S_1^2+(n_2-1)S_2^2}{n_1+n_2-2}\sim t(n_1+n_2-2)
$$

## 8.3 正态总体方差的假设检验
### 8.3.1 单个总体\(\chi^2\)检验
- 检验统计量：
$$
\chi^2=\frac{(n-1)S^2}{\sigma_0^2}\sim \chi^2(n-1)
$$
- 双侧拒绝域：\(\chi^2\le\chi^2_{1-\alpha/2}(n-1)\)或\(\chi^2\ge\chi^2_{\alpha/2}(n-1)\)

### 8.3.2 两个总体F检验
- 检验统计量：
$$
F=\frac{S_1^2}{S_2^2}\sim F(n_1-1,n_2-1)
$$

## 8.4 分布拟合检验
### 8.4.1 \(\chi^2\)拟合优度检验
> 用于检验总体是否服从指定分布。
- 检验统计量：
$$
\chi^2=\sum_{i=1}^k\frac{(f_i-np_i)^2}{np_i}\stackrel{近似}{\sim}\chi^2(k-r-1)
$$
- \(k\)：分组组数，\(r\)：分布中待估参数个数，\(f_i\)：频数，\(np_i\)：理论频数。

# 第九章 方差分析及回归分析
## 9.1 单因素方差分析
### 9.1.1 数学模型
- 观测模型：\(X_{ij}=\mu+\alpha_i+\varepsilon_{ij}\)，\(\varepsilon_{ij}\stackrel{iid}{\sim}N(0,\sigma^2)\)，\(\sum_{i=1}^k n_i\alpha_i=0\)
- 假设：\(H_0:\alpha_1=\alpha_2=\dots=\alpha_k=0,\ H_1:\exists\alpha_i\neq0\)

### 9.1.2 平方和分解
- 总平方和：\(S_T=\sum_{i=1}^k\sum_{j=1}^{n_i}(X_{ij}-\bar{X}_{\cdot\cdot})^2\)
- 因素平方和：\(S_A=\sum_{i=1}^k n_i(\bar{X}_{i\cdot}-\bar{X}_{\cdot\cdot})^2\)
- 误差平方和：\(S_E=\sum_{i=1}^k\sum_{j=1}^{n_i}(X_{ij}-\bar{X}_{i\cdot})^2\)
- 分解式：\(S_T=S_A+S_E\)

### 9.1.3 F统计量
$$
F=\frac{S_A/(k-1)}{S_E/(n-k)}\sim F(k-1,n-k),\ n=\sum n_i
$$

## 9.2 双因素方差分析
### 9.2.1 无交互作用双因素模型
- \(X_{ij}=\mu+\alpha_i+\beta_j+\varepsilon_{ij}\)，约束\(\sum\alpha_i=\sum\beta_j=0\)
- 平方和分解：\(S_T=S_A+S_B+S_E\)
$$
F_A=\frac{S_A/(r-1)}{S_E/[(r-1)(s-1)]},\quad F_B=\frac{S_B/(s-1)}{S_E/[(r-1)(s-1)]}
$$

### 9.2.2 有交互作用双因素模型
- \(X_{ijk}=\mu+\alpha_i+\beta_j+\gamma_{ij}+\varepsilon_{ijk}\)，\(\gamma_{ij}\)为交互效应
- 平方和分解：\(S_T=S_A+S_B+S_{AB}+S_E\)

## 9.3 一元线性回归
### 9.3.1 一元线性回归模型
> \(y_i=\beta_0+\beta_1 x_i+\varepsilon_i,\ \varepsilon_i\stackrel{iid}{\sim}N(0,\sigma^2)\)
- \(\beta_0\)截距，\(\beta_1\)回归系数。

### 9.3.2 最小二乘估计
$$
\hat\beta_1=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2},\quad \hat\beta_0=\bar y-\hat\beta_1\bar x
$$
- 回归方程：\(\hat y=\hat\beta_0+\hat\beta_1 x\)

### 9.3.3 平方和分解
- \(S_{yy}=\sum(y_i-\bar y)^2=S_{回}+S_{剩}\)
$$
F=\frac{S_{回}/1}{S_{剩}/(n-2)}\sim F(1,n-2)
$$

## 9.4 多元线性回归
- 模型：\(y=\beta_0+\beta_1 x_1+\dots+\beta_p x_p+\varepsilon,\varepsilon\sim N(0,\sigma^2)\)
- 矩阵形式\(\boldsymbol Y=\boldsymbol X\boldsymbol \beta+\boldsymbol \varepsilon\)，最小二乘\(\hat{\boldsymbol\beta}=(\boldsymbol X^\mathrm{T}\boldsymbol X)^{-1}\boldsymbol X^\mathrm{T}\boldsymbol Y\)

# 第十章 随机过程及其统计描述
## 10.1 随机过程基本概念
> 随机过程\(\{X(t),t\in T\}\)：参数\(t\in T\)，任意固定\(t\)，\(X(t)\)为随机变量；固定样本为时间函数（样本轨道）。
- \(T\)为参数集，离散参数：随机序列；连续参数：连续参数随机过程。

### 10.1.1 有限维分布族
- \(n\)维分布：\(F_n(x_1,x_2,\dots,x_n;t_1,\dots,t_n)=P\{X(t_1)\le x_1,\dots,X(t_n)\le x_n\}\)
- 有限维分布族确定随机过程全部统计规律。

### 10.1.2 数字特征
- 均值函数：\(\mu_X(t)=E[X(t)]\)
- 自相关函数：\(R_X(t_1,t_2)=E[X(t_1)X(t_2)]\)
- 自协方差：\(C_X(t_1,t_2)=R_X(t_1,t_2)-\mu_X(t_1)\mu_X(t_2)\)
- 方差函数：\(\sigma_X^2(t)=C_X(t,t)\)

## 10.2 泊松过程
### 10.2.1 齐次泊松过程定义
> 计数过程\(\{N(t),t\ge0\}\)满足独立增量、平稳增量、\(P\{N(0)=0\}\)，\(P\{N(t+s)-N(s)=k\}=\frac{(\lambda t)^k e^{-\lambda t}}{k!}\)。
- 均值\(E[N(t)]=\lambda t\)，\(\lambda\)为强度。

### 10.2.2 数字特征
$$
R_N(s,t)=\lambda^2 st+\lambda\min(s,t),\quad C_N(s,t)=\lambda\min(s,t)
$$

## 10.3 维纳过程
### 10.3.1 标准维纳过程定义
> \(\{W(t),t\ge0\}\)：独立平稳增量，\(W(0)=0\)，\(W(t+s)-W(s)\sim N(0,\sigma^2 t)\)；\(\sigma=1\)为标准维纳。
- 均值\(\mu_W(t)=0\)，\(C_W(s,t)=\sigma^2\min(s,t)\)

# 第十一章 马尔可夫链
## 11.1 马尔可夫链基本定义
> 马尔可夫性：\(P\{X_{n+1}=j|X_n=i,X_{n-1}=i_{n-1},\dots,X_0=i_0\}=P\{X_{n+1}=j|X_n=i\}\)
- 离散状态、离散参数的马尔可夫过程称为马尔可夫链。

### 11.1.1 转移概率
- 一步转移概率：\(p_{ij}=P\{X_{n+1}=j|X_n=i\}\)
- 一步转移矩阵\(\boldsymbol P=(p_{ij})\)，满足\(\sum_j p_{ij}=1\)。

### 11.1.2 n步转移概率
$$
p_{ij}^{(n)}=P\{X_{m+n}=j|X_m=i\}
$$
- C-K方程：\(p_{ij}^{(m+n)}=\sum_{k}p_{ik}^{(m)}p_{kj}^{(n)}\)，\(\boldsymbol P^{(m+n)}=\boldsymbol P^{(m)}\boldsymbol P^{(n)}\)

## 11.2 状态分类
- 首达概率：\(f_{ij}^{(n)}=P\{首次n步从i到j\}\)，\(f_{ij}=\sum_{n=1}^\infty f_{ij}^{(n)}\)
- 常返：\(f_{ii}=1\)；非常返：\(f_{ii}<1\)
- 周期：\(d=\gcd\{n|p_{ii}^{(n)}>0\}\)，\(d=1\)为非周期。

## 11.3 平稳分布
- 平稳分布\(\boldsymbol\pi=(\pi_j)\)满足：\(\pi_j=\sum_i\pi_i p_{ij},\ \sum_j\pi_j=1\)

# 第十二章 平稳随机过程
## 12.1 平稳过程定义
### 12.1.1 严平稳过程
> 任意\(n,t_1,\dots,t_n,\tau\)，\(n\)维分布满足\(F_n(x_1,\dots,x_n;t_1+\tau,\dots,t_n+\tau)=F_n(x_1,\dots,x_n;t_1,\dots,t_n)\)。

### 12.1.2 宽平稳过程
- \(\mu_X(t)=\mu_X\)常数；
- \(R_X(t_1,t_2)=R_X(t_2-t_1)=R_X(\tau),\tau=t_2-t_1\)；
- \(E[X^2(t)]<+\infty\)。

## 12.2 相关函数性质
- \(R_X(\tau)=R_X(-\tau)\)偶函数；
- \(|R_X(\tau)|\le R_X(0)\)；
- \(R_X(\tau)\)非负定。

## 12.3 功率谱密度
### 12.3.1 维纳-辛钦公式
$$
S_X(\omega)=\int_{-\infty}^{+\infty}R_X(\tau)e^{-j\omega\tau}\mathrm d\tau,\quad
R_X(\tau)=\frac1{2\pi}\int_{-\infty}^{+\infty}S_X(\omega)e^{j\omega\tau}\mathrm d\omega
$$
- \(S_X(\omega)\)为自功率谱密度，实、非负偶函数。

## 12.4 各态历经性
> 时间平均：\(\langle X(t)\rangle=\lim_{T\to\infty}\frac1{2T}\int_{-T}^T X(t)\mathrm dt\)；
> 均值各态历经：\(\langle X(t)\rangle=\mu_X\)依概率1成立；
> 自相关各态历经：\(\langle X(t+\tau)X(t)\rangle=R_X(\tau)\)依概率1成立。