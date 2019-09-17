# collections in Python 3

---

collections - 集合类模块. 主要在 py3 内置数据类型 str, int, list, tuple,dict 等 基础上, 提供了额外的数据类型. 
* `namedtuple('name',['field_names'])`: 生成可以使用名字来访问元素内容的tuple子类, 增强代码可读性;           
* `deque()`: 双端队列, 最大的优点是可以从头部追加`.appendleft()`和取出`.popleft()`对象; [注: list对头部操作复杂度是O(n),而deque是O(1).]   
* `Counter()`: 计数器 (dict 子类);
* `OrderedDict()`: 有序字典, 对 key 排序; 
* `defaultdict('data type')`: 带有默认值的字典. key 不存在时返回默认值. 

---

###  `OrderedDict()`

> [leetcode-146](https://leetcode.com/problems/lru-cache/)    
> [有序字典](https://www.cnblogs.com/skyzy/p/9433424.html)

OrderedDict 也是 dict 的子类, 它可以"维护"添加 key-value对的顺序. 简单来说, 就是先添加的 key-value 对排在前面, 后添加的 key-value 对排在后面. 

因此, 即使两个 OrderedDict 中即使包含的 key-value 对完全相同, 但只要它们的顺序不同, 程序也依然会判断出两个 OrderedDict 是不相等的.

* `popitem(last=True)`: 默认弹出并返回最右边(最后加入)的 key-value 对. 如果将 last 参数设为 False, 则弹出并返回最左边(最先加入)的 key-value 对.
* `move_to_end(key, last=True)`: 默认将指定的 key-value 对移动到最右边(最后加入); 如果将 last 改为 False, 则将指定的 key-value 对移动到最左边(最先加入). 

---
参考:
[官方文档](https://docs.python.org/3/library/collections.html)
[1](https://www.liaoxuefeng.com/wiki/897692888725344/973805065315456)
[2](https://www.cnblogs.com/zhizhan/p/5692668.html)
[3](https://www.cnblogs.com/deeper/p/8073412.html)