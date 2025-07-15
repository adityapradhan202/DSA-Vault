# def swap_items(n1, n2):
#     temp = n1
#     n1 = n2
#     n2 = temp
#     return n1, n2

# def bubble_sort(array):
#     n = len(array)
#     i = 0
#     while i < n:
#         j = 0
#         while j < (n - 1 - i):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = swap_items(array[j], array[j+1])
#             j += 1
#         i += 1
#     return array

# def second_largest(array):
#     sorted = bubble_sort(array)
#     max_val = sorted[-1]
#     k = len(array) - 1
#     while k >= 0:
#         if sorted[k] < max_val:
#             return sorted[k]
#         k -= 1 # decrement
#     if sorted[k] == max_val:
#         return max_val
    
# def main():
#     inp = [4.3, 5, 6, 7]
#     print(second_largest(inp))

# The entire solution written above, for finding the second largest number in the list
# is a stupid solution

# There is a very simple solution for this problem

def second_largest(n):
    # Sample example of input
    # [1, 3, 5, 9]
    # Initialize the max_val and smax with smallest value possible
    max_val = float("-inf")
    smax = float("-inf") # second max
    i = 0
    while i < len(n):
        if n[i] > max_val:
            smax = max_val # Old value of max_val goes into smax
            max_val = n[i]
        elif not(n[i] >= max_val) and n[i] > smax:
            smax = n[i] 
        i += 1

    return smax

def main():
    inp_array = [2, 3, 4, 6, 77, 9]
    print(second_largest(inp_array))

if __name__ == "__main__":
    main()






