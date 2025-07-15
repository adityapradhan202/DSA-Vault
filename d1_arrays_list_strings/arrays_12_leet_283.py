# Link - https://leetcode.com/problems/move-zeroes/
from typing import List

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
    
    def moveZeroesTwoPointer(self, nums:List[int]) -> None:
        i = 0
        while i < len(nums):
            if nums[i] != 0:
                break
            i += 1
        if i == len(nums):
            return nums
        elif len(nums) == 1 and nums[0] != 0:
            return nums
        elif 0 not in nums:
            return nums
        
        p1 = 0
        p2 = 1
        while p1 < len(nums) and p2 < len(nums):
            if nums[p1] == 0 and nums[p2] != 0:
                temp = nums[p1]
                nums[p1] = nums[p2]
                nums[p2] = temp
                print(nums)
            elif nums[p1] == 0 and nums[p2] == 0:
                if nums[p2+1] != 0:
                    temp = nums[p2]
                    nums[p2] = nums[p2+1]
                    nums[p2+1] = temp
                    print(nums)
            
            p1 += 1
            p2 += 1
        return nums
    


s = Solution()
res = s.moveZeroesTwoPointer(nums=[0,1,0,3,12])
print(res)


        