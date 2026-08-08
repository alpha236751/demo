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

# 4. 控制流
## 4.1 顺序结构
1. add_edge
    add_edge 用于在两个节点之间添加一条有向边。边是图结构中最基本的元素之一，节点之间的执行顺序、分支跳转以及循环控制，最终都依赖节点和边共同表达。
    ```py
    builder = StateGraph(state_schema=OverAllState)
    builder.add_node("node_a", node_a)
    builder.add_node("node_b", node_b)
    builder.add_edge(START, "node_a")
    builder.add_edge("node_a", "node_b")
    builder.add_edge("node_b", END)
    ```
2. add_sequence
    add_sequence 支持传入一个可执行对象列表。LangGraph 会按照列表顺序依次添加节点，并在相邻节点之间自动添加边。默认情况下，函数名会被用作节点名称。
    ```py
    builder = StateGraph(state_schema=OverAllState)
    builder.add_edge(START, "node_a")
    builder.add_sequence([node_a, node_b])
    builder.add_edge("node_b", END)
    ```

3. 省略指向 END 的边
    从运行机制上看，LangGraph 会在每个 SuperStep 开始时，根据当前发生更新的 Channel 以及节点之间的触发关系，计算本轮需要执行的任务列表。如果没有新的节点被激活，也就没有新的任务需要执行，图运行自然结束。

    显式添加 END 边可以让图结构更加完整，也能更清晰地表达“流程到此结束”的语义。尤其是在分支、条件跳转、循环退出等场景中，显式指向 END 通常更利于阅读和维护。

## 4.2 分支结构
1. 静态分支 Static Branch
    节点的下游候选节点 在图编译阶段就完全确定，只是运行时根据条件选择哪条边执行。
    - 并行节点
        ```py
        builder = StateGraph(state_schema=OverAllState)
        builder.add_node("node_a", node_a)
        builder.add_node("node_b", node_b)
        builder.add_edge(START, "node_a")
        builder.add_edge(START, "node_b")

        builder.add_edge("node_a", END)
        builder.add_edge("node_b", END)
        ```
        上述案例中，node_a 和 node_b 都由 START 触发。图运行时，二者会在同一个超步中被调度，它们各自读取当前状态并独立执行。
    - 条件分支
        ```py
        def add_conditional_edges(
            self,
            source: str, # 条件分支的起始节点
            # 路由规则，是一个可执行对象，通常是函数
            path: Callable[..., Hashable | Sequence[Hashable]] 
            | Callable[..., Awaitable[Hashable | Sequence[Hashable]]]
            | Runnable[Any, Hashable | Sequence[Hashable]],
            # 路由规则的返回值到真实节点名之间的映射关系。 可以省略
            path_map: dict[Hashable, str] | list[str] | None = None,
        ) -> Self:
        ```
        > add_conditional_edges 也支持一次路由到多个下游节点。
    - defer node execution
        某些情况下，我们希望在所有常规任务节点执行完毕后，再进行日志、审计等收尾工作
        此时可以在添加节点时设置defer=True，如下：
        ```py
        builder.add_node("audit_node", audit_node, defer=True)
        ```
        当前节点不会在其被触发后立即执行，而是被延迟到常规图运行流程结束后，再在额外的超步中触发执行。
        常规流程结束后：调用finish()唤醒延迟节点
2. 动态分支 Dynamic Branch
    节点的后续执行路径在 运行时 才确定，可以根据当前状态、输入数据或中间结果，动态决定要触发哪些下游任务或跳转到哪个下游节点。
    Send（分发到哪个下游节点, 给这个下游节点传入什么私有状态）
    Command(goto=...)（运行时跳转到下游节点）
    - 并行节点 扇出（Fan-out）
        Send 结合 add_conditional_edges() 使用，可以用于动态扇出任务
        路由函数可以返回一个 Send 实例序列。每个 Send 实例都描述了一次独立的任务分发：

        如果多个并行任务写入同一个状态字段，通常需要为该字段定义 reducer，用于合并多个任务的输出。本例中三个任务分别写入 poem、ci_poem、joke 三个不同字段，因此不会发生同一字段的并发合并问题。
    - 条件分支
        Command 是 LangGraph 中用于控制图执行的多功能原语，它的构造器可以接受四个参数，并记录在同名类属性中：
        update：更新图状态，效果等同于节点直接返回状态更新字典；
        goto：指定节点执行完成后的跳转目标，可用于运行时条件分支。当需要同时更新状态并控制跳转时，比单独使用条件边更合适；
        graph：存在子图时，用于指定跳转发生在哪一层图中，例如从子图跳转到父图；
        resume：用于恢复被中断的图执行，常见于 human-in-the-loop 场景。

        需要注意的是，如果某个节点使用 Command(goto=...) 控制后续跳转，一般不要再给这个节点额外添加普通下游边。否则，普通边和 Command 指定的跳转都可能生效，导致多个下游节点被同时触发。
## 4.3 多分支汇聚：Fan-in
1. 静态扇入
“与”触发：上游所有分支全部到达才可触发下游节点
```py
builder.add_edge(["node_c", "node_d"], "node_e")
```
“或”触发：任意一个分支到达，都可以触发下游节点
```py
builder.add_edge("node_c", "node_e")
builder.add_edge("node_d", "node_e")
```

2. 动态扇入-MapReduce结构
Map：映射阶段 将输入数据映射为中间结果。
Reduce：归约阶段 将多个子任务产生的中间结果进行汇总、合并或聚合，得到最终结果。

## 4.4 循环结构
1. 循环结构实现
    ReAct 是 Reason + Action 的缩写，即“推理 + 行动”架构。其核心思想是：

    Reason：大模型根据当前消息状态进行推理，判断是否需要调用工具；
    Action：如果需要调用工具，则生成工具调用请求；
    Observation：工具执行后，将执行结果以 ToolMessage 的形式返回给大模型；
    Loop：大模型基于新的观察结果继续推理，决定是否继续调用工具；
    Final Answer：当大模型不再发起工具调用时，生成最终回答，流程结束。

    因此，ReAct 本质上是一个典型的 “LLM → Tool → LLM → Tool → ... → LLM” 循环结构。

    静态实现：通过 add_conditional_edges() 在图结构中显式定义条件路由；
    动态实现：通过 Command(goto=...) 在节点返回值中触发运行时跳转。

2. 引入递归限制
在存在循环结构的图中，如果没有合理的停止条件，运行图可能会一直循环执行。为了避免无限循环，LangGraph 提供了递归限制机制，用于限制单次图运行过程中允许执行的最大 SuperStep 数量。
当运行图在达到停止条件之前耗尽允许的最大步数时，LangGraph 会抛出 GraphRecursionError。开发者既可以在图内部提前检测剩余步数并优雅退出，也可以在图外部捕获异常并集中处理。

- 步骤计数器
    运行时配置对象config
    LangGraph 运行节点时，会向节点函数注入运行时配置对象 config。
    该对象通常使用 RunnableConfig 类型标注，用于记录本次运行的配置信息和部分运行时元数据。
- 配置递归限制
    recursion_limit 表示单次图运行过程中允许执行的最大 SuperStep 数量。可以在调用运行图时通过 config 显式配置：
    ```py
    graph.invoke(input, config={"recursion_limit": 10})
    ```
- 优雅退出：主动方法（Proactive Approach）
    RemainingSteps 是 LangGraph 提供的特殊托管值，表示剩余可用步数，由运行时维护。

    LangGraph 运行时会根据当前步数和 recursion_limit 计算剩余步数，并填充到 RemainingSteps 类型的状态字段中。开发者可以在状态中声明一个 RemainingSteps 类型的字段，来获取剩余可用步数。
    ```py
    class OverAllState(TypedDict):
        remaining_steps: RemainingSteps
    ```
- 异常中断：被动方法（Reactive Approach）
    如果图中存在循环结构，并且运行图在达到停止条件之前耗尽了允许的最大步数，LangGraph 会抛出 GraphRecursionError。

    开发者可以在图外部捕获该异常，处理递归限制超限的情况。由于这种方式是在异常已经发生之后再处理，因此称为 被动方法（Reactive Approach）

    ```py
    try:
        graph.invoke({}, config={"recursion_limit": 10})
    except GraphRecursionError as e:
        logger.info("超步数量达到最大限制，抛出异常: {}", e)
    ```

# 5. 节点执行和容错机制
节点执行失败时，如果未做任何处理，可能导致整个运行图执行失败。为了提升运行图的稳定性，处理临时故障、超时、异常恢复以及重复计算等问题，LangGraph 提供了一系列节点执行与容错机制：重试、超时设置、异常处理和节点缓存。

## 5.1 重试机制
重试机制用于处理临时性异常，例如网络抖动、远程服务短暂不可用、API 偶发失败等。
在添加节点时，可以通过 retry_policy= 配置节点的重试策略。
```py
builder.add_node(
    "node_a",
    node_a,
    retry_policy=RetryPolicy(
        max_attempts=3, # 表示最多尝试 3 次。 包括首次执行
        initial_interval=1, # 表示第一次重试前的等待时间，单位为秒。
        backoff_factor=2.0, # 表示重试间隔的增长倍数。 initial_interval * backoff_factor
        max_interval=128, # 表示相邻两次重试之间的最大等待时间。
        jitter=False, # 是否为重试间隔添加随机抖动
        retry_on=(HTTPError, ConnectionError), # 用于设置哪些异常需要触发重试。 可以放一个自定义函数
    )
)
```

## 5.2 超时控制
为单次节点设置超时时间，运行时长超过超时时间，节点运行失败，并抛出超时异常。
```py
builder.add_node(
    "call_model",
    call_model,
    timeout=TimeoutPolicy(run_timeout=60)
)
```

## 5.3 错误处理
错误处理机制用于在节点最终失败后，执行兜底逻辑。
```py
builder.add_node(
    "call_api",
    call_api,
    retry_policy=RetryPolicy(max_attempts=3),
    error_handler=handle_api_error
)
```
handle_api_error 可以返回状态更新，也可以通过 Command 路由到其他节点。

## 5.4 节点缓存
将节点的历史运行结果保存下来，后续当节点收到相同输入时，不再重复执行节点函数，而是直接返回之前缓存的结果。
1. 为节点配置 cache_policy
CachePolicy(
    key_func根据节点输入生成缓存 Key 的函数, 
    ttl缓存键值对的存活时间，单位为秒
    )
```py
builder.add_node(
    "node_a",
    node_a,
    cache_policy=CachePolicy(ttl=10) # 声明节点是否启用缓存，以及缓存策略是什么。
)
```
2. 编译图时启用缓存后端
```py
graph = builder.compile(cache=InMemoryCache()) # 声明缓存数据实际保存在哪里。
```

## 5.5 全局默认配置
当多个节点都需要配置相同的执行策略时，如果每个节点都重复配置，繁琐且耗时。

在较新版本中，可以通过 set_node_defaults 为所有节点设置默认配置，即全图默认配置 Graph defaults。

retry_policy
timeout
error_handler
cache_policy

# 6. 持久化机制和可恢复执行
## 6.1 概述
### 6.1.1 什么是可恢复执行
在工作流、Agent、任务编排系统里，可恢复执行 Durable Execution 指的是：

把一次任务执行过程中的关键进度、状态、结果保存到可靠存储中，使任务可以在中断、失败、等待外部输入后继续执行。

### 6.1.2 LangGraph的持久化机制
保存图在某个时刻的状态快照，也就是 Checkpoint。

保存到 Checkpointer 管理的存储后端中。 开发时可以使用基于内存的 InMemorySaver，生产环境中通常会使用数据库等可靠存储，如 PostgresSaver。

通过 thread_id 区分不同的执行线程。 同一个 thread_id 表示同一条持久化执行线，也可以理解为同一个会话。

开发者通常不会直接操作底层 Checkpoint，而是通过 get_state() 和 get_state_history() 查看 Checkpoint 的开发者视图 StateSnapshot。

## 6.2 启用可恢复执行
### 6.2.1 步骤
1. 在编译图时传入检查点存储器对象 checkpointer
2. 在调用图时传递带有 thread_id 的配置对象
### 6.2.2 检查点类型
InMemorySaver	langgraph-checkpoint	        内存（In-memory）
SqliteSaver	    langgraph-checkpoint-sqlite	    SQLite
PostgresSaver	langgraph-checkpoint-postgres	PostgreSQL
MongoDBSaver	langgraph-checkpoint-mongodb	MongoDB
RedisSaver	    langgraph-checkpoint-redis	    Redis
### 6.2.3 基于内存的检查点
```py
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import MessagesState
from langgraph.checkpoint.memory import InMemorySaver
from langchain_deepseek import ChatDeepSeek
from langchain.messages import HumanMessage

from dotenv import load_dotenv
load_dotenv(override=True)

model = ChatDeepSeek(
    ...
)

class OverAllState(MessagesState):
    output: str

def llm_node(state: OverAllState) -> OverAllState:
    ...

def output_node(state: OverAllState) -> OverAllState:
    ...

builder = StateGraph(state_schema=OverAllState)
builder.add_node("llm_node", llm_node)
builder.add_node("output_node", output_node)

builder.add_edge(START, "llm_node")
builder.add_edge("llm_node", "output_node")
builder.add_edge("output_node", END)

# 定义并在编译时传递 Checkpointer
checkpointer = InMemorySaver()
graph = builder.compile(checkpointer=checkpointer)

# 定义配置对象
config = {"configurable": {"thread_id": "chapter_6_6-2-2"}}
# 调用时传递
graph.invoke({"messages": [HumanMessage("你好，我是老王")]}, config=config)
graph.invoke({"messages": [HumanMessage("从现在开始，你是小王")]}, config=config)
res = graph.invoke({"messages": [HumanMessage("我是谁？你是谁？")]}, config=config)
print(res["output"])

print('=' * 30, '-> 完整消息列表 <-', '=' * 30)
for msg in res["messages"]:
    msg.pretty_print()
```
### 6.2.4 基于持久化数据库的检查点
```py
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import MessagesState
from langgraph.checkpoint.postgres import PostgresSaver
from langchain_deepseek import ChatDeepSeek
from langchain.messages import HumanMessage

from dotenv import load_dotenv
load_dotenv(override=True)

model = ChatDeepSeek(
    ...
)

class OverAllState(MessagesState):
    output: str

def llm_node(state: OverAllState) -> OverAllState:
    ...

def output_node(state: OverAllState) -> OverAllState:
    ...

builder = StateGraph(state_schema=OverAllState)
builder.add_node("llm_node", llm_node)
builder.add_node("output_node", output_node)
builder.add_edge(START, "llm_node")
builder.add_edge("llm_node", "output_node")
builder.add_edge("output_node", END)

# 定义并在编译时传递 Checkpointer
DB_URL = "postgresql://langgraph_user:123456@localhost:5432/langgraph_db?sslmode=disable"
with PostgresSaver.from_conn_string(DB_URL) as checkpointer:
    # 示例中为了方便演示直接调用 setup()
    # 实际项目中通常建议把数据库初始化/迁移作为独立步骤处理
    checkpointer.setup()
    graph = builder.compile(checkpointer=checkpointer)

    # 定义配置对象
    config = {"configurable": {"thread_id": "chapter_6_6.2.4"}}
    # 调用时传递
    graph.invoke({"messages": [HumanMessage("你好，我是老王")]}, config=config)
    graph.invoke({"messages": [HumanMessage("从现在开始，你是小王")]}, config=config)
    res = graph.invoke({"messages": [HumanMessage("我是谁？你是谁？")]}, config=config)
    print(res["output"])

    print('=' * 30, '-> 完整消息列表 <-', '=' * 30)
    for msg in res["messages"]:
        msg.pretty_print()
```
## 6.3 持久化模式
LangGraph 支持三种持久化模式，采用不同的检查点保存时机，在容灾能力和性能开销、响应时效性之间作取舍。

exit：退出模式。
运行退出时写入
只在计算图正常结束、异常退出、被中断（如 Human-In-The-Loop 中断）时保存检查点。不能处理中途进程崩溃的场景。这种模式响应**性能开销最小**，但**容灾能力最弱**。

async：异步模式。
每个超步末尾写入主检查点，任务完成后写入中间结果，后台异步写入
和 exit 模式相比，增加了性能开销，但写入操作发生在后台，不会引入明显的响应延迟，同时提升了容灾能力。

sync：同步模式。
和 async 区别在于，进入下一个超步之前等待当前主检查点的写入任务完成
和异步模式唯一的区别在于，LangGraph 会在进入下一个超步之前等待当前主检查点的写入任务完成。
它的容灾能力最强，但在 async 模式的基础上增加了响应延迟。

```py
# 调用时传递 持久化模式参数
res=graph.invoke(
    {"messages": [HumanMessage("你好")]},
    config=config,
    durability="async" # sync / exit
)
```
## 6.4 查看历史检查点
LangGraph 在配置检查点存储器后，会把同一个 thread_id 下的执行过程保存为一组检查点。
通过这些检查点，我们可以查看图运行的中间状态，也可以为后续的检查点回溯（重放、分叉）和失败恢复做准备。

### 6.4.1 查看完整历史检查点列表
```py
history_checkpoints = list(graph.get_state_history(config=config))
print(history_checkpoints)
```
get_state_history() 返回的是一个历史检查点迭代器。
将其转换为列表后，可以看到一组 StateSnapshot 对象。
### 6.4.2 查看最新检查点
```py
latest_history_checkpoint = graph.get_state(config=config)
print(latest_history_checkpoint)
```
### 6.4.3 根据ID查看指定检查点
如果希望查看某个历史检查点，可以在 configurable 中额外传入 checkpoint_id
```py
target_config = {
    "configurable": {
        "thread_id": "123",
        "checkpoint_id": "某个历史 checkpoint_id"
    }
}

snapshot = graph.get_state(config=target_config)
print(snapshot)
```

# 7. 图记忆管理
Agent 的三种记忆：

- 短期记忆：通过运行时状态 State 访问，并由检查点存储器 Checkpointer 保存，它按照 thread_id 组织，可以实现线程内的记忆共享。

- 长期记忆：通过长期记忆存储器 Store 访问和存储。数据通常按照元组类型的命名空间组织，以键值对的形式存储，提供跨会话的记忆共享。
可以按照命名空间+可选的过滤条件精确检索
也可以通过语义模糊匹配。

- 运行时上下文：通过上下文对象 Context 访问，只对本次调用生效，不会被持久化。
它更适合传递本次运行所需的外部依赖或调用参数，如用户名、模型配置、数据库连接、权限信息等。
## 7.1 短期记忆
只要编译图时启用了 Checkpointer，并且调用图时复用同一个 thread_id，LangGraph 就可以在多次调用之间共享同一会话线程下的状态。

## 7.2 长期记忆
长期记忆存储器在编译图时通过 store 参数传递，图节点中可以通过 Runtime 对象访问。

本节会在一个案例中同时用到短期记忆和长期记忆，两者均使用 PostgreSQL 作为持久化后端——短期记忆通过 PostgresSaver，长期记忆通过 PostgresStore，数据不会随进程退出而丢失。

### 7.2.1 准备长期记忆
```py
from typing import Final, Tuple
from langgraph.store.postgres import PostgresStore

# 与 6.2.4 节使用同一数据库
DB_URL = "postgresql://langgraph_user:123456@localhost:5432/langgraph_db?sslmode=disable"
with PostgresStore.from_conn_string(DB_URL) as store:
    # setup() 创建长期记忆所需的表结构，幂等操作
    store.setup()

    # 命名空间 - 层级结构：("users", "用户名")
    # Final 的作用是告诉静态类型检查器，该变量不应该被重新赋值，但 python 运行时不会阻止重新赋值
    USERS_NS: Final[Tuple[str]] = ("users", )
    PREFERENCES_KEY: Final[str] = "preferences"

    # 三层: (领域, 用户实体)
    # 每个 key 存储该用户的不同类型数据
    namespace1 = (*USERS_NS, "Alice")
    value1 = {
        "course": "计算机组成原理",
        "sports": "跑步",
        "food": "紫光园奶皮子酸奶"
    }

    namespace2 = (*USERS_NS, "Bob")
    value2 = {
        "course": "数字电路与模拟电路",
        "sports": "跑步",
        "food": "奶皮子糖葫芦"
    }

    namespace3 = (*USERS_NS, "Black")
    value3 = {
        "course": "数字电路与模拟电路",
        "sports": "羽毛球",
        "food": "紫光园奶皮子酸奶"
    }

    store.put(namespace1, PREFERENCES_KEY, value1)
    store.put(namespace2, PREFERENCES_KEY, value2)
    store.put(namespace3, PREFERENCES_KEY, value3)

    for item in store.search(USERS_NS):
        print(item)
```

namespace 使用元组是硬性约束，天然表达层级结构。本例使用两层命名空间 ("users", "Alice")，清晰区分了领域（users）和实体（用户名），而具体存储什么类型的数据则由 key 参数表达（如 "preferences"）。

(*USERS_NS, "Alice") 的写法表示对已有元组进行解包，再拼接新的命名空间片段。

PostgresStore 将长期记忆持久化到 PostgreSQL 中，程序重启后数据不会丢失，适合生产环境。本节使用和 6.2.4节、6.5.4.1节 相同的数据库实例。

如果希望支持语义检索，需要在 Store 中配置索引和 embedding 函数。未配置索引时，search() 只能按照命名空间和过滤条件检索。
### 7.2.2 访问长期记忆
长期记忆存储器可以通过节点函数中的 runtime.store 访问。
```py
# 获取长期记忆存储器 store
store = runtime.store

# 根据用户信息拼接命名空间，查询用户偏好
namespace = (*USERS_NS, username)
key = PREFERENCES_KEY
item = store.get(namespace, key)
```
## 7.3 运行时上下文
在某些场景下，我们希望在调用图时传入一些仅对当次调用有效的信息，比如当前登录用户、请求来源、调用方标识等。这些信息不适合放入图状态（图状态会被持久化并在同一会话中跨调用共享），而应该通过运行时上下文（Runtime Context）传递。

1. 初始化状态图时，使用 context_schema 定义上下文类型。
2. 调用图时通过 context 参数传入上下文对象。
3. 节点或路由函数中通过 runtime.context 访问上下文。

```py
from dataclasses import dataclass
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import MessagesState
from langgraph.runtime import Runtime
from langchain.messages import HumanMessage
from langchain_deepseek import ChatDeepSeek

from loguru import logger
from dotenv import load_dotenv
load_dotenv(override=True)

model = ChatDeepSeek(
    ...
)

# 1. 定义运行时上下文类型
@dataclass
class UserContext:
    username: str
    membership_level: str  # "普通用户" / "VIP"

# 2. 定义图状态
class OverAllState(MessagesState):
    user_input: str
    output: str

# 3. 定义节点：通过 runtime.context 访问运行时上下文
def llm_node(state: OverAllState, runtime: Runtime[UserContext]) -> OverAllState:
    runtime_context = runtime.context

    if runtime_context:
        username = runtime_context.username
        level = runtime_context.membership_level
        logger.info(f"当前用户: {username}, 会员等级: {level}")

        if level == "VIP":
            system_prompt = f"你是高级客服助理。当前VIP用户是{username}，请使用尊称'您'，语气热情周到，回复末尾加上'🎖️VIP专属服务'。"
        else:
            system_prompt = f"你是普通客服助理。当前用户是{username}，请友好简洁地回复。"
    else:
        logger.warning("运行时上下文为空，使用默认风格")
        system_prompt = "你是客服助理，请友好简洁地回复。"

    user_input = state["user_input"]
    messages = state.get("messages", [])
    response = model.invoke(
        [HumanMessage(content=system_prompt)] +
        messages +
        [HumanMessage(content=user_input)]
    )

    return {
        "messages": [response],
        "output": response.content
    }

# 4. 构建图，传入 context_schema
builder = StateGraph(state_schema=OverAllState, context_schema=UserContext)
builder.add_node("llm_node", llm_node)

builder.add_edge(START, "llm_node")
builder.add_edge("llm_node", END)

graph = builder.compile()

# === 第一次调用：传入运行时上下文（VIP用户） ===
print("=" * 30, "第一次调用：VIP用户", "=" * 30)
config = {"configurable": {"thread_id": "demo-7.3"}}
res = graph.invoke(
    {"user_input": "你好，帮我查一下最近有什么优惠活动"},
    config=config,
    context=UserContext(username="Alice", membership_level="VIP")
)

print(f"output: {res['output']}")
print()

# === 第二次调用：不传运行时上下文 ===
print("=" * 30, "第二次调用：不传上下文", "=" * 30)
res2 = graph.invoke(
    {"user_input": "再帮我看看有没有新品"},
    config=config
)

print(f"output: {res2['output']}")
```

## 7.4 Node总结
LangGraph 还可以在运行时注入运行时配置、运行时对象和流式写入器等参数。

普通图节点通常使用以下四个参数：
- state：输入节点的图状态。state 是位置传参，因此参数名称不重要，但通常约定命名为 state
- config：状态图的运行时配置，它是一个 RunnableConfig 实例，底层运行时在节点函数执行前通过关键字传参动态注入。
- runtime：状态图的运行时对象，可以通过它访问运行时上下文、长期记忆存储器等信息。底层运行时在节点函数执行前通过关键字传参动态注入。
- writer：流式写入器，通常用于自定义流式输出。详见流处理章节。

编译图时传入 checkpointer，并在调用时传入 config，可以在节点中通过 config 间接访问当前调用的配置信息，如 thread_id。

编译图时传入 store 后，可以在节点中通过 runtime.store 访问长期记忆存储器。

初始化状态图时传入 context_schema，并在调用时传入 context 后，可以在节点中通过 runtime.context 访问运行时上下文。

# 8. 中断
LangGraph 提供了两种中断机制：

- 动态中断：在图的任意节点中调用 interrupt() 函数实现
    它可以放在代码的任意位置，并且可以根据应用逻辑设置条件触发，所以是动态的。
    动态中断提供了人机交互接口，使得调用者可以人为干预计算图的运行，是业务逻辑的一部分。

- 静态中断：在编译或调用状态图时通过 interrupt_before 和 interrupt_after 参数设置断点
    它是在运行前确定的，不能根据业务逻辑条件触发，所以是静态的。
    静态中断主要用于调试，不是业务逻辑的一部分。

## 8.1 动态中断
### 8.1.1 启用中断
1. 配置检查点存储器

2. 设置 thread_id
    如果要确保中断后可以恢复执行，就需要保存运行图的完整状态，所以必须启用可恢复执行。

3. 在需要中断的位置调用 interrupt()
### 8.1.2 恢复中断
基于相同的配置再次调用计算图

将输入替换为 Command() 实例即可恢复运行。

通过 Command 实例的 resume 属性将用户反馈传递给计算图，中断节点重新运行时，传递给 resume 属性的值将会作为 interrupt() 函数的返回值。

### 8.1.3 常见使用模式
- 基础 HITL 模式：状态图触发一次中断，获取人类输入后继续执行。
- 多个并行中断：多个并行任务分别产生中断，并根据 中断 ID 接收各自的恢复数据。
- 审批模式：根据人类审批（批准、拒绝或其它处理方式），决定后续执行路径。
- 审核与编辑模式：将模型生成的内容交给人类检查，并允许人类直接修改后继续处理。
- 工具执行审批模式：在调用工具或执行具有副作用的操作之前，由人类确认是否允许执行。
- 单节点串行中断模式：在同一个节点内多次触发中断，上一个中断恢复后才能触发下一个。
- 人类输入验证模式：对人类输入进行校验；当输入不符合要求时，再次中断并要求重新输入。

### 8.1.4 使用规范
1. 不要用try/catch包裹interrupt()调用
    中断的触发是通过抛出 GraphInterrupt 异常实现的，如果用 try/catch 包裹，则底层运行时无法感知断点，不会中断计算图。
2. 不要更改单个节点内interrupt的调用顺序
    恢复运行时整个节点函数都会重新运行，而非精确地从断点继续
    同一节点中存在多个断点时：历史恢复记录被记录在检查点中，并在恢复运行时按顺序加载
    一旦中断恢复前后的断点顺序、数量不完全一致，将会导致语义混乱，程序执行结果无法满足预期。
3. 不要在interrupt()中传递复杂类型
    LangGraph 运行时会将 interrupt() 函数接收到的参数经过 JSON 序列化 之后传递给调用者。
4. 断点之前的副作用操作必须是幂等的
    中断恢复时，断点所在的函数会被重复执行，所以，如果断点之前存在不满足幂等性的副作用操作，将会导致多次调用结果不一致。

## 8.2 静态断点
LangGraph 提供了用于调试的 静态断点。

它是在状态图编译或调用时设置的，不会在运行时动态触发，不属于业务逻辑，所以称为 静态 断点。

动态断点提供了接收人类反馈的接口，而静态断点只是暂停计算图的运行，不能向调用者传递信息，也不能接收调用者的反馈。

静态断点也需要基于检查点恢复，所以必须配置检查点，启用可恢复运行机制。

计算图会在 interrupt_before 指定的节点执行之前产生中断，暂停计算

计算图会在 interrupt_after 指定的节点执行之后产生中断，暂停计算

计算图运行到断点位置会中断，和动态断点不同的是，它会在超步边界而非内部中断。

断点前的超步：三个阶段全部完成；断点后的超步：三个阶段都没有开始。

静态断点不会返回任何中断信息，只会将当前最新的状态返回。

因此，我们可以用静态断点查看每个超步边界的中间状态。

传入相同的配置并将 None 作为输入，再次调用计算图，会从断点位置继续运行。

支持在两个阶段设置静态断点
- 状态图编译时
```py
graph = builder.compile(
    checkpointer=checkpointer,
    interrupt_before=["node_a", "node_b"],
    interrupt_after=["node_a", "node_b"]
)
```
- 计算图调用时
```py
first_res = graph.invoke(
    {},
    config=config,
    interrupt_before=["node_a", "node_b"],
    interrupt_after=["node_a", "node_b"]
)
```
断点都是在运行时生效，计算图调用时设置的断点优先级更高。

# 9. 项目部署

# 10. 工具节点
## 10.1 手动处理工具调用
```py
from typing import Literal
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import MessagesState
from langchain.messages import HumanMessage, ToolMessage
from langchain.tools import tool
from langchain_deepseek import ChatDeepSeek

from loguru import logger
from dotenv import load_dotenv
load_dotenv(override=True)

@tool(parse_docstring=True)
def get_weather(city: str) -> str:
    ...

@tool(parse_docstring=True)
def get_news(home_or_abroad: bool) -> str:
    ...

tools_by_name = {
    "get_weather": get_weather,
    "get_news": get_news
}
tools = [get_weather, get_news]

model = ChatDeepSeek(...)
model_with_tools = model.bind_tools(tools=tools)

def llm_node(state: MessagesState) -> MessagesState:
    messages = state['messages']
    response = model_with_tools.invoke(messages)

    return {"messages": [response]}

def tool_node(state: MessagesState) -> MessagesState:
    last_msg = state['messages'][-1]
    if not last_msg.tool_calls:
        return {}

    tool_msgs = []
    for tool_call in last_msg.tool_calls:
        tool = tools_by_name[tool_call["name"]]
        logger.info("工具 {} 被调用, 对应的 tool_call: {}", tool_call["name"], tool_call)
        tool_res = tool.invoke(tool_call["args"])
        tool_msg = ToolMessage(
            name = tool_call["name"],
            content = tool_res,
            tool_call_id = tool_call["id"]
        )
        tool_msgs.append(tool_msg)

    return {
        "messages": tool_msgs
    }

def router(state: MessagesState) -> Literal["tool_node", END]:
    if state['messages'][-1].tool_calls:
        return "tool_node"
    return END

builder = StateGraph(state_schema=MessagesState)
builder.add_node("llm_node", llm_node)
builder.add_node("tool_node", tool_node)

builder.add_edge(START, "llm_node")
builder.add_conditional_edges("llm_node", router, path_map=["tool_node", END])
builder.add_edge("tool_node", "llm_node")

graph = builder.compile()

from IPython.display import display
display(graph)

res = graph.invoke({"messages": [HumanMessage("今天北京天气如何？国内有哪些新闻")]})
for msg in res['messages']:
    msg.pretty_print()
```

## 10.2 用ToolNode处理工具调用
```py

from typing import Literal
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt.tool_node import ToolNode
from langgraph.graph.message import MessagesState
from langchain.messages import HumanMessage
from langchain.tools import tool
from langchain_deepseek import ChatDeepSeek

from dotenv import load_dotenv
load_dotenv(override=True)

@tool(parse_docstring=True)
def get_weather(city: str) -> str:
    ...

@tool(parse_docstring=True)
def get_news(home_or_abroad: bool) -> str:
    ...

tools = [get_weather, get_news]

model = ChatDeepSeek(
    ...
)
model_with_tools = model.bind_tools(tools=tools)

def llm_node(state: MessagesState) -> MessagesState:
    messages = state['messages']
    response = model_with_tools.invoke(messages)

    return {
        "messages": [response]
    }

def router(state: MessagesState) -> Literal["tool_node", END]:
    if state['messages'][-1].tool_calls:
        return "tool_node"
    return END

builder = StateGraph(state_schema=MessagesState)
builder.add_node("llm_node", llm_node)
builder.add_node("tool_node", ToolNode(tools=tools))

builder.add_edge(START, "llm_node")
builder.add_conditional_edges("llm_node", router, path_map=["tool_node", END])
builder.add_edge("tool_node", "llm_node")

graph = builder.compile()

res = graph.invoke({"messages": [HumanMessage("今天北京天气如何？国内有哪些新闻？")]})
for msg in res['messages']:
    msg.pretty_print()
```

## 10.3 进阶用法

# 11. 流式执行
## 11.1 什么是流式执行
流式执行（Streaming Execution），是指程序在任务尚未全部完成时，就将执行过程中已经产生的中间结果、状态变化或事件持续输出给调用方，而不是等待整个任务结束后一次性返回最终结果。

在同步执行中，这些数据最终进入内部的同步流式队列；在异步执行中，则进入对应的异步队列。调用方通过迭代器逐条消费这些数据，因此不必等到整张图执行完毕后再获得反馈。

stream：同步 API
astream：异步 API