# 第一章 函数与极限
## 第一节 映射与函数
### 一、集合
- 集合由具有某种特定性质的事物构成，组成集合的对象称为元素。
- $a\in A$表示$a$属于集合$A$，$a\notin A$表示$a$不属于集合$A$。
- 空集$\varnothing$：不含任何元素的集合。
> 子集定义：若$\forall x\in A$，有$x\in B$，则$A\subset B$；$A=B\iff A\subset B且B\subset A$。
- 并集：$A\cup B=\{x\mid x\in A或x\in B\}$
- 交集：$A\cap B=\{x\mid x\in A且x\in B\}$
- 差集：$A-B=\{x\mid x\in A且x\notin B\}$
- 全集$U$下余集：$A^c=U-A$
- 区间：有限区间$(a,b),[a,b],[a,b),(a,b]$；无穷区间$[a,+\infty),(-\infty,b)$等。
- 邻域：$\mathring U(a,\delta)=\{x\mid 0<|x-a|<\delta\}$为$a$的去心$\delta$邻域，$U(a,\delta)=\{x\mid |x-a|<\delta\}$。

### 二、映射
> 映射定义：设$X,Y$非空集合，若法则$f$使$\forall x\in X$，有唯一$y\in Y$与之对应，则$f:X\to Y$为映射；$X$为定义域，$R_f=\{f(x)\mid x\in X\}$为值域。
- 满射：$R_f=Y$；单射：$x_1\neq x_2\implies f(x_1)\neq f(x_2)$；一一映射=单射+满射。
- 逆映射：$f$一一映射时，存在$f^{-1}:R_f\to X$满足$f^{-1}(y)=x\iff f(x)=y$。
- 复合映射：$g:X\to Y_1,f:Y_1\subset Y\to Z$，复合$f\circ g:X\to Z,(f\circ g)(x)=f[g(x)]$。

### 三、函数
> 函数定义：非空数集$D$，对应法则$f$，$\forall x\in D$，唯一实数$y$，记$y=f(x),x\in D$；$D$定义域，$R_f=\{f(x)\mid x\in D\}$值域。
- 四则运算：$f\pm g,fg,\dfrac{f}{g}(g(x)\neq0)$定义域为两函数定义域交集。
- 反函数：$y=f(x)$单调，则存在反函数$x=f^{-1}(y)$，$y=f^{-1}(x)$与原函数关于$y=x$对称。
- 复合函数：$y=f(u),u=\varphi(x)$，$y=f[\varphi(x)]$，$u$中间变量。
- 基本初等函数：幂函数$y=x^\mu$、指数$y=a^x(a>0,a\neq1)$、对数$y=\log_a x$、三角函数、反三角函数。
#### 函数基础性质
> 有界性：$\exists M>0,\forall x\in X,|f(x)|\le M$，称$f(x)$在$X$上有界。
> 单调性：$\forall x_1<x_2\in I$，$f(x_1)<f(x_2)$单调递增，$f(x_1)>f(x_2)$单调递减。
> 奇偶性：定义域$D$关于原点对称；$f(-x)=f(x)$偶函数；$f(-x)=-f(x)$奇函数。
> 周期性：$\exists l>0,f(x+l)=f(x),\forall x\in D$，$l$为周期。

## 第二节 数列的极限
### 一、数列极限定义
> $\lim\limits_{n\to\infty}x_n=A$：$\forall \varepsilon>0,\exists N\in\mathbb{N}^+$，当$n>N$时，$|x_n-A|<\varepsilon$。

### 二、收敛数列性质
- 唯一性：收敛数列极限唯一。
- 有界性：收敛数列必有界。
- 保号性：$\lim x_n=A>0$，$\exists N$，$n>N$时$x_n>0$；$A<0$同理。
- 子列收敛性：数列收敛于$A\iff$所有子列收敛于$A$。

## 第三节 函数的极限
### 一、自变量趋于有限值$x\to x_0$
> $\lim\limits_{x\to x_0}f(x)=A$：$\forall\varepsilon>0,\exists\delta>0$，$0<|x-x_0|<\delta$时，$|f(x)-A|<\varepsilon$。
- 左极限：$f(x_0^-)=\lim\limits_{x\to x_0^-}f(x)$；右极限：$f(x_0^+)=\lim\limits_{x\to x_0^+}f(x)$
- $\lim\limits_{x\to x_0}f(x)=A\iff f(x_0^+)=f(x_0^-)=A$

### 二、自变量趋于无穷$x\to\infty$
> $\lim\limits_{x\to\infty}f(x)=A$：$\forall\varepsilon>0,\exists X>0$，$|x|>X$时，$|f(x)-A|<\varepsilon$。
- $\lim\limits_{x\to+\infty}f(x),\lim\limits_{x\to-\infty}f(x)$，$\lim\limits_{x\to\infty}f(x)=A\iff$左右无穷极限均为$A$。

### 三、函数极限性质
- 唯一性：函数极限存在则唯一。
- 局部有界：$\lim\limits_{x\to x_0}f(x)=A$，$\exists\mathring U(x_0,\delta)$，$f(x)$在此邻域有界。
- 局部保号：$\lim f(x)=A>0$，去心邻域内$f(x)>0$；$A<0$同理。

## 第四节 无穷小与无穷大
### 一、无穷小
> $\lim f(x)=0$，称$f(x)$为该极限过程下无穷小。
- $\lim f(x)=A\iff f(x)=A+\alpha,\alpha$为同过程无穷小。
- 有限个无穷小的和、乘积仍为无穷小；有界量乘无穷小为无穷小。

### 二、无穷大
> $\forall M>0,\exists\delta>0$，$0<|x-x_0|<\delta$时$|f(x)|>M$，$\lim\limits_{x\to x_0}f(x)=\infty$。
- 无穷大与非零无穷小互为倒数。

## 第五节 极限运算法则
### 四则运算法则
设$\lim f(x)=A,\lim g(x)=B$
$$
\begin{align*}
\lim[f(x)\pm g(x)]&=A\pm B\\
\lim[f(x)\cdot g(x)]&=AB\\
\lim\frac{f(x)}{g(x)}&=\frac{A}{B}\quad(B\neq0)
\end{align*}
$$
- $\lim[cf(x)]=cA$，$\lim[f(x)]^n=A^n$。
### 复合函数极限
$\lim\limits_{x\to x_0}\varphi(x)=u_0$，$u\to u_0$时$\lim f(u)=A$，则$\lim\limits_{x\to x_0}f[\varphi(x)]=A$。

## 第六节 极限存在准则 两个重要极限
### 一、夹逼准则
- 数列：$y_n\le x_n\le z_n$，$\lim y_n=\lim z_n=A\implies\lim x_n=A$。
- 函数：$\mathring U$内$g(x)\le f(x)\le h(x)$，$\lim g=\lim h=A\implies\lim f=A$。
### 二、单调有界准则
单调有界数列必有极限。
### 三、两个重要极限
$$
\lim_{x\to0}\frac{\sin x}{x}=1,\quad \lim_{x\to\infty}\left(1+\frac1x\right)^x=e
$$

## 第七节 无穷小的比较
> $\lim\frac\alpha\beta=0$：$\alpha$是$\beta$高阶无穷小，$\alpha=o(\beta)$；
> $\lim\frac\alpha\beta=C\neq0$：同阶无穷小；$C=1$等价无穷小$\alpha\sim\beta$；
> $\lim\frac\alpha{\beta^k}=C\neq0$：$k$阶无穷小。
- 等价无穷小替换：$\alpha\sim\tilde\alpha,\beta\sim\tilde\beta,\lim\frac{\tilde\alpha}{\tilde\beta}$存在，则$\lim\frac\alpha\beta=\lim\frac{\tilde\alpha}{\tilde\beta}$。

## 第八节 函数的连续性与间断点
### 一、连续性
> $f(x)$在$x_0$连续：$\lim\limits_{x\to x_0}f(x)=f(x_0)$；等价$\lim\limits_{\Delta x\to0}\Delta y=0,\Delta y=f(x_0+\Delta x)-f(x_0)$。
- 左连续：$\lim\limits_{x\to x_0^-}f(x)=f(x_0)$；右连续：$\lim\limits_{x\to x_0^+}f(x)=f(x_0)$；在$x_0$连续$\iff$左右均连续。

### 二、间断点分类
- 第一类间断：左右极限都存在；可去间断（左右极限相等）、跳跃间断（左右不等）。
- 第二类间断：左右极限至少一个不存在。

## 第九节 连续函数的运算与初等函数连续性
- 连续函数四则运算结果在定义域内连续。
- 单调连续函数的反函数单调连续。
- 复合函数：$u=\varphi(x)$在$x_0$连续，$y=f(u)$在$u_0=\varphi(x_0)$连续，则$y=f[\varphi(x)]$在$x_0$连续。
- 初等函数在其定义区间内处处连续。

## 第十节 闭区间上连续函数的性质
> 最值定理：$f(x)\in C[a,b]$，$\exists\xi_1,\xi_2\in[a,b]$，$f(\xi_1)=\max f(x),f(\xi_2)=\min f(x)$。
> 有界定理：闭区间连续函数在区间上有界。
> 零点定理：$f\in C[a,b],f(a)f(b)<0$，$\exists\xi\in(a,b),f(\xi)=0$。
> 介值定理：$f\in C[a,b],f(a)=A,f(b)=B$，$\forall C\in(A,B),\exists\xi\in(a,b),f(\xi)=C$。

# 第二章 导数与微分
## 第一节 导数概念
### 1. 导数的定义
> 设函数$y=f(x)$在点$x_0$的某邻域内有定义，自变量$x$在$x_0$处取得增量$\Delta x(\Delta x\neq0)$，相应函数增量$\Delta y=f(x_0+\Delta x)-f(x_0)$，若$\Delta y$与$\Delta x$之比当$\Delta x\to0$时极限存在，则称$y=f(x)$在$x_0$可导，该极限为函数在$x_0$处导数，记作$f'(x_0)$。
$$
f'(x_0)=\lim_{\Delta x\to0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}
$$
- 导数等价定义形式：$f'(x_0)=\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}$
- 导函数：区间内任意$x$可导，$f'(x)=\lim_{\Delta x\to0}\frac{f(x+\Delta x)-f(x)}{\Delta x}$

### 2. 左右导数
> 左导数：$\Delta x\to0^-$时极限为左导数$f'_-(x_0)$；右导数：$\Delta x\to0^+$时极限为右导数$f'_+(x_0)$。
$$
\begin{align*}
f'_-(x_0)&=\lim_{\Delta x\to0^-}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}\\
f'_+(x_0)&=\lim_{\Delta x\to0^+}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}
\end{align*}
$$
- 函数在$x_0$可导$\iff f'_+(x_0)=f'_-(x_0)$

### 3. 导数几何意义
- $f'(x_0)$为曲线$y=f(x)$在$(x_0,f(x_0))$处切线斜率
- 切线方程：$y-f(x_0)=f'(x_0)(x-x_0)$
- 法线方程：$y-f(x_0)=-\frac1{f'(x_0)}(x-x_0)(f'(x_0)\neq0)$

### 4. 可导与连续关系
- 函数在$x_0$可导$\implies$函数在$x_0$连续；反之不成立

## 第二节 函数的求导法则
### 1. 四则运算求导法则
设$u=u(x),v=v(x)$均可导
- $(u\pm v)'=u'\pm v'$
- $(uv)'=u'v+uv'$
- $\left(\frac{u}{v}\right)'=\frac{u'v-uv'}{v^2}(v\neq0)$

### 2. 反函数求导法则
> 若$x=\varphi(y)$在区间$I_y$单调可导且$\varphi'(y)\neq0$，其反函数$y=f(x)$在对应区间$I_x$可导
$$
f'(x)=\frac1{\varphi'(y)}
$$

### 3. 复合函数链式求导法则
> $y=f(u),u=\varphi(x)$均可导，则$y=f[\varphi(x)]$可导
$$
\frac{\mathrm dy}{\mathrm dx}=\frac{\mathrm dy}{\mathrm du}\cdot\frac{\mathrm du}{\mathrm dx}
$$

### 4. 基本初等函数求导公式
- $(C)'=0$
- $(x^\mu)'=\mu x^{\mu-1}$
- $(\sin x)'=\cos x,\ (\cos x)'=-\sin x$
- $(\tan x)'=\sec^2x,\ (\cot x)'=-\csc^2x$
- $(\sec x)'=\sec x\tan x,\ (\csc x)'=-\csc x\cot x$
- $(a^x)'=a^x\ln a,\ (\mathrm e^x)'=\mathrm e^x$
- $(\log_a x)'=\frac1{x\ln a},\ (\ln x)'=\frac1x$
- $(\arcsin x)'=\frac1{\sqrt{1-x^2}},\ (\arccos x)'=-\frac1{\sqrt{1-x^2}}$
- $(\arctan x)'=\frac1{1+x^2},\ (\mathrm{arccot}x)'=-\frac1{1+x^2}$

## 第三节 高阶导数
### 1. 高阶导数定义
> $f'(x)$导数为二阶导数$f''(x)$，$n-1$阶导数的导数为$n$阶导数$f^{(n)}(x)$
$$
f^{(n)}(x)=\big[f^{(n-1)}(x)\big]'
$$

### 2. 常用高阶导数公式
- $(\mathrm e^x)^{(n)}=\mathrm e^x$
- $(\sin x)^{(n)}=\sin\left(x+\frac{n\pi}2\right)$
- $(\cos x)^{(n)}=\cos\left(x+\frac{n\pi}2\right)$
- $[\ln(1+x)]^{(n)}=(-1)^{n-1}\frac{(n-1)!}{(1+x)^n}$
- $(x^\mu)^{(n)}=\mu(\mu-1)\cdots(\mu-n+1)x^{\mu-n}$

### 3. 莱布尼茨公式
$$
(uv)^{(n)}=\sum_{k=0}^n \mathrm C_n^k u^{(k)}v^{(n-k)}
$$

## 第四节 隐函数及由参数方程所确定的函数的导数
### 1. 隐函数求导
- 方程$F(x,y)=0$两边对$x$求导，整理解出$y'$

### 2. 对数求导法
- 幂指函数$y=u(x)^{v(x)}$，两边取自然对数后求导

### 3. 参数方程求导
参数方程$\begin{cases}x=\varphi(t)\\y=\psi(t)\end{cases},\varphi'(t)\neq0$
$$
\frac{\mathrm dy}{\mathrm dx}=\frac{\psi'(t)}{\varphi'(t)}
$$
$$
\frac{\mathrm d^2y}{\mathrm dx^2}=\frac{\varphi'(t)\psi''(t)-\psi'(t)\varphi''(t)}{\varphi'^3(t)}
$$

## 第五节 函数的微分
### 1. 微分定义
> $y=f(x)$在$x_0$处增量$\Delta y=A\Delta x+o(\Delta x)$，$A$与$\Delta x$无关，则称$A\Delta x$为$f(x)$在$x_0$微分，记作$\mathrm dy$，$\mathrm dx=\Delta x$
$$
\mathrm dy=f'(x)\mathrm dx
$$
- 可微$\iff$可导

### 2. 微分四则运算法则
- $\mathrm d(u\pm v)=\mathrm du\pm\mathrm dv$
- $\mathrm d(uv)=v\mathrm du+u\mathrm dv$
- $\mathrm d\left(\frac uv\right)=\frac{v\mathrm du-u\mathrm dv}{v^2}(v\neq0)$

### 3. 一阶微分形式不变性
- $y=f(u)$，无论$u$是自变量还是中间变量，恒有$\mathrm dy=f'(u)\mathrm du$

# 第三章 微分中值定理与导数的应用
## 第一节 微分中值定理
### 一、罗尔定理
> 若函数$f(x)$满足：
> 1. 在闭区间$[a,b]$上连续；
> 2. 在开区间$(a,b)$内可导；
> 3. $f(a)=f(b)$，
> 则$\exists\xi\in(a,b)$，使得$f'(\xi)=0$。

### 二、拉格朗日中值定理
> 若函数$f(x)$满足：
> 1. 在闭区间$[a,b]$上连续；
> 2. 在开区间$(a,b)$内可导，
> 则$\exists\xi\in(a,b)$，满足
> $$f(b)-f(a)=f'(\xi)(b-a)$$
- 有限增量形式：$\Delta y=f'(x_0+\theta\Delta x)\Delta x,\ 0<\theta<1$

### 三、柯西中值定理
> 若$f(x),F(x)$满足：
> 1. 在$[a,b]$连续；
> 2. 在$(a,b)$可导；
> 3. $\forall x\in(a,b),F'(x)\neq0$，
> 则$\exists\xi\in(a,b)$，有
> $$\frac{f(b)-f(a)}{F(b)-F(a)}=\frac{f'(\xi)}{F'(\xi)}$$

## 第二节 洛必达法则
### 一、$\boldsymbol{\frac00}$型洛必达
> 设：
> 1. $x\to x_0$时$f(x)\to0,F(x)\to0$；
> 2. 在$\mathring U(x_0)$内$f,F$可导且$F'(x)\neq0$；
> 3. $\displaystyle\lim_{x\to x_0}\frac{f'(x)}{F'(x)}$存在或为$\infty$，
> $$\lim_{x\to x_0}\frac{f(x)}{F(x)}=\lim_{x\to x_0}\frac{f'(x)}{F'(x)}$$

### 二、$\boldsymbol{\frac\infty\infty}$型洛必达
- 满足对应趋近极限、去心邻域可导、导函数比值极限存在条件时，
$$\lim\frac{f(x)}{F(x)}=\lim\frac{f'(x)}{F'(x)}$$

### 三、其他未定式
- $0\cdot\infty、\infty-\infty、1^\infty、0^0、\infty^0$：恒等变形化为$\frac00$或$\frac\infty\infty$再使用洛必达。

## 第三节 泰勒公式
### 一、带佩亚诺余项泰勒公式
> $f(x)$在$x_0$处$n$阶可导，则
> $$f(x)=\sum_{k=0}^n\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k+o\left((x-x_0)^n\right)$$
- $x_0=0$为麦克劳林公式：
$$f(x)=\sum_{k=0}^n\frac{f^{(k)}(0)}{k!}x^k+o(x^n)$$

### 二、带拉格朗日余项泰勒公式
> $f(x)$在$[x_0,x]$内$n+1$阶可导，则
> $$f(x)=\sum_{k=0}^n\frac{f^{(k)}(x_0)}{k!}(x-x_0)^k+\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-x_0)^{n+1},\ \xi\text{介于}x_0,x\text{之间}$$

## 第四节 函数单调性与曲线凹凸性
### 一、单调性判定
> 设$f(x)$在$I$上可导：
> - $f'(x)\ge0,\forall x\in I\implies f(x)$在$I$单调不减；
> - $f'(x)>0,\forall x\in I\implies f(x)$在$I$严格单调递增；
> - $f'(x)\le0,\forall x\in I\implies f(x)$在$I$单调不增；
> - $f'(x)<0,\forall x\in I\implies f(x)$在$I$严格单调递减。

### 二、凹凸定义
- 凹：$\forall x_1,x_2\in I,\ f\left(\frac{x_1+x_2}{2}\right)<\frac{f(x_1)+f(x_2)}{2}$
- 凸：$\forall x_1,x_2\in I,\ f\left(\frac{x_1+x_2}{2}\right)>\frac{f(x_1)+f(x_2)}{2}$

### 三、凹凸判定定理
> $f(x)$二阶可导：
> - $f''(x)>0\implies$曲线在区间凹；
> - $f''(x)<0\implies$曲线在区间凸。

### 四、拐点
- 定义：连续曲线凹凸性改变的分界点$(x_0,f(x_0))$；
- 必要条件：拐点处若二阶可导则$f''(x_0)=0$。

## 第五节 函数极值与最值
### 一、极值定义
- $x_0$邻域内：$f(x)<f(x_0)\implies f(x_0)$极大值；$f(x)>f(x_0)\implies f(x_0)$极小值。

### 二、极值必要条件（费马引理推论）
> $f(x)$在$x_0$可导且取极值$\implies f'(x_0)=0$，$x_0$为驻点。

### 三、第一充分条件
> $f(x)$在$\mathring U(x_0)$可导，$x_0$连续：
> - $x<x_0,f'>0;\ x>x_0,f'<0\implies x_0$极大点；
> - $x<x_0,f'<0;\ x>x_0,f'>0\implies x_0$极小点；
> - $f'$不变号$\implies$非极值点。

### 四、第二充分条件
> $f'(x_0)=0,f''(x_0)\neq0$：
> - $f''(x_0)<0\implies$极大值；
> - $f''(x_0)>0\implies$极小值。

### 五、闭区间最值
- 最值取自：区间端点、区间内驻点、一阶不可导点的函数值。

## 第六节 函数图形描绘
### 一、渐近线
- 水平渐近：$\displaystyle\lim_{x\to\infty}f(x)=A\implies y=A$
- 铅直渐近：$\displaystyle\lim_{x\to x_0}f(x)=\infty\implies x=x_0$
- 斜渐近：$\displaystyle k=\lim_{x\to\infty}\frac{f(x)}{x},\ b=\lim_{x\to\infty}[f(x)-kx]\implies y=kx+b$

## 第七节 曲率
### 一、曲率公式
$$K=\frac{|y''|}{\big(1+y'^2\big)^{\frac32}}$$
### 二、曲率半径
$$\rho=\frac1K$$
### 三、曲率圆与曲率中心
- 曲率圆圆心：曲率中心，半径为曲率半径$\rho$。

# 第四章 不定积分
## 第一节 不定积分的概念与性质
### 一、原函数
> 若在区间$I$上$F'(x)=f(x)$，则$F(x)$为$f(x)$在$I$上的一个原函数。

### 二、不定积分定义
$$\int f(x)\mathrm{d}x=F(x)+C$$
$F(x)$是$f(x)$一个原函数，$C$为任意常数。

### 三、基本性质
- $\left[\int f(x)\mathrm{d}x\right]'=f(x),\quad \mathrm{d}\left[\int f(x)\mathrm{d}x\right]=f(x)\mathrm{d}x$
- $\int F'(x)\mathrm{d}x=F(x)+C,\quad \int \mathrm{d}F(x)=F(x)+C$
- $\displaystyle\int\left[f(x)\pm g(x)\right]\mathrm{d}x=\int f(x)\mathrm{d}x\pm\int g(x)\mathrm{d}x$
- $\displaystyle\int kf(x)\mathrm{d}x=k\int f(x)\mathrm{d}x\ (k\neq0)$

### 四、基本积分公式
$$
\begin{align*}
&\int k\mathrm{d}x=kx+C,\quad \int x^\mu\mathrm{d}x=\frac{x^{\mu+1}}{\mu+1}+C(\mu\neq-1)\\
&\int\frac1x\mathrm{d}x=\ln|x|+C,\quad \int e^x\mathrm{d}x=e^x+C\\
&\int a^x\mathrm{d}x=\frac{a^x}{\ln a}+C,\quad \int\sin x\mathrm{d}x=-\cos x+C\\
&\int\cos x\mathrm{d}x=\sin x+C,\quad \int\frac1{\cos^2x}\mathrm{d}x=\tan x+C\\
&\int\frac1{\sin^2x}\mathrm{d}x=-\cot x+C,\quad \int\frac1{1+x^2}\mathrm{d}x=\arctan x+C\\
&\int\frac1{\sqrt{1-x^2}}\mathrm{d}x=\arcsin x+C
\end{align*}
$$

## 第二节 换元积分法
### 一、第一类换元（凑微分）
$$\int f[\varphi(x)]\varphi'(x)\mathrm{d}x \xlongequal{u=\varphi(x)}\int f(u)\mathrm{d}u=F(u)+C=F[\varphi(x)]+C$$

### 二、第二类换元
$$\int f(x)\mathrm{d}x\xlongequal{x=\psi(t)}\int f[\psi(t)]\psi'(t)\mathrm{d}t=F(t)+C=F\left[\psi^{-1}(x)\right]+C$$
- 根式代换、三角代换：$\sqrt{a^2-x^2}$令$x=a\sin t$；$\sqrt{a^2+x^2}$令$x=a\tan t$；$\sqrt{x^2-a^2}$令$x=a\sec t$。

## 第三节 分部积分法
$$\int u\mathrm{d}v=uv-\int v\mathrm{d}u$$

## 第四节 有理函数的积分
### 一、有理分式拆分
- 假分式拆多项式+真分式；真分式分解为一次因式、二次质因式部分分式之和。
### 二、可化为有理积分的函数
- 三角有理式$R(\sin x,\cos x)$万能代换：$t=\tan\frac x2$
$$\sin x=\frac{2t}{1+t^2},\ \cos x=\frac{1-t^2}{1+t^2},\ \mathrm{d}x=\frac{2}{1+t^2}\mathrm{d}t$$
- 简单无理函数换元去根式。

## 第五节 积分表的使用
- 直接查表、变量变形后查表、分项后查表。

# 第五章 定积分
## 第一节 定积分的概念与性质
### 1. 定积分定义
> 设$f(x)$在$[a,b]$上有界，分割区间$a=x_0<x_1<\dots<x_n=b$，记$\Delta x_i=x_i-x_{i-1}$，$\lambda=\max\{\Delta x_i\}$，任取$\xi_i\in[x_{i-1},x_i]$，若$\lambda\to0$时$\sum_{i=1}^n f(\xi_i)\Delta x_i$极限存在，则极限为$f(x)$在$[a,b]$定积分。
$$
\int_a^b f(x)\mathrm dx=\lim_{\lambda\to0}\sum_{i=1}^n f(\xi_i)\Delta x_i
$$
- 补充约定：$\int_a^a f(x)\mathrm dx=0,\int_a^b f(x)\mathrm dx=-\int_b^a f(x)\mathrm dx$

### 2. 可积充分条件
- $f(x)$在$[a,b]$连续$\implies f(x)$在$[a,b]$可积
- $f(x)$在$[a,b]$有界且仅有有限个间断点$\implies f(x)$在$[a,b]$可积

### 3. 定积分基本性质
- $\int_a^b\left[k_1f(x)+k_2g(x)\right]\mathrm dx=k_1\int_a^b f(x)\mathrm dx+k_2\int_a^b g(x)\mathrm dx$
- $\int_a^b f(x)\mathrm dx=\int_a^c f(x)\mathrm dx+\int_c^b f(x)\mathrm dx$
- $f(x)\ge0,x\in[a,b]\implies\int_a^b f(x)\mathrm dx\ge0$
- $f(x)\le g(x),x\in[a,b]\implies\int_a^b f(x)\mathrm dx\le\int_a^b g(x)\mathrm dx$
- $\left|\int_a^b f(x)\mathrm dx\right|\le\int_a^b|f(x)|\mathrm dx$
- $m\le f(x)\le M,x\in[a,b]\implies m(b-a)\le\int_a^b f(x)\mathrm dx\le M(b-a)$

### 4. 积分中值定理
> $f(x)\in C[a,b]$，则$\exists\xi\in[a,b]$
$$
\int_a^b f(x)\mathrm dx=f(\xi)(b-a)
$$

## 第二节 微积分基本公式
### 1. 变上限积分函数
> $\Phi(x)=\int_a^x f(t)\mathrm dt,f\in C[a,b]$
$$
\Phi'(x)=f(x)
$$
- 推论：$\frac{\mathrm d}{\mathrm dx}\int_a^{\varphi(x)}f(t)\mathrm dt=f[\varphi(x)]\cdot\varphi'(x)$
- 推论：$\frac{\mathrm d}{\mathrm dx}\int_{\psi(x)}^{\varphi(x)}f(t)\mathrm dt=f[\varphi(x)]\varphi'(x)-f[\psi(x)]\psi'(x)$

### 2. 牛顿-莱布尼茨公式
> $F(x)$是$f(x)$在$[a,b]$的一个原函数
$$
\int_a^b f(x)\mathrm dx=F(b)-F(a)\xlongequal{\triangle}\left.F(x)\right|_a^b
$$

## 第三节 定积分的换元法和分部积分法
### 1. 定积分换元积分公式
> $x=\varphi(t)$在$[\alpha,\beta]$单调连续可导，$\varphi(\alpha)=a,\varphi(\beta)=b$，$f\in C[a,b]$
$$
\int_a^b f(x)\mathrm dx=\int_\alpha^\beta f[\varphi(t)]\varphi'(t)\mathrm dt
$$

### 2. 常用奇偶区间结论
- $f(x)$为奇函数，$\int_{-a}^a f(x)\mathrm dx=0$
- $f(x)$为偶函数，$\int_{-a}^a f(x)\mathrm dx=2\int_0^a f(x)\mathrm dx$

### 3. 定积分分部积分公式
$$
\int_a^b u\mathrm dv=\left.uv\right|_a^b-\int_a^b v\mathrm du
$$

## 第四节 反常积分
### 1. 无穷限反常积分
$$
\begin{align*}
\int_a^{+\infty}f(x)\mathrm dx&=\lim_{t\to+\infty}\int_a^t f(x)\mathrm dx\\
\int_{-\infty}^b f(x)\mathrm dx&=\lim_{t\to-\infty}\int_t^b f(x)\mathrm dx\\
\int_{-\infty}^{+\infty}f(x)\mathrm dx&=\int_{-\infty}^c f(x)\mathrm dx+\int_c^{+\infty}f(x)\mathrm dx
\end{align*}
$$
- $p$-积分：$\int_a^{+\infty}\frac1{x^p}\mathrm dx(a>0)$，$p>1$收敛，$p\le1$发散

### 2. 无界函数反常积分（瑕积分）
> $x=a$为瑕点，$\lim\limits_{x\to a^+}f(x)=\infty$
$$
\int_a^b f(x)\mathrm dx=\lim_{t\to a^+}\int_t^b f(x)\mathrm dx
$$
- $p$-瑕积分：$\int_0^a \frac1{x^p}\mathrm dx(a>0)$，$p<1$收敛，$p\ge1$发散

## 第五节 反常积分的审敛法
### 1. 无穷限反常积分比较审敛原理
- $0\le f(x)\le g(x),x\ge a$：$\int_a^{+\infty}g(x)\mathrm dx$收敛$\implies\int_a^{+\infty}f(x)\mathrm dx$收敛；$\int_a^{+\infty}f(x)\mathrm dx$发散$\implies\int_a^{+\infty}g(x)\mathrm dx$发散

### 2. 极限形式比较审敛法
$\lim\limits_{x\to+\infty}x^pf(x)=l$
- $0\le l<+\infty,p>1$，$\int_a^{+\infty}f(x)\mathrm dx$收敛
- $0<l\le+\infty,p\le1$，$\int_a^{+\infty}f(x)\mathrm dx$发散

### 3. 绝对收敛
- $\int_a^{+\infty}|f(x)|\mathrm dx$收敛$\implies\int_a^{+\infty}f(x)\mathrm dx$绝对收敛

### 4. 瑕积分比较审敛
$x=a$为瑕点，$\lim\limits_{x\to a^+}(x-a)^pf(x)=l$
- $0\le l<+\infty,p<1$，瑕积分收敛
- $0<l\le+\infty,p\ge1$，瑕积分发散

# 第六章 定积分的应用
## 第一节 定积分的元素法
### 一、元素法原理
- 所求量$U$满足三条件：$U$与变量$x\in[a,b]$相关；$U$对区间具有可加性；小区间$[x,x+\mathrm{d}x]$对应部分量$\Delta U\approx f(x)\mathrm{d}x$。
> 元素：$\mathrm{d}U=f(x)\mathrm{d}x$，$U=\displaystyle\int_{a}^{b}f(x)\mathrm{d}x$。

## 第二节 平面图形的面积
### 一、直角坐标情形
- 曲线$y=f(x),y=g(x)\ (f(x)\ge g(x))$与$x=a,x=b$围成面积：
$$A=\int_{a}^{b}\big[f(x)-g(x)\big]\mathrm{d}x$$
- 曲线$x=\varphi(y),x=\psi(y)\ (\varphi(y)\ge \psi(y))$与$y=c,y=d$围成面积：
$$A=\int_{c}^{d}\big[\varphi(y)-\psi(y)\big]\mathrm{d}y$$
### 二、极坐标情形
- 极曲线$r=r(\theta)$，$\alpha\le\theta\le\beta$围成曲边扇形面积：
$$A=\frac12\int_{\alpha}^{\beta}r^2(\theta)\mathrm{d}\theta$$

## 第三节 体积
### 一、旋转体体积
- $y=f(x)$，$x\in[a,b]$绕$x$轴旋转：
$$V_x=\pi\int_{a}^{b}f^2(x)\mathrm{d}x$$
- $x=\varphi(y)$，$y\in[c,d]$绕$y$轴旋转：
$$V_y=\pi\int_{c}^{d}\varphi^2(y)\mathrm{d}y$$
### 二、平行截面面积已知的立体
- 截面面积$A(x)$，$x\in[a,b]$：
$$V=\int_{a}^{b}A(x)\mathrm{d}x$$

## 第四节 平面曲线的弧长
### 一、直角坐标
$y=f(x),x\in[a,b]$：
$$s=\int_{a}^{b}\sqrt{1+y'^2}\mathrm{d}x$$
### 二、参数方程
$\begin{cases}x=x(t)\\y=y(t)\end{cases},\alpha\le t\le\beta$：
$$s=\int_{\alpha}^{\beta}\sqrt{x'^2(t)+y'^2(t)}\mathrm{d}t$$
### 三、极坐标
$r=r(\theta),\alpha\le\theta\le\beta$：
$$s=\int_{\alpha}^{\beta}\sqrt{r^2(\theta)+r'^2(\theta)}\mathrm{d}\theta$$

## 第五节 功、压力和引力
### 一、变力做功
变力$F(x)$沿$x$轴从$a$到$b$做功：
$$W=\int_{a}^{b}F(x)\mathrm{d}x$$
### 二、液体静压力
深度$h(x)$，液体密度$\rho$，$g$为重力加速度，窄条面积元素$\mathrm{d}S$：
$$\mathrm{d}P=\rho g h(x)\mathrm{d}S,\quad P=\int \rho g h(x)\mathrm{d}S$$
### 三、引力
按万有引力公式拆分水平、竖直引力分量，分别积分：
$$\mathrm{d}F=G\frac{m\mathrm{d}M}{r^2}$$

## 第六节 平均值
### 一、函数平均值
$f(x)$在$[a,b]$平均值$\bar{f}$：
$$\bar{f}=\frac1{b-a}\int_{a}^{b}f(x)\mathrm{d}x$$
### 二、均方根
$$\sqrt{\frac1{b-a}\int_{a}^{b}f^2(x)\mathrm{d}x}$$

# 第七章 微分方程
## 第一节 微分方程基本概念
### 一、相关定义
> 含有未知函数、未知函数导数与自变量的等式称为微分方程；出现的最高阶导数阶数为方程阶数。
- 解：代入方程使之恒成立的函数；含独立任意常数且常数个数等于阶数的解为通解。
- 初始条件：确定通解中任意常数的附加条件；确定常数后的解为特解。
- 初值问题：微分方程搭配初始条件构成定解问题。

## 第二节 可分离变量的微分方程
### 一、标准形式
$$\frac{\mathrm{d}y}{\mathrm{d}x}=f(x)g(y)$$
- 分离变量：$\displaystyle\frac{\mathrm{d}y}{g(y)}=f(x)\mathrm{d}x$，两边积分
$$\int\frac{\mathrm{d}y}{g(y)}=\int f(x)\mathrm{d}x$$

### 二、齐次方程
> $\displaystyle\frac{\mathrm{d}y}{\mathrm{d}x}=\varphi\left(\frac{y}{x}\right)$为齐次微分方程。
- 换元$u=\displaystyle\frac{y}{x}$，$y=ux$，$\displaystyle\frac{\mathrm{d}y}{\mathrm{d}x}=u+x\frac{\mathrm{d}u}{\mathrm{d}x}$，化为可分离变量型。

## 第三节 一阶线性微分方程
### 一、标准形式
$$\frac{\mathrm{d}y}{\mathrm{d}x}+P(x)y=Q(x)$$
- $Q(x)\equiv0$时为一阶齐次线性方程；$Q(x)\not\equiv0$为非齐次线性方程。
- 齐次通解：$$y=Ce^{-\int P(x)\mathrm{d}x}$$
- 非齐次通解（常数变易法）：
$$y=e^{-\int P(x)\mathrm{d}x}\left(\int Q(x)e^{\int P(x)\mathrm{d}x}\mathrm{d}x+C\right)$$

### 二、伯努利方程
$$\frac{\mathrm{d}y}{\mathrm{d}x}+P(x)y=Q(x)y^n\quad(n\neq0,1)$$
- 换元$z=y^{1-n}$，化为一阶线性微分方程。

## 第四节 可降阶的高阶微分方程
### 一、$y^{(n)}=f(x)$型
逐次积分：
$$y^{(n-1)}=\int f(x)\mathrm{d}x+C_1,\dots$$

### 二、$y''=f(x,y')$（缺$y$）
- 令$p=y'$，$y''=\displaystyle\frac{\mathrm{d}p}{\mathrm{d}x}$，降为一阶$\displaystyle\frac{\mathrm{d}p}{\mathrm{d}x}=f(x,p)$。

### 三、$y''=f(y,y')$（缺$x$）
- 令$p=y'$，$y''=\displaystyle p\frac{\mathrm{d}p}{\mathrm{d}y}$，降为$p\displaystyle\frac{\mathrm{d}p}{\mathrm{d}y}=f(y,p)$。

## 第五节 高阶线性微分方程
### 一、解的结构
> 齐次方程：$y''+P(x)y'+Q(x)y=0$；非齐次：$y''+P(x)y'+Q(x)y=f(x)$。
- 齐次叠加原理：$y_1,y_2$是齐次解，则$C_1y_1+C_2y_2$也是解。
- 线性无关：$\displaystyle\frac{y_1}{y_2}\not\equiv$常数；两个线性无关特解线性组合为二阶齐次通解。
- 非齐次通解 = 对应齐次通解 + 非齐次一个特解$y^*$。
- 叠加原理：$f=f_1+f_2$，$y_1^*,y_2^*$分别对应$f_1,f_2$特解，则$y_1^*+y_2^*$为原方程特解。

## 第六节 常系数齐次线性微分方程
### 一、二阶$y''+py'+qy=0$
- 特征方程：$r^2+pr+q=0$
1. 两相异实根$r_1\neq r_2$：$y=C_1e^{r_1 x}+C_2e^{r_2 x}$
2. 二重实根$r_1=r_2=r$：$y=(C_1+C_2 x)e^{rx}$
3. 共轭复根$r=\alpha\pm\beta i$：$y=e^{\alpha x}(C_1\cos\beta x+C_2\sin\beta x)$

### 二、$n$阶常系数齐次
- 依特征根实根、复根、重根规则逐项构造通解。

## 第七节 常系数非齐次线性微分方程
### 一、$f(x)=P_m(x)e^{\lambda x}$
$$y''+py'+qy=P_m(x)e^{\lambda x}$$
- 特解形式$y^*=x^k Q_m(x)e^{\lambda x}$，$k$为$\lambda$作为特征根重数，$Q_m$同次$m$次多项式。

### 二、$f(x)=e^{\alpha x}[P_l\cos\beta x+P_n\sin\beta x]$
- $\lambda=\alpha+\beta i$，$k$为$\lambda$特征根重数，
$$y^*=x^k e^{\alpha x}\big[R_m^{(1)}\cos\beta x+R_m^{(2)}\sin\beta x\big],m=\max\{l,n\}$$

## 第八节 欧拉方程
### 标准形式
$$x^n y^{(n)}+p_1 x^{n-1}y^{(n-1)}+\dots+p_n y=f(x)$$
- 换元$x=e^t$，$t=\ln x$，$x\frac{\mathrm{d}y}{\mathrm{d}x}=Dy,\ x^2y''=D(D-1)y$，化为常系数线性微分方程。

# 第八章 空间解析几何与向量代数
## 第一节 向量及其线性运算
### 1. 向量相关定义
> 既有大小又有方向的量称为向量，记$\vec{a},\overrightarrow{AB}$；向量的模记作$|\vec{a}|,|\overrightarrow{AB}|$。
- 模为$1$的向量为单位向量，模为$0$的向量为零向量$\vec 0$。
- 方向相同、模相等的向量互为相等向量。
- 方向相反、模相等的向量互为负向量。

### 2. 向量线性运算
- 加减法遵循平行四边形法则、三角形法则：$\vec a+\vec b,\vec a-\vec b=\vec a+(-\vec b)$
- 数乘：实数$\lambda$与$\vec a$数乘$\lambda\vec a$，$|\lambda\vec a|=|\lambda||\vec a|$；$\lambda>0$同向，$\lambda<0$反向，$\lambda=0$为零向量。
- 向量共线：$\vec a\neq\vec 0$，$\vec b\parallel\vec a\iff\exists\lambda,\vec b=\lambda\vec a$。

### 3. 空间直角坐标系与坐标表示
- 空间点$M$对应坐标$(x,y,z)$，$\overrightarrow{OM}=x\vec i+y\vec j+z\vec k$。
- $M_1(x_1,y_1,z_1),M_2(x_2,y_2,z_2)$：$\overrightarrow{M_1M_2}=(x_2-x_1,y_2-y_1,z_2-z_1)$
$$|\overrightarrow{M_1M_2}|=\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}$$
- 方向余弦：$\vec a=(a_x,a_y,a_z)$，$\cos\alpha=\frac{a_x}{|\vec a|},\cos\beta=\frac{a_y}{|\vec a|},\cos\gamma=\frac{a_z}{|\vec a|}$，$\cos^2\alpha+\cos^2\beta+\cos^2\gamma=1$。

## 第二节 数量积 向量积 混合积
### 1. 数量积（点积）
> $\vec a\cdot\vec b=|\vec a||\vec b|\cos\theta,\theta=\langle\vec a,\vec b\rangle$
- 坐标：$\vec a=(a_x,a_y,a_z),\vec b=(b_x,b_y,b_z)$
$$\vec a\cdot\vec b=a_xb_x+a_yb_y+a_zb_z$$
- $\vec a\perp\vec b\iff\vec a\cdot\vec b=0$

### 2. 向量积（叉积）
> $\vec c=\vec a\times\vec b$，$|\vec c|=|\vec a||\vec b|\sin\theta$，$\vec c\perp\vec a,\vec c\perp\vec b$，右手定则定方向
$$
\vec a\times\vec b=
\begin{vmatrix}
\vec i&\vec j&\vec k\\
a_x&a_y&a_z\\
b_x&b_y&b_z
\end{vmatrix}
$$
- $\vec a\parallel\vec b\iff\vec a\times\vec b=\vec 0$

### 3. 混合积
$$[\vec a\ \vec b\ \vec c]=(\vec a\times\vec b)\cdot\vec c=
\begin{vmatrix}
a_x&a_y&a_z\\
b_x&b_y&b_z\\
c_x&c_y&c_z
\end{vmatrix}$$
- 三向量共面$\iff[\vec a\ \vec b\ \vec c]=0$

## 第三节 平面及其方程
### 1. 点法式方程
> 法向量$\vec n=(A,B,C)$，过点$M_0(x_0,y_0,z_0)$
$$A(x-x_0)+B(y-y_0)+C(z-z_0)=0$$

### 2. 平面一般式
$$Ax+By+Cz+D=0$$
- $D=0$过原点；$A=0$平行$x$轴；$A=B=0$平行$xOy$面。

### 3. 截距式方程
$$\frac{x}{a}+\frac{y}{b}+\frac{z}{c}=1$$
$a,b,c$依次为$x,y,z$轴截距。

### 4. 两平面夹角
$\Pi_1:A_1x+B_1y+C_1z+D_1=0,\Pi_2:A_2x+B_2y+C_2z+D_2=0$
$$\cos\theta=\frac{|A_1A_2+B_1B_2+C_1C_2|}{\sqrt{A_1^2+B_1^2+C_1^2}\sqrt{A_2^2+B_2^2+C_2^2}}$$
- 垂直：$A_1A_2+B_1B_2+C_1C_2=0$；平行：$\frac{A_1}{A_2}=\frac{B_1}{B_2}=\frac{C_1}{C_2}$

## 第四节 空间直线及其方程
### 1. 对称式（点向式）
过$M_0(x_0,y_0,z_0)$，方向向量$\vec s=(m,n,p)$
$$\frac{x-x_0}{m}=\frac{y-y_0}{n}=\frac{z-z_0}{p}$$

### 2. 参数方程
$$
\begin{cases}
x=x_0+mt\\
y=y_0+nt\\
z=z_0+pt
\end{cases}\quad(t\in\mathbb R)
$$

### 3. 一般式（两平面交线）
$$
\begin{cases}
A_1x+B_1y+C_1z+D_1=0\\
A_2x+B_2y+C_2z+D_2=0
\end{cases}
$$

### 4. 直线夹角
$L_1:\vec s_1=(m_1,n_1,p_1),L_2:\vec s_2=(m_2,n_2,p_2)$
$$\cos\theta=\frac{|m_1m_2+n_1n_2+p_1p_2|}{\sqrt{m_1^2+n_1^2+p_1^2}\sqrt{m_2^2+n_2^2+p_2^2}}$$
- 垂直：$m_1m_2+n_1n_2+p_1p_2=0$；平行：$\frac{m_1}{m_2}=\frac{n_1}{n_2}=\frac{p_1}{p_2}$

## 第五节 曲面及其方程
### 1. 曲面一般方程
$$F(x,y,z)=0$$

### 2. 旋转曲面
$xOz$面$f(x,z)=0$绕$z$轴旋转：$f(\pm\sqrt{x^2+y^2},z)=0$

### 3. 柱面
缺变量方程：$F(x,y)=0$表示母线平行$z$轴的柱面。

### 4. 二次曲面
- 椭球面：$\frac{x^2}{a^2}+\frac{y^2}{b^2}+\frac{z^2}{c^2}=1$
- 单叶双曲面：$\frac{x^2}{a^2}+\frac{y^2}{b^2}-\frac{z^2}{c^2}=1$
- 双叶双曲面：$\frac{x^2}{a^2}-\frac{y^2}{b^2}-\frac{z^2}{c^2}=1$
- 椭圆抛物面：$z=\frac{x^2}{a^2}+\frac{y^2}{b^2}$
- 双曲抛物面：$z=\frac{x^2}{a^2}-\frac{y^2}{b^2}$

## 第六节 空间曲线及其方程
### 1. 曲线一般式
$$
\begin{cases}
F(x,y,z)=0\\
G(x,y,z)=0
\end{cases}
$$

### 2. 参数方程
$$
\begin{cases}
x=x(t)\\
y=y(t)\\
z=z(t)
\end{cases}
$$

### 3. 空间曲线在坐标面投影
消去$z$得$H(x,y)=0$，投影柱面；$xOy$面投影曲线：
$$
\begin{cases}
H(x,y)=0\\
z=0
\end{cases}
$$

# 第九章 多元函数微分法及其应用
## 第一节 多元函数的基本概念
### 一、平面点集相关概念
- 邻域：$U(P_0,\delta)=\{P\mid |PP_0|<\delta\}$，去心邻域$\mathring U(P_0,\delta)=\{P\mid 0<|PP_0|<\delta\}$
- 内点、外点、边界点、聚点、开集、闭集、连通集、区域、闭区域

### 二、二元函数定义
> 设$D\subset\mathbb R^2$，$\forall(x,y)\in D$，按对应法则$f$有唯一$z\in\mathbb R$与之对应，则$z=f(x,y)$，$D$为定义域。

### 三、二元函数极限
$$\lim_{(x,y)\to(x_0,y_0)}f(x,y)=A$$
> $(x,y)$以任意方式趋于$(x_0,y_0)$时，$f(x,y)$无限趋近常数$A$。

### 四、二元函数连续性
> $\lim\limits_{(x,y)\to(x_0,y_0)}f(x,y)=f(x_0,y_0)$，称$f(x,y)$在$(x_0,y_0)$连续。
- 多元初等函数在定义区域内处处连续。

## 第二节 偏导数
### 一、一阶偏导数定义
$$
\begin{align*}
\frac{\partial z}{\partial x}\bigg|_{(x_0,y_0)}&=\lim_{\Delta x\to0}\frac{f(x_0+\Delta x,y_0)-f(x_0,y_0)}{\Delta x}\\
\frac{\partial z}{\partial y}\bigg|_{(x_0,y_0)}&=\lim_{\Delta y\to0}\frac{f(x_0,y_0+\Delta y)-f(x_0,y_0)}{\Delta y}
\end{align*}
$$

### 二、高阶偏导数
- $\dfrac{\partial^2 z}{\partial x^2}=\dfrac{\partial}{\partial x}\left(\dfrac{\partial z}{\partial x}\right),\dfrac{\partial^2 z}{\partial x\partial y}=\dfrac{\partial}{\partial y}\left(\dfrac{\partial z}{\partial x}\right)$
> 二阶混合偏导在区域内连续，则$\dfrac{\partial^2 z}{\partial x\partial y}=\dfrac{\partial^2 z}{\partial y\partial x}$。

## 第三节 全微分
### 一、全微分定义
> $\Delta z=f(x+\Delta x,y+\Delta y)-f(x,y)=A\Delta x+B\Delta y+o(\rho),\rho=\sqrt{(\Delta x)^2+(\Delta y)^2}$，则$dz=A\mathrm dx+B\mathrm dy$。
- 可微必连续、可微则一阶偏导存在：$A=\dfrac{\partial z}{\partial x},B=\dfrac{\partial z}{\partial y}$
$$\mathrm dz=\frac{\partial z}{\partial x}\mathrm dx+\frac{\partial z}{\partial y}\mathrm dy$$
> 一阶偏导数在该点连续，则函数在该点可微。

## 第四节 多元复合函数求导法则
### 一、链式求导
$z=f(u,v),u=\varphi(x,y),v=\psi(x,y)$
$$
\frac{\partial z}{\partial x}=\frac{\partial z}{\partial u}\frac{\partial u}{\partial x}+\frac{\partial z}{\partial v}\frac{\partial v}{\partial x},\quad
\frac{\partial z}{\partial y}=\frac{\partial z}{\partial u}\frac{\partial u}{\partial y}+\frac{\partial z}{\partial v}\frac{\partial v}{\partial y}
$$
### 二、全微分形式不变性
$$\mathrm dz=\frac{\partial z}{\partial u}\mathrm du+\frac{\partial z}{\partial v}\mathrm dv$$

## 第五节 隐函数求导
### 一、一元隐函数$F(x,y)=0$
$$\frac{\mathrm dy}{\mathrm dx}=-\frac{F_x}{F_y}\quad(F_y\neq0)$$
### 二、二元隐函数$F(x,y,z)=0$
$$\frac{\partial z}{\partial x}=-\frac{F_x}{F_z},\quad \frac{\partial z}{\partial y}=-\frac{F_y}{F_z}\quad(F_z\neq0)$$

## 第六节 多元函数微分学的几何应用
### 一、空间曲线切线与法平面
参数式$x=x(t),y=y(t),z=z(t)$，$t=t_0$处切向量$\boldsymbol T=(x'(t_0),y'(t_0),z'(t_0))$
- 切线：$\dfrac{x-x_0}{x'(t_0)}=\dfrac{y-y_0}{y'(t_0)}=\dfrac{z-z_0}{z'(t_0)}$
- 法平面：$x'(t_0)(x-x_0)+y'(t_0)(y-y_0)+z'(t_0)(z-z_0)=0$

### 二、曲面切平面与法线
曲面$F(x,y,z)=0$，法向量$\boldsymbol n=(F_x,F_y,F_z)\big|_{(x_0,y_0,z_0)}$
- 切平面：$F_x(x_0,y_0,z_0)(x-x_0)+F_y(x_0,y_0,z_0)(y-y_0)+F_z(x_0,y_0,z_0)(z-z_0)=0$
- 法线：$\dfrac{x-x_0}{F_x}=\dfrac{y-y_0}{F_y}=\dfrac{z-z_0}{F_z}$

## 第七节 方向导数与梯度
### 一、方向导数
$$\frac{\partial f}{\partial l}=\frac{\partial f}{\partial x}\cos\alpha+\frac{\partial f}{\partial y}\cos\beta+\frac{\partial f}{\partial z}\cos\gamma$$
$(\cos\alpha,\cos\beta,\cos\gamma)$为方向$\boldsymbol l$单位方向余弦。

### 二、梯度
$$\mathrm{grad}f=\nabla f=\left(\frac{\partial f}{\partial x},\frac{\partial f}{\partial y},\frac{\partial f}{\partial z}\right)$$
- 方向导数：$\dfrac{\partial f}{\partial l}=\nabla f\cdot\boldsymbol e_l$。

## 第八节 多元函数极值及其求法
### 一、极值必要条件
> $z=f(x,y)$在$(x_0,y_0)$偏导存在且取极值，则$f_x(x_0,y_0)=0,f_y(x_0,y_0)=0$，$(x_0,y_0)$为驻点。

### 二、极值充分条件
设$A=f_{xx}(x_0,y_0),B=f_{xy}(x_0,y_0),C=f_{yy}(x_0,y_0)$，$\Delta=AC-B^2$
- $\Delta>0,A>0$：极小值；$\Delta>0,A<0$：极大值；
- $\Delta<0$：非极值；$\Delta=0$：判别失效。

### 三、条件极值（拉格朗日乘数法）
目标$f(x,y)$，约束$\varphi(x,y)=0$，构造$L(x,y,\lambda)=f(x,y)+\lambda\varphi(x,y)$
$$
\begin{cases}
L_x=f_x+\lambda\varphi_x=0\\
L_y=f_y+\lambda\varphi_y=0\\
L_\lambda=\varphi(x,y)=0
\end{cases}
$$

# 第十章 重积分
## 第一节 二重积分的概念与性质
### 一、二重积分定义
$$\iint_D f(x,y)\mathrm d\sigma=\lim_{\lambda\to0}\sum_{i=1}^n f(\xi_i,\eta_i)\Delta\sigma_i$$
$\lambda$为小区域直径最大值，$D$为积分区域。
> $\mathrm d\sigma=\mathrm dx\mathrm dy$为直角坐标系下面积元素。

### 二、二重积分性质
- $\displaystyle\iint_D\left[f(x,y)\pm g(x,y)\right]\mathrm d\sigma=\iint_D f\mathrm d\sigma\pm\iint_D g\mathrm d\sigma$
- $\displaystyle\iint_D kf(x,y)\mathrm d\sigma=k\iint_D f(x,y)\mathrm d\sigma$
- $D=D_1\cup D_2,D_1\cap D_2=\emptyset$：$\displaystyle\iint_D f\mathrm d\sigma=\iint_{D_1}f\mathrm d\sigma+\iint_{D_2}f\mathrm d\sigma$
- $f\equiv1$：$\displaystyle\iint_D \mathrm d\sigma=S_D$，$S_D$为$D$面积
- $f\le g\implies\displaystyle\iint_D f\mathrm d\sigma\le\iint_D g\mathrm d\sigma$
- 估值：$mS_D\le\iint_D f\mathrm d\sigma\le MS_D$，$m=\min f,M=\max f$
- 积分中值定理：$\exists(\xi,\eta)\in D,\iint_D f(x,y)\mathrm d\sigma=f(\xi,\eta)S_D$

## 第二节 二重积分的计算法
### 一、直角坐标
- $X$型：$D:a\le x\le b,\varphi_1(x)\le y\le\varphi_2(x)$
$$\iint_D f\mathrm dx\mathrm dy=\int_a^b\mathrm dx\int_{\varphi_1(x)}^{\varphi_2(x)}f(x,y)\mathrm dy$$
- $Y$型：$D:c\le y\le d,\psi_1(y)\le x\le\psi_2(y)$
$$\iint_D f\mathrm dx\mathrm dy=\int_c^d\mathrm dy\int_{\psi_1(y)}^{\psi_2(y)}f(x,y)\mathrm dx$$

### 二、极坐标变换
$x=\rho\cos\theta,y=\rho\sin\theta,\mathrm dx\mathrm dy=\rho\mathrm d\rho\mathrm d\theta$
$$\iint_D f(x,y)\mathrm dx\mathrm dy=\iint_{D'}f(\rho\cos\theta,\rho\sin\theta)\rho\mathrm d\rho\mathrm d\theta$$

## 第三节 三重积分
### 一、三重积分定义
$$\iiint_\Omega f(x,y,z)\mathrm dv=\lim_{\lambda\to0}\sum_{i=1}^n f(\xi_i,\eta_i,\zeta_i)\Delta v_i$$
直角坐标$\mathrm dv=\mathrm dx\mathrm dy\mathrm dz$。

### 二、直角坐标计算
- 投影法（先一后二）：$z_1(x,y)\le z\le z_2(x,y),(x,y)\in D_{xy}$
$$\iiint_\Omega f\mathrm dv=\iint_{D_{xy}}\mathrm dx\mathrm dy\int_{z_1}^{z_2}f\mathrm dz$$
- 截面法（先二后一）：$c_1\le z\le c_2,(x,y)\in D_z$
$$\iiint_\Omega f\mathrm dv=\int_{c_1}^{c_2}\mathrm dz\iint_{D_z}f\mathrm dx\mathrm dy$$

### 三、柱坐标变换
$x=\rho\cos\theta,y=\rho\sin\theta,z=z,\mathrm dv=\rho\mathrm d\rho\mathrm d\theta\mathrm dz$
$$\iiint_\Omega f\mathrm dv=\iiint_{\Omega'}f(\rho\cos\theta,\rho\sin\theta,z)\rho\mathrm d\rho\mathrm d\theta\mathrm dz$$

### 四、球坐标变换
$x=r\sin\varphi\cos\theta,y=r\sin\varphi\sin\theta,z=r\cos\varphi$
$\mathrm dv=r^2\sin\varphi\mathrm dr\mathrm d\varphi\mathrm d\theta$
$$\iiint_\Omega f\mathrm dv=\iiint_{\Omega'}f\cdot r^2\sin\varphi\mathrm dr\mathrm d\varphi\mathrm d\theta$$

## 第四节 重积分的应用
### 一、平面面积
$$S=\iint_D \mathrm dx\mathrm dy$$
### 二、空间立体体积
$$V=\iiint_\Omega \mathrm dv=\iint_D\left[z_2(x,y)-z_1(x,y)\right]\mathrm dx\mathrm dy$$
### 三、曲面面积
曲面$z=f(x,y),(x,y)\in D$
$$A=\iint_D\sqrt{1+\left(\frac{\partial z}{\partial x}\right)^2+\left(\frac{\partial z}{\partial y}\right)^2}\mathrm dx\mathrm dy$$
### 四、静矩与形心
平面薄片$D$面密度$\rho(x,y)$
$$M=\iint_D\rho\mathrm d\sigma,\quad \bar x=\frac1M\iint_D x\rho\mathrm d\sigma,\quad \bar y=\frac1M\iint_D y\rho\mathrm d\sigma$$
### 五、转动惯量
$$I_x=\iint_D y^2\rho\mathrm d\sigma,\quad I_y=\iint_D x^2\rho\mathrm d\sigma$$

# 第十一章 曲线积分与曲面积分
## 第一节 对弧长的曲线积分（第一类曲线积分）
### 1. 定义
> $L$为平面光滑曲线弧，$f(x,y)$在$L$上有界，分割$L$为$n$小段$\Delta s_i$，$\lambda=\max\{\Delta s_i\}$，任取$(\xi_i,\eta_i)\in\Delta s_i$
$$
\int_L f(x,y)\mathrm ds=\lim_{\lambda\to0}\sum_{i=1}^n f(\xi_i,\eta_i)\Delta s_i
$$
- 空间曲线$\Gamma$：$\int_\Gamma f(x,y,z)\mathrm ds=\lim\limits_{\lambda\to0}\sum f(\xi_i,\eta_i,\zeta_i)\Delta s_i$

### 2. 性质
- $\int_L(k_1f+k_2g)\mathrm ds=k_1\int_Lf\mathrm ds+k_2\int_Lg\mathrm ds$
- $L=L_1+L_2$：$\int_L f\mathrm ds=\int_{L_1}f\mathrm ds+\int_{L_2}f\mathrm ds$
- 与曲线方向无关

### 3. 计算公式
- $L:\begin{cases}x=x(t)\\y=y(t)\end{cases},\alpha\le t\le\beta$
$$
\int_L f(x,y)\mathrm ds=\int_\alpha^\beta f[x(t),y(t)]\sqrt{x'^2(t)+y'^2(t)}\mathrm dt\quad(\alpha<\beta)
$$
- $\Gamma:\begin{cases}x=x(t)\\y=y(t)\\z=z(t)\end{cases},\alpha\le t\le\beta$
$$
\int_\Gamma f\mathrm ds=\int_\alpha^\beta f[x(t),y(t),z(t)]\sqrt{x'^2+y'^2+z'^2}\mathrm dt
$$

## 第二节 对坐标的曲线积分（第二类曲线积分）
### 1. 定义
> $L$为有向光滑曲线，$\int_L P\mathrm dx=\lim\limits_{\lambda\to0}\sum P(\xi_i,\eta_i)\Delta x_i,\int_L Q\mathrm dy=\lim\limits_{\lambda\to0}\sum Q(\xi_i,\eta_i)\Delta y_i$
$$
\int_L P\mathrm dx+Q\mathrm dy=\int_L P\mathrm dx+\int_L Q\mathrm dy
$$
- 空间：$\int_\Gamma P\mathrm dx+Q\mathrm dy+R\mathrm dz$

### 2. 性质
- $L^-$为$L$反向弧：$\int_{L^-}P\mathrm dx+Q\mathrm dy=-\int_L P\mathrm dx+Q\mathrm dy$
- $L=L_1+L_2$：$\int_L=\int_{L_1}+\int_{L_2}$

### 3. 计算公式
$L:\begin{cases}x=x(t)\\y=y(t)\end{cases}$，起点$t=\alpha$，终点$t=\beta$
$$
\int_L P\mathrm dx+Q\mathrm dy=\int_\alpha^\beta\big\{P[x(t),y(t)]x'(t)+Q[x(t),y(t)]y'(t)\big\}\mathrm dt
$$

### 4. 两类曲线积分联系
$$
\int_L P\mathrm dx+Q\mathrm dy=\int_L(P\cos\alpha+Q\cos\beta)\mathrm ds
$$
$\cos\alpha,\cos\beta$为$L$切向量方向余弦。

## 第三节 格林公式及其应用
### 1. 格林公式
> $D$为分段光滑正向闭区域，$P,Q\in C^1(D)$
$$
\oint_L P\mathrm dx+Q\mathrm dy=\iint_D\left(\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)\mathrm dx\mathrm dy
$$

### 2. 平面曲线积分与路径无关条件
单连通域$D$内$\frac{\partial Q}{\partial x}=\frac{\partial P}{\partial y}\iff\int_L P\mathrm dx+Q\mathrm dy$与路径无关。

### 3. 全微分求原函数
$\frac{\partial Q}{\partial x}=\frac{\partial P}{\partial y}$时，$u(x,y)=\int_{x_0}^x P(x,y_0)\mathrm dx+\int_{y_0}^y Q(x,y)\mathrm dy$满足$\mathrm du=P\mathrm dx+Q\mathrm dy$

### 4. 闭曲线围成面积
$$
A=\frac12\oint_L x\mathrm dy-y\mathrm dx
$$

## 第四节 对面积的曲面积分（第一类曲面积分）
### 1. 定义
> $\Sigma$光滑曲面，$f(x,y,z)$在$\Sigma$有界
$$
\iint_\Sigma f(x,y,z)\mathrm dS=\lim_{\lambda\to0}\sum f(\xi_i,\eta_i,\zeta_i)\Delta S_i
$$

### 2. 计算公式
$\Sigma:z=z(x,y)$，$D_{xy}$为$\Sigma$在$xOy$投影域
$$
\iint_\Sigma f\mathrm dS=\iint_{D_{xy}}f[x,y,z(x,y)]\sqrt{1+z_x'^2+z_y'^2}\mathrm dx\mathrm dy
$$

## 第五节 对坐标的曲面积分（第二类曲面积分）
### 1. 定义
$$
\begin{align*}
\iint_\Sigma R\mathrm dx\mathrm dy&=\lim\sum R(\xi_i,\eta_i,\zeta_i)(\Delta S_i)_{xy}\\
\iint_\Sigma P\mathrm dy\mathrm dz&=\lim\sum P(\xi_i,\eta_i,\zeta_i)(\Delta S_i)_{yz}\\
\iint_\Sigma Q\mathrm dz\mathrm dx&=\lim\sum Q(\xi_i,\eta_i,\zeta_i)(\Delta S_i)_{zx}
\end{align*}
$$
$$
\iint_\Sigma P\mathrm dy\mathrm dz+Q\mathrm dz\mathrm dx+R\mathrm dx\mathrm dy=\iint_\Sigma P+\iint_\Sigma Q+\iint_\Sigma R
$$

### 2. 性质
$\Sigma^-$取反向侧：$\iint_{\Sigma^-}=-\iint_\Sigma$

### 3. 计算公式
$\Sigma:z=z(x,y)$取上侧
$$
\iint_\Sigma R\mathrm dx\mathrm dy=\iint_{D_{xy}}R[x,y,z(x,y)]\mathrm dx\mathrm dy
$$

### 4. 两类曲面积分关系
$$
\iint_\Sigma P\mathrm dy\mathrm dz+Q\mathrm dz\mathrm dx+R\mathrm dx\mathrm dy=\iint_\Sigma(P\cos\alpha+Q\cos\beta+R\cos\gamma)\mathrm dS
$$
$\cos\alpha,\cos\beta,\cos\gamma$为$\Sigma$法向量方向余弦。

## 第六节 高斯公式
### 1. 高斯公式
> $\Omega$由分片光滑闭曲面$\Sigma$外侧围成，$P,Q,R\in C^1(\Omega)$
$$
\oiint_\Sigma P\mathrm dy\mathrm dz+Q\mathrm dz\mathrm dx+R\mathrm dx\mathrm dy=\iiint_\Omega\left(\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z}\right)\mathrm dv
$$

### 2. 散度
$$
\mathrm{div}\vec A=\frac{\partial P}{\partial x}+\frac{\partial Q}{\partial y}+\frac{\partial R}{\partial z},\quad\vec A=(P,Q,R)
$$

## 第七节 斯托克斯公式
### 1. 斯托克斯公式
> $\Gamma$为$\Sigma$正向边界曲线
$$
\oint_\Gamma P\mathrm dx+Q\mathrm dy+R\mathrm dz=\iint_\Sigma
\begin{vmatrix}
\mathrm dy\mathrm dz&\mathrm dz\mathrm dx&\mathrm dx\mathrm dy\\
\frac{\partial}{\partial x}&\frac{\partial}{\partial y}&\frac{\partial}{\partial z}\\
P&Q&R
\end{vmatrix}
$$

### 2. 旋度
$$
\mathrm{rot}\vec A=\left(\frac{\partial R}{\partial y}-\frac{\partial Q}{\partial z},\frac{\partial P}{\partial z}-\frac{\partial R}{\partial x},\frac{\partial Q}{\partial x}-\frac{\partial P}{\partial y}\right)
$$

# 第十二章 无穷级数
## 第一节 常数项级数的概念和性质
### 一、级数定义
> 给定数列$\{u_n\}$，$u_1+u_2+\dots+u_n+\dots=\sum\limits_{n=1}^{\infty}u_n$称为常数项无穷级数；$s_n=\sum\limits_{k=1}^n u_k$为部分和。
- 收敛：$\lim\limits_{n\to\infty}s_n=s$，级数收敛于$s$；极限不存在则级数发散。
- 余项：$r_n=s-s_n=\sum\limits_{k=n+1}^{\infty}u_k$。

### 二、基本性质
- $\sum u_n$收敛于$s$，则$\sum ku_n$收敛于$ks$；$\sum u_n,\sum v_n$分别收敛于$s,\sigma$，$\sum(u_n\pm v_n)=s\pm\sigma$。
- 增减有限项不改变级数敛散性。
- 收敛级数任意加括号后仍收敛，且和不变。
> 必要条件：$\sum\limits_{n=1}^{\infty}u_n$收敛$\implies\lim\limits_{n\to\infty}u_n=0$。

## 第二节 正项级数审敛法
> $u_n\ge0$，$\sum u_n$为正项级数，$\{s_n\}$单调递增；收敛$\iff\{s_n\}$有上界。
### 一、比较审敛法
- $0\le u_n\le v_n$：$\sum v_n$收敛$\implies\sum u_n$收敛；$\sum u_n$发散$\implies\sum v_n$发散。
- 极限形式：$\lim\limits_{n\to\infty}\dfrac{u_n}{v_n}=l$，$0<l<+\infty$时两级数同敛散；$l=0$，$\sum v_n$收敛则$\sum u_n$收敛；$l=+\infty$，$\sum v_n$发散则$\sum u_n$发散。
- $p-$级数：$\sum\limits_{n=1}^{\infty}\dfrac1{n^p}$，$p>1$收敛，$p\le1$发散。

### 二、比值审敛法（达朗贝尔）
$$\lim_{n\to\infty}\frac{u_{n+1}}{u_n}=\rho$$
$\rho<1$收敛；$\rho>1$发散；$\rho=1$判别失效。

### 三、根值审敛法（柯西）
$$\lim_{n\to\infty}\sqrt[n]{u_n}=\rho$$
$\rho<1$收敛；$\rho>1$发散；$\rho=1$判别失效。

## 第三节 交错级数与任意项级数
### 一、莱布尼茨判别法
> 交错级数$\sum_{n=1}^{\infty}(-1)^{n-1}u_n,u_n>0$，满足$u_n\ge u_{n+1},\lim\limits_{n\to\infty}u_n=0$，级数收敛，余项$|r_n|\le u_{n+1}$。

### 二、绝对收敛与条件收敛
- $\sum|u_n|$收敛$\implies\sum u_n$绝对收敛；$\sum u_n$收敛、$\sum|u_n|$发散为条件收敛。
- 绝对收敛级数重排后仍收敛且和不变。

## 第四节 幂级数
### 一、幂级数标准形式
$$\sum_{n=0}^{\infty}a_n x^n,\quad \sum_{n=0}^{\infty}a_n(x-x_0)^n$$
> 阿贝尔定理：$x=x_0\neq0$收敛，则$|x|<|x_0|$处处绝对收敛；$x=x_1$发散，则$|x|>|x_1|$处处发散。
- 收敛半径$R$：$|x|<R$收敛，$|x|>R$发散；收敛区间$(-R,R)$。
$$R=\frac1\rho,\quad\rho=\lim_{n\to\infty}\left|\frac{a_{n+1}}{a_n}\right|$$

### 二、幂级数运算与分析性质
- 收敛半径小者为四则运算后级数收敛半径。
- 收敛区间内和函数$S(x)$连续；逐项求导、逐项积分收敛半径不变：
$$S'(x)=\sum_{n=1}^{\infty}n a_n x^{n-1},\quad \int_0^x S(t)\mathrm{d}t=\sum_{n=0}^{\infty}\frac{a_n}{n+1}x^{n+1}$$

## 第五节 函数展开成幂级数
### 一、泰勒级数
> $f(x)$在$x_0$邻域内任意阶可导，泰勒级数：
$$f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(x_0)}{n!}(x-x_0)^n$$
$x_0=0$为麦克劳林级数：
$$f(x)=\sum_{n=0}^{\infty}\frac{f^{(n)}(0)}{n!}x^n$$
- 充要条件：余项$\lim\limits_{n\to\infty}R_n(x)=0$。

### 二、常用麦克劳林展开式
$$
\begin{align*}
e^x&=\sum_{n=0}^{\infty}\frac{x^n}{n!},x\in\mathbb R\\
\sin x&=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n+1)!}x^{2n+1},x\in\mathbb R\\
\cos x&=\sum_{n=0}^{\infty}\frac{(-1)^n}{(2n)!}x^{2n},x\in\mathbb R\\
\frac1{1+x}&=\sum_{n=0}^{\infty}(-1)^n x^n,|x|<1\\
\ln(1+x)&=\sum_{n=1}^{\infty}\frac{(-1)^{n-1}}{n}x^n,x\in(-1,1]\\
(1+x)^\alpha&=1+\sum_{n=1}^{\infty}\frac{\alpha(\alpha-1)\cdots(\alpha-n+1)}{n!}x^n,|x|<1
\end{align*}
$$

## 第六节 函数项级数的一致收敛性
### 一、一致收敛定义
> $\forall\varepsilon>0,\exists N$，$n>N$时，$\forall x\in I,|S(x)-S_n(x)|<\varepsilon$，级数在区间$I$一致收敛。
### 二、魏尔斯特拉斯判别法
- 若$|u_n(x)|\le M_n$，$\sum M_n$收敛，则$\sum u_n(x)$在$I$一致收敛。
### 三、一致收敛级数性质
- 和函数连续；可逐项积分；逐项求导。

## 第七节 傅里叶级数
### 一、周期$2\pi$傅里叶展开
> $f(x)$周期$2\pi$，傅里叶系数：
$$
\begin{align*}
a_n&=\frac1\pi\int_{-\pi}^{\pi}f(x)\cos nx\mathrm{d}x,\ n=0,1,2\dots\\
b_n&=\frac1\pi\int_{-\pi}^{\pi}f(x)\sin nx\mathrm{d}x,\ n=1,2\dots
\end{align*}
$$
傅里叶级数：$\displaystyle\frac{a_0}{2}+\sum_{n=1}^{\infty}(a_n\cos nx+b_n\sin nx)$。
- 收敛定理：$f(x)$分段光滑，间断点处级数收敛于$\displaystyle\frac{f(x^+)+f(x^-)}{2}$。
- 奇函数：$a_n=0$，正弦级数；偶函数：$b_n=0$，余弦级数。

### 二、周期$2l$傅里叶级数
$$
\begin{align*}
a_n&=\frac1l\int_{-l}^{l}f(x)\cos\frac{n\pi x}{l}\mathrm{d}x\\
b_n&=\frac1l\int_{-l}^{l}f(x)\sin\frac{n\pi x}{l}\mathrm{d}x
\end{align*}
$$
$$f(x)\sim\frac{a_0}{2}+\sum_{n=1}^{\infty}\left(a_n\cos\frac{n\pi x}{l}+b_n\sin\frac{n\pi x}{l}\right)$$

### 三、奇偶延拓
- 奇延拓：展开为正弦级数；偶延拓：展开为余弦级数。