# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 21:40:48 2019

@author: dellbook
"""
import random
def twoway_quick(nums,left,right): #双路快排, 对于重复数字将它们等分
    if right-left <=0: return
    randomindex = random.randint(left,right) #随机选择piovot
    nums[right], nums[randomindex] = nums[randomindex], nums[right]
    L,R,x = left, right-1,nums[right]
    while True:
        while L<right and nums[L]<x:L+=1
        while R>left and nums[R]>x: R-=1
        if R<=L: break
        nums[L], nums[R] = nums[R], nums[L]
        L, R= L+1, R-1
    nums[right], nums[L] = nums[L], nums[right] #不能省, R便可看作分割点
    twoway_quick(nums, left, L-1)
    twoway_quick(nums, L+1, right)
    return

def bucket(nums):
    maxx, minn  = max(nums), min(nums)
    dic = [[] for i in range(maxx//10 - minn//10 +1)]
    for x in nums:
        idx = x//10 -minn//10
        dic[idx].append(x)
    nums.clear()
    for col in dic: #每个列调用快排排序
        print(col)
        twoway_quick(col,0,len(col)-1)
        nums.extend(col)
        print(col)

def main():
    nums = [int(n) for n in input().split()] #直接输入数组,空格键隔断
    bucket(nums) #桶排序
    out = (nums)
    print(out)
    return 0

if __name__ == '__main__':
    main()