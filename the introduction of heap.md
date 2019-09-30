# Heap

待解决: 堆找第k小数, python实现堆; AVL树或者红黑树,最短路算法——Dijkstra，需要用到堆来优化

#### 定义:
就是用**完全二叉树**的性质来维护的**数组**. (无指针.) 一次操作的时间复杂度为 O(1) ~ O($log$N).

#### 用途：

* 构建优先队列 (priority queue);
* 支持堆排序;
* 快速找出一个集合中的极值;
* 在朋友面前装逼 XD

#### 分类
最大堆 (爸爸 > 儿子) 和最小堆 (爸爸 < 儿子).
> c.f.: 二叉排序树 [BST] (左儿子 < 爸爸 < 右儿子).
> * 除了排序方式不同外, BST 内存占用 >> 堆.
> * 树 "平衡" 时操作才能达到 $log$ 量级. 且除 AVL树 / 红黑树, 其余均不能按任意顺序位置插入/删除数据, 但堆可以.
> * BFS 搜索会很快, 但堆很慢.

#### 堆中的父子关系
```python
#len(heap) = n, 当前节点 index
father = (index-1)//2 #index=0时辈分最高
son1 = 2*index+1   #注意index>n//2时儿子还没生出来呢
son2 = 2*index+2  
# index >0
heap[fateher] >= heap[index]
```
* n个节点的堆高度是 `floor(log(2,n))`, 叶节点位于数组floor(n/2) 和 n-1 之间.

#### 操作(复杂度 O($log$n))
* `shiftUp()`: 如果一个节点比它的父节点大 (最大堆) 或者小 (最小堆), 那么需要将它同父节点交换位置. 这样是这个节点在数组的位置上升.
* `shiftDown()`: 如果一个节点比它的子节点小 (最大堆) 或者大 (最小堆), 那么需要将它向下移动. 这个操作也称作 "堆化 (heapify)".
* `insert(value)`: 在堆的尾部添加一个新的元素, 然后使用 `shiftUp()` 来修复堆.  
* `remove()`: 移除并返回极值. 为了将这个节点删除后的空位填补上, 需要将最后一个元素移到根节点的位置, 然后使用 `shiftDown()` 方法来修复堆.

#### 堆的建立
最优算法: **递归**. 从最后一个拥有子节点的节点向上遍历, 使用 `shiftDown()`将遍历到的每一个子树变成堆.
```python
import os
import sys
#抄的, 就是heapify(list)
def sink(list,root):
    if 2*root+1 < len(list):
        k = 2*root+2 if 2*root+2 < len(list) and list[2*root+2] < list[2*root+1] else 2*root+1     #让k成为较小的子节点的index
        if list[root] > list[k]:
            (list[root],list[k]) = (list[k],list[root])     #交换值
            sink(list,k)              #对子节点为根节点的子树建堆

def main(argv):
    list = [int(arg) for arg in argv]
    for i in range(len(list)//2-1,-1,-1):
        sink(list,i)
    print(list)
if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1:])
```
### python3: heapq 模块
内置模块. 可以用来求前n个最大/最小值.
```python
heapq.nlargest(n,heap)   #前n个最大值
heapq.nsmallest(n,heap)   #前n个最小值
heapq.heappush(heap, item)  #新元素入队堆
heapq.heappop(heap)   #弹出堆顶元素
heapq.heapify(list)   #将列表list进行堆调整, 默认的是小根堆
```
若 heap 储存的是truple (a,b,c), 则堆内部操作时先比较 a,  a 相同时再比较b, 之类的.
#### 参考    
 [数据结构：堆(Heap)](https://www.jianshu.com/p/6b526aa481b1)    
[堆的python实现及其应用](https://www.cnblogs.com/yscl/p/10090939.html)   
[Python3实现最小堆建堆算法](https://www.cnblogs.com/xshrim/p/4077394.html)   
[使用Python模块: heapq模块(堆)](https://blog.csdn.net/abc_12366/article/details/80423249)
