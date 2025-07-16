# Link - https://leetcode.com/problems/move-zeroes/
from typing import List
import numpy as np
import pandas as pd


class Solution:
    # Python solution - with inbuilt
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                break
            i += 1
        if i == len(nums):
            return nums

        count = 0
        for num in nums:
            if num == 0:
                count += 1
        for _ in range(count):
            nums.remove(0)
            nums.append(0)
        
        return nums
    
    # Best solution
    def moveZeroesV2(self, nums:List[int]) -> None:
        # example [1,0,2,0,3]
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            else:
                # If zero is encountered, i += 1 and move on
                continue
        for i in range(j, len(nums)):
            nums[i] = 0
        return nums
    
s = Solution()
res = s.moveZeroesV2(nums=[1,0,1,0])
print(res)


        