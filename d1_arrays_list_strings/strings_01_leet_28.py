# Leetcode problem 28
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/

class Solution:
    # Solving manually
    # Complexity O(n*m), better than O(n^2)
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)):
            if i <= len(haystack) - len(needle):
                sliced = haystack[i:i+len(needle)]
                if sliced == needle:
                    return i
            if i == len(haystack) - 1:
                return -1
            
    # Solving with inbuilts (n*m)
    def str_posi_inbuilt(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1
             
def main():
    s = Solution()
    # print(s.strStr(haystack="hello", needle="lyyi"))

    print(s.str_posi_inbuilt(haystack="hello", needle="ll"))

if  __name__ == "__main__":
    main()
