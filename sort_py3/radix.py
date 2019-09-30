# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 13:57:46 2019

@author: dellbook
"""
import collections
def radix(nums):
    n = len(str(max(nums))) #取得位数
    dic = [collections.deque() for i in range(10)]
    for i in range(n):
        for x in nums:
            dic[(x//(10**i)) %10].append(x)
        inn = 0
        for k in range(len(nums)):
            while not dic[inn]:
                inn+=1
            nums[k] = dic[inn].popleft()
    return nums
        
def main():
    nums = [int(n) for n in input().split()] #直接输入数组,空格键隔断
    nums1 = radix(nums) #基数排序
    out = (nums1)
    print(out)
    return 0

if __name__ == '__main__':
    main()