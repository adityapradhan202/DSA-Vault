# Leetcode problem 349
# Intersection of array

from typing import List

class Solution:
    # This is O(n^2)
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ins = [] # intersection

        for j in range(len(nums1)):
            for i in range(len(nums2)):
                if nums1[j] == nums2[i]:
                    ins.append(nums1[j]) # Append in the list
        # Time complexity till here goes to O(n^2)

        return list(set(ins))

    def intersection(self, nums1: List[int], nums2:List[int]) -> List[int]:
        ins = []
        for num in nums1:
            if num in nums2:
                ins.append(num)
        return list(set(ins))
    
    # This is O(n)
    def intersection_built_in(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        s1.intersection_update(s2)
        return s1
    
def main():
    nums1 = [3, 4, 5]
    nums2 = [9, 4, 3, 3, 2]
    sol = Solution()
    print(sol.intersection(nums1, nums2))

if __name__ == "__main__":
    main()

