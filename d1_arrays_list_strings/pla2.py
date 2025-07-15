"""
Prrofessor Kishore wanted the kids to learn about Special numbers. (A two-digit number is said to be a spcial number if the sum of sum of its digits and product of its digits is equal to the nummber itself. For example, 19 is a special number. The digits in 19 are 1 and 9. The sum of the digits is 10 and the prodict is 9, 10+9)
"""

def check_special_number(number:int):
    digits = [int(n) for n in str(number)]
    sum = 0
    product = 1
    for d in digits:
        sum += d
        product *= d
    if sum + product == number:
        return f"{number} is a Special Number"
    else:
        return f"{number} is not a spcecial number"

def main():
    print(check_special_number(number=19))
    
if __name__ == "__main__":
    main()
