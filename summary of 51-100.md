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
**[法2]** 利用有序结合二分法 (或者按顺序) 寻找插入区间待插入的位置,再进行判断插入.  !!!但插入/删除列表元素, 复制新列表仍需要 O(N)时间复杂度. 所以事实上时间复杂度并没有变. 

58. **Length of Last Word. [E]**   
很简单...大概需要看看字符串函数?

59. **Spiral Matrix II. [M]**    
lc54 的反向. 贪吃蛇走法/ 逐层走法.

60. **Permutation Sequence. [M]**   
联动 41/46. 回溯时要注意两个地方: 利用 k//(idx!) 和 k%(idx!) 递归, 选择某个值后要删除切片元素/ 移动剩余所有元素位置(时间复杂度好像是O(N^2)). [代码容易出错的地方太多, 就记下解题思路吧.]
  
61. **Rotate List. [M]**    
需要注意的是可能 **k >n=len(list)**. 两次遍历: 第一次得到n, 第二次移动**k%n**位列表. 不需要双指针. (循环列表可能会超时, 不可取.)  
 

62. **Unique Paths.[M]**    
**[法1]** 简单 dynamic programming. `dp[i][j]=dp[i-1][j]+dp[i][j-1]`, 还可以精简为一维dp.     
**[法2]** 公式直接算. 从 `start` 到 `finish` 一共 `m-1+n-1` 个格子 (不包括 `finish`), 其中 `m-1`次r, `n-1` 次d => 格子数 `C^{n-1}_{m+n-2}`. 即:  ` ans = math.factorial(m+n-2) / math.factorial(m-1) / math.factorial(n-1)`

63. **Unique Paths II. [M]**   
lc62的升级版, 修复了直接调用数学公式的bug. 还是简单 dynamic programming. `dp[i][j]=dp[i-1][j]+dp[i][j-1] if not obstacleGrid[i][j] else 0`, 也可以精简为一维dp.    
(C++ 好像还有数据太大超出范围的问题?=> long long )
 
64. **Minimum Path Sum. [M]**    
lc62的升级版, 依旧是很简单的 dynamic programming. `dp[i][j] = grid[i][j] + min(dp[i-1][j],dp[i][j-1])`. 同样可以精简为一维 dp 数组.  

65. **Valid Number. [H]**    
**[法1]** 暴力直接法, WA了好多次orz...    
**[法2]** DFA.   
![dfa](https://wx2.sinaimg.cn/mw690/006qmTkdly1g73xfzx39rj323l1qitqs.jpg)
**[法3]** 正则表达式匹配.   
**[法4]** py3 作弊法.  
```
        try: float(s)
        except: return False
        return True
```

66. **Plus One. [E]**
67. **Add Binary. [E]**
68. **Text Justification. [H]**
69. **Sqrt(x). [E]**
70. **Climbing Stairs. [E]**

