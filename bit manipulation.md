# Bit Manipulation 位运算

## 位操作符

* `&` 与 (and) 运算. 两个位都是1, 结果才是1.        

|   |1 |0 |0 |1 |1 |    
|-- |--|--|--|--|--|    
|`&`|1 |1 |0 |0 |1 |    
|   |1 |0 |0 |0 |1 |

* `|` 或 (or) 运算. 两个位都是0, 结果才是0.         

|   |1 |0 |0 |1 |1 |   
|-- |--|--|--|--|--|    
|`\|`|1 |1 |0 |0 |1 |    
|   |1 |1 |0 |1 |1 |     

* `^`异或 (xor) 运算. 两个位相同取0, 不同取0. (因此`a^a` 为0, `0^a` 为a.)    

|   |1 |0 |0 |1 |1 |   
|-- |--|--|--|--|--|      
|`^`|1 |1 |0 |0 |1 |    
|   |0 |1 |0 |1 |0 |

* `~` 取反 (not) 运算. 0 <-> 1. (e.g. -a = ~a+1.)    

|`~`|1 |0 |0 |1 |1 |   
|-- |--|--|--|--|--|      
|   |0 |1 |1 |0 |0 |

* `<<` 左移 (shl) 运算. 向左移位, 高位丢弃,低位补 0.

*  `>>` 右移 (shr) 运算. 向右移位, 低位丢弃, 对无符号数, 高位补0; 对于有符号数, 高位补符号位.  

## 常见位运算问题

1. 乘除2: 正整数a右移k位 `a>>=k`<=> `a*=2**k`; 正整数a(>=2的k次方) 左移k位 `a<<=k`<=> `a//=2**k`.

2. 两数交换. (`^` 满足交换律)
```
    a ^= b  # a = (a^b)
    b ^= a  # b = b^(a^b) = (b^b)^a = 0^a = a
    a ^= b  # a = (a^b)^a = b
```

3. 判断奇偶.
```
    if a & 1 :
        print("odd number")
    else:
        print("even number")
```

4. 取逆: `a = ~a+1` 即为 -a.  
5. 求绝对值.
```
    i =a>>31 #int a右移31位是符号位, 正数0 负数1
    abs = ~a+1 if i else a
```
或:
```
    i =a>>31 #int a右移31位是符号位, 正数0 负数1
    abs = (a^i)-i
```

## 例题

* [78. Subsets. [M]](https://leetcode.com/problems/subsets/)

* [89. Gray Code. [M]](https://leetcode.com/problems/gray-code/)

* [136. Single Number. [E]](https://leetcode.com/problems/single-number/)

* [137. Single Number II. [M]](https://leetcode.com/problems/single-number-ii/)

* [201. Bitwise AND of Numbers Range. [M]](https://leetcode.com/problems/bitwise-and-of-numbers-range/)
