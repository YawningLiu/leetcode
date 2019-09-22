# [65. Valid Number [H]](https://leetcode.com/problems/valid-number/)

## 问题描述
其实判断字符串是否是浮点数 'float'. 估计以后并不会遇到, 但遇到的许多新知识值得学习.


## [法1] 暴力直接法.
只要你 WA 的足够多, 就一定能 AC!   

## [法2] DFA.

>  我与 DFA 的第一次相识---人生若只如初见

### DFA介绍
Deterministic finite automata(DFA): 确定有穷自动机.    
其特征为: 有一个有限状态集合 (K) 和一些从一个状态通向另一个状态的边 , 
每条边上标记有一个符号(δ), 其中一个状态是初态 (q0), 某些状态是终态(F). 
但不同于不确定的有限自动机(NFA), 
DFA中不会有从同一状态出发的两条边标志有相同的符号.   
大白话 : DFA 的每一步操作都是确定的, 
即: 当一个状态面对一个输入符号的时候，它所转换到的是一个唯一确定的状态.
```
M = ( K, Σ, δ, q0, F )
```
*  K: 有穷状态集(DFA所有状态组成集合)
*  Σ： 输入字母表, 即输入符号集合.
*  δ： 将 S×Σ 映射到 S 的**状态转换函数**.    
> s∈K, a∈Σ,  δ(s,a) 表示从状态 s 出发, 沿着标记为 a 的边所能到达的状态.
*  q0：开始状态 (或初始状态), q0∈K. 
*  F：接收状态（或终止状态）集合, F⊆ S. 
 
### 本题中的DFA 
![dfa](https://wx2.sinaimg.cn/mw690/006qmTkdly1g73xfzx39rj323l1qitqs.jpg)

## [法3] 正则表达式.
### 代码
```python3
     def isNumber(self, s: str) -> bool:
        regex = "^\s*(-|\+)?([0-9]+\.?|\.[0-9]+)([0-9]+)?(e(-|\+)?[0-9]+)?\s*$"
        if re.match(regex, s):return True
        return False
```
### 代码中出现的正则表达式符号

| 符号 | 描述 |     
|:-----|:---------------|       
| `^`      | 匹配字符串起始部分.        |   
| `\s`     | 匹配空格字符.             |   
| `*`      | 匹配 **0 次或多次** 前面出现的正则表达式.   |   
| `()`　    | 匹配封闭的正则表达式, 另存为子组. |    
| `\|`　    | 择 1 匹配的管道符号, 从多个模式中选择其一.  |   
| `+`　     | 匹配 **1 次或多次** 前面出现的正则表达式. |    
| `?`　     | 匹配 **0 次或 1 次** 前面出现的正则表达式.   |    
| `[x-y]` 　| 匹配 x~y 范围中任意单一字符 |    
| `.`　     | 匹配任意字符(除换行符`\n`), 因此当小数点时用 `\.`. |    
| `$`     　| 匹配字符串终止部分. |       

### 分析

| 代码 | 含义 |     
|:-----|:---------------|       
| `^\s*`      | 其实位置, 空格出现0次或多次.        |   
| `(-|\+)?`   | `+,-` 其中之一 出现0次或1次.        |   
| `[0-9]+\.?` | 出现了0-9中数字>=1次,然后出现小数次数1次或没有小数点. |   
| `\.[0-9]+`  | 小数点 + 至少一位数字 |    
| `([0-9]+)?` | 出现至少一位有效数字, 这个子组出现1次/0次. |      
| `(e(-|\+)?[0-9]+)?`| e+符号子组+至少一位数字, 这个子组出现1次/0次. |

### 常用的re函数：

| 函数/方法(省略前缀 `re.`)  | 作用   |     
|:-----|:---------------|       
|  `match(p, s, flags=0)`  | 从其实位置开始匹配. 如果 s 包含 p, 则匹配成功, 返回Match对象. 失败返回None.|     
| `search(p, s, flags=0)`  | 扫描 s 并返回第一个成功被 p 匹配的 s 子串. 失败返回None. |    
| `findall(p, s, flags=0)` | 找到 s 中所有被 p 匹配的子串(非重复), 返回一个列表. |
| `finditer(p, s, flags=0)` | 同 `findall()`, 但返回的是迭代器.     |     
| `split(p, s, max=0)`     | 根据模式分割符 p, 将 s 分割为列表并返回,最多切 max 次. | 

函数参数说明：    
* p(pattern) : 匹配的正则表达式
* s(string) ： 要匹配的字符串
* flags：标记为，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
  
### `re.match()` 详解
```python3
re.match(pattern, string, [flags])
```
从首字母开始开始匹配, string 如果包含pattern子串, 则匹配成功, 返回Match对象.
失败则返回None. 若要完全匹配, pattern要以`$`结尾.  

Match对象为 `MatchObject` 实例, 其中有这次匹配的信息: 它是从哪里开始(start)和结束(end), 它所匹配的子串(group(0))等等. 
 
e.g.: `p, s ="c*a.*ja", "aasssaijsja"`    
<_sre.SRE_Match object; span=(0, 11), match='aasssaijsja'>

## [法4] 作弊法.  

注: 这里不能使用 `if...else...`, 因为会 return False 的异常字符在 `float()` 中会出错, 所以只能用 `try...except...` 捕获异常. 

```python3
        try: float(s)
        except: return False
        return True
```

## 参考资料    
[编译原理：有穷自动机（DFA与NFA）](https://blog.csdn.net/qq_39521554/article/details/79416553)   

[什么是NFA(不确定的有穷自动机)和DFA(确定的有穷自动机)](https://www.cnblogs.com/AndyEvans/p/10240790.html)    

[正则表达式手册](http://tool.oschina.net/uploads/apidocs/jquery/regexp.html)   

[Python3 re模块](https://www.cnblogs.com/smxiazi/p/8911964.html)  
   
[Python3 正则表达式](https://www.runoob.com/python3/python3-reg-expressions.html)
