def bubble_sort(array):
    i = 0
    while i < len(array):
        j = 0 # J needs to restart to zero at the start
        while j < (len(array) - 1 - i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
            j += 1
        i+= 1
    return array # Sorted array

def main():
    array = [9, 8, 3, 1, 5]
    print(bubble_sort(array))

if __name__ == "__main__":
    main()