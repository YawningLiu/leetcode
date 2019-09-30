# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 16:36:38 2019

@author: dellbook
"""
def merge(nums, left, mid, right):
    idx1, idx2, idx = left, mid +1, 0
    new = [None] *(right - left +1)
    while idx1 <=mid and idx2 <=right and idx <= right-left:
        if nums[idx1] > nums[idx2]:
            new[idx] =nums[idx2]
            idx2 += 1
        else:
            new[idx] =nums[idx1]
            idx1 += 1
        idx +=1
    while idx1 <=mid :
        new[idx] =nums[idx1]
        idx+=1
        idx1+=1
    while idx2 <=right:
        new[idx] =nums[idx2]
        idx+=1
        idx2+=1
    for i in range(left,right+1):
        nums[i] = new[i-left]

def mergesort(nums,left,right):
    if right <= left:return 
    mid = (left+right)//2
    mergesort(nums,left, mid)
    mergesort(nums, mid+1, right)
    merge(nums,left,mid,right)

def iterative_mergesort(nums):
    n, gap = len(nums), 1
    while gap < n:
        left = 0
        while left + gap < n:
            mid = left +gap-1
            right = min(n-1,mid+gap)
            merge(nums,left,mid,right)
            left = right+1
        gap <<= 1


def main():
    #import json#inp = input("list:")
    nums = [int(n) for n in input().split()] #直接输入数组,空格键隔断
    iterative_mergesort(nums) #选择
    out = (nums)
    print(out)
    return 0

if __name__ == '__main__':
    main()