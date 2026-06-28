# 一、vscode+python开发环境
## vscode扩展
- chinese 中文汉化
- python扩展 4
- jupyter扩展 5
- markdown扩展 2
- trae 字节ai编程助手
- EvenBetterTOML toml语法高亮
- ruff 代码风格和语法检查

## 解释器(有环境管理软件就不必要了)
python解释器 清华镜像https://mirrors.tuna.tsinghua.edu.cn/python/

## 三方包：
pytorch：深度学习框架
pandas：处理表格数据
matplotlib：数据可视化
numpy：科学计算
scikit-learn：机器学习工具包
openai：OPENAI API接口
ipykernel: jupyter内核
torchinfo: nn模型结构摘要信息
jieba: 中文分词工具
gensim: 加载和训练词向量的工具
tqdm: 进度条工具
flask: python微服务框架
streamlit: web应用框架
requests: 发送HTTP请求
hydra-core：超参数配置管理
tensorboard：可视化训练过程



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
- miniforge镜像下载 https://mirrors.tuna.tsinghua.edu.cn/github-release/conda-forge/miniforge/
- 新建虚拟环境 `mamba create -n torch211-cu130 python=3.12`
- 检查环境列表 `mamba env list`
- 激活虚拟环境 `conda activate torch211-cu130`
- 关闭虚拟环境 `conda deactivate torch211-cu130`
- 删除虚拟环境 `mamba env remove -n torch211-cu130`
- 查看当前环境下安装的包(无依赖) `mamba env export --from-history`

# 四、uv和pixi
## 4.1 uv
用 Rust 编写的新一代高性能 Python 工具链，旨在替代 pip, venv, pyenv, poetry 等多个工具。核心特点：极速解析依赖、自动管理虚拟环境、内置锁文件机制。

### 4.1.1 安装
以管理员身份运行 PowerShell
```shell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 安装完成后，配置环境变量，重启 PowerShell 

# 配置好环境变量后，检查安装是否成功
uv --version
```

### 4.1.2 虚拟环境管理
uv 在项目中使用 `uv add` / `uv sync` 时会**自动创建 `.venv` 虚拟环境**，无需手动操作。以下为手动管理环境的命令，供特殊场景参考：
```shell
# 创建虚拟环境（指定 Python 版本）
uv venv -p 3.10

# 创建虚拟环境到指定目录
uv venv my_venv -p 3.12

# 激活环境 (Windows PowerShell)
.\my_venv\Scripts\activate
# 激活环境 (macOS / Linux)
source my_venv/bin/activate

# 退出环境
deactivate

# 删除虚拟环境（直接删除目录即可）
Remove-Item -Recurse -Force .venv
```

### 4.1.3 项目搭建
uv 提供两套工作流：**原生 uv 工作流（推荐）** 和 **pip 兼容模式**。

**原生 uv 工作流**
```shell
# 1. 初始化项目（自动生成 pyproject.toml 和 .venv）
uv init my_project -p 3.10
cd my_project

# 2. 添加依赖（自动创建/更新 .venv 和 uv.lock）
uv add requests
uv add pandas numpy

# 3. 添加开发依赖（仅开发时使用，不打包到发布版本）
uv add --dev pytest ruff

# 4. 在项目环境中运行脚本
uv run python main.py
uv run pytest

# 5. 移除依赖
uv remove requests

# 6. 查看依赖树
uv tree

# 7. 根据 uv.lock 同步环境（团队协作时，他人拉取项目后执行）
uv sync

# 8. 更新所有依赖到最新兼容版本
uv lock --upgrade
```

**pip 兼容模式**（适合已有 requirements.txt 的旧项目）
```shell
# 安装依赖
uv pip install requests

# 导出依赖列表
uv pip freeze > requirements.txt

# 从 requirements.txt 批量安装
uv pip install -r requirements.txt
```

**Python 版本管理**（替代 pyenv）
```shell
# 查看可安装的 Python 版本
uv python list

# 安装指定 Python 版本
uv python install 3.10
uv python install 3.12

# 查看已安装的 Python 版本
uv python list --only-installed
```

### 4.1.4 pyproject.toml 结构
```toml
[project]
name = "my_project"
version = "0.1.0"
description = "A small project to demonstrate uv usage"
readme = "README.md"
requires-python = ">=3.10"
dependencies = [
    "requests>=2.28",
    "pandas>=2.0",
]

# 可选依赖（按需安装的额外功能组）
[project.optional-dependencies]
gpu = [
    "torch>=2.0",
]
web = [
    "flask>=3.0",
]

# 命令行入口脚本（pip install 后可全局调用）
[project.scripts]
my-cli = "my_project.cli:main"

# 开发依赖组（uv add --dev 会写入此处）
[dependency-groups]
dev = [
    "pytest>=8.0",
    "ruff>=0.5",
]

# 第三方工具配置
[tool.uv]
# 指定 PyPI 镜像源（加速国内下载）
index-url = "https://pypi.tuna.tsinghua.edu.cn/simple"

[tool.ruff]
# 行宽（与 Black 兼容）
line-length = 88
# 目标 Python 版本
target-version = "py310"
# 启用的规则集
lint.select = ["E", "F", "I", "N", "W"]

[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"

# 打包上传 PyPI 配置
[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"
```




## 4.2 pixi
受 cargo 启发、兼容 conda 生态的高性能跨语言包管理器，可视为 conda 的现代化替代品

略


# 六、ruff

1. 快速修复
   在错误提示上点击
2. 全部修复
   打开命令面板，执行 `Ruff:Fix all auto-fixable problems`
3. 格式化文档
   format document shift + alt +f
4. 组织导入
   organize imports shift + alt + o