# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 23:03:44 2019

@author: dellbook
"""
def selection(nums):
    for i in range(len(nums)-1):
        idx = min(range(i,len(nums)), key = lambda x: nums[x])
        if idx !=i:
          nums[i], nums[idx] = nums[idx], nums[i]
    return nums
        
def main():
    #import json#inp = input("list:")
    nums = [int(n) for n in input().split()] #直接输入数组,空格键隔断
    #num = list(map(int, input().strip().split())
    nums1 = selection(nums) #选择
    out = (nums1)
    print(out)
    return 0

if __name__ == '__main__':
    main()