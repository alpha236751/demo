# 1. 什么是提示词工程
- **Prompt** ：提示词是指在生成文本时，给模型提供的一种提示，用于引导模型生成符合要求的文本。
- **Prompt Engineering** ：提示词工程是指在生成文本时，根据不同的任务和需求，设计和实现不同的提示词，以提高模型的性能和效果。
## 1.1 使用prompt的两个方式
1.获得具体问题的具体结果
2.获得一般问题的通用结果
## 1.2 prompt调优
目标：具体、丰富、少歧义

# 2. Prompt的典型构成
- **角色**：给ai定义一个匹配任务的角色
- **指示**：对任务进行描述
- **上下文**：给出任务其他相关背景，尤其在多轮交互中
- **例子**：必要时给出举例 学术称为one-shot learning、few-shot learning、zero-shot learning或in-context learning
- **输入**：任务的输入信息
- **输出**：输出的格式描述
## 2.1 NLU自然语言理解
- 自然语言理解（Natural Language Understanding， NLU）：让机器读懂人类自然语言的技术

```python
from openai import OpenAI
from os import getenv
from dotenv import load_dotenv

# 读取 .env 文件，把里面的键值对加载到系统环境变量中。
load_dotenv()  

# 创建 Deepseek 客户端
client = OpenAI(
api_key=getenv("DEEPSEEK_API_KEY"),
base_url="https://api.deepseek.com",
)

# 基于prompt生成文本
def get_completion(prompt, model="deepseek-v4-pro"):
    messages = [{"role": "user", "content": prompt}]
    response = client.chat.completions.create(
        model=model,
        messages=messages,
    )
    return response.choices[0].message.content

# 任务描述
instruction = """
你的任务是识别用户对手机流量套餐产品的选择条件
每种流量套餐产品包含三个属性：名称(name)，月费价格(price)，和月流量(data)
根据用户输入，识别用户在上述三种属性上的倾向
"""
# 输出格式
output_format = """
以JSON格式输出
1. name字段的取值为string类型，取值必须为以下之一：经济套餐、畅游套餐、无限套餐、校园套餐、null
2. price字段的取值为一个结构体 或 null，结构体包含两个字段：
(1)operator(string类型)，取值范围：'<=', '>=', '=='
(2)value(int类型)
3. data字段的取值为一个结构体 或 null，结构体包含两个字段：
(1)operator(string类型)，取值范围：'<=', '>=', '=='
(2)value(int类型 或 string类型), string类型只能取值'无上限‘
4.sort字段表示用户意图，取值为一个结构体，包含两个字段：
(1)ordering(string类型)，取值范围：'ascend', 'descend'
(2)value, 存储要求排序的字段，取值范围：'price','data'

只输出包含用户提及的字段，不要猜测任何用户未直接提及的字段。不要输出值为null的字段。
"""
# 例如
examples = """
便宜的套餐: {"sort":{"ordering":"ascend","value":"price"}}
有没有不限流量的: {"data":{"operator":"==","value":"无上限"}}
流量大的: {"sort":{"ordering":"descend","value":"data"}}
100G以上流量的套餐最便宜的是哪个: {"sort":{"ordering":"ascend","value":"price"},"data":{}}
月费不超过200的: {"price":{"operator":"<=","value":200}}
就费月费180哪个套餐: {"price":{"operator":"==","value":180}}
经济套餐: {"name":"经济套餐"}
"""
# 输入
input_text = "有没有便宜的套餐"
# input_text = "有没有土豪套餐"
# input_text = "办个200G的套餐"
# input_text = "有没有流量大的套餐"
# input_text = "200元以下，流量大的套餐有啥"
# input_text = "你说那个10G的套餐，叫啥名字"

# prompt
prompt = f"""
{instruction}
{output_format}
例如：
{examples}

用户输入：{input_text}
""" 

# 调用模型
response = get_completion(prompt)
print(response)

```  
## 2.2 DST多轮对话
- 对话状态跟踪(Dialogue State Tracking, DST): 记录用户在多轮对话中的状态，包括用户输入、模型输出、上下文等。
## 2.3 NLG自然语言生成
- 自然语言生成（Natural Language Generation, NLG）：让模型根据输入信息生成符合要求的自然语言文本。

# 3.进阶技巧
## 3.1 思维链(COT)
- 思维链（chain of thought, COT）：在提问时以[let's think step by step]开头，ai就会把问题拆分为多个步骤，逐步解决
## 3.2 自我一致性（SC）
- 自我一致性（self-consistency）：用相同的prompt，多次调用模型，最后取结果出现的次数最多的那个。
## 3.3 思维树（ToT）
- 思维树（Thought of Tree, ToT）
1.思维分解：把复杂问题拆成粒度适中的子步骤（“思维”），既不太大难处理，也不太小无意义。
2.思维生成：每个节点生成多个候选下一步（如 3-5 个），常用采样或提示生成。   
3.状态评估：模型自评或互评每个路径的优劣 / 可行性，为每条路径打分排序。
4.搜索与剪枝：用 BFS/DFS 探索，保留高分分支、剪掉无效分支，必要时回溯重来。

# 4. 防止Prompt注入
## 4.1 Prompt注入分类器
- 先检查用户输入的prompt是否包含危险的代码，拦截掉危险的代码
## 4.2 直接在输入中防御
- 直接在用户输入的prompt中添加防御措施，时刻提醒不要忘记
  
# 5. 内容审核：Moderation API
可以调用Openai的Moderation API，对用户输入的文本进行审核，检查是否包含危险的内容。

# 6. OpenAI API的几个重要参数
OpenAI提供两类API：
- **Completion API** ： 续写文本
- **Chat API** ： 多轮对话（主流）
```python
def get_chat_completion(prompt, model="deepseek-v4-pro"):
    messages.append({"role": "user", "content": prompt})
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        # 以下为默认值
        temperature=1, # 控制模型的随机性，0~2之间，值越小，模型越确定
        seed=None, # 随机种子，temperature=0时,每次生成相同的结果
        stream=False, # 是否流式输出，False表示直接返回所有内容
        top_p=1, # 随机采样时，只考虑前top_p%的概率分布的token
        n=1, # 一次返回几条结果
        max_tokens=100, # 每条结果最多几个token，超过截断
        presence_penalty=0, # 防止重复输出
        frequency_penalty=0, # 防止输出重复
        logit_bias={}, # 对token的偏置，用于调整模型对不同token的输出概率
    )
    return response.choices[0].message.content
```
