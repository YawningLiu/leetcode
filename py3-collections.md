# collections in Python 3
collections - 集合类模块. 主要在 py3 内置数据类型 str, int, list, tuple,dict 等 基础上, 提供了额外的数据类型. 
* `namedtuple('name',['field_names'])`: 生成可以使用名字来访问元素内容的tuple子类, 增强代码可读性;           
* `deque()`: 双端队列, 最大的优点是可以从头部追加`.appendleft()`和取出`.popleft()`对象; [注: list对头部操作复杂度是O(n),而deque是O(1).]   
* `Counter()`: 计数器 (dict 子类);
* `OrderedDict()`: 有序字典, 对 key 排序; 
* `defaultdict('data type')`: 带有默认值的字典. key 不存在时返回默认值. 

参考    
[官方文档](https://docs.python.org/3/library/collections.html)
[1](https://www.liaoxuefeng.com/wiki/897692888725344/973805065315456)
[2](https://www.cnblogs.com/zhizhan/p/5692668.html)
[3](https://www.cnblogs.com/deeper/p/8073412.html)