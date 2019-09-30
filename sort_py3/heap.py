# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:08:50 2019

@author: dellbook
"""
def initialize(nums): #初始化最大堆
    n = len(nums)
    for i in range((n-1)//2,-1,-1):
        heapify(nums,i,n)
    return nums

def heapify(nums,i,n): #调整大小为n的堆的第i个元素
    if i>=n:return
    maxx = i
    if 2*i + 1 < n and  nums[maxx] < nums[2*i+1]:
        maxx = 2*i+1
    if 2*i+2 < n and nums[maxx] < nums[2*i+2]:
        maxx = 2*i+2        
    if maxx != i:
        nums[maxx], nums[i] = nums[i], nums[maxx]
        heapify(nums,maxx,n)
    return 

def heapsort(nums):
    nums = initialize(nums)
    for k in range(len(nums)-1,-1,-1):
        nums[0], nums[k] = nums[k], nums[0]
        heapify(nums,0,k)
    return nums

def main():
    #import json#inp = input("list:")
    nums = [int(n) for n in input().split()] #直接输入数组,空格键隔断
    #num = list(map(int, input().strip().split())
    nums1 = heapsort(nums) #选择
    out = (nums1)
    print(out)
    return 0

if __name__ == '__main__':
    main()