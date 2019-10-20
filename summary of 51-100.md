# 总结(51-100)

> => 应该掌握的知识点: DFA(确定有穷自动机), 正则表达式, 牛顿法, Binets 方法, 计数排序, 三路快排, 位运算, 树, DFS/BFS, 线段树, morris 遍历, cantalan 数, 中序遍历.
> => 再次出现的知识点: 回溯, 单调栈, 动态规划, 分治, 贪婪, 双向队列, 滑动窗口.      
> => 待掌握:  Floyd 算法.

51. **N-Queens. [H]**   
经典的 N 皇后回溯问题. 画好递归树(dfs), 做好剪枝,设置好四个方向的状态即可. 没什么难的.    

52. **N-Queens II. [H]**    
同上一道问题. 没啥难的.   

53. **Maximum Subarray. [E]**    
你以为是 **Dynamic programming**的? 其实是我 **divide and conquer** 哒!      

  **[法1]** Dynamic programming => Two pointers. 时间复杂度 O(N).
```
dp = num[:]#dp[i]: 以i为最后下标的最大子序和, 则初始 dp[i] = nums[i]
dp[i] = max (dp[i],dp[i]+dp[i-1]) #i>0 时的状态转移函数
```
  **[法2]** Divide and conquer. 时间复杂度 O(Nlog(N)).   
将数组cut, 则最大子序应该在: ① 左子数组; ② 右子数组; ③横跨左右子数组. 分别计算并最后取最大值即可.      

54. **Spiral Matrix. [M]**   
贪吃蛇走法/ 逐层走法. 没啥意思.  

55. **Jump Game. [M]**    
45 的简化版. 考点还是 Greedy.  

56. **Merge Intervals. [M]**    
 **[法1]** 只要想到排序, 这道题很好写. `intervals.sort(key=lambda x: x[0])`    
 **[法2]** 不用sort, 使用 graph + BFS 做. 可惜 TLE.

57. **Insert Interval. [H]**       
 **[法1]** 看作57的子问题.    
 **[法2]** 利用有序结合二分法 (或者按顺序) 寻找插入区间待插入的位置,再进行判断插入.
  !!!但插入/删除列表元素, 复制新列表仍需要 O(N)时间复杂度. 所以事实上时间复杂度并没有变.

58. **Length of Last Word. [E]**   
很简单...大概需要看看字符串函数?

59. **Spiral Matrix II. [M]**    
lc54 的反向. 贪吃蛇走法/ 逐层走法.

60. **Permutation Sequence. [M]**   
联动 41/46. 回溯时要注意两个地方: 利用 k//(idx!) 和 k%(idx!) 递归,
选择某个值后要删除切片元素/ 移动剩余所有元素位置(时间复杂度好像是O(N^2)). [代码容易出错的地方太多, 就记下解题思路吧.]

61. **Rotate List. [M]**    
需要注意的是可能 **k >n=len(list)**.
两次遍历: 第一次得到n, 第二次移动**k%n**位列表. 不需要双指针. (循环列表可能会超时, 不可取.)  


62. **Unique Paths.[M]**          
 **[法1]** 简单 dynamic programming. `dp[i][j]=dp[i-1][j]+dp[i][j-1]`, 还可以精简为一维dp.     
 **[法2]** 公式直接算. 从 `start` 到 `finish` 一共 `m-1+n-1` 个格子
 (不包括 `finish`), 其中 `m-1`次r, `n-1` 次d => 格子数 `C^{n-1}_{m+n-2}`.
  即:  ` ans = math.factorial(m+n-2) / math.factorial(m-1) / math.factorial(n-1)`

63. **Unique Paths II. [M]**   
lc62的升级版, 修复了直接调用数学公式的bug. 还是简单 dynamic programming. `dp[i][j]=dp[i-1][j]+dp[i][j-1] if not obstacleGrid[i][j] else 0`, 也可以精简为一维dp.    
(C++ 好像还有数据太大超出范围的问题?=> long long )

64. **Minimum Path Sum. [M]**    
lc62的升级版, 依旧是很简单的 dynamic programming. `dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])`. 同样可以精简为一维 dp 数组.  

65. **Valid Number. [H]**  
[github](https://github.com/YawningLiu/leetcode/blob/master/65-valid-number.md) 已写.
 **[法1]** 暴力直接法.  **[法2]** DFA.
  **[法3]** 正则表达式匹配. **[法4]** py3 作弊法.  

66. **Plus One. [E]**    
 简单+1, 就是这么简单.  

67. **Add Binary. [E]**     
 2进制求和. 也很水.

68. **Text Justification. [H]**    
没什么技巧, 就是模拟放置, 空格计算涉及到取商和取余. 所以也没啥意思.

69. **Sqrt(x). [E]**    
计算 根号x, 二分法/牛顿法, 也没什么意思.

70. **Climbing Stairs. [E]**    
斐波那契(Fibonacci) 数列. 动态规划 / 直接套公式 / Binets 方法.    
  Binets 方法: Q = [1, 1 ; 1, 0 ];
  Q<Sup>N+1</Sup> = [F<Sub>N+1</Sub>, F<Sub>N</Sub> ;
  F<Sub>N</Sub>, F<Sub>N-1</Sub> ].  
  用快速求幂法时间复杂度 O(logN).     

71. **Simplify Path. [M]**    
把所给出的路径化简为 unix 的绝对路径, 根据题意写就行. 没啥意思.

72. **Edit Distance. [H]**    
 **[法1]** Dynamic programming. 状态转移方程:
 ```
 # 初值:dp[0][i] = i, dp[j][0] = j
     if word1[i-1]==word2[j-1]:
         dp[j][i]=dp[j-1][i-1]
     else:
         dp[j][i]=min(dp[j][i-1],dp[j-1][i-1],dp[j-1][i])+1  #选择步数最小的方法
 ```
 **[法2]** 双向队列 `collections.deque` (其实就是把递归的压栈改成储存于数组), 注意要设置 visited 防止重复的结果. 关键步骤:
 ```
 q.extend([(w1[1:], w2[1:], d), (w1, w2[1:], d), (w1[1:], w2, d)])
 ```

73. **Set Matrix Zeroes. [M]**     
难点在于 O(1) space. 其实也没什么意思....    
  **法1**: 用2个常数记录第1行/列来记录矩阵其他行列是否有0,
再用第1行/列来记录矩阵其他行列是否有0.    
  **法2**: 找一个不存在于矩阵中的值为标记值; 第一次遍历矩阵,
  将0出现的行/列改为标记值; 第二次遍历矩阵, 将标记值改为0.

74. **Search a 2D Matrix. [M]**    
直接用二分法即可. 没什么意思.    

75. **Sort Colors. [M]**     
  即 [荷兰国旗问题](https://www.jianshu.com/p/356604b8903f).
  **法1**: counting sort.     
  **法2**: 题目要求的一次遍历 + 常数空间. 双指针, 类似三路快排.

76. **Minimum Window Substring. [M]**    
  **sliding window** 典型题目. 具体使用了哈希表(充当计数器) 和 双指针(实现窗口滑动).

77. **Combinations. [M]**    
回溯 (递归) / 迭代 (字符序) / 动态规划.    
熟记就行. 库函数:
```
return list(itertools.combinations(range(1, n+1), k))
```

78. **Subsets. [M]**    
方法很多. **[法1] 常用解法**: 迭代 / 递归 / 库函数.
  ```
  res = []
  for i in range(len(nums)+1):
      for tmp in itertools.combinations(nums, i):  # 库函数
        res.append(tmp)
  return res
  ```
  **[法2] 位运算**. 数组中每个数字分为在子数组中和不在子数组中, 即 为1, 0, 且在二进制下对应唯一的数字.

79. **Word Search. [M]**    
DFS 标准算法 (也就是回溯). 把矩阵看做一个图, 利用图的深度优先遍历即可. 注意 状态重置 / 记录状态是否遍历过.   

80. **Remove Duplicates from Sorted Array II. [M]**    
lc-26 升级版. 原地删除就是快慢指针, 一个指向被遍历元素, 一个指向待写入位置.   

81. **Search in Rotated Sorted Array II. [M]**    
lc-33 升级版. 有重复数字时的情况. 讨论下特殊情况即可.     

82. **Remove Duplicates from Sorted List II. [M]**    
  **[法1]** 哑节点 + 快慢指针 / **[法2]** 递归.

83. **Remove Duplicates from Sorted List. [E]**    
lc-82 的简单版. 没啥意思.

84. **Largest Rectangle in Histogram. [H]**    
  **[法1]**  **stack**. O(n) time. 类似42题的单调栈法. 为了精简代码, 利用 py3 特性增加: `height.append(0)`. 即矩阵末尾添加 0 元素.      
  **[法2]** **divide and conquer**. O(nlogn) time. 类似归并排序, 矩阵平均分为两个子矩阵 + middle列, 递归求子矩阵最大值, 再求横跨两个子矩阵的最大值, 取最大.            
  **[法3]** **divide and conquer + segment tree**. O(nlogn) time.
  上面的分治是利用从中间等分, 这里的分治是从最小值处划分, 类似快排.
  (线段树的使用就是为了排除最小值在极限情况下时间复杂度又变成了O(n<Sup>2</sup>) 的情况)     
  **[法4]** 找下标. O(n) time. 利用两个数组分别记录 A[i] 左/右 分别比之小第一个数的下标,
  类似单调栈, 计算这两个数组时每个i最多出现2次, 因此这个方法耗时也是线性的.  

85. **Maximal Rectangle. [H]**     
    **[法1]** 利用 84题的解法即可 (栈的解法).   
    **[法2]** 动态规划. 如何确定最优子结构 + 如何利用最优子结构来推导当前最优解.
    对于矩阵上里每一行, 找出比当前值小的最近左 / 右 下标 (类似84的解法4).

86. **Partition List. [M]**     
链表划分为大于和小于x的两部分, 链表基础操作, 不难.

87. **Scramble String. [H]**     
  **[法1]** 剪枝的递归.  两个需要注意的点:
  ① `sort` 的妙用 => 节省了很多不必要的时间;
  ② hash 表的 使用 => 储存已得到的结果, 即剪枝.   
  **[法2]** 动态规划. 即正向使用递归. 需要三维动态矩阵来储存结果.

88. **Merge Sorted Array. [E]**    
双指针. 分为: 从前往后添加 (常见) / 从后往前添加 (省去了更多的数据移动, 牛逼!).

89. **Gray Code. [M]**    
  **[法1]** 类似集合取子集时的回溯.    
  **[法2]** 位运算. 利用格雷码的定义: ` G(i) = i ^ (i//2)`.
  ```
  return [i ^ i >> 1  for i in range(1 << n)]
  ```
    **[法3]** 镜像反射法 + 数学归纳法. 已知G(n), 则      
    `G(n+1) = ( [0] + G(n) ) ∪ ( [1] + Reverse(G(n)) )`.

90. **Subsets II. [M]**     
lc-78 升级版, 增加了重复数字的影响. 这时就需要**排序**. **回溯**标准题, 排序后注意剪枝即可.  (**迭代**也可以, 但是没那么显然: 另需一个指标记录当前数字出现多少次, 再与当前被选择数组比较.)

91. **Decode Ways. [M]**    
递归 / 动态规划. 可以由 n 维dp数组缩减为常数 dp 变量.

92. **Reverse Linked List II. [M]**    
链表基础题. 多画图即可, 注意题目要求只能遍历一次.

93. **Restore IP Addresses. [M]**      
简单回溯(dfs)题. (其实暴力也能做, 因为数组不大).     
IP格式: 4部分, 每部分 0~255, 且不能出现以0开头的多位数.  

94. **Binary Tree Inorder Traversal. [M]**    
二叉树遍历标准题目.  **[法1]** 递归; **[法2]** 迭代 + 栈;        
 **[法3]** **Morris Traversal**. 不需要额外空间,  但会破坏树的结构. 把根节点挪到其左节点的最右叶子节点,根节点的左节点设为空.     
 => 不破坏树结构: 在寻找最右叶子节点时, 分为两类: 空(添加根节点) / 等于当前根节点 (删去最右叶子节点). [代价: 耗费更多时间.]

95. **Unique Binary Search Trees II. [M]**     
递归. 可以利用左右子树**同构** + 记忆化词典节省空间. (动态规划太复杂, 特点不够鲜明.)    

96. **Unique Binary Search Trees. [M]**   
  **[法1]** 动态规划. 状态转移方程比较简单.     
   => 还可以利用**对称性**减少循环步骤.      
  **[法3]** **cantalan 数**. 利用公式计算即可:
  C<Sub>​n</sub>=(2n)∗(2n−1)∗...∗(n+1)/(n+1)!      
  ![排序图](https://wx4.sinaimg.cn/mw690/006qmTkdly1g82q4b6hr0j307q01wdfp.jpg)

97. **Interleaving String. [H]**      
  **[法1]** 二维动态规划. (记忆法回溯也可)  dp[i][j] 表示 s1[:i] & s2[:j] 与 s3[:i+j] 是否匹配,
  比较简单, 还可以简化为一维的动态规划.      
  **[法2]** BFS / DFS + 双向队列 / 栈. 模拟图的遍历(向下/向右遍历),
  建立 m*n 矩阵, 并用visited记录已遍历过的点.
  如果当前点能走通就加入队列.       
  [DFS 也是相同思路, 把队列换成栈即可.]      

98. **Validate Binary Search Tree. [M]**   
  **[法1]** 递归(即 DFS). 在普通 DFS 递归的基础上加上最小/大值的递归即可.     
  **[法2]** BFS / DFS + 双向队列 / 栈. 用队列/栈保存bool变量 + 最大/小值.  
  **[法3]** **中序遍历**. 边遍历边比较当前数字是否比前一个数字大.

99. **Recover Binary Search Tree. [H]**     
[注: 只有两个节点被交换.] (递归法太暴力了, 不写了.)  
本题在BST里交换了两个数字, 即在有序序列中交换了两个数字,  
因此本质还是中序遍历. 利用 lc-94的三种遍历方法均可.   
交换两个数字分为以下两种情况:
+ 相邻的两个数字交换, 产生一组逆序对.
+ 不相邻的两个数字交换, 产生2组逆序对. 被交换的数字就是第一组逆序对的前者和第二组逆序对的后者.  


100. **Same Tree. [E]**    
方法很多: 前序 / 中序 / 后序 / 层次遍历. 又可细分为 递归/ 迭代+栈 / morris 遍历.
