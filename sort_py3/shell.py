# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 21:37:43 2019

@author: dellbook
"""
def shell(nums):
    gap = len(nums)//2  #间隔, 每次砍半
    while gap >=1:
        for idx in range(0,gap): #一共gap各个组
            for i in range(idx+gap ,len(nums), gap): #从每组第二个元素开始进行插排
                while i > idx and nums[i] < nums[i-gap]:
                    nums[i], nums[i-gap] = nums[i-gap],nums[i]
                    i -= gap
        gap //= 2
    return nums

def main():
    #import json#inp = input("list:")
    nums = [int(n) for n in input().split()] #直接输入数组,空格键隔断
    #num = list(map(int, input().strip().split())
    nums1 = shell(nums) #希尔排序
    out = (nums1)
    print(out)
    return 0

if __name__ == '__main__':
    main()
    