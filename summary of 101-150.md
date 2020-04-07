# 总结(101-150)

101. **Symmetric Tree. [E]**    
二叉树遍历的基础操作. 类似100. 可以使用 递归DFS / 迭代DFS (with 栈) / 迭代BFS (with队列).

102. **Binary Tree Level Order Traversal. [M]**      
二叉树遍历. 本质是分层BFS. 可以使用 DFS + 层数递归 / BFS + 层数 + 队列迭代 / BFS +嵌套内层循环 + 队列迭代.

103. **Binary Tree Zigzag Level Order Traversal. [M]**      
偶数层逆序的102. 除了上述三种方法, 还可以用两个栈当不同层分开操作.

104. **Maximum Depth of Binary Tree. [E]**       
老生常谈的二叉树遍历, 老方法.

105. **Construct Binary Tree from Preorder and Inorder Traversal. [M]**     
  **[法1]** 暴力递归构造. O(n<sup>2</sup>) time, O(1) space.   
  **[法2]** 哈希表 + 递归. 哈希表储存中序对应值下标, 再利用中序根分割左右子树的特点,
  分别对其进行递归. (前序用来储存当前根的具体值). O(n) time, O(1) space + 递归的树深.   
  **[法3]** 数组下标 + 递归. 利用 中序里根分割左右子树, 利用左子树对应根, 右子树对应
None, 分别对前序里出现的根进行递归. O(n) time, 递归的树深. **star**      
eg: 前序: [3, 9, 6, 20, 17,2]; 中序: [9, 6, 3, 17, 20, 2].
![法3图片](https://wx3.sinaimg.cn/mw690/006qmTkdly1g8odi5nn0nj30pj0980ss.jpg)       

  **[法4]** 迭代 + 栈.  同3, 只不过用栈代替递归.

106. **Construct Binary Tree from Inorder and Postorder Traversal. [M]**    
同105, 逆着考虑即可. (因为preorder: root -> left - > right, postorder: left - > right -> root.)

107. **Binary Tree Level Order Traversal II. [E]**       
层次遍历, 同102. 前者先根后叶子, 本题先叶子后根.

108. **Convert Sorted Array to Binary Search Tree. [E]**        
有序数组 -> BST. 二分 + DFS/ 递归 (or 栈).

109. **Convert Sorted List to Binary Search Tree. [M]**      
  **[法1]** 列表转数组, 同108; 或者利用快慢指针找中点, 再分别对其左右节点递归(太慢).  
  **[法2]**  先计算列表总长, 模拟中序递归(左根右)即可按顺序建立各点.  

110. **Balanced Binary Tree. [E]**       
类似104.
> 补充平衡二叉树定义:   => 详细方法和步骤见 **220** .       
它是一棵空树或它的左右两个子树的高度差的绝对值<= 1, 并且左右子树都是平衡二叉树.

111. **Minimum Depth of Binary Tree. [E]**     
类似 104(110).   

112. **Path Sum. [E]**    
携带着sum的DFS. (BFS / 栈也行)

113. **Path Sum II. [M]**    
同112,  用全局列表保存结果即可.

114. **Flatten Binary Tree to Linked List. [M]**   
易知展开的链表为前序.    
  **[法1]** 暴力递归法 (自顶向下).  把右子点接在左子树的最右子树, 再进行递归.     
  **[法2]** 后序遍历 + 递归 (自底向上).
  自底向上就是从最右开始操作, 因此必须按照右 -> 左 -> 根(后序)的顺序操作. 设置一个全局变量保存上一个底部节点.  **star**
  <img src="https://wx2.sinaimg.cn/mw690/006qmTkdly1g8r0qso6tij310o1cxqcw.jpg" width = "420" height = "560" alt="后序操作" align=center>          

  **[法3]** 迭代 + 栈. 用栈模拟递归流程, 即可得到上述两种方法的迭代版本.

115. **Distinct Subsequences. [H]**    		   
Dynamic programming. (i.e. 记忆化递归, 懒得这个了...) 其实就是匹配的问题.      
状态转移方程:
`dp[i][j] = dp[i-1][j-1] + dp[i][j-1] if s[j-1]==t[i-1] else dp[i][j-1].`  

116. **Populating Next Right Pointers in Each Node. [M]**    
  **[法1]** (通用解法, O(1) 空间.) **BFS**. 利用 `next` 指针在层之间的关系代替 queue.    
  **[法2]** 非常数空间的方法. e.g.  队列 / 递归(将下一层连起来, 再对左右子树递归.)

117. **Populating Next Right Pointers in Each Node II. [M]**        
思路同116. 利用 BFS + `next` 指针 + **哑**节点 即可.  

118. **Pascal's Triangle. [E]**    		    
杨辉三角. Dynamic programming.

119. **Pascal's Triangle II. [E]**    		       
同118, 直接改就可.  或者利用二次项公式:
第k 行 <=> 二项式 (x+y) <sup>2</sup> 的展开项系数(组合数).

120. **Triangle. [M]**    
Dynamic programming(类似 115, 但更简单). 自顶向下 / 指底向上(更好, 不用最后再求一遍最小值.)

121. **Best Time to Buy and Sell Stock. [E]**

122. **Best Time to Buy and Sell Stock II. [E]**

123. **Best Time to Buy and Sell Stock III. [H]**

124. **Binary Tree Maximum Path Sum. [H]**    
DFS(递归) + 全局变量. 不算难.  注意题目的含义.

125. **Valid Palindrome. [E]**     
注意两个函数: `s.lower`, `s.isalnum()`. (其实考点应该是大小写字母的映射和转换, 我偷懒了orz...)

126. **Word Ladder. [H]**     
  **BFS + DFS**. 详见  [题解: 126/127. Word Ladder](https://github.com/YawningLiu/leetcode/blob/master/word%20ladder.md) . 127 的进阶版.          
主要思路如下: ① 先用127的BFS查询是否有路径(注意储存父子关系 / 同层节点可以重复使用); ② 再利用已知信息进行DFS.   
需注意节点可以重复使用. (不预判而直接使用BFS/DFS 会TLE)

127. **Word Ladder. [M]**     
  **BFS**.  又双叒叕不会做了....详见  [题解: 126/127. Word Ladder](https://github.com/YawningLiu/leetcode/blob/master/word%20ladder.md) .         
主要思路如下: ① 预处理, 建立图的邻接表; ② BFS对邻接表进行搜索, 注意在遍历时添加好深度和 visited 集合.  => 进阶: 双向 BFS[从始末分别建立两个队列进行BFS搜索]

128. **Longest Consecutive Sequence.[H]**     
要求O(n) time. [注: 比较类排序是O(nlogn). 非比较类排序为 O(n),  因此可以用先非比较排序, 再判断]      
  **[法1]** 利用`set()`查找元素用时为 O(1)的性质. 注意理解为什么是时间复杂度是 O(n)的.      
  **[法2]** **Union Fond** 并查集.  利用 Hash 表合并. (未解之谜: 为什么是 O(n)的? => 应该是, 最多 3n 次.)    
  **[法3]** 类似并查集. 对每个x 找到 x+/-1 为边界的长度, 得到以 x 为边界的长度, 再更新x对应边界的值.  (感觉不如前2个方法显然.)

129. **Sum Root to Leaf Numbers. [M]**         
又一道二叉树遍历, 见112.

130. **Surrounded Regions. [M]**    
注意. **反向思维**. 由于内部判断点数量为 O(n<sup>2</sup>),
边界点数量为 O(n), 故**逆向**考虑: 先通过边界找到不变的点"O",
再调换内部的 "O". (正向会TLE.)     
=> 优化: 边界及相连的 "O" 改为其他字符.      
DFS; BFS; **Union Find** (并查集):

131. **Palindrome Partitioning. [M]**
132. **Palindrome Partitioning II. [H]**
133. **Clone Graph. [M]**
134. **Gas Station.[M]**
135. **Candy. [H]**
136. **Single Number. [E]**
137. **Single Number II. [M]**
138. **Copy List with Random Pointer .[M]**
139. **Word Break. [M]**
140. **Word Break II. [H]**
