# 第一章 行列式
## 1.1 二阶与三阶行列式
### 1.1.1 二阶行列式
> **定义**：由四个数排成二行二列的数表
> $$
> \begin{matrix}
> a_{11} & a_{12} \\
> a_{21} & a_{22}
> \end{matrix}
> $$
> 表达式$a_{11}a_{22}-a_{12}a_{21}$称为该数表对应的**二阶行列式**，记作
> $$
> D=
> \begin{vmatrix}
> a_{11} & a_{12} \\
> a_{21} & a_{22}
> \end{vmatrix}
> =a_{11}a_{22}-a_{12}a_{21}
> $$

### 1.1.2 三阶行列式
> **定义**：由九个数排成三行三列的数表对应的**三阶行列式**定义为
> $$
> D=
> \begin{vmatrix}
> a_{11} & a_{12} & a_{13} \\
> a_{21} & a_{22} & a_{23} \\
> a_{31} & a_{32} & a_{33}
> \end{vmatrix}
> $$
> $$
> =a_{11}a_{22}a_{33}+a_{12}a_{23}a_{31}+a_{13}a_{21}a_{32}-a_{13}a_{22}a_{31}-a_{12}a_{21}a_{33}-a_{11}a_{23}a_{32}
> $$

## 1.2 全排列和对换
### 1.2.1 全排列
> **定义**：把$n$个不同的元素排成一列，叫做这$n$个元素的**全排列**（简称排列）。
> **推论**：$n$个不同元素的全排列总数为$P_n=n!$。

### 1.2.2 逆序数
> **定义**：在一个排列中，如果一对数的前后位置与大小顺序相反，即前面的数大于后面的数，那么它们就称为一个**逆序**。一个排列中逆序的总数就称为这个排列的**逆序数**。
> **分类**：
> - 逆序数为偶数的排列称为**偶排列**；
> - 逆序数为奇数的排列称为**奇排列**。

### 1.2.3 对换
> **定义**：在排列中，将任意两个元素对调，其余元素不动，这种作出新排列的变换叫做**对换**。将相邻两个元素对换，叫做**相邻对换**。
- **性质1**：一个排列中的任意两个元素对换，排列改变奇偶性。
- **推论**：奇排列调成标准排列的对换次数为奇数，偶排列调成标准排列的对换次数为偶数。
- **性质2**：$n$级排列中，奇、偶排列的个数相等，各占$\displaystyle\frac{n!}{2}$个。

## 1.3 $n$阶行列式的定义
> **定义**：$n$阶行列式
> $$
> D=
> \begin{vmatrix}
> a_{11} & a_{12} & \dots & a_{1n} \\
> a_{21} & a_{22} & \dots & a_{2n} \\
> \vdots & \vdots & \ddots & \vdots \\
> a_{n1} & a_{n2} & \dots & a_{nn}
> \end{vmatrix}
> =\sum(-1)^{\tau(p_1p_2\dots p_n)}a_{1p_1}a_{2p_2}\dots a_{np_n}
> $$
> 其中$p_1p_2\dots p_n$为自然数$1,2,\dots,n$的一个排列，$\tau$为该排列的逆序数，$\sum$表示对所有$n$级排列求和。

### 1.3.1 特殊行列式
- **对角行列式**
$$
\begin{vmatrix}
\lambda_1 & & & \\
& \lambda_2 & & \\
& & \ddots & \\
& & & \lambda_n
\end{vmatrix}
=\lambda_1\lambda_2\dots\lambda_n
$$
$$
\begin{vmatrix}
& & & \lambda_1 \\
& & \lambda_2 & \\
& \ddots & & \\
\lambda_n & & &
\end{vmatrix}
=(-1)^{\frac{n(n-1)}{2}}\lambda_1\lambda_2\dots\lambda_n
$$
- **上三角行列式**
$$
\begin{vmatrix}
a_{11} & a_{12} & \dots & a_{1n} \\
0 & a_{22} & \dots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \dots & a_{nn}
\end{vmatrix}
=a_{11}a_{22}\dots a_{nn}
$$
- **下三角行列式**
$$
\begin{vmatrix}
a_{11} & 0 & \dots & 0 \\
a_{21} & a_{22} & \dots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
a_{n1} & a_{n2} & \dots & a_{nn}
\end{vmatrix}
=a_{11}a_{22}\dots a_{nn}
$$

## 1.4 行列式的性质
> **定义**：将行列式$D$的行换成同序数的列得到的新行列式，称为$D$的**转置行列式**，记作$D^T$。
- **性质1**：行列式与它的转置行列式相等，即$D=D^T$。
- **性质2**：互换行列式的两行（列），行列式变号。
  - 推论：如果行列式有两行（列）完全相同，则此行列式等于零。
- **性质3**：行列式的某一行（列）中所有的元素都乘以同一数$k$，等于用数$k$乘此行列式。
  - 推论：行列式中某一行（列）的所有元素的公因子可以提到行列式符号的外面。
- **性质4**：行列式中如果有两行（列）元素成比例，则此行列式等于零。
- **性质5**：若行列式的某一行（列）的元素都是两数之和，则该行列式可拆分为两个行列式之和。
- **性质6**：把行列式的某一行（列）的各元素乘以同一数然后加到另一行（列）对应的元素上去，行列式不变。

## 1.5 行列式按行（列）展开
### 1.5.1 余子式与代数余子式
> **余子式定义**：在$n$阶行列式中，把元素$a_{ij}$所在的第$i$行和第$j$列上的所有元素都划去，留下来的$n-1$阶行列式叫做元素$a_{ij}$的**余子式**，记作$M_{ij}$。
> **代数余子式定义**：$A_{ij}=(-1)^{i+j}M_{ij}$，称$A_{ij}$为元素$a_{ij}$的**代数余子式**。

### 1.5.2 展开定理
> **定理**：行列式等于它的任一行（列）的各元素与其对应的代数余子式乘积之和，即
> $$
> D=\sum_{j=1}^n a_{ij}A_{ij} \quad (i=1,2,\dots,n)
> $$
> $$
> D=\sum_{i=1}^n a_{ij}A_{ij} \quad (j=1,2,\dots,n)
> $$
- **推论**：行列式某一行（列）的元素与另一行（列）的对应元素的代数余子式乘积之和等于零，即
$$
\sum_{j=1}^n a_{ij}A_{kj}=0 \quad (i\ne k)
$$
$$
\sum_{i=1}^n a_{ij}A_{ik}=0 \quad (j\ne k)
$$

## 1.6 克拉默法则
> **克拉默法则**：如果$n$元线性方程组
> $$
> \begin{cases}
> a_{11}x_1+a_{12}x_2+\dots+a_{1n}x_n=b_1 \\
> a_{21}x_1+a_{22}x_2+\dots+a_{2n}x_n=b_2 \\
> \quad\vdots \\
> a_{n1}x_1+a_{n2}x_2+\dots+a_{nn}x_n=b_n
> \end{cases}
> $$
> 的系数行列式$D\ne0$，则方程组有**唯一解**
> $$
> x_1=\frac{D_1}{D},\quad x_2=\frac{D_2}{D},\quad \dots,\quad x_n=\frac{D_n}{D}
> $$
> 其中$D_j(j=1,2,\dots,n)$是把系数行列式$D$中第$j$列的元素用方程组右端的常数项代替后所得到的$n$阶行列式。

### 1.6.1 推论
- **推论1**：如果线性方程组无解或有两个不同的解，则它的系数行列式必为零。
- **推论2**：$n$元齐次线性方程组，若系数行列式$D\ne0$，则齐次方程组**仅有零解**。
- **推论3**：若$n$元齐次线性方程组有非零解，则它的系数行列式必为零。

# 第二章 矩阵及其运算
## 2.1 矩阵
### 2.1.1 矩阵定义
> 由 $m\times n$ 个数 $a_{ij}(i=1,2,\dots,m;j=1,2,\dots,n)$ 排成 $m$ 行 $n$ 列的数表
$$
A=\begin{pmatrix}
a_{11} & a_{12} & \dots & a_{1n}\\
a_{21} & a_{22} & \dots & a_{2n}\\
\vdots & \vdots & & \vdots\\
a_{m1} & a_{m2} & \dots & a_{mn}
\end{pmatrix}
$$
称为 $m\times n$ 矩阵，简记 $A=(a_{ij})_{m\times n}$，$a_{ij}$ 为矩阵第 $i$ 行第 $j$ 列元素。
- 行数与列数都等于 $n$ 的矩阵称为$n$阶方阵。
- $m=1$ 时，$A=(a_{11},a_{12},\dots,a_{1n})$，称为行矩阵；$n=1$ 时，$A=\begin{pmatrix}a_{11}\\a_{21}\\\vdots\\a_{m1}\end{pmatrix}$，称为列矩阵。
- 元素全为0的矩阵称为零矩阵，记作$O$。
> 两个矩阵行数、列数分别相等，称为同型矩阵；同型矩阵对应元素全部相等，则两矩阵相等。

### 2.1.2 特殊方阵
- **对角矩阵**：$n$阶方阵除主对角线元素外其余元素全为0
$$
\Lambda=\mathrm{diag}(\lambda_1,\lambda_2,\dots,\lambda_n)=
\begin{pmatrix}
\lambda_1 & & \\
& \lambda_2 & \\
& & \ddots & \\
& & & \lambda_n
\end{pmatrix}
$$
- **单位矩阵**：主对角线元素全为1的对角矩阵，记作$E$
$$
E_n=\begin{pmatrix}
1 & & \\
& 1 & \\
& & \ddots & \\
& & & 1
\end{pmatrix}
$$
- **数量矩阵**：主对角线元素全为$\lambda$的对角矩阵 $\lambda E$。

## 2.2 矩阵的运算
### 2.2.1 矩阵加法
> 设$A=(a_{ij})_{m\times n},B=(b_{ij})_{m\times n}$为同型矩阵，$A+B=(a_{ij}+b_{ij})_{m\times n}$。
- $A+B=B+A$
- $(A+B)+C=A+(B+C)$
- $A+O=A$
- 负矩阵：$-A=(-a_{ij})_{m\times n}$，$A+(-A)=O$，矩阵减法$A-B=A+(-B)$

### 2.2.2 数乘矩阵
> $\lambda$为数，$A=(a_{ij})_{m\times n}$，$\lambda A=(\lambda a_{ij})_{m\times n}$。
- $\lambda(\mu A)=(\lambda\mu)A$
- $(\lambda+\mu)A=\lambda A+\mu A$
- $\lambda(A+B)=\lambda A+\lambda B$
- $1\cdot A=A$

### 2.2.3 矩阵乘法
> $A=(a_{ij})_{m\times s},B=(b_{ij})_{s\times n}$，乘积$C=AB=(c_{ij})_{m\times n}$，其中
$$c_{ij}=\sum_{k=1}^s a_{ik}b_{kj},\quad i=1,\dots,m;j=1,\dots,n$$
- $(AB)C=A(BC)$
- $A(B+C)=AB+AC,\ (B+C)A=BA+CA$
- $\lambda(AB)=(\lambda A)B=A(\lambda B)$
- $E_mA_{m\times n}=A,\ AE_n=A$
- 矩阵乘法一般不满足交换律、消去律；$AB=O$不能推出$A=O$或$B=O$。

### 2.2.4 方阵幂运算
> $A$为$n$阶方阵，$A^k=\underbrace{AA\cdots A}_{k个}$。
- $A^kA^l=A^{k+l}$
- $(A^k)^l=A^{kl}$

## 2.3 矩阵的转置
> $A=(a_{ij})_{m\times n}$，转置矩阵$A^\mathrm{T}=(a_{ji})_{n\times m}$。
- $(A^\mathrm{T})^\mathrm{T}=A$
- $(A+B)^\mathrm{T}=A^\mathrm{T}+B^\mathrm{T}$
- $(\lambda A)^\mathrm{T}=\lambda A^\mathrm{T}$
- $(AB)^\mathrm{T}=B^\mathrm{T}A^\mathrm{T}$
> $A^\mathrm{T}=A$称对称矩阵；$A^\mathrm{T}=-A$称反对称矩阵。

## 2.4 方阵的行列式
> $n$阶方阵$A$，元素构成的$n$阶行列式记作$|A|$或$\det A$。
- $|A^\mathrm{T}|=|A|$
- $|\lambda A|=\lambda^n|A|$
- $|AB|=|A||B|$（$A,B$为同阶方阵）

## 2.5 逆矩阵
### 2.5.1 逆矩阵定义
> $A$为$n$阶方阵，若存在$n$阶方阵$B$满足$AB=BA=E$，则$A$可逆，$B$是$A$的逆矩阵，记作$A^{-1}$。
- 可逆矩阵逆矩阵唯一。

### 2.5.2 伴随矩阵
> $A=(a_{ij})_{n\times n}$，$A_{ij}$是$|A|$中$a_{ij}$的代数余子式，伴随矩阵
$$
A^*=\begin{pmatrix}
A_{11} & A_{21} & \dots & A_{n1}\\
A_{12} & A_{22} & \dots & A_{n2}\\
\vdots & \vdots & & \vdots\\
A_{1n} & A_{2n} & \dots & A_{nn}
\end{pmatrix}
$$
- $AA^*=A^*A=|A|E$

### 2.5.3 可逆判定与运算性质
> $n$阶方阵$A$可逆$\iff|A|\neq0$，且$\displaystyle A^{-1}=\frac1{|A|}A^*$。
- $(A^{-1})^{-1}=A$
- $(\lambda A)^{-1}=\displaystyle\frac1\lambda A^{-1}\ (\lambda\neq0)$
- $(AB)^{-1}=B^{-1}A^{-1}$（$A,B$同阶可逆）
- $(A^\mathrm{T})^{-1}=(A^{-1})^\mathrm{T}$

## 2.6 分块矩阵
### 2.6.1 分块运算规则
- 同型矩阵按相同分块方式分块，加法为对应子块相加。
- 数乘矩阵：数乘所有子块。
- 矩阵乘法：左矩阵列分块与右矩阵行分块一致，子块按矩阵乘法运算。
- 分块转置：先整体转置再各子块转置。

### 2.6.2 分块对角阵
$$
M=\mathrm{diag}(M_1,M_2,\dots,M_s)=
\begin{pmatrix}
M_1 & & \\
& M_2 & \\
& & \ddots & \\
& & & M_s
\end{pmatrix}
$$
- $|M|=|M_1||M_2|\cdots|M_s|$
- $M$可逆$\iff$每个$M_i$均可逆，$\displaystyle M^{-1}=\mathrm{diag}(M_1^{-1},M_2^{-1},\dots,M_s^{-1})$

# 第三章 矩阵的初等变换与线性方程组
## 3.1 矩阵的初等变换
### 3.1.1 初等变换定义
> **定义**：下面三种变换称为矩阵的初等行变换：
> 1. 对换两行（对换第$i,j$两行，记作$r_i\leftrightarrow r_j$）；
> 2. 以数$k\neq0$乘某一行中的所有元素（第$i$行乘$k$，记作$r_i\times k$）；
> 3. 把某一行所有元素的$k$倍加到另一行对应的元素上去（第$j$行的$k$倍加到第$i$行，记作$r_i+kr_j$）。
> 把定义中的“行”换成“列”，即得矩阵的初等列变换（所用记号是把$r$换成$c$）；初等行变换与初等列变换统称初等变换。

> **定义**：若矩阵$\boldsymbol{A}$经过有限次初等变换变成矩阵$\boldsymbol{B}$，则称$\boldsymbol{A}$与$\boldsymbol{B}$等价，记作$\boldsymbol{A}\sim\boldsymbol{B}$。

- 矩阵等价满足下述性质：
  - 自反性：$\boldsymbol{A}\sim\boldsymbol{A}$；
  - 对称性：若$\boldsymbol{A}\sim\boldsymbol{B}$，则$\boldsymbol{B}\sim\boldsymbol{A}$；
  - 传递性：若$\boldsymbol{A}\sim\boldsymbol{B},\boldsymbol{B}\sim\boldsymbol{C}$，则$\boldsymbol{A}\sim\boldsymbol{C}$。

### 3.1.2 行阶梯形与行最简形矩阵
> **定义**：行阶梯形矩阵满足：
> 1. 非零行在零行上方；
> 2. 非零行首非零元所在列随行数增大右移。

> **定义**：行最简形矩阵是特殊行阶梯形矩阵，非零行首非零元为$1$，首非零元所在列其余元素全为$0$。

> **定理**：任意矩阵$\boldsymbol{A}_{m\times n}$总可经有限次初等行变换化为行阶梯形，进一步化为行最简形；再经初等列变换可化为等价标准形
$$
\boldsymbol{F}=\begin{pmatrix}
\boldsymbol{E}_r & \boldsymbol{O}\\
\boldsymbol{O} & \boldsymbol{O}
\end{pmatrix}
$$
其中$r$为非零行行数。

## 3.2 初等矩阵
### 3.2.1 初等矩阵定义
> **定义**：由单位矩阵$\boldsymbol{E}$经过一次初等变换得到的矩阵称为初等矩阵。

- 三类初等矩阵：
  - 互换$\boldsymbol{E}$的$i,j$行（列），得初等对换矩阵$\boldsymbol{E}(i,j)$；
  - $\boldsymbol{E}$第$i$行（列）乘$k\neq0$，得初等倍乘矩阵$\boldsymbol{E}(i(k))$；
  - $\boldsymbol{E}$第$j$行$k$倍加至第$i$行（第$i$列$k$倍加至第$j$列），得初等倍加矩阵$\boldsymbol{E}(ij(k))$。

### 3.2.2 初等矩阵相关定理
> **定理**：设$\boldsymbol{A}$是$m\times n$矩阵，对$\boldsymbol{A}$施行一次初等行变换，等价于在$\boldsymbol{A}$左侧乘相应$m$阶初等矩阵；对$\boldsymbol{A}$施行一次初等列变换，等价于在$\boldsymbol{A}$右侧乘相应$n$阶初等矩阵。

> **定理**：方阵$\boldsymbol{A}$可逆$\iff$存在有限个初等矩阵$\boldsymbol{P}_1,\boldsymbol{P}_2,\dots,\boldsymbol{P}_l$，使
$$
\boldsymbol{A}=\boldsymbol{P}_1\boldsymbol{P}_2\cdots\boldsymbol{P}_l
$$

- 推论：$n$阶方阵$\boldsymbol{A}\sim\boldsymbol{E}\iff\boldsymbol{A}$可逆；矩阵$\boldsymbol{A}_{m\times n}\sim\boldsymbol{B}\iff$存在$m$阶可逆阵$\boldsymbol{P}$、$n$阶可逆阵$\boldsymbol{Q}$，满足$\boldsymbol{B}=\boldsymbol{PAQ}$。

## 3.3 矩阵的秩
### 3.3.1 秩的定义
> **定义**：在矩阵$\boldsymbol{A}$中任取$k$行$k$列，交叉元素构成$k$阶行列式，称为$\boldsymbol{A}$的$k$阶子式。

> **定义**：矩阵$\boldsymbol{A}$中最高阶非零子式的阶数称作矩阵$\boldsymbol{A}$的秩，记作$R(\boldsymbol{A})$；规定零矩阵的秩$R(\boldsymbol{O})=0$。

### 3.3.2 秩的基础性质
- 基本性质：
  - $0\le R(\boldsymbol{A}_{m\times n})\le\min\{m,n\}$；
  - $R(\boldsymbol{A})=R(\boldsymbol{A}^\mathrm{T})$；
  - 若$\boldsymbol{A}\sim\boldsymbol{B}$，则$R(\boldsymbol{A})=R(\boldsymbol{B})$；
  - 设$\boldsymbol{P},\boldsymbol{Q}$可逆，则$R(\boldsymbol{PAQ})=R(\boldsymbol{A})$。

- 运算相关性质：
  - $R(\boldsymbol{A}+\boldsymbol{B})\le R(\boldsymbol{A})+R(\boldsymbol{B})$；
  - $R(\boldsymbol{AB})\le\min\{R(\boldsymbol{A}),R(\boldsymbol{B})\}$；
  - 若$\boldsymbol{A}_{m\times n}\boldsymbol{B}_{n\times l}=\boldsymbol{O}$，则$R(\boldsymbol{A})+R(\boldsymbol{B})\le n$。

## 3.4 线性方程组的解
### 3.4.1 非齐次线性方程组
> **定理**：$n$元非齐次线性方程组$\boldsymbol{A}_{m\times n}\boldsymbol{x}=\boldsymbol{b}$
> 1. 无解$\iff R(\boldsymbol{A})<R(\overline{\boldsymbol{A}})$，$\overline{\boldsymbol{A}}=(\boldsymbol{A}\mid\boldsymbol{b})$为增广矩阵；
> 2. 有唯一解$\iff R(\boldsymbol{A})=R(\overline{\boldsymbol{A}})=n$；
> 3. 有无穷多解$\iff R(\boldsymbol{A})=R(\overline{\boldsymbol{A}})<n$。

### 3.4.2 齐次线性方程组
> **定理**：$n$元齐次线性方程组$\boldsymbol{A}_{m\times n}\boldsymbol{x}=\boldsymbol{0}$必有零解；
> 1. 仅有零解$\iff R(\boldsymbol{A})=n$；
> 2. 有非零解$\iff R(\boldsymbol{A})<n$。

- 推论：$n$阶方阵$\boldsymbol{A}$构成的$\boldsymbol{A}\boldsymbol{x}=\boldsymbol{0}$有非零解$\iff|\boldsymbol{A}|=0$。

# 第四章 向量组的线性相关性
## 4.1 向量组及其线性组合
### 4.1.1 n维向量
> **定义**：$n$个有序数$a_1,a_2,\dots,a_n$构成的数组$\boldsymbol{\alpha}=\begin{pmatrix}a_1\\a_2\\\vdots\\a_n\end{pmatrix}$称为$n$维列向量，$\boldsymbol{\alpha}^\mathrm{T}=(a_1,a_2,\dots,a_n)$为$n$维行向量，$a_i$为向量分量。

- 向量运算规则：
  - 加法：$\boldsymbol{\alpha}+\boldsymbol{\beta}=(a_1+b_1,a_2+b_2,\dots,a_n+b_n)^\mathrm{T}$；
  - 数乘：$k\boldsymbol{\alpha}=(ka_1,ka_2,\dots,ka_n)^\mathrm{T},k\in\mathbb{R}$。

> **定义**：同维数有限个向量构成向量组；矩阵$\boldsymbol{A}_{m\times n}$的各列构成列向量组，各行构成行向量组。

### 4.1.2 线性组合与线性表示
> **定义**：设向量组$A:\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\dots,\boldsymbol{\alpha}_m$，对任意实数$k_1,k_2,\dots,k_m$，称
$$\boldsymbol{b}=k_1\boldsymbol{\alpha}_1+k_2\boldsymbol{\alpha}_2+\dots+k_m\boldsymbol{\alpha}_m$$
为向量$\boldsymbol{b}$由向量组$A$线性表示；$\boldsymbol{b}$能被线性表示等价于方程组$\boldsymbol{A}\boldsymbol{x}=\boldsymbol{b}$有解。

> **定理**：向量$\boldsymbol{b}$可由$\boldsymbol{\alpha}_1,\dots,\boldsymbol{\alpha}_m$线性表示$\iff R(\boldsymbol{A})=R(\boldsymbol{A},\boldsymbol{b})$，$\boldsymbol{A}=(\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\dots,\boldsymbol{\alpha}_m)$。

> **定义**：向量组$B$中每个向量均可由向量组$A$线性表示，称$B$可由$A$线性表示；若两向量组可互相线性表示，则称两向量组等价。

> **定理**：向量组$B$可由$A$线性表示$\iff R(\boldsymbol{A})=R(\boldsymbol{A},\boldsymbol{B})$；若$B$可由$A$表示，则$R(B)\le R(A)$；等价向量组秩相等。

## 4.2 向量组的线性相关性
### 4.2.1 线性相关定义
> **定义**：向量组$\boldsymbol{\alpha}_1,\boldsymbol{\alpha}_2,\dots,\boldsymbol{\alpha}_m$，若存在不全为零的数$k_1,\dots,k_m$使
$$k_1\boldsymbol{\alpha}_1+k_2\boldsymbol{\alpha}_2+\dots+k_m\boldsymbol{\alpha}_m=\boldsymbol{0}$$
称向量组**线性相关**；仅$k_1=\dots=k_m=0$时上式成立，则称**线性无关**。

> **定理**：$m$个$n$维列向量构成矩阵$\boldsymbol{A}=(\boldsymbol{\alpha}_1,\dots,\boldsymbol{\alpha}_m)$，
> 向量组线性相关$\iff R(\boldsymbol{A})<m$；线性无关$\iff R(\boldsymbol{A})=m$。

- 推论：
  - $m>n$时，$m$个$n$维向量必线性相关；
  - $n$个$n$维向量线性相关$\iff|\boldsymbol{A}|=0$，无关$\iff|\boldsymbol{A}|\neq0$。

### 4.2.2 相关无关基础性质
- 部分相关则整体相关，整体无关则部分无关；
- 原向量组无关，每个向量添加分量得到的延伸向量组仍无关；原向量组相关，去掉分量的缩短组仍相关；
- $\boldsymbol{\alpha}_1\dots\boldsymbol{\alpha}_m$无关，添向量$\boldsymbol{\beta}$后相关$\iff\boldsymbol{\beta}$可由$\boldsymbol{\alpha}_1\dots\boldsymbol{\alpha}_m$唯一线性表示。

## 4.3 向量组的秩
> **定义**：向量组$A$的一个部分组$A_0:\boldsymbol{\alpha}_{i_1},\dots,\boldsymbol{\alpha}_{i_r}$满足：①$A_0$线性无关；②$A$中任意向量均可由$A_0$线性表示，则$A_0$为$A$的**最大线性无关向量组（极大无关组）**，极大无关组所含向量个数$r$称作向量组的秩$R_A$。

- 基本结论：
  - 矩阵的秩等于其列向量组的秩，也等于行向量组的秩；
  - 向量组任意两个极大无关组等价，所含向量数目相等；
  - 向量组$B$可由$A$线性表示$\Rightarrow R_B\le R_A$。

## 4.4 线性方程组解的结构
### 4.4.1 齐次线性方程组$\boldsymbol{A}\boldsymbol{x}=\boldsymbol{0}$
> **定义**：齐次方程组全体解向量构成解空间$S$，$\dim S=n-R(\boldsymbol{A})$，$n$为未知数个数。

> **定义**：解空间$S$的极大无关组称为方程组的**基础解系**，基础解系所含向量个数$t=n-R(\boldsymbol{A})$。

- 性质：
  - 若$\boldsymbol{\xi}_1,\boldsymbol{\xi}_2$是解，则$\boldsymbol{\xi}_1+\boldsymbol{\xi}_2,k\boldsymbol{\xi}_1(k\in\mathbb{R})$仍是解；
  - 基础解系$\boldsymbol{\xi}_1,\dots,\boldsymbol{\xi}_t$，通解：$\boldsymbol{x}=k_1\boldsymbol{\xi}_1+k_2\boldsymbol{\xi}_2+\dots+k_t\boldsymbol{\xi}_t,\ k_i\in\mathbb{R}$。

### 4.4.2 非齐次线性方程组$\boldsymbol{A}\boldsymbol{x}=\boldsymbol{b}$
> **定理**：设$\boldsymbol{\eta}^*$是非齐次方程组一个特解，$\boldsymbol{\xi}_1\dots\boldsymbol{\xi}_t$是对应齐次$\boldsymbol{A}\boldsymbol{x}=\boldsymbol{0}$的基础解系，则非齐次通解
$$\boldsymbol{x}=\boldsymbol{\eta}^*+k_1\boldsymbol{\xi}_1+\dots+k_t\boldsymbol{\xi}_t$$

- 解的性质：
  - $\boldsymbol{\eta}_1,\boldsymbol{\eta}_2$为$\boldsymbol{A}\boldsymbol{x}=\boldsymbol{b}$解，则$\boldsymbol{\eta}_1-\boldsymbol{\eta}_2$是$\boldsymbol{A}\boldsymbol{x}=\boldsymbol{0}$的解；
  - $\boldsymbol{\eta}^*$是$\boldsymbol{A}\boldsymbol{x}=\boldsymbol{b}$解，$\boldsymbol{\xi}$是$\boldsymbol{A}\boldsymbol{x}=\boldsymbol{0}$解，则$\boldsymbol{\eta}^*+\boldsymbol{\xi}$是$\boldsymbol{A}\boldsymbol{x}=\boldsymbol{b}$解。

## 4.5 向量空间
> **定义**：非空$n$维向量集合$V$，满足：$\forall\boldsymbol{\alpha},\boldsymbol{\beta}\in V,k\in\mathbb{R}$，有$\boldsymbol{\alpha}+\boldsymbol{\beta}\in V,k\boldsymbol{\alpha}\in V$，称$V$为向量空间。

> **定义**：$V$中极大无关组$\boldsymbol{\alpha}_1,\dots,\boldsymbol{\alpha}_r$称为$V$的一组**基**，基所含向量数$r$为空间维数$\dim V$；任意$\boldsymbol{\alpha}\in V$可唯一表示$\boldsymbol{\alpha}=x_1\boldsymbol{\alpha}_1+\dots+x_r\boldsymbol{\alpha}_r$，系数$(x_1,\dots,x_r)^\mathrm{T}$为$\boldsymbol{\alpha}$在该基下的坐标。

> **定义**：由基$\boldsymbol{\alpha}_1\dots\boldsymbol{\alpha}_r$到$\boldsymbol{\beta}_1\dots\boldsymbol{\beta}_r$满足$(\boldsymbol{\beta}_1,\dots,\boldsymbol{\beta}_r)=(\boldsymbol{\alpha}_1,\dots,\boldsymbol{\alpha}_r)\boldsymbol{P}$，可逆矩阵$\boldsymbol{P}$称作从旧基到新基的过渡矩阵。

# 第五章 相似矩阵及二次型
## 5.1 向量的内积、长度及正交性
### 5.1.1 内积与向量长度
> 设$n$维实向量$\boldsymbol x=\begin{pmatrix}x_1\\x_2\\\vdots\\x_n\end{pmatrix},\boldsymbol y=\begin{pmatrix}y_1\\y_2\\\vdots\\y_n\end{pmatrix}$，内积
$$[\boldsymbol x,\boldsymbol y]=x_1y_1+x_2y_2+\dots+x_ny_n=\boldsymbol x^\mathrm{T}\boldsymbol y$$
- $[\boldsymbol x,\boldsymbol y]=[\boldsymbol y,\boldsymbol x]$
- $[\lambda\boldsymbol x,\boldsymbol y]=\lambda[\boldsymbol x,\boldsymbol y]$
- $[\boldsymbol x+\boldsymbol y,\boldsymbol z]=[\boldsymbol x,\boldsymbol z]+[\boldsymbol y,\boldsymbol z]$
- $[\boldsymbol x,\boldsymbol x]\ge0$，$[\boldsymbol x,\boldsymbol x]=0\iff\boldsymbol x=\boldsymbol 0$

> 向量长度$\|\boldsymbol x\|=\sqrt{[\boldsymbol x,\boldsymbol x]}=\sqrt{x_1^2+x_2^2+\dots+x_n^2}$
- $\|\lambda\boldsymbol x\|=|\lambda|\|\boldsymbol x\|$
- 单位向量：$\|\boldsymbol x\|=1$；非零向量单位化：$\boldsymbol e=\dfrac{\boldsymbol x}{\|\boldsymbol x\|}$

> $[\boldsymbol x,\boldsymbol y]=0$称$\boldsymbol x$与$\boldsymbol y$正交；$\boldsymbol 0$与任意向量正交。
- 正交向量组内各向量两两正交，正交向量组线性无关。

### 5.1.2 施密特正交化
设$\boldsymbol a_1,\boldsymbol a_2,\dots,\boldsymbol a_r$线性无关，正交化：
$$
\begin{align*}
\boldsymbol b_1&=\boldsymbol a_1\\
\boldsymbol b_2&=\boldsymbol a_2-\dfrac{[\boldsymbol a_2,\boldsymbol b_1]}{[\boldsymbol b_1,\boldsymbol b_1]}\boldsymbol b_1\\
\boldsymbol b_3&=\boldsymbol a_3-\dfrac{[\boldsymbol a_3,\boldsymbol b_1]}{[\boldsymbol b_1,\boldsymbol b_1]}\boldsymbol b_1-\dfrac{[\boldsymbol a_3,\boldsymbol b_2]}{[\boldsymbol b_2,\boldsymbol b_2]}\boldsymbol b_2\\
&\vdots\\
\boldsymbol b_r&=\boldsymbol a_r-\sum_{k=1}^{r-1}\dfrac{[\boldsymbol a_r,\boldsymbol b_k]}{[\boldsymbol b_k,\boldsymbol b_k]}\boldsymbol b_k
\end{align*}
$$
再单位化$\boldsymbol e_i=\dfrac{\boldsymbol b_i}{\|\boldsymbol b_i\|}$。

### 5.1.3 正交矩阵
> $A$为$n$阶实方阵，$A^\mathrm{T}A=E$，称$A$为正交矩阵。
- $A^{-1}=A^\mathrm{T}$
- $|A|=\pm1$
- $A$的列（行）向量是两两正交的单位向量
> $P$正交矩阵，$\boldsymbol y=P\boldsymbol x$称为正交变换；正交变换保持向量内积与长度不变。

## 5.2 方阵的特征值与特征向量
### 5.2.1 定义
> $A$为$n$阶方阵，$\lambda$数、非零列向量$\boldsymbol x$满足$A\boldsymbol x=\lambda\boldsymbol x$，$\lambda$是$A$特征值，$\boldsymbol x$是对应$\lambda$的特征向量。
$$(A-\lambda E)\boldsymbol x=\boldsymbol 0$$
> $f(\lambda)=|A-\lambda E|$为$A$特征多项式，$|A-\lambda E|=0$为特征方程，根为特征值。

### 5.2.2 基本性质
- $\displaystyle\sum_{i=1}^n\lambda_i=\sum_{i=1}^n a_{ii}=\mathrm{tr}(A)$（迹）
- $\lambda_1\lambda_2\cdots\lambda_n=|A|$
- $A$可逆$\iff$全部特征值非零
- $\lambda$是$A$特征值，则$\lambda^k$是$A^k$特征值；$\varphi(\lambda)$是$\varphi(A)$特征值
- $A$与$A^\mathrm{T}$特征值相同
- 不同特征值对应的特征向量线性无关

## 5.3 相似矩阵
### 5.3.1 相似定义
> $A,B$为$n$阶方阵，存在可逆阵$P$使$P^{-1}AP=B$，称$B$相似于$A$。
- $A\sim B\implies|A|=|B|$，$A,B$特征多项式、特征值相同

> $A$可对角化$\iff$存在可逆$P$，$P^{-1}AP=\Lambda=\mathrm{diag}(\lambda_1,\lambda_2,\dots,\lambda_n)$
- $n$阶方阵$A$可对角化$\iff A$有$n$个线性无关特征向量
- $A$的$n$个特征值互不相同$\implies A$可对角化

## 5.4 实对称矩阵的对角化
- 实对称矩阵特征值全为实数
- 实对称矩阵不同特征值对应的特征向量相互正交
> $A$实对称，必存在正交矩阵$P$，$P^{-1}AP=P^\mathrm{T}AP=\Lambda$，$\Lambda$对角元为$A$特征值

## 5.5 二次型及其标准形
### 5.5.1 二次型定义
> $n$元二次齐次多项式
$$f=\sum_{i=1}^n\sum_{j=1}^n a_{ij}x_ix_j,\quad a_{ij}=a_{ji}$$
写成矩阵形式：
$$f=\boldsymbol x^\mathrm{T}A\boldsymbol x,\quad A=(a_{ij})_{n\times n},A^\mathrm{T}=A$$
$A$为二次型矩阵，$r(A)$为二次型秩。

> 可逆线性变换$\boldsymbol x=C\boldsymbol y$，$f=\boldsymbol y^\mathrm{T}(C^\mathrm{T}AC)\boldsymbol y$；$B=C^\mathrm{T}AC$称$A$合同。

> 仅含平方项$f=k_1y_1^2+k_2y_2^2+\dots+k_ny_n^2$为标准形。

### 5.5.2 正交变换化二次型
任实二次型$f=\boldsymbol x^\mathrm{T}A\boldsymbol x$，存在正交变换$\boldsymbol x=P\boldsymbol y$，
$$f=\lambda_1y_1^2+\lambda_2y_2^2+\dots+\lambda_ny_n^2$$
$\lambda_1,\dots,\lambda_n$是$A$全部特征值。

## 5.6 配方法化二次型
- 含平方项：选定平方项变量配方消交叉项
- 无平方项：作可逆变换构造平方项再配方

## 5.7 正定二次型
### 5.7.1 惯性定理
> 实二次型经可逆变换化成标准形，正、负平方项个数不变（正惯性指数$p$、负惯性指数$q$，$r=p+q$）；规范形$f=y_1^2+\dots+y_p^2-y_{p+1}^2-\dots-y_{p+q}^2$唯一。

### 5.7.2 正定定义与判定
> $\forall\boldsymbol x\neq\boldsymbol 0,\ f=\boldsymbol x^\mathrm{T}A\boldsymbol x>0$，称$f$正定，$A$正定矩阵。
- $f$正定$\iff$正惯性指数$p=n$
- $f$正定$\iff A$各阶顺序主子式全大于0（霍尔维茨定理）
- $f$负定$\iff$奇数阶顺序主子式$<0$，偶数阶$>0$

# 第六章 二次型
## 6.1 二次型及其标准形
### 6.1.1 二次型定义
> **定义**：含有$n$个变量$x_1,x_2,\dots,x_n$的二次齐次多项式
> $$
> f(x_1,x_2,\dots,x_n)=\sum_{i=1}^n\sum_{j=1}^n a_{ij}x_ix_j,\quad a_{ij}=a_{ji}
> $$
> 称为$n$元二次型。
> 矩阵形式：
> $$
> f=\boldsymbol x^T A\boldsymbol x,\quad A=(a_{ij})_{n\times n},A^T=A,\boldsymbol x=(x_1,x_2,\dots,x_n)^T
> $$
- **定义**：实对称矩阵$A$称作二次型$f$的矩阵，$f$称作对称矩阵$A$的二次型，矩阵$A$的秩称为**二次型的秩**。

### 6.1.2 合同变换
> **定义**：设$\boldsymbol x=C\boldsymbol y$，$C$为可逆方阵，称该变换为可逆线性变换；若$C$正交矩阵，称为正交变换。
> **定义**：对$n$阶方阵$A,B$，若存在可逆矩阵$C$满足$B=C^TAC$，称$A$与$B$**合同**。
- **性质**：合同矩阵秩相等。

### 6.1.3 二次型标准形
> **定义**：只含平方项的二次型$f=k_1y_1^2+k_2y_2^2+\dots+k_ny_n^2$称为二次型的**标准形**。
- **定理**：任意实二次型均可经过可逆线性变换化为标准形；任意实对称矩阵必合同于对角矩阵。

## 6.2 化二次型为标准形
### 6.2.1 正交变换法
- **定理**：任给实二次型$f=\boldsymbol x^T A\boldsymbol x$，总存在正交变换$\boldsymbol x=P\boldsymbol y$，使得
$$
f=\lambda_1y_1^2+\lambda_2y_2^2+\dots+\lambda_ny_n^2
$$
其中$\lambda_1,\lambda_2,\dots,\lambda_n$是$A$的全部特征值，$P$为正交矩阵。

### 6.2.2 配方法
- **结论**：任意实二次型均可通过配方法作可逆线性变换化为标准形。

## 6.3 正定二次型
### 6.3.1 惯性定理
> **惯性定理**：实二次型经任意可逆线性变换化为标准形，标准形中正平方项个数$p$、负平方项个数$q$唯一确定。
> - $p$：**正惯性指数**；$q$：**负惯性指数**；$r=p+q=\mathrm{r}(A)$
> **规范形定义**：形如$f=y_1^2+\dots+y_p^2-y_{p+1}^2-\dots-y_{p+q}^2$的二次型为二次型规范形。
- **推论**：两个实对称矩阵合同$\iff$秩相等且正惯性指数相等。

### 6.3.2 正定二次型
> **定义**：实二次型$f=\boldsymbol x^T A\boldsymbol x$，若$\forall \boldsymbol x\ne\boldsymbol 0$，恒有$f>0$，称$f$为**正定二次型**，$A$为**正定矩阵**；若恒有$f<0$，称负定二次型、负定矩阵。
- **判定定理**
  - $f$正定$\iff$正惯性指数$p=n$；
  - $f$正定$\iff A$的各阶顺序主子式全大于零（霍尔维茨定理）；
  - $f$正定$\iff A$全部特征值大于$0$；
  - $A$正定$\iff$存在可逆矩阵$C$，$A=C^TC$。
- **负定判定**：$A$负定$\iff$奇数阶顺序主子式$<0$，偶数阶顺序主子式$>0$。