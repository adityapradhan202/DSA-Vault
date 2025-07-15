from typing import List
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ins = [] # commons
        occ = [] # occurences

        # Getting commons
        for n1 in nums1:
            for n2 in nums2:
                if n1 == n2:
                    ins.append(n1)
        ins = list(set(ins))

        for i in ins:
            occ1 = 0
            occ2 = 0
            for j in nums1:
                if i == j:
                    occ1 += 1
            for j in nums2:
                if i == j:
                    occ2 += 1
            if occ1 == occ2:
                occ.append(occ1)
            elif occ1 > occ2:
                occ.append(occ2)
            elif occ2 > occ1:
                occ.append(occ1)

        output = []
        for i in range(len(ins)):
            output += [ins[i]] * occ[i]
            # print(output)
        return output
    
def main():
    s = Solution()
    print(s.intersect(nums1=[4,9,5], nums2=[9,4,9,8,4]))

main()
                

