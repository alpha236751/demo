# NumPy + Pandas + Matplotlib 数据分析全套笔记
> 环境：Python + Jupyter Notebook，包含**代码示例、语法说明、实战用法**，可直接运行学习

## 一、NumPy 数值计算库
### 1. ndarray 数组
#### 1.1 三大核心特性
1. **多维性**：支持0维、1维、2维及高维数组
```python
import numpy as np

# 0维数组（标量）
arr = np.array(5)
print(arr)
print(arr.ndim)

# 1维数组（向量）
arr = np.array([1, 2, 3])
print(arr)
print(arr.ndim)

# 2维数组（矩阵）
arr = np.array([[1, 2, 3],[4, 5, 6]])
print(arr)
print(arr.shape)
```

2. **同质性**：数组内**所有元素数据类型必须一致**，自动向上转型
```python
# 数字+字符串 → 全部转为字符串
arr = np.array([1,'hello'])
print(arr)

# 整型+浮点 → 全部转为浮点
arr = np.array([1,1.5])
print(arr)
```

3. **高效性**：底层C实现，运算速度远快于Python原生列表，支持向量化运算。

#### 1.2 ndarray 常用属性
```python
arr = np.array([[1, 2, 3], [4, 5, 6]])
print('数组形状:', arr.shape)    # (行数, 列数)
print('数组维度:', arr.ndim)     # 维度数
print('数组元素个数:', arr.size) # 总元素数量
print('数组元素类型:', arr.dtype)# 元素数据类型
print('数组转置:', arr.T)        # 行列互换
```

#### 1.3 数组创建
##### 1.3.1 基础创建 + 深拷贝
```python
# 指定数据类型创建数组
arr = np.array([1, 2, 3], dtype=float)
# copy() 深拷贝，互不影响
arr1 = arr.copy()
arr1[0] = 100
print(arr)
print(arr1)
```

##### 1.3.2 预定义填充数组
```python
# 全0数组
arr1 = np.zeros((2, 3))
# 全1数组
arr2 = np.ones((5,))
# 空数组（内存原有值，不初始化）
arr3 = np.empty((3,5))
# 指定值填充
arr4 = np.full((3,4), 100)
# 复刻形状并填充指定值
arr5 = np.full_like(arr4, 200)
```

##### 1.3.3 数值范围生成数组
```python
# 等差数列：start, stop, step
arr1 = np.arange(1, 11, 2)
# 等间隔数列：起止、元素个数
arr2 = np.linspace(0, 10, 6)
# 对数等比数列：base=底数
arr3 = np.logspace(0, 4, 3, base=2)
```

##### 1.3.4 特殊矩阵
```python
# 单位矩阵
arr1 = np.eye(3, dtype=int)
# 对角矩阵
arr2 = np.diag([1, 2, 3])
```

##### 1.3.5 随机数组
```python
# [0,1) 随机浮点数
arr1 = np.random.rand(2, 3)
# 指定范围随机浮点数 [low, high)
arr2 = np.random.uniform(5, 10, (2, 3))
# 指定范围随机整数 [low, high)
arr3 = np.random.randint(5, 10, (2, 3))
# 标准正态分布(均值0，方差1)
arr4 = np.random.randn(2, 3)

# 随机种子：固定随机结果（可复现）
np.random.seed(20)
arr5 = np.random.randint(1, 10, (2, 5))
print(arr5)
```

#### 1.4 数据类型
```python
# 布尔型
arr1 = np.array([True, False, True], dtype=bool)
# 32位整型
arr2 = np.array([1, 2, 3], dtype=np.int32)
# 无符号16位整型
arr3 = np.array([1, 2, 3], dtype=np.uint16)
```

#### 1.5 索引与切片
##### 一维数组
```python
arr = np.random.randint(0, 10, 10)
print(arr)
print(arr[3])          # 单索引取值
print(arr[1:8:2])      # 切片 [起始:结束:步长]
print(arr[(arr > 5) & (arr < 8)]) # 布尔索引（多条件加括号）
```

##### 二维数组
```python
arr = np.random.randint(0, 100, (5,7))
print(arr)
print(arr[3,2])                # 单行单列取值
print(arr[1:3,2:5])            # 行列切片
print(arr[arr > 50])           # 布尔索引（返回一维）
print(arr[:,2][arr[:,2] > 50]) # 指定列筛选
```

#### 1.6 数组运算
##### 常规四则运算（逐元素运算）
```python
# 一维
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a+b, a-b, a*b, a/b, a**2)

# 二维
a = np.array([[1, 2, 3],[4, 5, 6]])
b = np.array([[7, 8, 9],[10, 11, 12]])
print(a+b, a-b, a*b, a/b)
```

##### 广播机制
**不同形状数组自动补齐维度运算**
```python
a = np.array([1,2,3])
b = np.array([[4],[5],[6]])
print(a+b)
```

##### 矩阵乘法
- `*`：逐元素相乘
- `@`：数学矩阵乘法
```python
a = np.array([[1, 2], [4, 5]])
b = np.array([[7, 8], [10, 11]])
print(a * b)
print(a @ b)
```

### 2. NumPy 常用函数
#### 2.1 基础数学函数
```python
arr = np.array([1, 4, 9])
print(np.sqrt(arr))        # 平方根
print(np.exp(1))          # 自然指数 e^x
print(np.log(2.71828))    # 自然对数 ln(x)
print(np.sin(np.pi/2))    # 正弦
print(np.cos(0))         # 余弦
print(np.abs([1,-2,-3]))  # 绝对值
print(np.power(arr, 2))   # 幂运算

# 取整
arr = np.array([1.3, 3.5, 3.6])
print(np.round(arr))      # 四舍五入（银行家舍入）
print(np.ceil(arr))       # 向上取整
print(np.floor(arr))      # 向下取整

# 缺失值判断
arr = np.array([1.3, np.nan, 3.6])
print(np.isnan(arr))
```

#### 2.2 统计函数
```python
arr = np.array([1, 2, 3, 4, 5])
print(np.sum(arr))        # 求和
print(np.mean(arr))       # 平均值
print(np.median(arr))     # 中位数
print(np.std(arr))        # 标准差
print(np.var(arr))        # 方差
print(np.max(arr), np.argmax(arr)) # 最大值 + 索引
print(np.min(arr), np.argmin(arr)) # 最小值 + 索引
print(np.percentile(arr, 50))      # 分位数
print(np.cumsum(arr))     # 累计和
print(np.cumprod(arr))    # 累计乘积
```

#### 2.3 比较与逻辑函数
```python
# 大小比较
print(np.greater([1,2,3,4], 3))    # >
print(np.less([1,2,3,4], 3))       # <
print(np.greater_equal([1,2,3,4],3))# >=
print(np.less_equal([1,2,3,4], 3)) # <=

# 相等判断
print(np.equal([1,2,3,4], 4))
print(np.not_equal([1,2,3,4], 4))

# 逻辑运算
print(np.logical_and([1,0,1,0], [1,0,0,1])) # 与
print(np.logical_or([1,0,1,0], [1,0,0,1]))  # 或
print(np.logical_not([1,0,1,0]))            # 非

# 存在判断
print(np.any([1,0,1,0]))  # 任意一个为True则返回True
print(np.all([1,0,1,0]))  # 全部为True才返回True

# 条件赋值
arr = np.array([1,2,3,4,5,6])
print(np.where(arr > 3, arr, 4))  # 单条件
print(np.select([arr>3, arr==3, arr<3], 
                ['大于三','等于三','小于三'], default='其他')) # 多条件
```

#### 2.4 排序、拼接、变形
```python
# 排序
arr = np.array([3,5,2,7,4,8,1,9])
print(np.sort(arr))    # 排序后数组
print(np.argsort(arr)) # 排序后原索引

# 去重
arr = np.array([3,5,5,7,4,4,1,9])
print(np.unique(arr))

# 数组合并
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
print(np.concatenate([arr1, arr2]))

# 数组分割
arr = np.array([1,2,3,4,5,6])
print(np.split(arr, 2))      # 平均分成2份
print(np.split(arr, [1, 4])) # 按索引分割

# 形状重塑
arr = np.array([1,2,3,4,5,6])
print(arr.reshape(2, 3))

# 综合案例
arr = np.array([28,30,29,31,32,30,29])
avg = np.mean(arr)
max_val = np.max(arr)
min_val = np.min(arr)
day = arr[arr >30]
print(f'{avg:.2f}', max_val, min_val, day)
```

## 二、Pandas 数据分析库
```python
import pandas as pd
import numpy as np
```

### 1. Series 一维序列
#### 1.1 创建 Series
```python
# 列表创建 + 自定义索引、名称
s = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'], name = '数字')
print(s)

# 字典创建：key=索引，value=值
s = pd.Series({'a':1, 'b':2, 'c':3, 'd':4, 'e':5})
print(s)
```

#### 1.2 常用属性
```python
s = pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'], name = '数字')
print(f'index: {s.index}')
print(f'values: {s.values}')
print(f'shape: {s.shape}')
print(f'ndim: {s.ndim}')
print(f'size: {s.size}')
print(f'name: {s.name}')
print(f'dtype: {s.dtype}')
```

#### 1.3 数据访问
- `loc`：**显式索引**（自定义标签）
- `iloc`：**隐式索引**（数字位置）
```python
print(s.loc["a"])
print(s.iloc[0 : 3])

print(s['b'])
print(s[s<3])       # 布尔筛选
print(s.head(3))    # 前N行
print(s.tail(3))    # 后N行
```

#### 1.4 常用统计与处理方法
```python
s = pd.Series([31,24,32,None,23,23,23,45,51], index = ['a','b','c','d','e','f','g','h','i'])

s.describe()               # 综合统计信息
print(s.count())           # 非空元素个数
print(s.isna())            # 判断缺失值
print(s.isin([31,24]))     # 判断是否包含指定值

# 统计指标
print(s.mean(), s.median(), s.sum(), s.max(), s.min())
print(s.std(), s.var(), s.quantile(0.25))

print(s.mode())            # 众数
print(s.value_counts())    # 统计值出现次数
print(s.drop_duplicates()) # 去重（保留原索引）
print(s.unique())          # 去重（返回数组）

# 排序
print(s.sort_values())     # 按值排序
print(s.sort_index())      # 按索引排序
```

### 2. DataFrame 二维数据表（核心）
#### 2.1 创建 DataFrame
```python
df = pd.DataFrame({
    'id':[1, 2, 3, 4, 5],
    'name':['张三','李四','王五','赵六','钱七'],
    'age':[18, 19, 20, 21, 22],
    'score':[90, 80, 70, 60, 50]
}, index=['a','b','c','d','e'], columns=['id','name','score','age'])
print(df)
```

#### 2.2 基础属性
```python
print(df.index)      # 行索引
print(df.columns)    # 列名
print(df.dtypes)     # 每列数据类型
print(df.ndim)       # 维度
print(df.shape)      # 形状 (行数,列数)
print(df.size)       # 总元素数
print(df.T)          # 转置
print(df.values)     # 转为numpy数组
```

#### 2.3 数据选取
```python
# 取行
print(df.loc['a'])    # 按标签取行
print(df.iloc[0])     # 按位置取行

# 取列
print(df.name)
print(df['name'])
print(df[['name', 'id']]) # 多列

# 取单个元素
print(df.loc['a', 'id'])
print(df.iloc[0, 0])

# 头尾数据
print(df.head(2))
print(df.tail(2))

# 布尔筛选
print(df[(df.score > 60)&(df.id > 2)])

# 随机抽样
print(df.sample(2))
```

#### 2.4 常用统计与排序
```python
# 单列统计
print(df.score.mean(), df.score.median(), df.score.std())
print(df.score.max(), df.score.min(), df.score.sum())
print(df.score.value_counts())

# 排序
print(df.sort_values(by = ['score', 'age'], ascending = [True, False]))
print(df.nlargest(2, 'score'))  # 取分数最大2行
print(df.nsmallest(2, 'age'))   # 取年龄最小2行

# 字符串匹配
df.name.str.contains("三")
```

#### 2.5 query 条件查询（简洁语法）
```python
data = {
    "name": ["张三", "李四", "王五", "小明", "小红"],
    "rating": [9.2, 8.5, 9.5, 7.8, 9.1],
    "release_year": [1994, 2000, 1994, 2010, 1999],
    "city": ["北京", "上海", "广州", "深圳", "北京"],
    "score num": [88, 76, 92, 65, 85],
    "income": [2000, 1500, 3000, 1800, 2500]
}
df = pd.DataFrame(data)

# 1. 基础比较
print(df.query("rating > 9.0"))
# 2. 多条件
print(df.query("rating>9.0 and release_year==1994"))
# 3. 字符串匹配
print(df.query("name.str.contains('小')"))
# 4. 成员判断 in / not in
print(df.query("city in ['北京', '上海']"))
# 5. 引用外部变量 @变量名
year = 1994
print(df.query("release_year == @year"))
# 6. 列名含空格：反引号 ``
print(df.query("`score num` > 80"))
# 7. 列间运算
print(df.query("income * rating > 20000"))
# 8. 缺失值判断
df_null = df.copy()
df_null.loc[2, "city"] = np.nan
print(df_null.query("city.isna()"))
```

#### 2.6 merge 表合并
**四种连接方式**：内连接、左连接、右连接、外连接
```python
df1 = pd.DataFrame({'id': [1,2,3,4], 'name': ['张三','李四','王五','赵六']})
df2 = pd.DataFrame({'id': [3,4,5,6], 'score': [85,92,78,90]})

# 内连接 inner（默认）：只保留交集
pd.merge(df1, df2, on='id', how='inner')
# 左连接 left：保留左表所有数据
pd.merge(df1, df2, on='id', how='left')
# 右连接 right：保留右表所有数据
pd.merge(df1, df2, on='id', how='right')
# 外连接 outer：保留两表所有数据
pd.merge(df1, df2, on='id', how='outer')
```

### 3. 完整数据分析流程
#### 3.1 数据导入与导出
```python
# CSV
df = pd.read_csv('./data/data.csv')
df.to_csv('./data/data_export.csv', index=False)

# JSON
import json
with open('./data/sales.json', 'r') as f:
    data = json.load(f)
df = pd.DataFrame(data)
df.to_json('./data/sales_export.json', orient='records')
```

#### 3.2 数据清洗
##### 3.2.1 缺失值处理
```python
df = pd.DataFrame({'a':[1, None, 3], 'b':[4, 8, 6], 'c':[7, 8, None]})
print(df.isnull()) # 检测缺失值

# 删除缺失值
df.dropna()                # 删除含缺失值的行
df.dropna(axis=1)          # 删除含缺失值的列
df.dropna(thresh=3)        # 保留至少3个有效值的行
df.dropna(subset=['a'])     # 指定列检测缺失值并删行

# 填充缺失值
df.fillna(0)                          # 统一填充0
df.fillna({'a':0, 'c':2})             # 按列分别填充
df.fillna(df['c'].mean())             # 均值填充
df.ffill()                            # 前向填充（用上一行）
df.bfill()                            # 后向填充（用下一行）
```

##### 3.2.2 重复值处理
```python
data = {
    'name':['alice','alice','bob','alice','jack','bob'],
    'age':[26,25,30,25,35,30],
    'city':['NY','NY','LA','NY','SF','LA']
}
df = pd.DataFrame(data)
print(df.duplicated())                # 检测重复行
df.drop_duplicates()                  # 整行去重
df.drop_duplicates(subset=['name'])   # 指定列去重
df.drop_duplicates(subset=['name'], keep='last') # 保留最后一条
```

##### 3.2.3 数据类型转换
```python
df = pd.DataFrame({
    'name':['alice','bob', 'jack'],
    'age':[26,25,30],
    'city':['NY','NY','LA']
})
df['age'] = df['age'].astype('float32')
df['city'] = df['city'].astype('category')

# map 映射转换
df['city'] = df['city'].map({'NY':True,'LA':False})
```

##### 3.2.4 数据变形（长宽表转换、分列）
```python
data = {
    'ID': [1, 2],
    'name': ['alice s', 'bob s'],
    'Math': [90, 85],
    'English': [88, 92]
}
df = pd.DataFrame(data)

df.T # 转置

# 宽表 → 长表 melt
df2 = df.melt(id_vars=['ID','name'], var_name='subject', value_name='score')
# 长表 → 宽表 pivot
df3 = df2.pivot(index=['ID', 'name'],columns='subject',values='score')

# 字符串分列
df[['first', 'last']] = df['name'].str.split(' ',expand=True)
```

##### 3.2.5 数据分箱（连续值→离散分类）
```python
df1 = df.head()[['student_id', 'english']]
# 按区间分箱
df1['english_bin'] = pd.cut(df1['english'], bins=[60,80,90,100], labels=['及格','良','优秀'])
# 按数量等分分箱
pd.qcut(df1['english'], 3).value_counts()
```

##### 3.2.6 时间数据处理
```python
# 时间戳对象
d = pd.Timestamp('2023-01-01 17:35:23')
print(d.year, d.month, d.day, d.hour)
print(d.day_name()) # 星期

# 字符串转时间类型
df = pd.DataFrame({'date': ['2023-01-01 03:20:10', '2023-01-02 10:04:00']})
df['date'] = pd.to_datetime(df['date'])
df['week'] = df['date'].dt.day_name()
```

##### 3.2.7 分组聚合 groupby
```python
df.groupby('地区').get_group('华东')          # 取出指定分组
df.groupby('地区')['单价'].mean()            # 分组聚合
df.groupby("地区").filter(lambda x: x['单价'].mean() > 3000) # 分组过滤
df.groupby('地区')['单价'].transform('mean') # 分组广播（每行附加分组统计值）
```

##### 3.2.8 透视表 pivot_table
```python
# index行分组，columns列展开，values计算字段，aggfunc聚合方式
df.pivot_table(index='地区', columns='品类', values='单价', aggfunc='mean', margins=True)
```

## 三、Matplotlib 数据可视化
### 基础配置 + 通用数据
```python
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams

# 解决中文乱码
rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False # 解决负号显示问题

data = {
    "月份": ['一月', '二月', '三月', '四月', '五月', '六月', '七月', '八月', '九月', '十月', '十一月', '十二月'],
    "销售额": [320, 450, 390, 560, 680, 720, 650, 800, 920, 850, 980, 1100],
    "成本": [180, 220, 210, 280, 320, 350, 310, 380, 420, 390, 450, 500],
    "利润": [140, 230, 180, 280, 360, 370, 340, 420, 500, 460, 530, 600],
    "访客数": [120, 150, 140, 180, 220, 250, 230, 280, 320, 300, 350, 400]
}
df = pd.DataFrame(data)
```

### 1. 折线图
```python
plt.figure(figsize=(10, 6))
plt.plot(df['月份'], df['销售额'], label = '销售额')
plt.title('销售额与月份的关系', color = 'red', fontsize = 16)
plt.xlabel('月份', fontsize = 12)
plt.ylabel('销售额', fontsize = 12)
plt.ylim(0, 1200)
plt.legend()
plt.grid(alpha = 0.5, linestyle = '--')
plt.show()
```

### 2. 柱状图
```python
plt.figure(figsize=(10, 6))
plt.bar(df['月份'], df['销售额'], label = '销售额', color = 'orange')
plt.title('销售额与月份的关系', color = 'red', fontsize = 16)
plt.xlabel('月份')
plt.ylabel('销售额')
plt.legend()
plt.grid(axis = 'y', alpha = 0.5, linestyle = '--')
plt.show()
```

### 3. 饼图
```python
plt.figure(figsize=(10, 6))
plt.pie(df['访客数'],labels = df['月份'].tolist(),
         autopct = '%.2f%%',
         explode=(0, 0.1, 0, 0, 0,0, 0,0,0,0,0,0))
plt.title('访客占比', color = 'red', fontsize = 16)
plt.legend()
plt.show()
```

### 4. 散点图
```python
plt.figure(figsize=(10, 6))
plt.scatter(df['月份'], df['销售额'], label = '销售额')
plt.title('销售额与月份的关系')
plt.xlabel('月份')
plt.ylabel('销售额')
plt.legend()
plt.grid(alpha = 0.5, linestyle = '--')
plt.show()
```

### 5. 多子图布局
```python
month = ['1','2','3','4']
sales = [100,150,80,130]

plt.figure(figsize=(10,8))
# 2行2列 第1个子图
f1 = plt.subplot(2,2,1)
f1.plot(month, sales, label = '销售额')
# 2行2列 第2个子图
f2 = plt.subplot(2,2,2)
f2.bar(month, sales, label = '销售额')
# 2行2列 第3个子图
f3 = plt.subplot(2,2,3)
f3.scatter(month, sales, label = '销售额')
# 2行2列 第4个子图（横向柱状图）
f4 = plt.subplot(2,2,4)
f4.barh(month, sales, label = '销售额')

plt.tight_layout() # 自动调整间距
plt.show()
```

---

## 笔记总结
1. **NumPy**：底层数值计算，核心 `ndarray`，向量化运算、切片、广播、数学函数。
2. **Pandas**：表格数据分析，`Series`+`DataFrame`，**数据读写、清洗、筛选、分组、合并、透视**是业务核心。
3. **Matplotlib**：可视化图表，折线/柱状/饼图/散点图、多子图，用于数据呈现与洞察。
4. 完整链路：`数据读取 → 清洗 → 特征处理 → 统计分析 → 可视化`。