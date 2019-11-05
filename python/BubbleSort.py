def bubble_sort_ascended(a):
    k =0
    for i in range(0, len(a)):
        flag = False
        k = k + 1
        for j in range(len(a)-1, i, -1):
            if(a[j] < a[j-1]):
                flag = True
                a[j], a[j-1] = a[j-1], a[j]
        if(not flag):
            break
        print("after %d change: "%k, a)
    return a

def bubble_sort_dascended(a):
    k =0
    for i in range(0, len(a)):
        flag = False
        k = k + 1
        for j in range(len(a)-1, i, -1):
            if(a[j] > a[j-1]):
                flag = True
                a[j], a[j-1] = a[j-1], a[j]
        if(not flag):
            break
        print("after %d change: "%k, a)
    return a

def main():
    Array = list(map(int,input("please input the array(split by space):").split()))
    print("input is: ", Array)
    SortedArrayAscend = bubble_sort_ascended(Array)
    print("ascend result is: ", SortedArrayAscend)

    SortedArrayDascend = bubble_sort_dascended(Array)
    print("dascend result is: ", SortedArrayDascend)

if __name__ == "__main__":
    main()