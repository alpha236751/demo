# 一、 yaml
一种用于配置文件的标记语言
比XML简洁
json不能写注释，yaml可以

yaml语法：
- 大小写敏感
- `#` 注释
- 缩进表示层级
- 缩进只能使用空格
- 空格数不重要 只要相同层级对齐

## 1.1 表示纯量scalar
表示浮点数、整数、时间戳、字符串

```yaml
# 字符串（引号可省略，但含特殊字符时需要加）
name: Alice
greeting: "hello world"
multi_line: |
  这是多行字符串
  会保留换行符
folded: >
  这也会折叠成
  一行字符串

# 数字
integer: 42
float: 3.14
scientific: 6.02e23

# 布尔值
enabled: true
disabled: false
# 也支持: yes/no, on/off（不推荐，容易混淆）

# 空值
nothing: null
# 也支持: ~

# 日期时间（ISO-8601）
date: 2025-06-28
datetime: 2025-06-28T15:30:00+08:00
```

## 1.2 表示列表

```yaml
# 行内写法（流式）
fruits: [apple, banana, orange]

# 块式写法（更常用）
fruits:
  - apple
  - banana
  - orange

# 对象列表
users:
  - name: Alice
    age: 25
  - name: Bob
    age: 30
```



## 1.3 嵌套

```yaml
server:
  host: localhost
  port: 8080
  database:
    name: mydb
    user: admin
```

## 1.4 锚点与别名

```yaml
# & 定义锚点，* 引用别名
defaults: &defaults
  timeout: 30
  retries: 3

service_a:
  <<: *defaults        # << 表示 合并 default 的所有键
  name: service-a

service_b:
  <<: *defaults
  name: service-b
  timeout: 60          # 可覆盖
```

## 1.5 多文档（一个文件多个 YAML 文档）

```yaml
# --- 分隔多个文档
---
document: 1
---
document: 2
...
```

## 1.6 类型标签（强制指定类型）

```yaml
# 强制为字符串，避免自动类型转换
version: !!str 3.10
port: !!str 8080

# 其他标签: !!int, !!float, !!bool, !!null, !!timestamp
```

## 1.7 常见坑

| 坑 | 示例 | 说明 |
|---|---|---|
| **Tab 缩进** | 用 Tab 代替空格 | ❌ YAML 不允许 Tab，只允许空格 |
| **冒号后无空格** | `key:value` | ❌ 必须是 `key: value` |
| **Yes/No 变布尔** | `country: no` | ❌ `no` 会被解析为 `false`，应加引号 `"no"` |
| **数字变字符串** | `version: 3.10` | ❌ 可能被解析为浮点数 `3.1`，应加引号 `"3.10"` |
| **`*` 被当别名** | `path: *.txt` | ❌ 应加引号 `"*.txt"` |

## 1.8 与 JSON 对比

| | YAML | JSON |
|---|---|---|
| 可读性 | ✅ 高 | 😐 中 |
| 注释 | ✅ 支持 `#` | ❌ 不支持 |
| 锚点/引用 | ✅ 支持 | ❌ 不支持 |
| 多文档 | ✅ 支持 `---` | ❌ 不支持 |
| 解析速度 | 较慢 | 较快 |
| 适用场景 | 配置文件 | API 数据交换 |

# 二、 OmegaConf
一种用于配置文件的工具，用于解析和操作yaml配置文件。

## 2.1 基础使用

```python
from omegaconf import OmegaConf

# 1. 字典 -> OmegaConf 对象
# create() 将普通 dict 转换为 DictConfig，支持点号访问和字典式访问
cfg = OmegaConf.create({
    "model": {
        "name": "resnet",
        "num_classes": 10
    }
})

# 2. OmegaConf 对象 -> YAML 字符串
print(OmegaConf.to_yaml(cfg))
# model:
#   name: resnet
#   num_classes: 10

# 3. 点号访问（推荐）和字典式访问
print(cfg.model.name)          # resnet
print(cfg["model"]["name"])    # resnet

# 4. YAML 文件 -> OmegaConf 对象
conf = OmegaConf.load("config.yaml")
```

## 2.2 变量插值

```yaml
# config.yaml
server:
  host: localhost
  port: 8080
  url: http://${server.host}:${server.port}/api   # ${} 引用其他字段
```

```python
from omegaconf import OmegaConf

conf = OmegaConf.load("config.yaml")
print(conf.server.url)  # http://localhost:8080/api

OmegaConf.resolve(conf) # 解析 ${} 引用
print(OmegaConf.to_yaml(conf)) # 解析后的 YAML 字符串
```

## 2.3 合并配置

```python
from omegaconf import OmegaConf

base = OmegaConf.create({"db": {"host": "localhost", "port": 5432}})
override = OmegaConf.create({"db": {"port": 3306, "user": "admin"}})

# merge 用 override 覆盖 base 中的同名键，并添加新键
merged = OmegaConf.merge(base, override)
print(OmegaConf.to_yaml(merged))
# db:
#   host: localhost
#   port: 3306
#   user: admin
```

## 2.4 命令行参数

```python
from omegaconf import OmegaConf

# 从命令行参数创建配置对象
conf = OmegaConf.from_cli()
print(OmegaConf.to_yaml(conf))
```

```shell
python test1.py server.port=8080 log.level=INFO
# 输出:
# server:
#   port: '8080'
# log:
#   level: INFO
```

## 2.5 其他常用方法

| 方法 | 用途 |
|------|------|
| `OmegaConf.create(dict)` | 字典 → OmegaConf 对象 |
| `OmegaConf.load("a.yaml")` | YAML 文件 → OmegaConf 对象 |
| `OmegaConf.to_yaml(cfg)` | OmegaConf 对象 → YAML 字符串 |
| `OmegaConf.to_container(cfg)` | OmegaConf 对象 → 原生 Python 字典 |
| `OmegaConf.merge(c1, c2)` | 合并多个配置（后者覆盖前者） |
| `OmegaConf.save(cfg, "a.yaml")` | 保存到文件 |
| `OmegaConf.select(cfg, "a.b.c")` | 按路径访问嵌套值 |
| `OmegaConf.update(cfg, "a.b", value)` | 按路径更新值 |

# 三、 hydra
一种用于超参数配置管理的工具，底层基于 OmegaConf。

## 3.1 安装
```shell
pip install hydra-core
```

## 3.2 基础使用

```python
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))
    print(f"模型: {cfg.model.name}, 类别数: {cfg.model.num_classes}")

if __name__ == "__main__":
    my_app()
```

```yaml
# conf/config.yaml
model:
  name: "resnet"
  num_classes: 10
```

## 3.3 命令行覆盖

```shell
# 覆盖或添加配置中的值
python app.py model.name=vit +model.num_classes=100
```

## 3.4 多配置组合（Config Groups）

Hydra 通过「配置组」实现模块化配置，不同配置组存放在独立子目录中。

**目录结构：**
```
conf/
├── config.yaml          # 主配置，通过 defaults 声明组合哪些配置
├── db/                  # 配置组：数据库
│   ├── mysql.yaml
│   └── postgres.yaml
└── server/              # 配置组：服务器
    ├── local.yaml
    └── prod.yaml
```

**配置组内容：**
```yaml
# conf/db/mysql.yaml
db:
  driver: mysql
  host: localhost
  port: 3306
```

```yaml
# conf/db/postgres.yaml
db:
  driver: postgresql
  host: localhost
  port: 5432
```

```yaml
# conf/server/local.yaml
server:
  port: 8080
  debug: true
```

```yaml
# conf/server/prod.yaml
server:
  port: 80
  debug: false
```

**主配置（声明默认组合）：**
```yaml
# conf/config.yaml
defaults:
  - db: mysql          # 默认使用 mysql
  - server: local      # 默认使用 local
  - _self_             # 当前文件自身的配置

model:
  name: "resnet"
  num_classes: 10
```

```python
import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    print(OmegaConf.to_yaml(cfg))

if __name__ == "__main__":
    my_app()
```

**命令行切换：**
```shell
# 默认组合：mysql + local
python app.py

# 切换到 postgres + prod
python app.py db=postgres server=prod

# 也可以只覆盖部分
python app.py db=postgres
```

