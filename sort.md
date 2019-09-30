# 排序算法总结

- [0. 概括](#0.1-算法分类)
- [1. 冒泡排序](#1-冒泡排序-bubble-sort)
- [2. 快速排序](#2-快速排序-quick-sort)
- [3. 直接插入排序](#3-直接插入排序-insertion-sort)
- [4. 希尔排序](#4-希尔排序-shell-sort)
- [5. 简单选择排序](#5-简单选择排序-selection-sort)
- [6. 堆排序](#6-堆排序-heap-sort)
- [7. 归并排序](#7-归并排序-merge-sort)
- [8. 计数排序](#8-计数排序-counting-sort)
- [9. 桶排序](#9-桶排序-bucket-sort)
- [10. 基数排序](#10-基数排序-radix-sort)
- [参考资料](#参考资料)
---
## 0  概括
本次总结只考虑对数组的排序.  

### 0.1 算法分类
排序算法大体可分为两种：

* 比较类排序: 通过比较来决定元素间的相对次序.
时间复杂度 O(nlogn) ~ O(n<sup>2</sup>) ,
由于其时间复杂度不能突破 O(nlogn), 因此也称为非线性时间比较类排序.
主要有: 冒泡排序, 选择排序, 插入排序, 归并排序, 堆排序, 快速排序等.
* 非比较类排序： 不通过比较来决定元素间的相对次序. 时间复杂度可以达到 O(n).
它可以突破比较排序的时间下界, 以线性时间运行,
因此也称为线性时间非比较类排序.
主要有: 计数排序, 基数排序, 桶排序等.

![排序图](https://wx3.sinaimg.cn/mw690/006qmTkdly1g788owt6o4j30fo0b9glt.jpg)

### 0.2 算法复杂度

|排序方法|时间(平均)|时间(最好)|时间(最坏)|空间|稳定性|      
|-------|-------|-------|-------|----|-----|    
|冒泡排序|O(n<sup>2</sup>)|O(n)|O(n<sup>2</sup>)|O(1)|稳定|      
|快速排序|O(nlogn)|O(nlogn)|O(n<sup>2</sup>)|O(logn)~O(n)|不稳定|    
|直接插入|O(n<sup>2</sup>)|O(n)|O(n<sup>2</sup>)|O(1)|稳定|   
|希尔排序|O(nlogn) ~ O(n<sup>2</sup>)|O(n<sup>1.3</sup>)|O(n<sup>2</sup>)|O(1)|不稳定|    
|简单选择|O(n<sup>2</sup>)|O(n<sup>2</sup>)|O(n<sup>2</sup>)|O(1)|不稳定|        
|堆排序|O(nlogn)|O(nlogn)|O(nlogn)|O(1)|不稳定|    
|归并(bottom up)|O(nlogn)|O(nlogn)|O(nlogn)|O(n)|稳定|    
|归并(top down)|O(nlogn)|O(nlogn)|O(nlogn)|O(n)|稳定|    
||    
|计数排序|O(n+k)|O(n+k)|O(n+k)|O(n+k)|稳定|      
|桶排序|O(n+k)|O(n)|O(n<sup>2</sup>)|O(n+k)|稳定|     
|基数排序|O(n*r) | O(n*r)| O(n*r) |O(n+k)|稳定|    

在非比较排序中, k 代表容量大小(计数排序中为元素所在范围大小, 基数排序中为基数容量), r 为关键字的数量.


### 0.3 关于稳定性
排序算法稳定性的简单形式化定义为：
如果 `arr[i] = arr[j]`, 排序前 `arr[i]` 在`arr[j]`之前,
排序后 `arr[i]` 还在 `arr[j]` 之前, 则称这种排序算法是稳定的.

通俗地讲就是保证排序前后两个相等的数的相对顺序不变.
(可以通过自定义比较函数来去除稳定性问题)
> eg: 对于冒泡排序, 原本是稳定的排序算法, 如果将记录交换的条件改成 `arr[i] >= arr[i + 1]`, 则两个相等的记录就会交换位置, 从而变成不稳定的排序算法.

> [知乎](https://www.zhihu.com/question/24637339) 上关于时间复杂度的一点讲解:    
可以用 **逆序数** 来理解: 假设我们要从小到大排序, 一个数组中取两个元素如果前面比后面大, 则为一个逆序, 容易看出排序的本质就是消除逆序数. 可以证明对于随机数组, 逆序数是O(n<sup>2</sup>)的. 如果采用 "交换相邻元素" 的办法来消除逆序, 每次正好只消除一个, 因此必须执行O(n<sup>2</sup>)的交换次数. 因此冒泡, 插入等算法只能到时间复杂度平方级别. 反过来, 基于交换元素的排序要想突破这个下界, 必须执行一些比较, 交换相隔比较远的元素, 使得一次交换能消除一个以上的逆序. 希尔, 快排, 堆排之类算法都是交换比较远的元素, 只不过规则各不同罢了.  





## 1 冒泡排序 Bubble Sort
冒泡排序是一种简单的排序算法. 它列重复地走访过要排序的数,
一次比较两个元素, 如果它们的顺序错误就把它们交换过来.
走访数列的工作是重复地进行直到没有再需要交换,
也就是说该数列已经排序完成.
这个算法的名字由来是因为越小的元素会经由交换慢慢 "浮" 到数列的顶端.   

### 1.1 算法描述
+ 进行n-1次排序(每次把第 n 大 的数字排序).
+ 第 i 次排序为 从 0~n-1-i. 检查这个序列中两两的数,
如果前面的大于后面的就将它们交换,
这样使得大的数往后面走, 每次冒泡就会将一个大的数往后面冒,
从而达到目的.

### 1.2 代码实现
``` python
def bullesort(nums): #冒泡排序-基础
    for i in range(len(nums)):
        for j in range(len(nums)-i-1):
            if nums[j] >nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums
```
还可以进一步优化:
* 记录每次大循环时最后交换的那个位置end;
(这时如果元素基本上是正序,就是最好情况O(n))
* 下一轮交换只需要进行到 end 即可

``` python
def bullesort1(nums): # 冒泡排序 - 改进
    for i in range(len(nums)-1):
        end = 0 #end 后都不用比了
        for j in range(len(nums)-i-1):
            if nums[j] >nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
                end = j+1
        i = len(nums) - end -1
    return nums
```

### 1.3 鸡尾酒排序 -- 改进的冒泡排序
也叫做定向冒泡排序:
* 两边同时冒泡(先把从前往后比较, 再从后往前比较)
* 比冒泡更加高效一点, 但改进不是很大

```python
def bullesort2(nums): # 鸡尾酒冒泡排序
    left, right = 0, len(nums)-1
    while left < right:
        for j in range(left,right): #从前往后冒
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
        right-=1
        for j in range(right,left,-1): #从后往前冒
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
        left+=1
    return nums
```

### 1.4 算法分析

表现最稳定的排序算法之一, 因为无论什么数据进去都是 O(n<sup>2</sup>) 的时间复杂度, 唯一的好处可能就是不占用额外的内存空间. (但是太慢.)

## 2 快速排序 Quick Sort

快速排序的基本思想: 通过一趟排序将待排记录分隔成独立的两个子部分, 其中一部分记录的关键字均比另一部分的关键字小. 再分别对这两部分记录继续进行排序, 当拆分后的子部分中元素个数为 1 时, 即可达到整个序列有序的状态.  

### 2.1 算法描述
+ 在待排序序列中找到一个元素, 即 "基准(piovot)";
+ 重新排序数列, 比 piovot 值小的元素放在 piovot 前面, 其余放在后面. 这一步结束之后, piovot 将序列分为了 < 它和 >= 它的两部分. 称为分区 (partition) 操作:
+递归地 (recursive) 把两个子部分排序.

### 2.2 代码实现
```python
def quick(nums, left, right ): #快速排序
    if right-left <=0: return #即列表长为 1 /0 时return
    x, idx = nums[right], left #piovot,分割序列的下标
    for i in range(left,right):
        if nums[i] < x:
            nums[i],nums[idx] = nums[idx],nums[i]
            idx+=1
    nums[idx], nums[right] = nums[right], nums[idx]
    quick(nums, left, idx-1)
    quick(nums, idx+1, right)
    return
```
### 2.3 代码优化

然而, 上述快排存在两个问题:
+ 若选取的划分的元素 (piovot = nums[right]) 很小(大), 即 piovot 选择不好, 后面划分的数组极度不平衡 (例如逆序数组), 快排将降到 O(n<sup>2</sup>);     
  * 优化一之 **随机快排**: 随机选取一个元素作 piovot. 只需在上述算法中加入随机量的选择:

```python
  import random  
  randomindex = random.randint(left,right)
  nums[right], nums[randomindex] = nums[randomindex], nums[right]
```

+ 若待排序数组重复元素很多, 划分的数组也会极度不平衡, 从而再次退化成 O(n<sup>2</sup>).    
  * 优化二之 **双路快排**: 可以让 partition 后返回的 piovot 停在最中间, 从而解决重复元素多的问题.
  + 优化三之 **三路快排**: (荷兰国旗问题) 更好的解决重复元素多的问题. 将数组划分成 <piovot, =piovot, >piovot 三部分.

#### 2.3.1 双路快排
+ 设置两个指针L,R (一个从left开始, 一个从right开始), < piovot 指针L后移, >piovot 指针R前移.
+ 当 指针L,R 停止时, L处满足 >=随机选择piovot, 指针R满足<=piovot时, 如果二者没有相遇, 就交换数字, 继续扫描, 相遇就停止扫描, 还得交换位置(思考为什么).

```python
def twoway_quick(nums,left,right): #双路快排, 对于重复数字将它们等分
    if right-left <=0: return
    randomindex = random.randint(left,right) #随机选择piovot
    nums[right], nums[randomindex] = nums[randomindex], nums[right]
    L,R,x = left, right-1,nums[right]
    while True:
        while L<right and nums[L]<x:L+=1
        while R>left and nums[R]>x: R-=1
        if R<=L: break
        nums[L], nums[R] = nums[R], nums[L]
        L, R= L+1, R-1
    nums[right], nums[L] = nums[L], nums[right] #不能省, R便可看作分割点
    twoway_quick(nums, left, L-1)
    twoway_quick(nums, L+1, right)
    return
```
#### 2.3.2 三路快排
荷兰国旗问题. 如 [LeetCode75-Sort Colors](https://leetcode.com/problems/sort-colors/).  
+ 重点是 partition 过程: 将 <piovot 放到左边, >piovot 的放在右边, =piovot 放到中间;
+ 再对左右区间重复第二步.

```python
def threeway_quick(nums,left,right):
    if right-left <=0: return
    randomindex = random.randint(left,right) #随机选择pioviot
    nums[right], nums[randomindex] = nums[randomindex], nums[right]
    L,R, cur, x = left-1, right, left, nums[right]
    while cur < R:
        if nums[cur] < x:
            L+=1
            nums[cur],nums[L] = nums[L],nums[cur]
            cur+=1
        elif nums[cur] > x:
            R-=1
            nums[cur],nums[R] = nums[R],nums[cur]
        else:
            cur+=1  
    nums[right],nums[cur] = nums[cur],nums[right]
    threeway_quick(nums, left, L)
    threeway_quick(nums, R+1, right)
    return
```
### 2.4 算法分析

快速排序是一种非稳定排序算法, 形式上类似于归并排序, 操作上刚好相反, 一个是对集合先拆分后操作, 一个是对集合先操作后拆分. 对于 n 个元素的初始集合, 因为在每个子集合的拆分过程中, 都需要对集合进行遍历比较, 所以若对 k 个元素的集合进行拆分, 则比较次数级别为 O(k), 平均交换次数为 k/2, 即交换次数级别为 O(k).
累加可得快速排序的比较和交换复杂度为 nlogn ~ n<sup>2</sup>. 排序过程属于原地排序, 不需要额外的存储空间, 所以空间复杂度只有递归时的压栈复杂度: logn ~ n. 在对快排进行优化后, 还可以进一步避免复杂度退化的情况.

## 3 直接插入排序 Insertion Sort

插入排序是一种简单直观的排序算法. 它的工作原理是通过构建有序序列, 对于未排序数据, 在已排序序列中从后向前扫描, 找到相应位置并插入.
> **c.f. 插入排序 v.s. 冒泡排序 v.s. 选择排序**   
* 冒泡排序是通过在待排序集合中, 不断地比较和交换元素位置来确定极值, 然后标记该极值为已排序.
* 选择排序是通过比较待排序集合中的元素大小来确定极值位置, 然后交换元素位置, 构成已排序元素.
* 而插入排序的不同之处在于, 它是顺序选择待排序集合中元素, 依次添加到已排序集合中的适当位置上.  所以插入排序的操作主要作用于已排序集合上，而非待排序集合。

### 3.1 算法描述
一般来说, 插入排序都采用 in-place 在数组上实现. 具体如下：
+ 从第一个元素开始, 认为该元素已被排序;
+ 取出下一个元素, 在已经排序的元素序列中从后向前扫描;
+ 如果被扫描元素(已排序)>新元素, 待排序元素移到下一位置;
+ 重复步骤3, 直到找到已排序的元素小于或者等于新元素的位置, 将新元素插入到该位置后.
+ 重复步骤2~4, 直到待排序集合为空.

### 3.2 代码实现
```python
def insertion(nums): #直接插入排序
    for i in range(1,len(nums)):
        x,j = nums[i],i-1
        while j>-1 and x <nums[j]:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = x
    return nums
def insertion1(nums): #另一种写法
    for i in range(1,len(nums)):
        while i > 0 and nums[i] < nums[i-1]:
            nums[i],nums[i-1] = nums[i-1], nums[i]
            i-=1        
    return nums
```

### 3.3 二分插入排序

二分插入排序是对插入排序的一个小小的改进:
+ 改进的地方在于在前面已经排好序的序列中找当前要插入的元素的时候采用二分查找的方式去找那个插入的位置;
+ 找到待插入位置后, 再进行元素的移动.

```python
def insertion_bi(nums):
    for i in range(1,len(nums)):
        l,r,x = 0, i-1, nums[i]
        while l<=r:
            mid = (l+r)//2
            if nums[mid] > x:
                r = mid -1
            else:
                l = mid +1
        for j in range(i-1,l-1,-1):
            nums[j+1] = nums[j]
        nums[l] = x
    return nums
```

### 3.4 算法分析

插入排序是一种稳定排序算法, 排序过程中, 如果两个元素值相等, 则不交换元素位置. 它的复杂度和数据状况有关:
+ 最坏情况下, 如当序列为逆序时, 算法的交换复杂度和比较复杂度都为 O(n<sup>2</sup>);
+ 最好情况下, 当序列比较有序时, 每一次迭代过程中,  只需要做少量几次比较交换即可. 算法的比较复杂度为和交换复杂度基本是 O(n).  因此在工程上, 当数组比较有序时会使用.

## 4 希尔排序 Shell Sort

希尔排序是简单插入排序的改进版. 它与插入排序的不同之处在于, 它会优先比较距离较远的元素. 又称**缩小增量排序**.

### 4.1 算法描述
+ 设待排序元素序列有n个元素, 取一个整数 gap (<n) 作为间隔.
+ 将全部元素分为 gap 个子序列. 所有距离为 gap 的元素放在同一个子序列中.
+ 在每个子序列中分别实行直接插入排序.
+ 然后缩小间隔 gap, 重复步骤 2~3 至 gap=1 (直接插入排序).

![希尔排序图解](https://wx4.sinaimg.cn/mw690/006qmTkdly1g7gqdj4lhfj30p30hq0zz.jpg)

开始时, gap 取值较大, 每个子序列中的元素较少, 排序速度较快. 到排序后期 gap 取值逐渐变小, 子序列中元素个数逐渐增多, 但由于前面工作的基础, 大多数元素已经基本有序, 所以排序速度仍然很快.

### 4.2 代码实现
```python
def shell(nums):
    gap = len(nums)//2  #间隔, 每次砍半
    while gap >=1:
        for idx in range(0,gap): #一共gap各个组
            for i in range(idx+gap ,len(nums), gap): #从每组第二个元素开始进行插排
                while i > idx and nums[i] < nums[i-gap]: #插排的内循环
                    nums[i], nums[i-gap] = nums[i-gap],nums[i]
                    i -= gap
        gap //= 2
    return nums
```

### 4.3 算法分析

希尔排序的运行时间依赖于增量序列的选择.
> + 使用原始希尔增量时希尔排序的最坏情形运行时间为 O(n<sup>2</sup>).
+ Hibbard增量序列: 1,4,7,…,2<sup>k</sup>-1,...这个增量的特点是增量没有公因子.      
 使用Hibbard增量的希尔排序的最坏情形运行时间为 O(n<sup>3/2</sup>).
+ Sedgewick提出了几种增量序列，其中最好的是序列 {1,5,19,41,109,…}.
该序列中的项或者是 9\*4<sup>i</sup>-9\*2<sup>i</sup>+1 的形式, 或者是4<sup>i</sup>-3\*2<sup>i</sup>+1.
其最坏情形运行时间猜想为 O(n<sup>4/3</sup>).         

> c.f.: 希尔排序 v.s. 插入排序
+ 对于 n 个元素的序列, 由插入排序的结论可知, 插入排序的最好情况为序列处于已排序状态, 比较和交换复杂度为 O(n);  最坏情况为序列处于逆序状态, 比较和交换复杂度为 O(n<sup>2</sup>).
+ 对于希尔排序而言, 若分组的个数为 gap, 则每个分组的元素个数近似为 n/gap.
最好情况下(正序) 希尔排序的每个增量值对应的比较复杂度近似为O(nlogn), 交换复杂度0.
+ 不过对于希尔排序, 逆序并不一定为最坏情况, 因为增量值的变化规则是人为设定的. 即使给出的初始序列为逆序状态, 当增量值减为一的时候, 此时的序列一定相对于最初状态有序很多. 当增量值变化规则为2<Sup>k</Sup>-1 时, 比较和交换的时间复杂度最坏为 O(2<Sup>k3/2</Sup>).

## 5 简单选择排序 Selection Sort

选择排序的工作原理：首先在未排序序列中找到最小(大)元素, 存放到排序序列的起始位置.  然后, 再从剩余未排序元素中继续寻找最小(大)元素, 然后放到已排序序列的末尾.
> c.f.: 选择 v.s. 冒泡    
相同之处在于都维护了待排序集合和已排序集合, 每次迭代结束都会产生一个已排序元素. 不同之处在于冒泡排序的极值元素是通过不断的比较和交换位置产生的, 选择排序则是不断比较和一次交换位置产生. 所以相对冒泡排序, 性能上具有优势.

### 5.1 算法描述
+ 待排序集合为初始集合, 已排序集合初始为空.
+ 在待排序序列中找到最小元素, 放到已排序序列的末尾;
+ 重复步骤 2 至待排序集合为空.

### 5.2 代码实现
```python
def selection(nums):
    for i in range(len(nums)-1):
        idx = min(range(i,len(nums)), key = lambda x: nums[x])
        if idx !=i:
          nums[i], nums[idx] = nums[idx], nums[i]
    return nums
```

### 5.3 算法分析
最符合大家思维的算法. 但时间复杂度保持在 O(n<sup>2</sup>), 算法不稳定.

## 6 堆排序 Heap Sort
堆的详细描述见 [堆的介绍(最大堆)](/the-introduction-of-heap.md) .     
堆排序是指利用堆这种数据结构所设计的一种排序算法, 是一个反复调整堆的过程.

### 6.1 算法描述
* 利用待排序数组建立一个最大堆;
* 把堆顶元素和堆尾元素互换;
* 堆(待排序数组)尺寸 -1, 调整新堆
* 重复上述步骤至堆尺寸 =1.

### 6.2 代码实现
```python
def initialize(nums): #初始化最大堆
    n = len(nums)
    for i in range((n-1)//2,-1,-1):
        heapify(nums,i,n)
    return nums

def heapify(nums,i,n): #调整大小为n的堆的第i个元素
    if i>=n:return
    maxx = i
    if 2*i + 1 < n and  nums[maxx] < nums[2*i+1]:
        maxx = 2*i + 1
    if 2*i + 2 < n and nums[maxx] < nums[2*i+2]:
        maxx = 2*i + 2        
    if maxx != i:
        nums[maxx], nums[i] = nums[i], nums[maxx]
        heapify(nums,maxx,n)
    return

def heapsort(nums):
    nums = initialize(nums)
    for k in range(len(nums)-1,-1,-1):
        nums[0], nums[k] = nums[k], nums[0]
        heapify(nums,0,k)
    return nums
```
### 6.3 算法分析
堆排序是一种不稳定排序算法. 对于 n 个元素的序列, 构造堆过程时, 需要遍历的元素次数为O(n), 每个元素的调整次数为 O(logn), 所以构造堆复杂度为 O(nlogn). 迭代替换待排序集合首尾元素的次数为O(n), 每次替换后调整次数为  O(logn), 所以迭代操作的复杂度为 O(nlogn). 故总时间复杂度为 O(logn). 排序过程属于原地排序, 不需要额外的存储空间, 所以空间复杂度为 O(1).

## 7 归并排序 Merge Sort

归并排序是建立在归并操作上的一种有效的排序算法. 该算法是采用分治法 (divide and conquer) 的一个非常典型的应用. 将待排序集合拆分为多个子集合, 对子集合排序后, 合并子集合成为较大的子集合, 不断合并最终完成整个集合的排序.  
> 以下所讲归并都是指二路归并:    
之前的简单选择/冒泡/直接插入排序都是维持一个待排序集合和一个已排序集合, 在每次的迭代过程中从待排序集合中移动一个元素到已排序集合中, 通过不断的迭代来完成排序, 所以需要进行的迭代次数一般都是 O(n) 级别. 而归并排序则是每轮迭代消除半数的待排序子集合, 所以需要进行的迭代次数为 O(logn) 级别.

### 7.1 top down (递归)算法描述

+ 把长度为n的待排序序列分成两个长度为n/2的子序列;
+ 对这两个子序列分别采用归并排序;
+ 将两个排序好的子序列合并成一个最终的排序序列.

### 7.2 top down (递归)代码实现
```python
def merge(nums, left, mid, right): #合并
    idx1, idx2, idx = left, mid +1, 0
    new = [None] *(right - left +1)
    while idx1 <=mid and idx2 <=right and idx <= right-left:
        if nums[idx1] > nums[idx2]:
            new[idx] =nums[idx2]
            idx2 += 1
        else:
            new[idx] =nums[idx1]
            idx1 += 1
        idx +=1
    while idx1 <=mid :
        new[idx] =nums[idx1]
        idx, idx1 = idx+1, idx1+1
    while idx2 <=right:
        new[idx] =nums[idx2]
        idx, idx2 = idx+1, idx2+1
    for i in range(left,right+1):
        nums[i] = new[i-left]

def mergesort(nums,left,right): #递归
    if right <= left:return
    mid = (left+right)//2
    mergesort(nums,left, mid)
    mergesort(nums, mid+1, right)
    merge(nums,left,mid,right)
```
### 7.3 bottom up (迭代)代码实现
```python
def iterative_mergesort(nums):
    n, gap = len(nums), 1
    while gap < n:
        left = 0
        while left + gap < n:
            mid = left +gap-1
            right = min(n-1,mid+gap)
            merge(nums,left,mid,right)
            left = right+1
        gap <<= 1
```
省略了 O(logn)的压栈空间, 本质上迭代和递归没有太大差别.  


### 7.4 算法分析

归并排序是一种稳定排序算法, 排序过程中, 如果两个元素值相等, 则不交换元素位置. 对于 n 个元素的序列, 根据算法执行的比较次数和元素移动次数可知, 算法的时间复杂度为 O(nlogn). 算法执行过程中, 需要申请额外的序列空间来保存临时元素, 所以算法的空间复杂度为 O(n).


## 8 计数排序 Counting Sort

计数排序有着线性时间复杂度, 是一种快于任何比较排序算法的排序算法. 其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中, 因此计数排序要求输入的数据必须是有确定范围的整数.

### 8.1 算法描述

+ 找出待排序的数组 arr 中最大和最小的元素max, min, 构造新数组 count 长度为 max-min+1;
+ 统计数组中值为 i 的元素出现的次数, 存入新数组 count 的第 i-min 项;
+ 对 count 中所有的计数累加 (从第一个元素开始, 每一项和前一项相加), 这时候 count[arr[i]] 表示的值就是小于等于 arr[i] 的元素的个数;
+ 反向填充目标数组 temp: 将数组元素 arr[i] 放在 temp 的第 count[arr[i]-min]-1 处, 每放一个元素就将 count[arr[i]] 减去1, 这样可以确保计数排序的稳定性.

### 8.2 代码实现
```python
def counting(nums): #计数排序
    maxx, minn = max(nums), min(nums)
    count = [0]*(maxx-minn+1)
    for x in  nums: #构造计数数组
        count[x-minn] += 1
    for i in range(1,len(count)): #计数数组累加
        count[i] += count[i-1]
    temp = [None] * len(nums)
    for i in range(len(nums)-1,-1,-1): #反向填充, 维持稳定性
        temp[count[nums[i] - minn]-1] = nums[i]
        count[nums[i] - minn] -= 1
    return temp
```

### 8.3 算法分析

计数排序的优势在于在对一定范围内的整数排序时, 它的时间/空间复杂度均为 Ο(n+k)(其中k是整数的范围). 当然这是一种牺牲空间换取时间的做法. 由此可知, 计数排序只适用于元素值较为集中的情况, 若数组中最大最小元素值相差甚远, 即 O(k) > O(nlogn) 的时候其效率反而不如一些基于比较的排序.  
通过额外空间的作用方式可知, 若待排序集合中的元素值为浮点数形式或其他形式, 则需要对元素值或元素差值做变换, 以保证所有差值都为一个非负整数形式.  

## 9 桶排序 Bucket Sort

桶排序是将待排序集合中处于同一个值域的元素存入同一个桶中, 即根据元素值特性将集合拆分为多个区域, 形成的这些桶从值域上看是有序的. 再对每个桶中元素进行排序, 则所有桶中元素所构成的集合是已排序的.

> **c.f. 桶排序 v.s. 计数排序**  
桶排序是对计数排序的改进, 计数排序申请的额外空间跨度从min value 到max value, 若待排序集合中元素不是依次递增的, 则必然有空间浪费情况. 桶排序则是弱化了这种浪费情况, 将 min ~ max 之间的每一个位置申请空间, 更新为 min 到 max 之间每一个固定区域申请空间, 减少了元素值大小不连续情况下的空间浪费情况.

> **c.f.: 桶排序 v.s. 快排**     
快速排序是将集合拆分为两个值域(桶), 再分别对两个桶进行排序. 桶排序则是将集合拆分为多个桶, 对每个桶进行排序.  两者不同之处在于, 快排是在集合本身上进行排序, 属于原地排序方式, 且对每个桶的排序方式也是快排. 桶排序则是提供了额外的操作空间, 在额外空间上进行排序, 避免了构成桶过程的元素比较和交换操作，同时可以自主选择恰当的排序算法对桶进行排序。

### 9.1 算法描述

+ 据待排序集合中最大元素和最小元素的差值范围和映射规则等,, 确定申请的桶个数 (一般选择定量数组为空桶);
+ 扫描序列, 根据每个元素的值所属区间 (可以设置一个映射函数), 放入指定的桶中(顺序放置) [此时原序列可以看成空的];
+ 对每个不是空的桶中的元素进行排序 (使用其它排序算法或以递归方式继续使用桶排序), 并移动到已排序集合中.  

### 9.2 代码实现
```python
def bucket(nums):
    maxx, minn  = max(nums), min(nums)
    dic = [[] for i in range(maxx//10 - minn//10 +1)]
    for x in nums:
        idx = x//10 -minn//10
        dic[idx].append(x)
    nums.clear()
    for col in dic: #每个列调用快排排序
        print(col)
        twoway_quick(col,0,len(col)-1)
        nums.extend(col)
        print(col)
```
### 9.3 算法分析

桶排序是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。桶排序 (Bucket sort)的工作的原理：假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排）。

桶排序最好情况下使用线性时间O(n)，桶排序的时间复杂度，取决与对各个桶之间数据进行排序的时间复杂度，因为其它部分的时间复杂度都为O(n)。很显然，桶划分的越小，各个桶之间的数据越少，排序所用的时间也会越少。但相应的空间消耗就会增大。


桶排序过程中存在两个关键环节:       
* 元素值域的划分，也就是元素到桶的映射规则。映射规则需要根据待排序集合的元素分布特性进行选择，若规则设计的过于模糊、宽泛，则可能导致待排序集合中所有元素全部映射到一个桶上，则桶排序向比较性质排序算法演变。若映射规则设计的过于具体、严苛，则可能导致待排序集合中每一个元素值映射到一个桶上，则桶排序向计数排序方式演化。
* 排序算法的选择，从待排序集合中元素映射到各个桶上的过程，并不存在元素的比较和交换操作，在对各个桶中元素进行排序时，可以自主选择合适的排序算法，桶排序算法的复杂度和稳定性，都根据选择的排序算法不同而不同。


## 10 基数排序 Radix Sort

基数排序属于 "分配式排序", 也可以称为多关键字排序, 是按照不同的位数，或者优先级来排列某个元素，同计数排序类似，也是一种非比较性质的排序算法. 将待排序集合中的每个元素拆分为多个总容量空间较小的对象, 对每个对象执行桶排序.  

> **基数排序 v.s. 桶排序**        
 桶排序需要选择适当的**映射规则**, 来完成集合中元素到多个桶的映射, 也可以称之为值域划分. 但它对元素总容量敏感, 当集合中元素跨度很大时, 映射规则的设计比较困难:
 * 若规则设计的宽泛一些, 桶的个数较少, 可以避免很多空桶的情况, 但是可能会存在元素分布不均, 桶排序则演变为普通的比较性质排序;
 * 若规则设计的较为精确, 则桶的个数较多, 可能会存在大部分桶都是空桶的情况, 空间浪费较大.                          

> 基数排序在桶排序的基础上做了优化.
它在排序过程中也使用了桶排序操作, 不过对于桶排序面向的对象进行了优化. e.g., 若元素是 int, 则选择 1\~10 作为排序对象, 则每一位的容量空间大小只有 10; 同理若元素是 str，则选择 a\~z(A\~Z) 可使得每个字符的容量空间大小为 26. 此时每个桶宽度, 或者称为值域跨度为一. 因此将待排序集合中所有元素移动到各个桶上之后, 不需要再对每个桶进行排序.

### 10.1  基数排序分为两种模式:
* Least significant digit (LSD) - 最低位优先法    
短的关键字被认为是小的, 排在前面,
然后相同长度的关键字再按照词典顺序或者数字大小等进行排序.
e.g.: 1, 2, 3, 10, 或者 "b, c, d, e, ab".     
* Most significance digit (MSD) - 最高位优先法     
直接按照字典的顺序进行排序, 对于字符串, 单词或者是长度固定的整数排序比较合适.
e.g.: 1, 10, 2, 3 或者 "ab, b, c, d, e".     
   > 假设我们有一些二元组(a, b),
要对它们进行以 a 为首要关键字, b的次要关键字的排序.
则可以:
  * 先按照首要关键字排序, 分成首要关键字相同的若干堆;
  * 再按照次要关键值分别对每一堆进行单独排序;
  * 最后再把这些堆连到一起, 使首要关键字较小的堆排在上面.

### 10.2 算法描述 (用 LSD 实现数组排序)
* 将所有待比较正整数统一为数组中最大数的位数, 数位较短的数前面补零;
* 从最低位开始进行基数为10的计数排序, 将所有元素移动到对应的桶中;
* 再将所有桶中元素移动回原始集合中,
* 重复上述步骤至最高位计数排序之后, 此时数列就是有序的.

### 10.3 代码实现
```python
def radix(nums):
    n = len(str(max(nums))) #取得位数
    dic = [collections.deque() for i in range(10)] #桶,用双向队列方便点
    for i in range(n):#从低位到高位比较
        for x in nums:
            dic[(x//(10**i)) %10].append(x)
        inn = 0
        for k in range(len(nums)):
            while not dic[inn]:
                inn+=1
            nums[k] = dic[inn].popleft()
    return nums
```


### 10.4 算法分析

易知基数排序的时间复杂度为 O(nr)，其中 r 为元素最大位数, 也就是迭代比较的次数. 且算法过程中不存在元素之间的跨位置交换, 因此属于稳定排序方式. 需要申请的空间大小为 n+k. 其中 k: 待排序元素的基数, 是一个定值.

基数排序不一定要按照每一位进行排序, 也可以用元素中的几位构成的组合做基数. 同时排序算法也不一定是桶排序方式, 可以是别的排序算法, 也可以给不同位使用不同的排序算法. 总之基数排序提供了一个针对**复杂元素类型**的排序思路, 可以针对元素中不同部分, 选择不同的排序方式.




## 参考资料  

+ [各种排序算法总结(全面)](https://github.com/ZXZxin/ZXBlog/blob/master/%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E7%AE%97%E6%B3%95/Algorithm/Sort/%E5%90%84%E7%A7%8D%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95%E6%80%BB%E7%BB%93(%E5%85%A8%E9%9D%A2).md)

+ [十大经典排序算法](http://www.sohu.com/a/258093323_650579)

+ [常用排序算法介绍](https://github.com/zhipingChen/SortingAlgorithm)

+ [数据结构排序算法之快速排序演示](https://www.bilibili.com/video/av18980345?from=search&seid=17123423182247162402)

+ [004 快速排序（四） 双路排序](https://www.jianshu.com/p/e0364a3166f9)

+ [理解希尔排序的排序过程](https://blog.csdn.net/weixin_37818081/article/details/79202115)

+ [数据结构排序算法之希尔排序演示](https://www.bilibili.com/video/av17062242?from=search&seid=15487942313356277630)

+ [希尔排序与堆排序](https://www.bilibili.com/video/av15961896)

+ [数据结构排序算法之堆排序演示](https://www.bilibili.com/video/av18980178)

+ [堆排序(heapsort)](https://www.bilibili.com/video/av47196993)

+ [桶排序-算法思想](https://www.bilibili.com/video/av55573441)
