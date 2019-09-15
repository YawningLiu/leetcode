# 总结(1-50)

> => 应该掌握的知识点:  哈希表, 链表基本操作, 马拉车, 动态规划,  二分法, 分治, 第k小的数, 排序, 回溯, 二指针, 堆, 优先队列, 滑动窗口, 贪婪, 单调栈, FFT.     
> => 待掌握: 线段树segment, 字典树tire, Floyd 算法, 各种排序算法.  

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
非常典型的一道题. Dynamic programing; monotone stack; without extra space, 都是线性时间复杂度. 尤其是 ms 非常牛逼了  
**[法1]** 双指标法. 从左 -> 右 扫描一次, 从右 -> 左扫描一次, 分别记录 '(' 和 ')'个数, 找出里面最大值. => 特殊性太强, 看看就好.  
 **[法2]** 动态规划. dp[i+1] 表示以第i个括号结尾的合法括号有多少. 状态转移函数: 
```
if s[i] ==')':  #以s[i]=='(' 结尾肯定不合法     
    if i > 0 and s[i-1]=='(': #正好构成()   
        dp[i+1] = dp[i-1]+2
    if i > dp[i] and s[i-1]==')':  #s[i-1]==')'时怎样合法
        if dp[i-dp[i]-1]=='(': #已知s[i-dp[i]]到s[i]是合法的
            dp[i+1] = dp[i]+2+dp[i-dp[i]-1] #当前合法+上一组可能存在的合法括号 
```
**[法3]** 单调栈. '('入栈,')'出栈. 每次计算栈里的值. 为了方便计算, 初始化 `stack =[-1]`. 
```
if s[i]=="(":  #'('下标入栈 => monotone stack总是下标入栈
    stack.append(i)
else:  # ')' 栈尾元素出栈. 出栈后栈顶元素是当前合法括号开头下标的前一位.
                stack.pop() 
                if not stack: #栈空, 当前')'不合法,下标进.
                    stack.append(i)
                else: #栈非空,说明s中元素两两搞cp去了
                    res = max(res,i-stack[-1])
```    

33. **Search in Rotated Sorted Array. [M]**    
搜索旋转后的无重复排序数组. 最直观的方法两次使用二分法: 先找旋转点, 再找target.       
另外一种是旋转点 和 target 同时找 (代码比较复杂容易出错, 但画画图思路就清楚了).  
 
34. **Find First and Last Position of Element in Sorted Array. [M]**    
Binary search. 没啥难的, 注意边界细节就行. 

35. **Search Insert Position. [E]**    
Binary search. 没啥难点. 

36. **Valid Sudoku. [M]**   
哈希表. 笨办法三次遍历, 聪明办法一次遍历, 没啥意思. 

37. **Sudoku Solver. [H]**     
Hash table; backtracking. 回溯算法典型题目之一, 没啥特点.   

38. **Count and Say. [E]**    
难点在理解题目. 程序本身太简单了.  

39. **Combination Sum. [M]**      
**先排序!!!** (为了后续的剪枝 + 去重操作.)    
**[法1]**. Backtracking, 回溯经典题目. 先向前列举所有情况, 得到结果/确定无解就向上一层回溯.    
**[法2]**. Dynamic programing. 用 hashmap 保存每个可能的取值结果. 注意剪枝以及去重 (有序存表, 则添加新元素时,新元素 >= -1位置再储存, 即可避免重复元素).    
40. **Combination Sum II. [M]**   
**先排序!!!** 不用考虑答案重复, 同39. (本题如果用dp, 重复元素不太好弄, 得用集合及其性质, 特殊性太强, 暂时不考虑了.) 回溯时的算法有一点点不同. 多一句排重语句:
```
if i>0 and x == candidates[i-1]:
    continue
```    
   
41. **First Missing Positive. [H]**    
**Hash table.** O(n) time and O(1) space. 借鉴哈希表的思想, "in-place" 即把自己当 hashmap解决问题.   
**[法1]**  O(2n).  <=> dic[k]=k+1的hash表. 第一次遍历, 在k处放置数字k+1; 第二次遍历,寻找最小的不在规定位置的数. 需要注意的是**重复数字**情况:`nums[nums[i]-1]==nums[i]` 时跳出循环.    
**[法2]**  O(3n).  <=> dic[k]=True(正)的hash表.  第一次遍历, 把1<=x<=n的数挪前并记录长度r; 第二次遍历, 把前 r 的数 x 以下标为映射所找到的nums[x] 变成负数; 第三次遍历, 寻找第一个正数,下标+1.    
**[法3]**  O(3n).  <=> dic[k]=True(>0) 的hash表. 首先结尾补0. 第一次遍历, 把 range(1,n) 之外的数变为0; 第二次遍历, 以非0
数 x%n 为下标所得到的 nums[x]+n; 第三次遍历, 寻找第一个小于n的数的下标 (即没有出现过).   

42. **Trapping Rain Water. [H]**     
Dynamic programming 简化得到 two pointers; monotone stack.    
**[法1]** Two pointers. 其实是由动态规划精简而来的. (理解了就会很简单.)          
先说动态规划: dpleft[i]: i-th 列左边最大值, dpright[i]: i-th 列右边最大值. =>三次遍历(求 dpleft, 求 dpright, 求所接雨水).   
由于dp数组每个值只用到一次, 故dp数组可精简为首尾指针left,right, 以及左右最大值maxl, maxr. 
当 `maxl<maxr` 时, left指针后移, 新left位更新maxl并计算接水量, 反之亦然.      
**[法2]** Monotone stack. **注意入栈的是元素下标而不是元素本身!** 联动84.   
当`H[i]<stack[-1]`, 有积水,入栈; 反之, 出栈, 计算积水含量, 并将`H[i]` 入栈, 作为新的高度. (没 two pointers 简单.)

43. **Multiply Strings. [M]**    
**[法1]** 简单粗暴直接计算.    
**[法2]** 竖式相加. 但也没啥意思...   
**[法3]** **FFT(快速Fourier变换)** 的 n\log(n) 解法. (牛逼啊, 我怎么就没想到, 太丢数学系的脸了)    
<img src="https://wx3.sinaimg.cn/mw1024/006qmTkdly1g6vydttmg9j310b0u0n9n.jpg" width = "270"  alt="fft" 
align=center>
```
        import numpy as np  #使用到的函数
        A,B = np.fft.fft(a),np.fft.fft(b)
        C = np.multiply(A,B)
        c= np.fft.ifft(C)
```


44. **Wildcard Matching. [H]**   
[知乎](https://zhuanlan.zhihu.com/p/72179123)写过了.    
**[法1]**  Dynamic Programing. 没啥难的, 照着 lc10 写出状态转移方程即可.    
**[法2]**  Greedy. (i.e. 所谓的双指针法). 
```
    # i,j : s, p 中指针位置;  match,star : *出现时s被匹配后的指针位置, p中指针位置
    while i < len(s):
        if j < len(p) and (p[j] == s[i] or p[j] == "?"): # 普通匹配
            i,j = i+1,j+1  
        elif j < lp and p[j]=='*': # *出现了, 暂定这个'*'匹配了0个字符
            star, match, j = j, i, j+1 
        elif star!=-1:  # 当前 s[i]与 p[j]不匹配, s中被'*'匹配的字符数量+1, i,j回去
            match+=1  #s中被匹配的字符数量多1个, 看看行不行
            i,j = match, star+1  #i,j 返回去继续尝试
        else: return False
```

45. **Jump Game II. [H]**     
  **Greedy**. 典型的贪婪算法(也可以理解为BFS), 理解思想就容易多了. 从前 -> 后, 从后 -> 前两种方法. (遇到此类题, 多测试一些数据)
 
46. **Permutations. [M]**   
Backtracking 经典题型: "回溯" = "BFS" + "状态重置" + "剪枝".    
本题回溯方法很多, 可分为: 对插入位置回溯, 对交换位置回溯. 
```    
return list(itertools.permutations(nums))  #py3有专门的库函数你怕不怕.   
```     

47. **Permutations II. [M]**   
**排序**. 本题的回溯就需要剪枝(去重)了. 用 `continue` 去重.  
交换 + 插入 两种方法 . 回溯经典题型. 
```
return list({p for p in itertools.permutations(nums)}) #一句话解决
```
48. **Rotate Image. [M]**    
找规律, 没啥特点.
 
49. **Group Anagrams. [M]**    
[知乎](https://zhuanlan.zhihu.com/p/74650414)已写. 还是 Hash Table 的应用.  
**[法1]** 对str中元素 x 进行 `tuple(sorted(x))` ,  `''.join(sorted(x))` 作为 key 存入dict, 最后 `dict.values()`.    
**[法2]** 对由于只有小写字母, 故可将其转化为长为26的列表进行操作.     
**[法3]** 算数基本定理. 原理同上, 尤其唯一性来的, 但只适用于单词长度较短时, (单词较长会溢出.) 

50. **Pow(x, n). [M]**   
**Binary search** + 注意 边界. 有递归 + 迭代两种形式. 其实就是考考二分法. 
