# Given an alphanumeric string s, return the second largest numerical digit that appears in s, 
# or -1 if it does not exist.
# An alphanumeric string is a string consisting of lowercase English letters and digits.

# Link - https://leetcode.com/problems/second-largest-digit-in-a-string/description/
# Note - Alphanumeric string is a string which contains lower case english alphabets and numbers

class Solution:
    def secondHighest(self, s: str) -> int:

        numbers = []
        for char in s:
            if char.isnumeric():
                numbers.append(int(char))
        j = 0
        while j < len(numbers):
            if numbers[j] == numbers[0]:
                j += 1
                continue
            else:
                break
        if j == len(numbers):
            return -1
        # Till here Space Complexity is O(n)
        
        max_val = float("-inf")
        smax = float("-inf")
        for char in s:
            if char.isnumeric():
                if int(char) > max_val:
                    smax = max_val
                    max_val = int(char)
                elif not(int(char) >= max_val) and int(char) > smax:
                    smax = int(char)
        return smax
        # Till here space complexity is O(n) and time complexity is O(n)
    
    # Better solution
    # Space complexity o(1) and time complexity o(n)
    def secondHighest_o1(self, s:str) -> int:
        max_val = -1
        smax = -1
        for char in s:
            if char.isnumeric():
                num = int(char)
                if num > max_val:
                    smax = max_val
                    max_val = num
                elif not(num  >= max_val) and num > smax:
                    smax = num

        return smax

def main():

    s = Solution()
    print(s.secondHighest_o1("aa11s11111111ca2"))

if __name__ == "__main__":
    main()
        
