# 一、 yaml
一种用于配置文件的标记语言

## 1.1 表示纯量
```yaml
boolean: true
float: 1.23
int: 123
str: "hello world"
date: 2023-01-04
datetime: 2023-01-04 12:34:00
```

## 1.2 表示列表
```yaml
list: [1, 2, 3, 4, 5]
list2: 
  - 6
  - 7
  - 8
  - 9
  - 10
```

## 1.3 表示字典
```yaml
dict: 
  key: value
  key2: value2
```

## 1.4 嵌套
```yaml
nested: 
  key: value
  key2: value2
```

# 二、 OmegaConf
一种用于配置文件的工具，用于解析和操作yaml配置文件。

## 2.1 基础使用
```python
from omegaconf import OmegaConf

toy_dict = {
    "model": {
        "name": "resnet",
        "num_classes": 10
    }
}
"""
将字典转换为 OmegaConf 配置对象（DictConfig 类型）。转换后的对象：
支持点号访问（例如 cfg.model.name）和字典式访问（cfg['model']['name']）。
支持变量插值、合并、类型检查等高级功能。
会保留原始数据结构，但提供了更丰富的操作接口。
"""
cfg = OmegaConf.create(toy_dict)
"""
将配置对象 cfg 序列化为 YAML 格式的字符串
"""
print(OmegaConf.to_yaml(cfg))
print(cfg.model.name) # 访问

# yaml -> OmegaConf
conf = OmegaConf.load("aaa.yaml")
```

## 2.2 进阶使用
```python
from omegaconf import OmegaConf

# 从命令行参数创建配置对象
conf = OmegaConf.from_cli() 
print(OmegaConf.to_yaml(conf))
"""
server:
  port: 8080
log:
  level: INFO
"""
```
```shell
python test.py server.port=8080 log.level=INFO
```


# 二、 hydra
一种用于超参数配置管理的工具

## 2.1 安装
```shell
pip install hydra-core
```
## 2.2 配置
```yaml
config:
  model:
    name: "resnet"
    num_classes: 10
```
## 2.3 使用
```python
import hydra
```
