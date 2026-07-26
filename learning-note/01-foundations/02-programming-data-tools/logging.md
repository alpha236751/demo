# 1. python内置模块 logging
## 1.1 简单使用
默认logger名为root
默认日志级别为INFO 格式为levelname:name:message

```python
import logging
# root logger 配置
logging.basicConfig(level=logging.INFO)
# logging使用的是root logger
logging.debug("调试信息")
logging.info("程序启动")
logging.warning("警告")
logging.error("发生错误")
logging.critical("严重错误")
```

输出：

INFO:root:程序启动
WARNING:root:警告
ERROR:root:发生错误
CRITICAL:root:严重错误


## 1.2 自定义logger
大型项目不要直接用 logging.info()，而是创建 logger。

```python
import logging
# 配置root logger
logging.basicConfig(
    level=logging.INFO
)
# 其他logger都算作root的子logger
logger = logging.getLogger("my_app")
# 通过日志传播 propagate 把日志传给父logger 
# 这里用root的streamhandler输出
logger.info("启动服务")
```
> 不推荐使用basicConfig对日志等级进行自我创作，因为会影响代码的移植性，代码在别人那里容易起冲突

## 1.3 输出到文件
```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO
)

logging.info("保存到文件")
```
生成：

app.log

## 1.4 设置日志格式

```python
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s: %(message)s"
)

logging.info("服务器启动")
```

输出：

2026-07-26 10:20:30 INFO root: 服务器启动

常用字段：
%(asctime)s	    时间
%(levelname)s	日志级别
%(name)s	    logger名字
%(message)s	    日志内容

## 1.5 捕获异常
不要：
```py
try:
    x = 1 / 0
except:
    logging.error("出错")
```
因为丢失堆栈。
ERROR:root:出错

推荐：
```py
try:
    x = 1 / 0
except Exception:
    logging.exception("计算失败")
```
输出：

ERROR:root:计算失败
Traceback...
ZeroDivisionError

## 1.6 logging 的核心结构
1. Logger记录器
2. Handler处理器
3. Formatter格式化器
4. Filter过滤器





