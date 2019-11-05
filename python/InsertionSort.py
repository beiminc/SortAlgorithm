def insertion_sort_ascended(a):
    k =0
    for i in range(1, len(a)):
        if(a[i] < a[i-1]):  # 第i位之前已排好序，如果当前i位比i-1大，则已成升序，不用再排
            k = k+1
            for j in range(i, 0, -1):
                if(a[j] < a[j-1]):
                    a[j-1], a[j] = a[j], a[j-1]
            print("after %d change: "%k, a)
    return a

def insertion_sort_dascended(a):
    k =0
    for i in range(1, len(a)):
        if(a[i] > a[i-1]):  # 第i位之前已排好序，如果当前i位比i-1大，则已成降序，不用再排
            k = k+1
            for j in range(i, 0, -1):
                if(a[j] > a[j-1]):
                    a[j-1], a[j] = a[j], a[j-1]
            print("after %d change: "%k, a)
    return a

def main():
    Array = list(map(int,input("please input the array(split by space):").split()))
    print("input is: ", Array)
    SortedArrayAscend = insertion_sort_ascended(Array)
    print("ascend result is: ", SortedArrayAscend)

    SortedArrayDascend = insertion_sort_dascended(Array)
    print("dascend result is: ", SortedArrayDascend)


if __name__ == "__main__":
    main()
