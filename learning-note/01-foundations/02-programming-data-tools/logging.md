# 1. python内置模块 logging
## 1.1 日志级别
- DEBUG 调试信息 
- **INFO** 一般信息
- **WARNING** 警告信息 可能有问题
- **ERROR** 错误信息 影响程序正常运行
- CRITICAL 致命错误信息

默认日志级别为INFO 格式为asctime - name - message
```python
logging.debug("debug message")
logging.info("info message")
logging.warning("warning message")
logging.error("error message")
logging.critical("critical message")
```

## 1.2 全局配置
默认logger名为root
```python
logging.basicConfig(
    level=logging.INFO, # 日志级别
    format="%(asctime)s - %(levelname)s - %(message)s", # 日志格式
    filename="xxx/log.txt", # 日志文件目录
    filemode="w", # 日志文件模式 w 写入模式 a 追加模式
    )
```
## 1.3 自定义Logger
```python
test_logger = logging.getLogger(__name__)
```
## 1.4 Handler
```python
stream_handler = logging.StreamHandler()
# file_handler = logging.FileHandler("xxx/log.txt", "w")

# 按时间自动切割（滚动）日志文件 
# 当前 app.log 文件会被重命名为 app.log.2026-07-10（日期格式会根据切割时间变化），
# 然后创建一个新的空 app.log 文件继续写入
file_handler = logging.TimedRotatingFileHandler(
    filename="xxx/log.txt", # 当前日志会写入此文件，切割时会加上时间后缀重命名
    when='h', # 切割时间单位。'S'(秒), 'M'(分), 'H'(时), 'D'(天), 'W0'-'W6'(周一到周日), 'midnight'(每天午夜)
    interval=1, # 时间间隔。与 when 配合使用，例如 when='H', interval=6 表示每6小时切割一次
    backupCount=0, # 保留的历史日志文件数量。超过此数量，最旧的文件会被自动删除
    encoding=None, 
    delay=False, 
    utc=False, # False 使用本地时间，True 使用UTC时间来决定切割时机
    atTime=None # datetime.time 对象，用于指定 'midnight' 或按周切割时的具体时间点
    )

file_handler.setLevel(logging.INFO) # 日志级别
file_handler.setFormatter(formatter) # 日志格式

test_logger.addHandler(stream_handler) # 添加到logger
test_logger.addHandler(file_handler) # 添加到logger
```
## 1.5 Formatter

```python
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
```
- %(asctime)s 日志时间
- %(levelname)s 日志级别
- %(message)s 日志信息
- %(name)s 日志记录器名称
- %(filename)s 日志文件名
- %(lineno)s 日志行号

## 1.6 捕获异常
```python
try:
    a = 1 / 0
except Exception as e:
    logging.exception("除零异常：%s", e)
```







