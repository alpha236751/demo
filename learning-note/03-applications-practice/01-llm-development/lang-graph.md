# 1. LangGraph总览
## 1.1 LangGraph和LangChain的区别
LangChain 围绕Agent 提供模型 工具 消息 结构化输出 和 记忆管理
LangGraph 适合复杂工作流，提供持久化、流式输出、Durable Execution、Hitl等，更为底层的编排框架

## 1.2 图的基本要素
State、Node、Edge

## 1.3 图运行过程
Superstep 路由->执行->提交

Checkpoint 

## 1.4 Graph API 和 Functional API
1. Graph API
    显式定义三要素 
    适合图，多分支结构
2. Functional API
    @entrypoint定义工作流入口
    @task定义可被检查点记录的内容
    适合线性

# 2. 图的基础构建和运行
1. 定义全局状态
2. 创建状态图
3. 定义图结构

## 2.1 全局状态
全局状态是 LangGraph 运行图每个节点都可以访问的公共对象。
```py
class OverAllState(TypedDict):
    logs: Annotated[list[str], add]
    cur_id: str
```

## 2.2 状态图
```py
builder = StateGraph(state_schema=OverAllState)
```

## 2.3 图结构
```py
# 定义图节点
def node_1(state: OverAllState) -> OverAllState:
    pre_id = state["cur_id"]
    return {
        "logs": ["node_1 运行完毕"],
        "cur_id": pre_id + ", node_1"
    }

def node_2(state: OverAllState) -> OverAllState:
    pre_id = state["cur_id"]
    return {
        "logs": ["node_2 运行完毕"],
        "cur_id": pre_id + ", node_2"
    }

# 添加节点到状态图
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)

# 添加边到状态图
builder.add_edge(START, "node_1")
builder.add_edge("node_1", "node_2")
builder.add_edge("node_2", END)
```

## 2.4 编译和调用
```py
graph = builder.compile()

print(graph.invoke({"cur_id": "start"}))
```

## 2.5 图的可视化

# 3. 图的状态(State)
## 3.1 定义
官方推荐了三种定义Schema的方式：TypedDict、dataclass、Pydantic

1. TypedDict
字典
```py
from typing import TypedDict, Annotated

class OverAllState(TypedDict):
    logs: Annotated[list[str], add]
    cur_id: str
```

2. dataclass
属性调用方式由`['字段名']`变为`.`字段名。
```py
from dataclasses import dataclass
from typing import Annotated

@dataclass
class OverAllState:
    logs: Annotated[list[str], add]
    cur_id: str
```

3. Pydantic
Pydantic模型的字段访问方式和dataclass相同。
```py
from pydantic import BaseModel
from typing import Annotated

class OverAllState(BaseModel):
    logs: Annotated[list[str], add]
    cur_id: str
```

## 3.2 State Reducer
State Reducer 是 LangGraph 中用于合并状态更新的核心机制。
在 LangGraph 的 StateGraph 中，每个节点可以读取和写入共享状态，而 Reducer 定义了如何将多个节点对同一状态键的更新合并

Reducer 本质上是一个二元合并函数，用于定义当同一个字段产生多个更新值时，LangGraph 应该如何将这些值合并为一个最终结果。

函数签名：(Value, Value) -> Value

```py
def my_reducer(left: list[str], right: list[str]) -> list[str]:
    return left + right

left = ['a', 'b']
right = ['c']
print(my_reducer(left, right))
```

Reducer 通常通过 Python 的 typing.Annotated 与状态字段进行关联。

常用内置Reducer
1. operator.add
operator.add 是 Python 内置的加法操作函数，底层由 C 实现

它接收两个参数，等价于 a（第一个参数）+b（第二个参数）

2. langgraph.graph.message.add_messages
add_messages 是 LangGraph 中专用于合并消息列表的 Reducer 函数，常用于维护对话历史类的状态字段。

add_messages 的作用可以概括为：
在保留历史消息的基础上追加新消息，并允许通过相同的消息 id 覆盖已有消息。

3. 默认行为
如果某个 State 字段没有显式定义 Reducer，
LangGraph 会使用默认的状态更新行为：
后一次更新值会覆盖该字段原有的状态值。

## 3.3 节点中访问State

节点函数的第一个参数通常是当前运行图的状态对象，也就是 State

state 表示当前节点执行时可以访问到的全局状态快照。
节点可以通过读取 state 中的字段获取上游节点写入的数据，并基于这些数据完成当前节点的业务逻辑。

### State更新
节点函数通常不需要返回更新后的完整状态，只需要返回本节点对状态的局部更新。

对于节点没有返回的字段，LangGraph 会保留其原有状态值；

对于节点返回的字段，LangGraph 会根据该字段是否配置了 Reducer 来决定如何合并更新值。

如果字段配置了 Reducer，则使用对应的 Reducer 函数将旧值和新值合并；
如果字段没有配置 Reducer，则按照默认规则使用节点返回的新值覆盖原值。

### Overwrite绕过Reducer
在某些场景下，我们可能并不希望继续执行 Reducer 的聚合逻辑，而是希望本次更新直接覆盖旧值。这时可以使用 Overwrite。

Overwrite 的作用是：告诉 LangGraph 本次状态更新不走该字段原本定义的 Reducer，而是直接用新值覆盖状态中的旧值。

需要注意的是，Overwrite 只影响当前这一次更新，并不会修改状态字段本身的 Reducer 定义。后续节点如果继续正常返回该字段的更新值，仍然会按照原来的 Reducer 逻辑进行合并。
```py
from langgraph.types import Overwrite

def node_b(state: OverAllState):
    return {
        "logs": Overwrite(["node_b"]),
        "id": "node_b"
    }
```

## 3.4 Multi Schema
### 3.4.1 状态类型
LangGraph 支持在一个图中使用多个状态 Schema，用于区分图的外部输入、外部输出、内部共享状态以及节点间的临时状态。

- 全局状态 / 内部状态：
  图内部主要使用的状态，创建 StateGraph 时传递给 state_schema 参数。
  它通常包含图运行过程中需要读写的大部分字段。
- 输入状态：
  图对外接收输入时使用的状态，创建 StateGraph 时传递给 input_schema 参数。
  它用于约束调用图时允许传入哪些字段。
- 输出状态：
  图最终对外返回结果时使用的状态，创建 StateGraph 时传递给 output_schema 参数。
  它用于约束图运行结束后只返回哪些字段。
- 私有状态：
  图内部节点之间传递的临时状态，通常不作为图的输入，也不作为图的最终输出。
  它可以通过节点函数的入参类型注解声明，并在节点返回值中写入。

> 需要注意，输入状态和输出状态主要面向图的边界，即“图如何接收外部输入”和“图如何返回外部结果”；
> 而全局状态和私有状态主要面向图内部节点之间的数据传递。

### 3.4.2 状态之间的关系
1. 输入状态和输出状态通常应是全局状态的子集 输入状态描述图对外需要接收的数据，输出状态描述图最终需要返回的数据。通常情况下，它们都应该是全局状态的一部分。
```py
class InputState(TypedDict):
    username: str

class OutputState(TypedDict):
    graph_output: str

class OverAllState(TypedDict):
    username: str
    nickname: str
    graph_output: str
```
2. 私有状态和全局状态应尽量避免字段重名 私有状态的定位是图内部某些节点之间传递的临时字段。如果私有状态字段和全局状态字段重名，虽然某些情况下程序仍然可以运行，但容易让人误以为该字段是全局共享字段，从而造成理解混乱。 因此，推荐让私有状态字段和全局状态字段保持清晰边界。
3. 节点函数应明确声明入参状态类型和返回状态类型 节点函数的第一个参数通常是当前节点可读取的状态。通过类型注解声明该参数，可以明确表达该节点需要读取哪些字段。 同时，给节点函数声明返回状态类型，也可以帮助阅读者理解该节点会更新哪些字段。
```py
def node_1(state: InputState) -> OverAllState:
    return {
        "nickname": "Dear " + state["username"]
    }
```
4. 节点函数中不应该访问入参状态类型中不存在的字段 节点实际接收到的状态会按照其入参类型进行裁剪。
如果在该函数中访问：`state["nickname"]`, nickname 不属于 InputState，运行时就可能抛出 KeyError。
```py
def node_1(state: InputState) -> OverAllState:
    return {
        "nickname": state["username"]
    }
```
5. 节点函数返回的字典应尽量和返回类型注解保持一致 从 Python 类型注解的角度看，函数返回类型只是静态提示，运行时不会自动强制校验。 从 LangGraph 的运行机制看，节点返回的是对状态的部分更新，不是完整状态。只要返回字段已经被图记录为可用状态字段，LangGraph 就可以将其作为状态更新处理。 不过，从工程规范上讲，节点返回字典中的字段最好和函数返回类型注解保持一致，这样更利于阅读、调试和维护。

案例：
```py
from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class InputState(TypedDict):
    username: str

class OutputState(TypedDict):
    graph_output: str

class OverAllState(TypedDict):
    nickname: str
    username: str
    graph_output: str

class PrivateState(TypedDict):
    greeting: str

def node_1(state: InputState) -> OverAllState:
    # 向全局状态写入数据
    return {
        "nickname": "Dear " + state["username"]
    }

def node_2(state: OverAllState) -> PrivateState:
    # 从全局状态读取数据，写入私有状态
    return {
        "greeting": state["nickname"] + ", 早上好~"
    }

def node_3(state: PrivateState) -> OutputState:
    # 从私有状态读取数据，写入输出状态
    return {
        "graph_output": state["greeting"] + " 很高兴认识你！"
    }

builder = StateGraph(OverAllState,input_schema=InputState,output_schema=OutputState)
builder.add_node("node_1", node_1)
builder.add_node("node_2", node_2)
builder.add_node("node_3", node_3)
builder.add_edge(START, "node_1")
builder.add_edge("node_1", "node_2")
builder.add_edge("node_2", "node_3")
builder.add_edge("node_3", END)

graph = builder.compile()
print(graph.invoke({"username":"小黄"}))
```

## 3.5 预定义状态
### 3.5.1 MessagesState
LangGraph 构建的计算图通常会和 LLM 结合使用，而 LLM 在运行过程中通常需要维护一组消息列表。为了提升开发效率，LangGraph 官方提供了一个预定义状态类型：
langgraph.graph.message.MessagesState。

```py
# 源码
class MessagesState(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
# 使用时继承
class OverAllState(MessagesState):
    username: str
    output: str
```

### 3.5.2 AgentState
AgentState 是 LangChain Agent 内部使用的状态类型。
由于 LangChain Agent 底层也是基于 LangGraph 运行图构建的，
所以从技术上讲，开发者也可以将 AgentState 或其子类作为自定义 LangGraph 的状态类型。

该状态中主要包含三个字段。
```py
# messages 用于存储 Agent 运行过程中的消息列表。
messages: Required[Annotated[list[AnyMessage], add_messages]]
# jump_to 是 LangChain Agent 内部使用的控制字段，主要服务于 Agent 中间件体系。
jump_to: NotRequired[Annotated[JumpTo | None, EphemeralValue, PrivateStateAttr]]
# structured_response 用于存储 Agent 最终生成的结构化输出。
structured_response: NotRequired[Annotated[ResponseT, OmitFromInput]]
```
总体来看，AgentState 是专门为 LangChain Agent 运行时设计的状态类型。

因此，在普通自定义 LangGraph 项目中，一般不建议直接基于 AgentState 扩展图状态。

