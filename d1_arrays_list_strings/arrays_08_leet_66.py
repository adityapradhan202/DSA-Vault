"""
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].

"""

from typing import List
class Solution:
    def plus_one(self, digits:List[int]) -> List[int]:
        last = digits[-1]
        if last < 9:
            digits[-1] = digits[-1] + 1
            return digits
        else:
            # when last = 9
            if len(digits) == 1:
                return [1,0]
            else:
                digits[-1] = 0
                digits[-2] = digits[-2] + 1
                return digits
def main():
    s = Solution()
    print(s.plus_one([9]))
    [1].ex
    
if __name__ == "__main__":
    main()

                
