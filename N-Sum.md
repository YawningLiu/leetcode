#N-Sum

###关键词: Hash Table, Sort, Two Pointers. 

(待补充:N-Sum)

####[1. Two Sum](https://leetcode.com/problems/two-sum/) [E].

**题目**: 已知数组nums, target; return nums中和=target的两数 else 空数组.  

**解法**:  
1. Brute Force(暴力求解). <font color=#0099ff>[AC]</font>    
&emsp; 就是双层循环~~. 时间复杂度 O(N^2); 空间复杂度 O(1).   
2. Sort + 双指针. <font color=#0099ff>[AC]</font>   
&emsp; 先快排; 再用两个指针从前后扫描逼近真值, 最后返回真值对应的数组下标. 重点是数组下标-数组真值的对应关系 时间复杂度 O(N$\log$ N); 空间复杂度 O(1).  
3. Two-pass Hash Table.  <font color=#0099ff>[AC]</font>     
&emsp; 把内层循环换为Hash Table. 空间换时间(太值啦!) 时间复杂度 O(N); 空间复杂度 O(N).  
&emsp; *这种情况尤其要注意一个元素不能使用两次!*  
4. One-pass Hash Table. <font color=#0099ff>[AC]</font>
 <font color=#dc4040>**[best]**</font>      
&emsp; 进一步精简, 边循环边找答案边储存新值. 

**Note**:  一个元素只能用一次! 防止重复元素的使用呦 ~.  

####[15. 3Sum](https://leetcode.com/problems/3sum/) [M].

**题目**: 已知数组nums; return nums中所有sum=0的排序后的三个数 else 空数组, 且 return 的三元组不能重复. 

**解法**:  
1. Brute Force. <font color=#000ff>[Time Limit Exceeded]</font>    
&emsp; 时间复杂度 O(N^3), 超时错误.   
2. 看作2Sum 的变种问题 => Sort + 双指针. <font color=#0099ff>[AC]</font>  <font color=#dc4040>**[main]**</font>  
&emsp;由于时间复杂度至少 O(N^2), 而 **sort** 时间复杂度 O(N$\log$ N), 且排序后可以有效避免重复数组(遇到重复数 continue).  
3. Sort + One-pass HashTable (Set). <font color=#0099ff>[AC]</font>      
&emsp;  set 排除重复元素 [=> `map(list, set)`]. 第一个数更新后重置hashmap (这里用 set 也行, 虚假的 Hashmap), 遍历每个元素,并储存相应值.    
4. 真正的 Hash Table.  <font color=#dc4040>**[main][best]**</font>  
&emsp; `from collections import defaultdict`  
&emsp; 先两次遍历: 第一次 => 储存nums元素和各个元素出现次数至dict; 第二次 => 对dict中元素另储存为正数数 pos 和负数数组 neg.排序. 再对 `a in pos`, `b in neg` 找 -(a+b) 是否在memo. 记得考虑特殊情况 
`[0,0,0], -(a+b) =a, b`.   

**Note**:   
1. **由于排序 了,第一个数>0 or 第一个数+第二个数>0.etc 即可 return 了.** <font color=#dc4040>**(key)** </font>.    
2. 本题关键点在于排序.  

####[16. 3Sum Closest](https://leetcode.com/problems/3sum-closest/) [M].

**题目**: 3 Sum变种.  return nums中 sum closest to target 的三个数 else 空数组. 

**解法**:  
1. Brute Force. <font color=#000ff>[Time Limit Exceeded]</font>      
2. 3Sum 的变种问题 => Sort + 双指针. <font color=#0099ff>[AC]</font>  <font color=#dc4040>**[main]** </font>   
&emsp; 除了常规操作, 还可以增加一些语句排除**无用循环**.   
&emsp; (1). target==ans,return;   
&emsp; (2). 对于第一个数`nums[i]==nums[i-1]`, `continue`;   
&emsp; (3). 由于已排序, 则nums[i]确定时,找到数组能达到的最优解,比ans差, continue.  

**Note**:   
1. hashmap大失败.    
2. 对于无用循环的排除, 可以有效提高计算速度.  

####[18. 4Sum](https://leetcode.com/problems/4sum/) [M].

**题目**: return nums中所有sum=target的排序后的四个数 else 空数组, 且 return 的三元组不能重复. 

**解法**:  
1. 3 Sum 的变种 => Sort + 双指针. <font color=#0099ff>[AC]</font>  <font color=#dc4040>**[main]**</font>   
&emsp;时间复杂度 O(N^3), 提高效率重点在排除无用循环.   
假设当前4个数分别为a, b, c, d, 能达到的最大值为 max.  
&emsp; (1). a太大: `4*a > target` => `break`;   
&emsp; (2). a太小 or a=nums[i] 与前一个值相同: `a+3*max<target` or `nums[i]==nums[i-1]`, `continue`;   
&emsp; (3). a确定, b太大: `3*b>target-a` => `break`;   
&emsp; (4). a确定, b太小 or 重复(略): `b+2*max<target-a` => `continue`.  
2. hashmap + set 排除重复情况. <font color=#0099ff>[AC]</font> <font color=#dc4040> **[best]**</font>   
&emsp;  时间复杂度 O(N^3). 用 `sorted(list(set(nums)))` 来排除重复结果的影响.  
3. 2 Sum + hashmap. <font color=#0099ff>[AC]</font>   
&emsp; 先二重循环建立dict[sum] 储存和为sum的数组, 在对数组进行操作

**Note**: **无用循环的排除.** <font color=#dc4040>**(key)** </font>.    


####引申: N-Sum(待完成).

othesr: 560, 167,454, **560**, 654,   3 Sum Smaller, Two Sum(III)- Data Structure Design, Two Sum less than K. 




    