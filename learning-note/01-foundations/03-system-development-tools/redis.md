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
模式匹配规则
- *	    匹配 0 个或多个 任意字符
`n*`          匹配 name、n、new
- ?	    匹配 恰好 1 个 任意字符
`name?me `    匹配 name、nzme，但不匹配 nme
- [abc]   匹配方括号中的 任意 1 个字符
`n[a]me `     只匹配 name，不匹配 nbme


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

## 发布/订阅 (Pub/Sub)
消息不持久化 无法回溯历史 不支持背压 集群模式兼容性差
```bash
SUBSCRIBE channel # 订阅频道
PUBLISH channel message # 发布消息
```

# 四、 基本数据类型
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
SCARD key # 获取集合的元素数量 Cardinality 基数
SUNION key1 key2 # 合并集
SINTER key1 key2 # 取交集
SDIFF key1 key2 # 取差集
```

## zset 有序集合类型
```bash
ZADD key score value # 添加元素到有序集合
ZEMBERS key # 获取有序集合中的所有元素
ZCARD key # 获取有序集合的元素数量
ZREM key value1 value2 # 删除有序集合中的元素
ZRANGE key start end WITHSCORES # 获取有序集合范围内的元素 附带分数
ZSCORE key value # 获取元素的分数
ZRANK key value # 获取元素的排名 从小到大
ZREVRANK key value # 获取元素的排名 从大到小
```

## hash 哈希类型
```bash
HSET key field value # 设置哈希字段值对
HGET key field # 获取哈希字段值
HGETALL key # 获取哈希字段值对
HDEL key field # 删除哈希字段值对
HEXISTS key field # 检查哈希字段是否存在
HINCRBY key field increment # 增加哈希字段值    
HDECRBY key field decrement # 减少哈希字段值    
HKEYS key # 获取哈希字段名
HVALS key # 获取哈希字段值
HLEN key # 获取哈希字段数量
```

# 五、 高级数据类型
## Stream 消息队列
```bash
XADD key * field1 value1 # 添加消息到队列 *自动生成消息 ID
XRANGE key start end # 获取队列范围内的消息 - + 表示获取所有消息
XLEN key # 获取队列消息数量
XDEL key id # 删除队列消息
XTRIM key MAXLEN count | MAXID id # 修建队列，保留指定数量的消息 或指定 ID 之前的消息
XREAD COUNT count BLOCK milliseconds STREAMS key id  # 从队列读取消消息 
# count 表示读取的消息数量 
# BLOCK 表示阻塞时间毫秒 0 表示永久阻塞
# STREAMS 表示要读取消息的队列 id 表示从哪个 ID 开始读取 0 表示从头开始读取 $ 表示新的消息 
XGROUP CREATE key group_name id # 创建消费者组
XINFO GROUPS key # 获取消费者组信息
XGROUP CONSUMERS key group_name consumer_name # 添加消费者组中的消费者
XREADGROUP GROUP group_name consumer_name COUNT count BLOCK milliseconds STREAMS key > # 从消费者组读取消消息 > 表示从最新的消息
```

## Geospatial 地理空间类型
```bash
GEOADD key longitude latitude member # 添加地理空间元素
GEOPOS key member # 获取地理空间元素的位置
GEODIST key member1 member2 KM # 获取地理空间元素之间的距离 默认单位为米
GEOSEARCH key FROMMEMBER member BYRADIUS radius KM # 获取地理空间元素范围内的元素
```

## HyperLogLog 基数统计

## BitMap 位图类型

## Bitfield 位域类型

# 六、 事务
```bash
MULTI # 开启事务 multiple
EXEC # 执行事务 execute
DISCARD # 放弃事务 discard
```

# 七、 持久化
## RDB Redis Database 
在指定时间间隔将数据快照写入磁盘
可以通过配置文件中的save参数来配置
```conf
save 3600 1 # 每3600秒 只要有一次修改 就写入一次 默认配置
save 300 100 # 每300秒 100次修改 就写入一次
save 60 10000 # 每60秒 10000次修改 就写入一次
```
```bash
SAVE # 手动触发数据快入磁盘
BGSAVE # 异步保存数据库 
```
会阻塞 Redis 主进程，直到数据写入完成。

## AOF Append Only File
在每次写入操作后，将操作记录写入日志文件中
当Redis 启动时，会读取日志文件中的操作记录，重新执行，以恢复数据。
在配置文件中开启 AOF 持久化
```conf
appendonly yes # 开启 AOF 持久化
```

# 八、 主从集群
将主数据库master的数据异步发送到从数据库slave中
修改从数据库slave的配置文件 复制主数据库master的配置文件 改名为 redis-6380.conf
```conf
port 6380 # 从数据库端口号
pidfile /var/run/redis_6380.pid # 从数据库进程 ID 文件
dbfilename dump-6380.rdb # 从数据库数据文件名
replicaof 127.0.0.1 6379 # 设置主数据库的 IP 地址和端口号
```
启动从数据库slave
```bash
redis-server redis-6380.conf
```
连接从数据库slave
```bash
redis-cli -h 127.0.0.1 -p 6380
```

# 九、 哨兵模式
主从复制的缺点：主节点宕机后，需要手动提升从节点为主节点
哨兵本身也是一个进程 也会有单节点故障问题 
所以在实际生产环境中，会使用多个哨兵节点来保证哨兵模式的高可用。

- 监控 
- 通知 发布订阅
- 自动故障转移 自动选择一个从节点为主节点 将其他从节点设置为主节点的从节点
手写sentinel.conf文件
```conf
sentinel monitor mymaster 127.0.0.1 6379 1  # 监控主节点 mymaster 127.0.0.1 6379 1表示只需要一个哨兵节点同意 就 触发故障转移
```
启动哨兵模式
```bash
redis-sentinel sentinel.conf
```

# 十、 缓存异常
## 缓存穿透
查询的数据在缓存和数据库中都不存在，导致每次请求都无法命中缓存，必须直达数据库。

缓存空对象
## 缓存击穿
缓存有但刚好过期，大量请求同时打到DB

设置互斥锁 让请求排队 第一个请求会从DB中获取数据 并缓存到Redis中
## 缓存雪崩
大量缓存同一时间集体过期

给TTL设置随机值





