# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 09:54:08 2019

@author: dellbook
"""
def counting(nums):
    maxx, minn = max(nums), min(nums)
    count = [0]*(maxx-minn+1)
    for x in  nums: #构造计数数组
        count[x-minn] += 1
    for i in range(1,len(count)): #计数数组累加
        count[i] += count[i-1]
    temp = [None] * len(nums)
    for i in range(len(nums)-1,-1,-1): #反向填充, 维持稳定性
        idx = nums[i] - minn
        temp[count[idx]-1] = nums[i]
        count[idx]-=1
    return temp
    
def main():
    nums = [int(n) for n in input().split()] #直接输入数组,空格键隔断
    nums1 = counting(nums) #计数排序
    out = (nums1)
    print(out)
    return 0

if __name__ == '__main__':
    main()