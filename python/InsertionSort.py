def insertion_sort(a):
    k =0
    for i in range(1, len(a)):
        if(a[i]<a[i-1]):
            k = k+1
            for j in range(i, 0, -1):
                if(a[j] < a[j-1]):
                    a[j-1], a[j] = a[j], a[j-1]
            print("after %d change: "%k, a)
    return a

def main():
    Array = list(map(int,input("please input the array(split by space):").split()))
    print("input is: ", Array)
    SortedArray = insertion_sort(Array)
    print("result is: ", SortedArray)


if __name__ == "__main__":
    main()
