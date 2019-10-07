# 总结(51-100)

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
  **[法2]** Divide and conquer. 时间复杂度 O(N\log(N)).   
将数组cut, 则最大子序应该在: ① 左子数组; ② 右子数组; ③横跨左右子数组. 分别计算并最后取最大值即可.      

54. **Spiral Matrix. [M]**   
贪吃蛇走法/ 逐层走法. 没啥意思.  

55. **Jump Game. [M]**    
45 的简化版. 考点还是 Greedy.  

56. **Merge Intervals. [M]**    
 **[法1]** 只要想到排序, 这道题很好写. `intervals.sort(key=lambda x: x[0])`    
 **[法2]** 不同sort, 使用 graph + BFS 做. 可惜 TLE.

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
77. **Combinations. [M]**
78. **Subsets. [M]**
79. **Word Search. [M]**
80. **Remove Duplicates from Sorted Array II. [M]**
81. **Search in Rotated Sorted Array II. [M]**
82. **Remove Duplicates from Sorted List II. [M]**
83. **Remove Duplicates from Sorted List. [E]**
84. **Largest Rectangle in Histogram. [H]**
85. **Maximal Rectangle. [H]**
86. **Partition List. [M]**
