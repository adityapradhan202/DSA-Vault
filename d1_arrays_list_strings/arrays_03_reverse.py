def reverse_array(array):
    array_sort = array.copy() # Same length as actual array
    
    sort_len = len(array) # O(1) in python
    arr_len = len(array) # O(1) in python
    ind = 0
    # Complexity of this while loop - O(n)
    while ind < arr_len:
        array_sort[sort_len-1] = array[ind]
        ind += 1
        sort_len -= 1

    return array_sort

def main():
    array = [22, 45, 6, 7, 8, 9, 10, 15]
    print(reverse_array(array))

if __name__ == "__main__":
    main()

# len(array) and len(array) are O(1), length is saved as an property in python, for sequential dtypes
# while loop iterates over all the elements once  O(n)
# so overal time complexity of reversing an array becomes O(n)



        
