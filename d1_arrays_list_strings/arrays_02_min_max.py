def find_max(array):
    max_val = 0
    i = 0
    while i < len(array):
        if array[i] >= max_val:
            max_val = array[i]
        i += 1
    return max_val

def find_min(array):
    i = 0
    min_val = array[i]
    while i < len(array):
        if array[i] <= min_val:
            min_val = array[i]
        i += 1
    return min_val

def main():
    a1 = [4, 5, 6, 7]
    a2 = [9, 8, 6, 3, 2, 11, 2, 7, 9, 3, 1]
    print(find_max(a1))
    print(find_min(a2))


if __name__ == "__main__":
    main()

        