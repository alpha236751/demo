# 第一章 LangChain概述
## 1. 为什么需要LangChain
- 单一大语言模型的局限性
  - 知识受限于训练数据
  - 无法直接与外部交互
  - 不具备状态保持能力(上下文记忆)
- langchain应用场景
  - 构建企业知识库(RAG)
  - Agent的构建
  - 对话系统和聊天机器人
  - 多模态
  - 内容生成
  - 数据连接与处理

## 2. LangChain是什么
lang(language)、chain(chain) 链接大语言模型与其他各种计算资源和数据，构建AI应用
主要模块：
- langchain-core 官方核心API
- langchain-community 第三方集成（open-ai、anthropicic等）
- langgraph Agent框架
- langgraph-classic 向后兼容

## 3. LangChain家族
- langchain 简单智能体应用
- langgraph 复杂工作流编排
- deep agent 智能体执行框架
- langsmith 可视化监控与测试平台

## 4. 大模型应用场景介绍
- RAG
- Agent

智能体(Agent) = LLM + 工具(Tools) + 决策(planing) + 记忆(Memory) + 行动(Action)

1. 纯prompt
2. Agent + function calling
3. RAG
4. fine-tuning微调

# 第二章 模型的创建与调用
## 1. 模型调用的准备工作
### 1.1 模型历史演变
补全模型LLM 和 对话模型 chat model
GPT-3时代：以补全模型为主，采用"成语接龙"式文本补全，运行效果不稳定
GPT-3.5之后：对话模型成为主流，指令跟随能力显著增强

### 1.2 模型初始化方式
- API来源:
    使用模型提供商库：直接调用DeepSeek、智谱等厂商专用API
    **LangChain统一方式**：推荐方案，提供标准化调用接口
- 参数配置:
    **配置文件**：推荐将BASE_URL、API-KEY等参数写入配置文件
    硬编码：直接写在代码文件中
- 部署位置:
    在线部署：调用云端大模型服务
    本地部署：运行本地化模型如Ollama

### 1.3 线上大模型服务平台
OpenRouter：全球主流平台，含国外模型
CloseAI：亚洲最大平台，含国外模型
阿里云百炼：企业端友好
硅基流动：性价比高，适合个人学习
百度千帆：主打百度生态
火山引擎：主打字节多模态生态


## 2. 模型初始化-模型供应商
### 2.1 专用API调用
```python
import os

from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek

load_dotenv(override=True)
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

model = ChatDeepSeek(
    model="deepseek-v4-flash", api_key=DEEPSEEK_API_KEY, api_base=DEEPSEEK_BASE_URL
)

response = model.invoke("你好")
print(response.content)
```

### 2.2 兼容用法 Openai API
```python
import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI


load_dotenv(override=True)
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

model = ChatOpenAI(
    model="deepseek-v4-flash", api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL
)

response = model.invoke("你好")
print(response.content)
```

### 2.3 中转平台
1. OpenRouter
```python
import os

from dotenv import load_dotenv
from langchain_openrouter import ChatOpenRouter


load_dotenv(override=True)
# 'https://openrouter.ai/api/v1'
OPENROUTER_API_BASE = os.getenv("OPENROUTER_API_BASE")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenRouter(
    model="deepseek/deepseek-v4-flash", api_key=OPENROUTER_API_KEY, base_url=OPENROUTER_API_BASE
)

response = model.invoke("你好")
print(response.content)
```
2. CloseAI
`from langchain_openai import ChatOpenAI`
只能用OpenAI协议调用

## 3. 模型初始化-init_chat_model
```python
import os

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(override=True)
DEEPSEEK_API_BASE = os.getenv("DEEPSEEK_API_BASE")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

model = init_chat_model(
    model="deepseek-v4-flash", # 模型名称
    model_provider="deepseek", # 模型供应商
    # model="deepseek:deepseek-v4-flash",
    api_key=DEEPSEEK_API_KEY, # API-KEY
    base_url=DEEPSEEK_API_BASE, # 请求地址
    temperature=0.7, # 随机性参数 0.0~2.0
    max_tokens=1024, # 最大输出token数
    timeout=60, # 超时时间 单位秒
    max_retries=3, # 最大重试次数
)

response = model.invoke("你好")
print(response.content)
```

## 4. 模型初始化-本地模型
Ollama 和 vLLM
1. 下载Ollama
https://ollama.com
2. 安装Ollama
```shell
OllamaSetup.exe /DIR=指定目录
```
3. 模型下载
设置下载目录
在官网找到模型安装命令
```shell
ollama run 模型名称
```
此命令也作为日常直接调用模型的命令`\bye`关闭
4. 调用模型
```python
from langchain_ollama import ChatOllama

model = ChatOllama(
  model="模型名称",
  base_url="http://localhost:11434", # 默认端口号11434
  )
  
print(model.invoke("你好"))
```
```python
from langchain.chat_models import init_chat_model

model = init_chat_model(
    model="模型名称",
    model_provider="ollama", # 模型供应商
    base_url="http://localhost:11434", # 默认端口号11434
    )
print(model.invoke("你好"))
```

## 5. 模型调用
- invoke 阻塞式，一次性返回完整结果
- stream 流式输出，实时返回每个token
- batch 批量调用，批量处理多个输入

### 5.1 invoke

#### 5.1.1 输入参数
- 文本输入
 `model.invoke("你好")`

- 字典列表
  ```python
  conversation = [
    {"role": "user", "content": "你是小明"}
  ]
  response = model.invoke(conversation)
  print(response.content)

  conversation.append({"role": "assistant", "content": response.content})
  conversation.append({"role": "user", "content": "你是谁"})

  response = model.invoke(conversation)
  print(response.content)
  ```

- 消息对象列表
  ```python
  import os

  from dotenv import load_dotenv
  from langchain.chat_models import init_chat_model
  from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

  load_dotenv(override=True)
  DEEPSEEK_API_BASE = os.getenv("DEEPSEEK_API_BASE")
  DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

  model = init_chat_model(
      # model="deepseek-v4-flash",
      # model_provider="deepseek",
      model="deepseek:deepseek-v4-flash",
      api_key=DEEPSEEK_API_KEY,
      base_url=DEEPSEEK_API_BASE,
  )

  messages = [
      SystemMessage(content="你是一名数学老师"),
      HumanMessage(content="请计算2的平方"),
  ]
  response = model.invoke(messages)
  print(response.content)

  messages.append(AIMessage(content=response.content))
  messages.append(HumanMessage(content="那3呢"))
  response = model.invoke(messages)
  print(response.content)

  print(messages)
  ```

#### 5.1.2 返回值
```python
AIMessage(
    # 核心内容
    content='2的平方等于4。',
    additional_kwargs={
        # 拒绝回答原因
        'refusal': None, 
        # 推理内容
        'reasoning_content': '我们被问到："请计算2的平方"。这是一个非常简单的计算。2的平方就是2乘以2，等于4。所以答案是4。'
    },
    # 响应元数据
    response_metadata={
        'token_usage': {
            'completion_tokens': 37, # 生成回答消耗的token数
            'prompt_tokens': 9, # 输入消耗的token数
            'total_tokens': 46, # 总token数
            # 生成回答token细节
            'completion_tokens_details': {
              # 预测性token数
              'accepted_prediction_tokens': None, 
              # 音频token数
              'audio_tokens': None, 
              # 推理token数
              'reasoning_tokens': 30, 
              # 拒绝token数
              'rejected_prediction_tokens': None
              },
            # 输入token细节
            'prompt_tokens_details': {
              # 音频token数
              'audio_tokens': None, 
              # 从缓存中读取的token数
              'cached_tokens': 0
              },
            # 从缓存中读取的token数
            'prompt_cache_hit_tokens': 0,
            # 未从缓存中读取的token数
            'prompt_cache_miss_tokens': 9
        },
        'model_provider': 'deepseek',
        'model_name': 'deepseek-v4-flash',
        # 系统指纹
        'system_fingerprint': 'fp_8b330d02d0_prod0820_fp8_kvcache_20260402',
        # 响应ID
        'id': '6405e05f-1b1e-4a3b-83e5-ceffb48000b9',
        # 响应结束原因
        'finish_reason': 'stop',
        # 对数概率
        'logprobs': None
    },
    # 内部标识
    id='lc_run--019f2b61-5da0-75e3-9267-d650c01d3c8d-0',
    # 工具调用信息
    tool_calls=[],
    invalid_tool_calls=[],
    # token使用情况
    usage_metadata={
        'input_tokens': 9, # 输入token数
        'output_tokens': 37, # 输出token数
        'total_tokens': 46, # 总token数
        'input_token_details': {'cache_read': 0}, # 从缓存中读取的token数
        'output_token_details': {'reasoning': 30} # 推理token数
    }
) 
```

### 5.2 stream
返回迭代器
```python
for chunk in model.stream(messages):
    # 强制刷新缓冲区
    print(chunk.text, end="", flush=True)
```

### 5.3 batch

```python
messages = [
    "你好，你是谁",
    "计算2的平方",
    "中国首都是哪里"
]

# responses = model.batch(messages) # 按输入顺序返回 列表 [AIMessage, AIMessage, AIMessage]
responses = model.batch_as_completed(messages) # 按完成顺序返回 生成器 (索引, AIMessage)
for response in responses:
    print(response.content)
```

### 5.4 异步调用
ainvoke、astream、abatch 返回协程对象
```python
import asyncio
import os
from time import time

from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv(override=True)
DEEPSEEK_API_BASE = os.getenv("DEEPSEEK_API_BASE")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

model = init_chat_model(
    # model="deepseek-v4-flash",
    # model_provider="deepseek",
    model="deepseek:deepseek-v4-flash",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_API_BASE,
)


async def async_invoke():
    async_task = asyncio.create_task(model.ainvoke("你好"))

    for i in range(3):
        await asyncio.sleep(1)

    response = await async_task
    print(response.content)


start_time = time()
asyncio.run(async_invoke())
print(time() - start_time)
```

## 6. 拓展 
### 6.1 美化输出
1. pretty_print() 内置函数
2. rich 库 
`from rich import print as rich_print`

### 6.2 模型配置信息profile
print(model.profile) 不一定有

### 6.3 模型初始化参数
1. 查看所有参数
```python
from langchain_deepseek import ChatDeepseek
from langchain.chat_models import init_chat_model

print(ChatDeepseek.model_fields.keys())

model = init_chat_model()

print(model.model_fields.keys())
```

2. model_kwargs参数 模型本身支持 但Langchain没有直接列出
```python
model = init_chat_model(
    model = "deepseek:deepseek-v4-flash",
    model_kwargs={}
     )
```

3. extra_body参数 模型厂商 基于 OpenAI API 扩展的参数
```python
model = init_chat_model(
    model = "deepseek:deepseek-v4-flash",
    extra_body={"thinking": {"type": "enabled"}}
     )
```

4. 模型调用中的config参数
  允许在模型调用时动态配置和控制模型的行为
```python
model.invoke("你好", config={
  "run_name" = ""
  "tags" = []
  "callbacks" = []
  "metadata" = {} # 元数据
  "max_concurrency" = 5 # 最大并发数
  "recursion_limit" = int # 递归限制
  "configurable" = {} # 覆盖初始化模型参数
})
```

# 第三章 LangSmith
## 1. LangSmith 概述
### 1.1 什么是LangSmith
LangSmith是Langchain生态系统中专门用于LLM应用**调试**、**监控**、**评估**和**管理**的平台

# 第四章 消息与提示词模板
## 1. 认识消息
### 1.1 消息内部结构
role、content、metadata

### 1.2 消息类型
- 系统消息
- 用户消息
- 助手消息
- 工具调用消息

### 1.3 消息格式
- JSON格式
- 对象格式

### 1.4 消息对象字段说明
- SystemMessage
  - content
- HumanMessage
  - content
  - metadata
- AIMessage
  - content
  - response_metadata # 响应元数据
  - tool_calls # 工具调用信息
  - usage_metadata # 用量信息
- ToolMessage
  - content
  - name # 工具名称
  - tool_call_id # 工具调用ID

### 1.5 对话历史优化
保留系统消息和最近N轮的对话消息

### 1.6 content 和 content_blocks
- content 
  - 文本内容
  - 字典列表 保存多模态的数据
- content_blocks
  - 输入格式化 因为各大模型厂商对多模态输入API格式不同
    - 一个字典列表
    - 每个block包含type、用于区分内容类型
    - 支持text、image、video、audio、tool_call 以及 reasoning思维链
  - 输出格式化 不同模型输出格式可能不同
    - `print(response.content_blocks)`
  
## 2. 提示词模板
### 2.1 为什么推荐提示词模板
- 字符串拼接 简单易上手 但可读性差 不宜维护 难以支持复杂场景
- 提示词模板 结构清晰 易维护 可复用 

### 2.2 ChatPromptTemplate
#### 2.2.1 实例化方式
```python
from langchain_core.prompts import ChatPromptTemplate

# 或者去掉from_messages
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个AI助手，你的名字叫{name}"),
        ("human", "你好，最近怎么样"),
        ("ai", "我很好"),
        ("human", "{input}"),
    ]
)

result = chat_prompt_template.invoke({"name": "小智", "input": "1+1等于几"})
print(result)
```

#### 2.2.2 三种调用方式
```python
# invoke 返回ChatPromptValue对象
result = chat_prompt_template.invoke({"name": "小智", "input": "1+1等于几"})
# format 返回字符串
result = chat_prompt_template.format(name="小智", input="1+1等于几")
# format_messages 返回消息列表
result = chat_prompt_template.format_messages(name="小智", input="1+1等于几")
print(result)
```

#### 2.2.3 初始化参数类型
- 元组列表 `("human", "你好，最近怎么样")`
- 字符串列表 默认是用户消息
- 字典列表 `{"role": "human", "content": "你好，最近怎么样"}`
- **消息对象列表 不能声明变量**
- BaseMessagePromptTemplate
- BaseChatPromptTemplate 嵌套

### 2.3 高级特性
#### 2.3.1 部分变量预填充
```python
updated_template = chat_prompt_template.partial(name="小智")
result = updated_template.invoke({"input": "1+1等于几"})
```

#### 2.3.2 消息占位符
**placeholder** 处理简单数据类型
```python
chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个AI助手"),
        ("placeholder", "{conversation}"),
    ]
)

result = chat_prompt_template.invoke({
    "conversation": [
        ("user", "你好"),
        ("assistant", "你好，最近怎么样"),
        ("user", "我很好"),
    ]
})
``` 
**MessagesPlaceholder** 专门处理消息对象列表
```python
from langchain_core.prompts import MessagesPlaceholder

chat_prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个AI助手"),
        MessagesPlaceholder(variable_name="conversation"),
    ]
)

result = chat_prompt_template.invoke({
    "conversation": [
        HumanMessage(content="你好"),
        ("assistant", "你好，最近怎么样"),
        ("user", "我很好"),
    ]
})
```

#### 2.3.3 可复用模板库
```python
from langchain_core.prompts import ChatPromptTemplate

class PromptTemplateLibrary:
  TRANSLATOR = ChatPromptTemplate.from_messages([
    ("system", "你是一个翻译助手"),
    ("human", "翻译以下内容：\n{text}"),
  ])

messages = PromptTemplateLibrary.TRANSLATOR.format_messages(text="你好")
```

#### 2.3.4 模板组合
- 字符串组合 +
- 模板组合 +

#### 2.3.5 few-shot
```python
import os

from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate, FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI
from rich import print as rich_print

load_dotenv()
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_API_BASE = os.getenv("DEEPSEEK_API_BASE")


model = ChatOpenAI(
    model="deepseek-v4-flash",
    api_key=DEEPSEEK_API_KEY,
    base_url=DEEPSEEK_API_BASE,
)

# 示例数据 字典列表
examples = [{"word": "开心", "antonym": "难过"}, {"word": "高", "antonym": "矮"}]
# 示例提示词
example_prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{word}"),
        ("ai", "{antonym}"),
    ]
)

# fewshot模板
fewshot_template = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)
# 最终的提示词模板
prompt_template = ChatPromptTemplate.from_messages(
    [
        fewshot_template,
        ("human", "{word}"),
    ]
)
# 提示词
prompt = prompt_template.format(word="富有")

result = model.invoke(prompt)
rich_print(result)
```

# 第五章 工具使用
## 1. tools概述
### 1.1 工具调用方式function calling
1. 直接调用
```python
from langchain_core.tools import tool

@tool
def translate(text: str) -> str:
    """Translate the given text to a different language"""
    return text

translate.invoke("你好")
```
2. 基于模型调用
```python
from langchain_core.tools import tool
from langchain_deepseek import ChatDeepSeek

model = ChatDeepSeek(
    model="deepseek-v4-flash",
)


@tool
def get_current_weather(location: str) -> str:
    """Get the current weather in a given location"""
    return f"The current weather in {location} is sunny with a temperature of 25 degrees Celsius"


# 绑定工具
model_with_tools = model.bind_tools(
    [get_current_weather],
    tool_choice="auto", # none不带用工具 auto自动调用工具 required至少调用一个工具 直接指定工具名称强制调用该工具
       )
# 返回ToolMessage对象
response = model_with_tools.invoke("北京天气怎么样")

if response.tool_calls:
    print(response.tool_calls)
else:
    print(response.content)
```

## 2. 工具定义方式
### 2.1 不使用@tool装饰器
1. 模型绑定工具
```python
def get_current_weather(location: str) -> str:
    """Get the current weather in a given location"""
    return f"The current weather in {location} is sunny with a temperature of 25 degrees Celsius"

model_with_tools = model.bind_tools([get_current_weather])
```

2. 工具描述
注意换行不能省略
- 功能描述
- 参数描述
- 返回值描述
```python
def get_current_weather(location: str) -> str:
    """
    Get the current weather in a given location

    Args:
        location: The location to get the weather for

    Returns:
        A string describing the current weather in the location
    """
    return f"The current weather in {location} is sunny with a temperature of 25 degrees Celsius"
```
### 2.2 使用@tool装饰器
```python
# docstring描述 严格按照谷歌风格格式
@tool(parse_docstring=True)
def get_current_weather(location: str) -> str:
    """
    Get the current weather in a given location

    Args:
        location: The location to get the weather for

    Returns:
        A string describing the current weather in the location
    """
    return f"The current weather in {location} is sunny with a temperature of 25 degrees Celsius"
```

### 2.3 自定义args_schema
#### 2.3.1 pydantic模型
```python
class WeatherInput(BaseModel):
    location: str = Field(
        description="city name",
        default="北京",
    )
    unit: Literal["celsius", "fahrenheit"]


@tool(
    args_schema=WeatherInput, description="Get the current weather in a given location"
)
def get_current_weather(location, unit="celsius"):

    return f"The current weather in {location} is sunny with a temperature of 25 degrees {unit}"
```

#### 2.3.2 JsonSchema
```python
json_schema = {'properties': {'location': {'default': '北京',
     'description': 'city name',
     'type': 'string'},
    'unit': {'enum': ['celsius', 'fahrenheit'], 'type': 'string'}},
   'required': ['unit'],
   'type': 'object'}


@tool(
    args_schema=json_schema, description="Get the current weather in a given location"
)
def get_current_weather(location, unit="celsius"):

    return f"The current weather in {location} is sunny with a temperature of 25 degrees {unit}"
```

### 2.4 多工具调用
```python
from rich import print as rprint

# 绑定工具
tools = [get_stock_price, search_news]
model_with_tools = model.bind_tools(tools)

message_list = []
human_message = HumanMessage(content="Google今天的股价是多少？最近有什么新闻？")
# human_message = HumanMessage(content="比较一下微软和苹果的股价")
# human_message = HumanMessage(content="腾讯最近有什么重大新闻？")
# human_message = HumanMessage(content="海水为什么是咸的？")
message_list.append(human_message)


while True:
    response = model_with_tools.invoke(message_list)
    # rprint(response)
    # break

    message_list.append(response)

    if not response.tool_calls:
        print("不需要调用工具")
        break

    for tool_call in response.tool_calls:
        if tool_call["name"] == "get_stock_price":
            stock_result = get_stock_price.invoke(tool_call)
            print(stock_result)
            message_list.append(stock_result)
        elif tool_call["name"] == "search_news":
            news_result = search_news.invoke(tool_call)
            print(news_result)
            message_list.append(news_result)

for msg in message_list:
    rprint(msg)
```

## 3. 实践经验
1. 清晰的描述
   docstring
   自定义args_schema

2. 功能单一
   一个工具只负责一个功能

3. 如何处理工具失败
   工具内部处理
   agent级重试 使用prompt
   调用级重试 @retry 执行报错retry自动拦截 重新触发

4. 返回字符串
   避免LLM胡思乱想 采用其他编码格式

5. 同步 和 异步
   同步 CPU密集型
   异步 IO密集型

# 第六章 结构化输出 Structured Output
## 1. 结构化输出概述
### 1.1 什么是结构化输出
结构化输出是指将模型的输出转换为结构化的数据格式，例如JSON、Pydantic、TypedDict等。
更容易处理
结果更稳定
适合工程化 类型安全

## 2. 四种模式
### 2.1 Pydantic


# 第十章 RAG
## 1. Retrieval
### 1.1 大模型局限
- 知识滞后 训练数据有截至日期
- 知识缺失 依赖网络上公开静态数据
- 幻觉 

### 1.2 RAG优缺点
优点：
- 相比提示词工程 有丰富上下文和数据样本 不需要用户提供过多背景描述
- 相比微调 提升回答的时效性 和 可靠性
- 一定程度保护了企业业务数据隐私
缺点：
- 每次回答涉及外部系统数据检索 响应时延较高
- 引用外部知识数据 消耗大量token

### 1.3 工作流程
1. 数据源Source
2. 加载Load
   文档加载器Document Loaders -> Document对象
3. 转换Transform
   文档转换器Document Transformers
4. 嵌入Embed
   文档嵌入模型Text Embedding models
5. 存储Store
6. 检索Retrieve

## 2. 工作流程
### 2.1 文档加载器 Document Loaders
#### 2.1.1 加载txt
```python
from langchain_community.document_loaders import TextLoader

loader = TextLoader(
file_path="../asset/load/01-langchain-utf-8.txt",
encoding="utf-8",
)
docs = loader.load() # 返回文档列表
print(docs[0].page_content)
```

#### 2.1.2 CSV
```python
from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(
    file_path="../asset/load/02-load.csv",
    encoding="utf-8",
)
docs = loader.load() # 返回文档列表
print(docs[0].page_content)
```

#### 2.1.3 JSON
```python
from langchain_community.document_loaders import JSONLoader

# 情况1
loader = JSONLoader(
    file_path="../asset/load/03-load.json",
    jq_schema=".", # 提取所有字段
    text_content=False, # True表示 要求jq提取为字符串 
)

# 情况2
loader = JSONLoader(
    file_path="../asset/load/03-load.json",
    jq_schema=".messages[].content", # 提取messages内的所有content字段
    # text_content=False, # True表示 要求提取到的内容为字符串
)
# 情况3
loader = JSONLoader(
    file_path="../asset/load/03-response.json",
    jq_schema="""
        .data.items[] | {
            author,
            created_at: .created_at,
            content: (.title + "\n" + .content),
        }
        """, # 提取拼接
    text_content=False,
)
```

#### 2.1.4 PDF
1. 方式1 PyPDFLoader
```python
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(
    file_path="../asset/load/04-sample.pdf",
    extraction_mode="plain", # 默认plain 提取文本 layout 感知布局提取
)
docs = loader.load() # 返回文档列表
print(len(docs))
```
2. 方式2 MinerU
MinerU提供了PDF、Word、PPT、图片等文件解析，支持图像提取、OCR、公式、表格解析等功能。
```python
import os
import time
import requests
from dotenv import load_dotenv

# 预先获取MINERU_API_TOKEN，后续请求直接使用token
load_dotenv(override=True)


def upload_files(file_paths: list[str]) -> str:
    """批量上传文件"""
    url = "https://mineru.net/api/v4/file-urls/batch"
    api_token = os.getenv("MINERU_API_TOKEN")
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}",
    }

    files_info = [
        {
            "name": os.path.basename(file_path),
            "is_ocr": True,
            "data_id": f"file_{i}",
        }
        for i, file_path in enumerate(file_paths)
    ]

    data = {
        "enable_formula": True,
        "enable_table": True,
        "language": "ch",
        "files": files_info,
    }

    try:
        response = requests.post(url, headers=header, json=data)
        if response.status_code == 200:
            result = response.json()
            print("response success. result:{}".format(result))

            if result["code"] == 0:
                batch_id = result["data"]["batch_id"]
                urls = result["data"]["file_urls"]
                print("batch_id:{}\nurls:{}".format(batch_id, urls))

                for i in range(0, len(urls)):
                    with open(file_paths[i], "rb") as f:
                        res_upload = requests.put(urls[i], data=f)
                        if res_upload.status_code == 200:
                            print(f"{urls[i]} upload success")
                        else:
                            print(f"{urls[i]} upload failed")
                            return None

                return batch_id
            else:
                print("apply upload url failed, reason:{}".format(result.get("msg")))
                return None
        else:
            print(
                "response not success. status:{} ,result:{}".format(
                    response.status_code, response.text
                )
            )
            return None

    except Exception as err:
        print(err)
        return None


def download_files(batch_id):
    """批量获取任务结果"""
    if not batch_id:
        print("batch_id为空，跳过下载")
        return

    os.makedirs("parsed_files", exist_ok=True)

    url = f"https://mineru.net/api/v4/extract-results/batch/{batch_id}"
    api_token = os.getenv("MINERU_API_TOKEN")
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}",
    }

    failed_files = set()
    done_files = set()

    while True:
        res = requests.get(url, headers=header)
        result_json = res.json()

        if res.status_code != 200 or result_json.get("code") != 0:
            print("get result failed:", result_json)
            break

        extract_results = result_json["data"]["extract_result"]

        for result in extract_results:
            data_id = result["data_id"]

            if result["state"] == "failed":
                failed_files.add(data_id)

            elif result["state"] == "done" and data_id not in done_files:
                done_files.add(data_id)

                full_zip_url = result["full_zip_url"]
                res_download = requests.get(full_zip_url, stream=True)

                with open(
                    f"parsed_files/{result['file_name']}_{result['data_id']}.zip", "wb"
                ) as f:
                    for chunk in res_download.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)

        if len(failed_files) + len(done_files) == len(extract_results):
            break

        time.sleep(5)

    for i in failed_files:
        print("failed:", i)

    for i in done_files:
        print("done:", i)


file_paths = ["../asset/load/04-sample.pdf"]
batch_id = upload_files(file_paths)

if batch_id:
    download_files(batch_id)
```

#### 2.1.5 word(docx)
```python
loader = UnstructuredWordDocumentLoader(
    file_path="asset/load/05-ssg_chat.docx",
    mode="single", # single返回单个文档 elements按标题等元素切分文档
)
```

#### 2.1.6 markdown
```python
loader = UnstructuredMarkdownLoader(
    file_path="asset/load/06-ssg_chat.md",
    mode="single", # single返回单个文档 elements按标题等元素切分文档
    strategy="fast", # 快速解析 hi_res 高分辨率有版面分析
)
```

#### 2.1.7 HTML

#### 2.1.8 File Directory

### 2.2 文档切分器 Text Splitters
#### 2.2.1 Chunking拆分策略
- 根据句子切分
- 按照固定字符数切分
- 固定字符结合重叠窗口
- 递归字符切分
- 根据语义切分  

### 2.3 文档嵌入模型 Text Embedding models
#### 2.3.1 嵌入模型选择和初始化
```python
from langchain.embeddings import init_embeddings
from dotenv import load_dotenv
import os


load_dotenv(override=True)

embedding_model = init_embeddings(
    model="openai:text-embedding-3-large",
    api_key=os.getenv("CLOSEAI_API_KEY"),
    base_url=os.getenv("CLOSEAI_BASE_URL"),
   )
```
#### 2.3.2 嵌入模型调用
```python
# 句子向量化 返回一个向量
embedding_model.embed_query("你好")
# 文档向量化 返回向量列表
embedding_model.embed_documents(["你好", "你好吗"])
```

### 2.4 向量存储Vector Stores
#### 2.4.1 常用向量数据库
- FAISS 
- Chroma
- Milvus
- Redis

## 3 milvus
### 3.1 安装
```bash
docker-compose up -d

pip install pymilvus
```

### 3.2 数据模型
- Database 数据库 隔绝不同业务
- Collection 集合 类似数据库的表
- Partition 分区 collection的子集 一个collection默认至少有一个partition
- Entity 实体 类似数据库的一行数据

### 3.3 基本用法
#### 3.3.1 DDL 数据定义
1. 数据库相关
```python
from pymilvus import MilvusClient

# 创建客户端
client = MilvusClient(
    uri="http://8.217.149.47:19530",
)
# 列出所有数据库
print(client.list_databases())
# 查看指定数据库信息
print(client.describe_database(db_name="test_db"))
# 创建数据库
client.create_database(db_name="test_db")
# 使用数据库
client.use_database(db_name="my_database_2")
# 删除数据库 必须先删除所有collection
client.drop_database(db_name="test_db")
```

2. collection相关
```python
# 列出所有collection
print(client.list_collections())
# 创建collection 需要创建schema 设置index 创建collection
# 创建schema
schema = MilvusClient.create_schema(enable_dynamic_fields=True)
# 添加主字段
schema.add_field(
    field_name="my_id",
    datatype=DataType.INT64, # 只接受Int64或VarChar值
    is_primary=True, # 主字段
    auto_id=False,
)
# 添加向量字段 接受各种稀疏和密集向量嵌入 一个Collections最多添加四个向量字段
# SPARSE_FLOAT_VECTOR 稀疏向量
schema.add_field(
    field_name="my_vector",
    datatype=DataType.FLOAT_VECTOR, 
    dim=5 # 向量嵌入的维数
)
# 添加标量字段 包括VarChar、Boolean、Int、Float 和Double
schema.add_field(
    field_name="my_varchar",
    datatype=DataType.VARCHAR,
    max_length=512
)
# 为向量字段设置索引参数
index_params = client.prepare_index_params()
index_params.add_index(
    field_name="dense_vector", # 字段名
    index_name="dense_vector_index", # 索引名
    index_type="AUTOINDEX", # 索引类型
    metric_type="IP" # 相似度指标 IP CONSIN L2
)
# 创建collection
client.create_collection(
    collection_name="my_collection",
    schema=schema,
    index_params=index_params
)
# 删除collection
client.drop_collection(collection_name="edu_collection1")
```
#### 3.3.2 DML 数据操作
```python
# 查看collection元数据(表结构)
print(client.describe_collection(collection_name="edu_collection1"))
# 向量化
vectors = embedding_model.embed_documents(texts)
data = [
        {"id": 0, "vector": [0.3580376395471989, -0.6023495712049978, 0.18414012509913835, -0.26286205330961354,
                             0.9029438446296592], "color": "pink_8682"},
        {"id": 1, "vector": [0.19886812562848388, 0.06023560599112088, 0.6976963061752597, 0.2614474506242501,
                             0.838729485096104], "color": "red_7025"},
        {"id": 2, "vector": [0.43742130801983836, -0.5597502546264526, 0.6457887650909682, 0.7894058910881185,
                             0.20785793220625592], "color": "orange_6781"},
        {"id": 3, "vector": [0.3172005263489739, 0.9719044792798428, -0.36981146090600725, -0.4860894583077995,
                             0.95791889146345], "color": "pink_9298"},
        {"id": 4, "vector": [0.4452349528804562, -0.8757026943054742, 0.8220779437047674, 0.46406290649483184,
                             0.30337481143159106], "color": "red_4794"},
        {"id": 5, "vector": [0.985825131989184, -0.8144651566660419, 0.6299267002202009, 0.1206906911183383,
                             -0.1446277761879955], "color": "yellow_4222"},
        {"id": 6, "vector": [0.8371977790571115, -0.015764369584852833, -0.31062937026679327, -0.562666951622192,
                             -0.8984947637863987], "color": "red_9392"},
        {"id": 7, "vector": [-0.33445148015177995, -0.2567135004164067, 0.8987539745369246, 0.9402995886420709,
                             0.5378064918413052], "color": "grey_8510"},
        {"id": 8, "vector": [0.39524717779832685, 0.4000257286739164, -0.5890507376891594, -0.8650502298996872,
                             -0.6140360785406336], "color": "white_9381"},
        {"id": 9, "vector": [0.5718280481994695, 0.24070317428066512, -0.3737913482606834, -0.06726932177492717,
                             -0.6980531615588608], "color": "purple_4976"}
    ]
# 插入数据 upsert 找得到主键就更新 找不到就插入

res = client.upsert(
    collection_name="edu_collection1",
    data=data,
)
# {'upsert_count': 10, 'ids': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]}
print(res)
# 手动刷新collection
client.flush(collection_name="edu_collection1")
# 查看collection统计信息
stats = client.get_collection_stats(collection_name="edu_collection1")
print(stats)
```
#### 3.3.3 DQL 数据查询
1. 扫描数据
```python
from rich import print as rich_print
iterator = client.query_iterator(
    collection_name="edu_collection1",
    filter="", # where
    output_fields=["*"], # select
)
# 返回一个只能被遍历一次的迭代器？
while True:
    item = iterator.next()
    if not item:
        break
    rich_print(item)
```
2. 通过主键查询
```python
res = client.get(
    collection_name="edu_collection1",
    ids=[0, 1, 2],
)
for i in res:
    print(i)
```
3. 相似度查询
- 单向量查询
- 批向量查询
- 分区查询 partition_names=["partitionA"] 
- 使用输出字段查询 search_params={"metric_type": "IP", "params": {}}
- 过滤查询 filter='color like "red%"'
- 范围查询 search_params=search_params,
```json
search_params = {
        "metric_type": "IP",
        "params": {
            "radius": 0.8,  # 搜索圆的半径
            "range_filter": 1  # 范围过滤器，用于过滤出不在搜索圆内的向量。
        }
    }
```
```python
result = client.search(
    collection_name="edu_collection1",
    data=[[0.19886812562848388, 0.06023560599112088, 0.6976963061752597, 0.2614474506242501, 0.838729485096104]],
    limit=2, # 返回2条
    output_fields=["*"], # 返回所有字段
) # 返回一个二维列表，每行是一个向量的搜索结果
for i in result[0]:
    print(i)
```

#### 3.3.4 混合检索
要对两组 ANN(Approximate Nearest Neighbor Search,近似最近邻搜索) 搜索结果进行合并和重新排序，
有必要选择适当的重新排序策略。支持两种重排策略：加权排名策略（WeightedRanker）和倒数排序融合（RRFRanker）。
在选择重排策略时，需要考虑的一个问题是，在向量场中是否需要强调一个或多个基本 ANN 搜索。

### 3.4 向量索引
















