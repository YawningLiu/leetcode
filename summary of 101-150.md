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
None, 分别对前序里出现的根进行递归. O(n) time, 递归的树深.
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
趁机复习下 morris 遍历.

115. **Distinct Subsequences. [H]**    		
116. **Populating Next Right Pointers in Each Node. [M]**
117. **Populating Next Right Pointers in Each Node II. [M]**  
118. **Pascal's Triangle. [E]**    		
119. **Pascal's Triangle II. [E]**    		
120. **Triangle. [M]**    
