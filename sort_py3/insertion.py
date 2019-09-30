# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 20:48:23 2019

@author: dellbook
"""
def insertion(nums):
    for i in range(1,len(nums)):
        x,j = nums[i],i-1
        while j>-1 and x <nums[j]:
            nums[j+1] = nums[j]
            j-=1
        nums[j+1] = x
    return nums

def insertion1(nums):
    for i in range(1,len(nums)):
        while i > 0 and nums[i] < nums[i-1]:
            nums[i],nums[i-1] = nums[i-1], nums[i]
            i-=1        
    return nums
def insertion_bi(nums):
    for i in range(1,len(nums)):
        l,r,x = 0, i-1, nums[i]
        while l<=r:
            mid = (l+r)//2
            if nums[mid] > x:
                r = mid -1
            else:
                l = mid +1
        for j in range(i-1,l-1,-1):
            nums[j+1] = nums[j]
        nums[l] = x
    return nums



def main():
    #import json#inp = input("list:")
    nums = [int(n) for n in input().split()] #直接输入数组,空格键隔断
    #num = list(map(int, input().strip().split())
    nums1 = insertion_bi(nums) #
    out = (nums1)
    print(out)
    return 0

if __name__ == '__main__':
    main()