#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 15:15:29 2022
@author: parisbg
1968. Array With Elements Not Equal to Average of Neighbors

You are given a 0-indexed array nums of distinct integers. You want to rearrange the elements in the array such that every element in the rearranged array is not equal to the average of its neighbors.

More formally, the rearranged array should have the property such that for every i in the range 1 <= i < nums.length - 1, (nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

Return any rearrangement of nums that meets the requirements.
"""


#First and last values do not have necessary neighbors so we can ignore
#nums[]len(nums - 1] -- We don't have to check and nums[0]
#Traverse through the list
#[1, 2,3,4,5,6,7,8,9, 10]
#for i in range(1,len(nums-1))
#if nums[i] == (nums[i-1] + nums[i+1]) / 2
#Need to rearrange this value.. brute force way would be insert it at the end of the list
#else value does not match neighbors so continue to next iteration
#dict = {2:2,3:3,}

nums = [1,2,3,4,5,6,7,8,9,10]
result = []
nums.sort()

l,r = 0, len(nums)-1
while len(nums) != len(result):
    result.append(nums[l])
    l += 1

    if l <= r:
        result.append(nums[r])
        r -= 1
    
#return result