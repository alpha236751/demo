# 一、 安装 Redis
## Mac 或 Linux
```bash
# Mac
brew install redis 

# Linux
yum install redis
```
## Windows
- WSL
- Docker

# 二、 启动 Redis
## 服务端
```bash
redis-server
```
## 客户端
```bash
redis-cli 
# 连接参数
redis-cli -h 192.168.1.100 # host
redis-cli -p 6380 # port
redis-cli -s /tmp/redis.sock # socket
redis-cli -u redis://user:pass@host:port/0 # uri
# 认证参数
redis-cli -a mypassword
# 命令执行与输出参数
redis-cli -n 1 # 指定数据库编号
redis-cli --raw # 以原始格式输出
```

# 三、 基本操作
命令不区分大小写
键名区分大小写
## 通用操作
```bash
DEL key # 删除键
EXISTS key # 检查键是否存在
EXPIRE key seconds # 设置键过期时间
TTL key # 获取键过期时间
TYPE key # 获取键类型
KEYS pattern # 查找匹配模式的键 生产环境慎用
SCAN cursor # 增量迭代键 生产环境替代KEYS 渐进的非阻塞的返回结果 cursor是游标0表示从头开始
```

## 系统操作
```bash
AUTH 123456 # 输入密码
PING # 检查连接是否正常
QUIT # 退出 Redis 客户端连接
SELECT index # 切换到指定数据库
INFO # 获取 Redis 服务器状态信息
FLUSHDB # 清空当前数据库的所有键
FLUSHALL # 清空所有数据库的所有键
```

### 模式匹配规则
- *	    匹配 0 个或多个 任意字符
`n*`          匹配 name、n、new
- ?	    匹配 恰好 1 个 任意字符
`name?me `    匹配 name、nzme，但不匹配 nme
- [abc]   匹配方括号中的 任意 1 个字符
`n[a]me `     只匹配 name，不匹配 nbme

## str 字符串类型
默认类型
```bash
SET key value # 设置键值对
GET key # 获取键值对
MSET key1 value1 key2 value2 # 设置多个键值对
MGET key1 key2 # 获取多个键值对
INCR key # 增加键值对的数值
DECR key # 减少键值对的数值
SETNX key value # 设置键值对，如果键不存在才设置
SETEX key seconds value # 设置键值对，过期时间为 seconds 秒
```

## list 列表类型
```bash
LPUSH key value1 value2 value3 # 在列表头添加元素
RPUSH key value1 value2 value3 # 在列表尾添加元素
LRANGE key start end # 获取列表范围内的元素
LPOP key n # 从列表头弹出 n 个元素 ，默认弹出 1 个元素
RPOP key n # 从列表尾弹出 n 个元素 ，默认弹出 1 个元素
LLEN key # 获取列表长度
LTRIM key start end # 截断列表，保留指定范围内的元素
```

## set 集合类型
```bash
SADD key value1 value2 value3 # 添加元素到集合
SMEMBERS key # 获取集合中的所有元素
SISMEMBER key value # 检查元素是否在集合中
SREM key value1 value2 # 删除集合中的元素
SCARD key # 获取集合的元素数量
SUNION key1 key2 # 合并集
SINTER key1 key2 # 取交集
SDIFF key1 key2 # 取差集
```

## Z set 有序集合类型
```bash
ZADD key score value # 添加元素到有序集合
ZEMBERS key # 获取有序集合中的所有元素
ZCARD key # 获取有序集合的元素数量
ZREM key value1 value2 # 删除有序集合中的元素
ZRANGE key start end WITHSCORES # 获取有序集合范围内的元素 附带分数
ZSCORE key value # 获取元素的分数
ZRANK key value # 获取元素的排名 从小到大
ZREVRANK key value
```


