# Path 模块

### 1. 核心语法：创建路径与拼接（“/”运算符）
这是 `pathlib` 最标志性的语法糖。你不再需要写 `os.path.join(a, b)`。

```python
from pathlib import Path

# 1. 创建当前路径对象
p = Path()  # 当前目录 .
home = Path.home()  # 用户家目录 (C:\Users\你的名字 或 /home/xxx)
cwd = Path.cwd()    # 当前工作目录

# 2. 拼接路径 —— 直接用 / 符号！
project = Path("/home/user") / "projects" / "my_app"
# 在 Windows 上会自动转为反斜杠，在 Linux 上保持正斜杠，无需操心。

config_path = Path("docs") / "sub" / "config.ini"
print(config_path)  # 输出: docs/sub/config.ini (POSIX风格显示)
```

---

### 2. 解析路径属性（提取文件名、后缀、父目录）
替代了 `os.path.basename`、`os.path.splitext`、`os.path.dirname`。

```python
file = Path("/home/user/data/sample.csv")

print(file.name)        # sample.csv (完整文件名)
print(file.stem)        # sample (不带后缀的主文件名)
print(file.suffix)      # .csv (文件后缀，包含点)
print(file.suffixes)    # ['.csv'] (如果有多个后缀如 .tar.gz，会列出多个)
print(file.parent)      # /home/user/data (父目录)
print(file.parents[0])  # 同上，parents 可索引多级父目录，parents[1] 返回 /home/user
print(file.parents[1])  # /home/user
print(file.anchor)      # / (根目录锚点，Windows 下返回 '\')
print(file.parts) # ('\\', 'home', 'user', 'data', 'sample.csv')
```

---

### 3. 查询与判断（文件是否存在、类型）
替代 `os.path.exists`、`os.path.isfile`、`os.path.isdir`，返回布尔值，一目了然。

```python
p = Path("config.yaml")

print(p.exists())    # 是否存在
print(p.is_file())   # 是不是普通文件
print(p.is_dir())    # 是不是文件夹
print(p.is_symlink())# 是不是软链接
print(p.stat())      # 返回 os.stat_result 对象，包含大小、修改时间等
```

---

### 4. 目录遍历（衔接 `os.walk`）

- **`glob()` / `rglob()`**（模糊匹配，递归查找）：
```python
# 查找当前目录下所有 .txt 文件（不递归子文件夹）
for file in Path(".").glob("*.txt"):
    print(file)

# 查找项目下所有 .py 文件（递归所有子文件夹）
for py_file in Path("project").rglob("*.py"):
    print(py_file)  # 直接打印路径对象
```

- **`.iterdir()`**（完全对标 `os.walk`，但返回对象更直观）：
```python
for child in Path(".").iterdir():
    if child.suffix == ".md":
        print(child)  # 直接打印路径对象
```

---

### 5. 读写文件（最简洁的语法）
彻底告别 `open()` 的繁琐缩进（虽然依然可以用 `open()`），自带快捷方法：

```python
p = Path("notes.txt")

# 写入字符串（默认 utf-8）
p.write_text("Hello, World!", encoding="utf-8")

# 读取字符串
content = p.read_text(encoding="utf-8")

# 写入/读取二进制
p.write_bytes(b"Hello Bytes")
data = p.read_bytes()
```

---

### 6. 创建与删除目录/文件
替代 `os.mkdir`、`os.makedirs`、`os.remove`、`os.rmdir`：

```python
p = Path("new_folder/sub_folder")

# 创建目录（parents=True 相当于 os.makedirs，自动创建中间缺失的父目录）
p.mkdir(parents=True, exist_ok=True)  # exist_ok=True 表示如果已存在也不报错

file = Path("test.txt")
file.touch()          # 创建空文件，相当于 Linux touch

file.unlink()         # 删除文件
p.rmdir()             # 删除空目录（非空会报错）

# 若需删除非空目录，可用 shutil.rmtree，但 pathlib 提供了更安全的扩展（需第三方或自己递归）
```

---

### 7. 路径转换与解析（解决相对路径和绝对路径）
```python
p = Path("docs/readme.md")

print(p.absolute())   # 获取绝对路径（如 /home/user/docs/readme.md）
print(p.resolve())    # 解析软链接并返回绝对路径（比 absolute 更推荐）
print(p.relative_to("/home/user"))  # 返回相对路径: docs/readme.md
```

---

### 8. 与旧代码（os 模块）互操作
当你需要把 `Path` 传给只接受字符串的旧函数时，直接转成字符串即可：

```python
p = Path("/home/user/data/sample.csv")

# 转成字符串
str_path = str(p)  # '\\home\\user\\data\\sample.csv'

# 转成字节（用于底层系统调用）
bytes_path = bytes(p) # b'\\home\\user\\data\\sample.csv'
```

