# py3 - 字符串相关函数


看到什么记什么吧~
---
1. str 和 tuple 一样, 一旦确定就并不能更改 (故可以做 dict 的key).

2. `str.upper()`/`str.lower()`     
所有字符串的字母(仅限英文)变为大写/小写..
> `str.casefold()` 将所有字符串的字母(可以是其他语言)变为小写.

3. `str.strip()`   
 移除字符串左右两侧指定的字符, 默认为移除空格.   
> `str.lstrip()`, `str.rstrip()`. 分别**只**移除左, 右指定字符.  

4. `str.split()`      
通过指定分隔符按从左到右的顺序对字符串进行切片(切片后不含分隔符), 并以 list 形式返回. 默认分隔符为空格.   
> 可以指定分隔符的个数: `str.split(' ',k)`.分割符为k个(字符串被分为<=k+1段).  
>  `str.rsplit()` :从右到左进行切片.

格式：“字符串内容”.rsplit（“指定分隔符”）


5. `str.join(iterable)`  
将序列 (list/set,etc) 中的元素以指定的字符str拼接生成一个新的字符串.

6. is系列. 判断字符串的函数, 均返回 True/False.


|func| return Boolean |     
|----|:---------------|       
| `str.isdigit()`  | 是否str只由数字组成.        |   
| `str.isalpha()`  | 是否str只由字母组成.        |   
| `str.isalnum()`  | 是否str只由字母/数字组成.   |   
| `str.isupper()`　| 判断str中所有字母是否为大写. |    
| `str.islower()`　| 判断str中所有字母是否为小写. |   
| `str.isspace()`　| 判断str是否只由空白字符组成. |    

---
参考链接  
[Python3字符串方法](https://www.cnblogs.com/fyknight/p/7895894.html)    
[python 内置类型(五)---str](https://www.jianshu.com/p/e51ec57c50b6)
