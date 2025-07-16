from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Breaking down problem into parts
        # 1. Find the two biggest containers
        # 2. Find the position of two containers
        # 3. Find the area of the intersection (Final task)

    # Think about it!!!!
        sort_h = sorted(height)
        max_cont = 0
        min_cont = 0
        for h in sort_h:
            if h > max_cont:
                max_cont = h
        for j in range(len(sort_h)-1, -1, -1):
            if sort_h[j] < max_cont:
                min_cont = sort_h[j]
                break
        print(max_cont, min_cont)

        # Two pointer approach!
        p1 = 0
        p2 = len(height) - 1
        # Pending
        

s = Solution()
s.maxArea(height=[2, 3, 4, 5, 8, 88, 9, 8, 88])