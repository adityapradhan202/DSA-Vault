from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sort = sorted(nums)
        low = 0
        high = len(nums) - 1
        n1 = 0
        n2 = 0
        while low < high:
            curr_sum = nums_sort[low] + nums_sort[high]
            if curr_sum == target:
                n1 = nums_sort[low]
                n2 = nums_sort[high]
                break
            elif curr_sum < target:
                low += 1
            elif curr_sum > target:
                high -= 1
        ins = []
        for i in range(len(nums)):
            if nums[i] == n1:
                ins.append(i)
                break
        for j in range(len(nums)):
            if nums[j] == n2 and j != ins[0]:  # Make sure it's not the same index
                ins.append(j)
                break
        
        return ins
        

            

s = Solution()
print(s.twoSum(nums=[-1,-2,-3,-4,-5], target=-8))
    