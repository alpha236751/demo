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

## 3. 模型初始化 init_chat_model
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

## 5.2 stream
返回迭代器
```python
for chunk in model.stream(messages):
    # 强制刷新缓冲区
    print(chunk.text, end="", flush=True)
```

## 5.3 batch

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

## 5.4 异步调用
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
#### 2.2.1 两种实例化方式
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










