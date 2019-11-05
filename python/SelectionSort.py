def selection_sort_ascended(a):
    for i in range(len(a)):
        min_key = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_key]:
                min_key = j
        a[i], a[min_key] = a[min_key], a[i]
        print("after %d change:"%i, a)
    return a

def selection_sort_dascended(a):
    for i in range(len(a)):
        max_key = i
        for j in range(i + 1, len(a)):
            if a[j] > a[max_key]:
                max_key = j
        a[i], a[max_key] = a[max_key], a[i]
        print("after %d change:"%i, a)
    return a

def main():
    Array = list(map(int,input("please input the array(split by space):").split()))
    print("input is: ", Array)
    SortedArrayAscend = selection_sort_ascended(Array)
    print("ascend result is: ", SortedArrayAscend)

    SortedArrayDascend = selection_sort_dascended(Array)
    print("dascend result is: ", SortedArrayDascend)


if __name__ == "__main__":
    main()
