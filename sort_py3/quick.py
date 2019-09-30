# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:43:11 2019

@author: dellbook
"""
import random 
def quick(nums, left, right ):
    if right-left <=0: return #即列表长为 1 /0 时return
    x, idx = nums[right], left #piovot,分割序列的下标
    for i in range(left,right):
        if nums[i] < x:
            nums[i],nums[idx] = nums[idx],nums[i]
            idx+=1
    nums[idx], nums[right] = nums[right], nums[idx]
    quick(nums, left, idx-1)
    quick(nums, idx+1, right)
    return 
 
def random_quick(nums, left, right ):
    if right-left <=0: return #即列表长为 1 /0 时return
    randomindex = random.randint(left,right)
    nums[right], nums[randomindex] = nums[randomindex], nums[right]
    x, idx = nums[right], left #piovot,分割序列的下标
    for i in range(left,right):
        if nums[i] < x:
            nums[i],nums[idx] = nums[idx],nums[i]
            idx+=1
    nums[idx], nums[right] = nums[right], nums[idx]
    random_quick(nums, left, idx-1)
    random_quick(nums, idx+1, right)
    return        
        
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



def threeway_quick(nums,left,right):
    if right-left <=0: return 
    randomindex = random.randint(left,right) #随机选择pioviot
    nums[right], nums[randomindex] = nums[randomindex], nums[right]
    L,R, cur, x = left-1, right, left, nums[right]
    while cur < R:
        if nums[cur] < x:
            L+=1
            nums[cur],nums[L] = nums[L],nums[cur]
            cur+=1
        elif nums[cur] > x:
            R-=1
            nums[cur],nums[R] = nums[R],nums[cur]
        else:
            cur+=1  
    nums[right],nums[cur] = nums[cur],nums[right]
    threeway_quick(nums, left, L)
    threeway_quick(nums, R+1, right)
    return
    
def main():
    nums = [int(n) for n in input().split()] #直接输入数组,空格键隔断
    twoway_quick(nums,0,len(nums)-1) #快速排序
    out = (nums)
    print(out)
    return 0

if __name__ == '__main__':
    main()