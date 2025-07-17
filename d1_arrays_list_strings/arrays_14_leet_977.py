# [-4,-1,0,3,10]

from typing import List
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        # print(nums)
        left = 0 
        right = len(nums) - 1
        elements = []
        while left <= right:
            if nums[right] > nums[left]:
                elements.append(nums[right])
                right -= 1
            else:
                elements.append(nums[left])
                left += 1

        left = 0
        right = len(elements) - 1
        while left < right: # false whhen right > left or right == left
            temp = elements[left]
            elements[left] = elements[right]
            elements[right] = temp
            # or nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        return elements



s = Solution()
nums =[-17,-16,-4,-1,0,3,10]
print(s.sortedSquares(nums))