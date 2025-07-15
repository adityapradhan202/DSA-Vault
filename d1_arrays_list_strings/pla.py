"""
Jaffer wanted to excel in math. He was learning about the karperkar number from Meena, his Maths teacher. She gave him a few random numbers and asked him to find out whether they are kaprekar number or not. (consider an n-digit number k, Square it and add the right n digits to the left n or n-1 digits. If the resultant is sum is k, then k is karpekar number as 297^2 = 88209 & 88 + 209 = 297)
"""

class Solution:
    def check_karpekar(number):
        nsq = number ** 2
        digits_sq = [int(n) for n in str(number)]

        if len(digits_sq) == 2 and (digits_sq[0] + digits_sq[1] == number):
            return "Karpekar number"
        else:
            pass

        
            
