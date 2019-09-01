# 总结(1-100)

1. **Two Sum. [E]**   
hashmap, 没啥难点.  

2. **Add Two Numbers. [M]**   
链表相加,注意进位就ok.

3. **Longest Substring Without Repeating Characters. [M]**    
 **[法1]** Two pointers + Hash map 是很容易想到的一个方法(遍历2次).  
 **[法2]** 而 Hashmap 储存字符对应**下标**可以进行优化(遍历1次). 注意下标与子串长度的关系. 
4. **Median of Two Sorted Arrays. [H]**   
Binary search / Divide and conquer.  当时看感觉很难~   
 **[法1]** i.e. 二分法寻找**第k小的数**, 比较两个数组第k//2个数,并删去一半. 故时间复杂度 = O( $log$ k) = O($log$ (m+n) ).    
 **[法2]** 二分法割数组,使两边长度相同, 且左边max<=右边min. 时间复杂度 O( $log$ min(m,n)). 虽然比上一种快一点, 但判断界定边界极值太恶心了. (以前做+现在做红了15次, 第k小可是一次过的.) => 遇到了可以口头表述一下, 手撕还是算了吧. 

5. **Longest Palindromic Substring. [M]**   
 **[法1]** 动态规划, 时间复杂度 O(n^2). 没写,大概思路如下:   
```
#初始状态 
dp[i][i]=1  
dp[i][i+1]=1 if str[i]==str[i+1] else 0
#状态转移方程
dp[i][j] =dp[i+1][j-1] if str[i]==str[j] else 0
```
 **[法2]** 中心扩展法, 时间复杂度 O(n^2). 很简单.     
 **[法3]**  ***[Manacher's Algorithm 马拉车算法](https://blog.crimx.com/2017/07/06/manachers-algorithm/)***, 时间复杂度 O(n). 例如 "abbaopxpo" 中, idx = 16 时, 可达到的最右边界 c+p[c] = 14+5 = 19 > idx, 则 P[idx] = min(P[2*c-i], c+P[c]-i). 在用中心扩展法扩展P[idx].

|id|0 |1 |2 |3 |4 |5 |6 |7 |8 |9 |10|11|12|13|14|15|16|17|18|19|20|     
|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|--|       
|s |\$|\#|a |\#|b |\#|b |\#|a |\#|o |\#|p |\#|x |\#|p |\#|o |\#|\&|    
|P |0 |0 |1 |0 |1 |4 |1 |0 |1 |0 |1 |0 |1 |0 |5 |0 |1 |0 |1 |0 |0 |        

6. **ZigZag Conversion. [M]**   
找规律, 没啥意思.

7. **Reverse Integer. [E]**   
大概考点是int型溢出. 鉴于 py3 不会溢出, 先pass, 以后用 C++时再说.

8. **String to Integer (atoi). [M]**   
思路很简单,注意的是溢出, 以及py3 **正则表达式** `r'^[+|-]?\d+'`.   

9. **Palindrome Number. [E]**  
用好整除和取余, 很简单.   

10. **Regular Expression Matching. [H]**   
[知乎](https://zhuanlan.zhihu.com/p/72179123) 写过了. Backtracking 和 Dynamic programming. 重点在于匹配方法. 
```
#状态转移方程:
if p[j-1]!='*':
    dp[i][j] = dp[i-1][j-1] and (p[j-1] == s[i-1] or p[j-1] == ".")
else: 
    dp[i][j] = (dp[i-1][j] and (p[j-2] == s[i-1] or p[j-2] == ".")) or dp[i][j-2]
#py自带函数
re.match(p, s)
```

11. **Container With Most Water. [M]**     
Two pointers. 时间O(n), 空间O(1). 可以看作二叉线段树精简为双指针(?): e.g. [1,8,6,2,5,4,8,3,7]. (力扣里找的大佬的图片.)  
<img src="https://wx4.sinaimg.cn/mw690/006qmTkdly1g6c9578ec6j30n20kvmyx.jpg" width = "300" height = "200" alt="大佬图片" 
align=center>   
所以, 由双指针特性, 短边对应的被删除部分面积一定<当前面积.

12. **Integer to Roman. [M]**  
阿拉伯数字->罗马数字, 没啥意思. 

13. **Roman to Integer. [E]**  
罗马数字->阿拉伯数字, 没啥意思. 

14. **Longest Common Prefix. [E]**   
[知乎](https://zhuanlan.zhihu.com/p/72598654)写过了...就不写了.    
 **[法1]** 垂直比较.     
 **[法2]** 水平比较 => 叠加分治使得速度更快.   
引申: **[208. Implement Trie (Prefix Tree)](https://leetcode.com/problems/implement-trie-prefix-tree/)**.

15. **3Sum. [M]**  
总结过了. Sort + Two pointers / Hashmap.

16. **3Sum Closest. [M]**  
总结过了. Sort + Two pointers + 排除无用循环.

17. **Letter Combinations of a Phone Number. [M]**  
Backtracking.  只要会递归就好, 没啥特点.

18. **4Sum. [M]**  
总结过了. Sort + 剪枝.  

19. **Remove Nth Node From End of List. [M]**   
Two pointers (快慢指针). 链表基础操作.

20. **Valid Parentheses. [E]**   
Stack 基础操作.  

21. **Merge Two Sorted Lists. [E]**   
链表基础操作. 

22. **Generate Parentheses. [M]**   
Backtracking. 有两种回溯法.    
 **[法1]** 对左括号和右括号回溯 (设定index, 出现 "(" , " )" 时 index 分别怎么变化.)    
 **[法2]** 对括号闭合数 (Closure Number) 回溯. n组括号可以分为被一个大括号裹着的 i+1 个括号和另外 n-i-1 个括号.    

23. **Merge k Sorted Lists. [H]**   
21的扩展. divide and conquer. (Heap=>Priority Queue)   
 **[法1]** 暴力求解. lists -> array -> array.sort() -> lists. 时间复杂度 O(N$log$N), 空间复杂度 O(1).      
 **[法2]** 竖着每列最小元素逐一比较. 时间复杂度 O(kN), 空间复杂度 O(N) or O(1).   
 **[法3]** **Heap / Priority Queue** 优先级队列 / 堆. 对法2 的优化, 用优先级队列储存竖行元素, 这样每次比较时复杂度降为 log 级. 时间复杂度 **O(N$log$k)**, 空间复杂度 O(k).   
 注意, 在使用 `heapq` 模块时, 应该在指针前添加列表下标index,防止val相同时对指针 进行操作.     
 **[法4]** lists两两合并. 时间复杂度 O(kN), 空间复杂度 O(1).   
 **[法5]** **Divide And Conquer** 归并合并. 对法4 的优化. 时间复杂度 **O(N$log$k)**, 空间复杂度 O(1).     

24. **Swap Nodes in Pairs. [M]**   
链表节点交换. 递归 or 迭代. 多加几个指针,多画画图, 没啥难点. 

25. **Reverse Nodes in k-Group. [H]**    
24的拓展. 每 k 个值翻转一下. 递归(很简洁) or 迭代. 多加几个指针,多画画图, 没啥思想上的难点. 时间复杂度 O(kn), 空间复杂度 O(1).   
<img src="https://wx1.sinaimg.cn/mw1024/006qmTkdly1g6ffthrlw5j30bn09hdgh.jpg" width = "250"  alt="大佬图片" 
align=center> 
<img src="https://wx4.sinaimg.cn/mw1024/006qmTkdly1g6fftkiwijj30c702ht8p.jpg" width = "265"  alt="大佬图片" 
align=center> 

26. **Remove Duplicates from Sorted Array. [E]**  
Two pointers. 由于 **in-place**, 修改代替remove, 设置快慢指针. 

27. **Remove Element. [E]**   
Two pointers. 类似 26, 更简单. 除了类似上题的从前 -> 后的快慢指针, 还可以一头一尾, 头 = target时, 把尾的值覆盖过去. 

28. **Implement strStr(). [E]**   
Two pointers in string.(都不算.) 很简单,没啥意思. 

29. **Divide Two Integers. [M]**    
[知乎](https://zhuanlan.zhihu.com/p/73450264)写过了.  py一般没有这个烦恼. 以后用 C++ 时再看. 需要注意的地方:    
 范围 [-2^31,2^31-1], 不能超出范围 (C++可能需要写判断);    
 正负号不能用abs/ *(-1) 之类的;   
 注意除数要成倍增长.

30. **Substring with Concatenation of All Words. [H]**    
[知乎](https://zhuanlan.zhihu.com/p/73570551)写过了. Hash table, two pointers.    
 **[法1]** Twp hashmaps. 一个表 H1 用来储存words中单词以及出现次数(开始比较前就固定), 另一个表 H2 储存s中出现在H1表中的词的次数. s子串长度 = words总长 k\*n 时输出, H2 单词出现次数 > H1 时跳出.   
**[法2]** **Sliding window**, 滑动窗口. => 模拟长度=单词长度n的滑块. (s 被分成了 n 份, 需要 n 个滑块.) 在 Two maps的基础上作如下优化:    
 (已匹配) &nbsp;滑块移动到下一个单词(后移n位), 删去子串第一个词,判断下一个单词.  
(不匹配) &nbsp; 子串前i个单词匹配, 第i+1(<k)个单词不匹配, 滑块直接后移到 (i+2)*n处. (包含第i+1个单词的都不匹配.)    
(不匹配) &nbsp; 第i+1(<k)个单词匹配, 但此时H2次数>H1. 滑块移动到H2次数= H1次数的位置.   
==> 进一步优化: 匹配情况和不匹配的第二种情况可以合并. 当子串长度= k\*n 时输出结果即可.   
补一个好用的 py3 函数:
```
H1 = collections.Counter(words) #待补充:collections模块
```

31. **Next Permutation. [M]**  
重点是这个 "Next Permutation" 的理解. 数学系要是连这个都觉得难...就真的白念了.   
数列全部递减 => 最大, 逆序输出; 第一个递增数字a[i]>a[i-1] => 把a[i-1]挪到a[i]后面第一个比它小的数字前面(全比它大就放到最后). 

32. **Longest Valid Parentheses. [H]**   
重点来了! Dynamic Programing; stack,  Without extra space, 牛逼, 尤其是单调栈法, 好好再理解一次. 



33. **Search in Rotated Sorted Array. [M]**
34. **Find First and Last Position of Element in Sorted Array. [M]**
35. **Search Insert Position. [E]**
36. **Valid Sudoku. [M]**
37. **Sudoku Solver. [H]**