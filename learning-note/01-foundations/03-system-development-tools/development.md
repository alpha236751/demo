# 一、vscode+python开发环境
## vscode扩展
- python扩展 4
- jupyter扩展 5
- markdown扩展 2

## 解释器(有conda不必要)
python解释器 清华镜像https://mirrors.tuna.tsinghua.edu.cn/python/

## conda环境配置
- miniforge镜像下载 https://mirrors.tuna.tsinghua.edu.cn/github-release/conda-forge/miniforge/
- 新建虚拟环境 `mamba create -n torch211-cu130 python=3.12`
- 检查环境列表 `mamba env list`
- 激活虚拟环境 `conda activate torch211-cu130`
- 关闭虚拟环境 `conda deactivate torch211-cu130`
- 删除虚拟环境 `mamba env remove -n torch211-cu130`
- 查看当前环境下安装的包(无依赖) `mamba env export --from-history`

## 三方包：
pytorch：深度学习框架
pandas：处理表格数据
matplotlib：数据可视化
numpy：科学计算
scikit-learn：机器学习工具包
openai：OPENAI API接口
ipykernel: jupyter内核
torchinfo: nn模型结构摘要信息

# 二、pytorch框架
PyTorch 是一个开源的深度学习框架，主要用于构建和训练神经网络。
pytorch分为CPU版本和GPU版本
https://pytorch.org/get-started/locally/
- 检查兼容cuda版本 cmd `nvidia-smi`
- 激活虚拟环境 `conda activate torch211-cu130`
- 安装pytorch
1. 官方推荐pip命令 
   安装torch torchvision 指定下载源地址
   `pip3 install torch torchvision --index-url https://download.pytorch.org/whl/cu132`
2. conda官方 指定版本 指定channel源
   `不确定下载方式 我卡在加载索引上了`
3. conda-forge社区 自动匹配CUDA版本 指定channel源
   `mamba install pytorch=2.11 -c conda-forge`

> pytorch在2.6.0版本后不再官方维护其conda版本，开始由conda官方和conda-forge社区维护更新，版本常落后于最新版
> torchaudio已停止更新其功能，所以不用安装，或选择更专业的包
> torchvision根据自己需要选择安装

**CUDA**
- CUDA（Compute Unified Device Architecture，统一计算设备架构）是 NVIDIA 推出的并行计算平台和编程模型。
- nvidia-smi显示的 CUDA 版本是显卡驱动支持的最高 CUDA 版本
- PyTorch 安装的pytorch-cuda包是 PyTorch 运行所需的最小 CUDA 运行时集合
- CUDA Toolkit是 NVIDIA 官方提供的完整 CUDA 开发工具包，主要用于开发 CUDA 程序，而不是运行已编译好的 CUDA 程序

# 三、Python 环境与包管理（pip/venv/conda/mamba）
## 1. 原生 Python：基础环境与包管理
Python 官方提供**纯原生**的环境隔离和包管理方案，无需安装第三方工具，开箱即用。

### 1.1 核心工具
- **pip**：Python 官方默认的**包管理工具**
  - 作用：安装、卸载、更新 Python 纯代码编写的第三方库（如 requests、beautifulsoup4）
  - 局限：对**跨语言编译库**（C/Fortran 底层）兼容性极差，无法自动处理系统级依赖
- **venv**：Python 3.3+ 内置的**虚拟环境隔离工具**
  - 作用：为不同项目创建独立的 Python 运行环境，避免项目间库版本冲突
  - 特点：轻量、纯 Python 实现，仅隔离环境，不自带包管理能力

### 1.2 原生方案的痛点
纯 Python 实现的代码在**数学运算、科学计算**场景下性能极差（循环、矩阵运算效率低），因此诞生了大量**C/Fortran 底层编写、Python 接口调用**的高性能库（如 NumPy、Pandas、SciPy）。
而原生 pip 无法妥善安装、管理这类跨语言编译库，会出现依赖缺失、安装失败、版本不兼容等问题，这是 conda 诞生的核心原因。

---

## 2. Conda：跨语言的环境+包管理工具
为解决原生 pip 无法管理**编译型跨语言库**的问题，Conda 应运而生。

### 2.1 Conda 核心定位
**既是包管理工具，也是环境管理工具**，全能型解决方案：
- 下载、安装、更新、卸载各类库（含 Python 库、C/Fortran 编译库、系统依赖）
- 创建、切换、删除独立运行环境（比 venv 更强大，支持跨 Python 版本）
- 为**Windows/macOS/Linux** 提供预编译好的对应版本库，无需本地编译，安装即运行

### 2.2 Conda 仓库与渠道（Channel）
Conda 从远程仓库下载库，核心渠道分为三类：
1. **defaults 渠道**：Anaconda 官方维护，由三个子渠道组成，**商业使用需付费**
2. **conda-forge 渠道**：开源社区志愿者维护，**免费开源**，库更新快、覆盖广
3. 第三方/个人渠道：用户自行上传的自定义库

---

## 3. Anaconda / Miniconda / Miniforge
三者都是**预装 Conda 的发行版**，区别在于预装内容和默认渠道。

### 3.1 Anaconda（完整版）
- 定位：**全量科学计算软件包集合**
- 包含内容：conda 工具 + 数百个常用科学计算库（NumPy/Pandas/Matplotlib 等）+ 图形界面
- 优点：开箱即用，无需额外安装基础库
- 缺点：体积大，占用磁盘空间多

### 3.2 Miniconda（精简版）
- 定位：**最小化 Conda 发行版**
- 包含内容：仅 Python 解释器 + conda 命令行工具
- 优点：体积小，按需安装所需库，灵活轻便
- 特点：**默认使用官方 defaults 渠道**（商业使用收费）

### 3.3 Miniforge（开源定制版）
- 定位：社区维护的「开源版 Miniconda」
- 包含内容：仅 Python + conda 工具
- 核心优势：**默认渠道直接设置为 conda-forge**，完全免费、开源、无商业限制
- 适用场景：推荐个人开发者、开源项目使用

---

## 4. Mamba：高性能 Conda 替代品
### 4.1 定位
**Conda 的加强优化版**，完全兼容 Conda 的命令和使用习惯
### 4.2 核心优化
- 用 C++ 重写核心逻辑，**解决 Conda 安装/更新依赖时速度慢、卡死问题**
- 并行下载依赖，解析环境速度大幅提升
- 完全兼容 conda 的环境、渠道、命令语法
### 4.3 使用方式
安装后直接用 `mamba` 替换 `conda` 命令即可（如 `mamba install numpy`）
