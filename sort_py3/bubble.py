# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 14:44:09 2019

@author: dellbook
"""
def bullesort0(nums): # 冒泡排序 -基础
    for i in range(len(nums)-1):
        for j in range(len(nums)-i-1):
            if nums[j] >nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
    return nums

def bullesort1(nums): # 冒泡排序 - 改进
    for i in range(len(nums)-1):
        end = 0 #end 后都不用比了
        for j in range(len(nums)-i-1):
            if nums[j] >nums[j+1]:
                nums[j],nums[j+1] = nums[j+1],nums[j]
        i = len(nums) - end -1
    return nums

def bullesort2(nums): # 鸡尾酒冒泡排序 
    left, right = 0, len(nums)-1
    while left < right:
        for j in range(left,right): #从前往后冒
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
        right-=1
        for j in range(right,left,-1): #从后往前冒
            if nums[j] < nums[j-1]:
                nums[j], nums[j-1] = nums[j-1], nums[j]
        left+=1
    return nums

def main():
    #import json#inp = input("list:")
    nums = [int(n) for n in input().split()] #直接输入数组,空格键隔断
    #num = list(map(int, input().strip().split())
    nums1 = bullesort2(nums) #冒泡排序0,1,2 三个版本
    out = (nums1)
    print(out)
    return 0

if __name__ == '__main__':
    main()
    