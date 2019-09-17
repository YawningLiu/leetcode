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
62. **Unique Paths.[M]**
63. **Unique Paths II. [M]**
64. **Minimum Path Sum. [M]**
65. **Valid Number. [H]**
66. **Plus One. [E]**
67. **Add Binary. [E]**
68. **Text Justification. [H]**
69. **Sqrt(x). [E]**
70. **Climbing Stairs. [E]**

