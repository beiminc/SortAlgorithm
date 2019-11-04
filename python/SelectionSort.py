def selection_sort(a):
    for i in range(len(a)):
        min_key = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_key]:
                min_key = j
        a[i], a[min_key] = a[min_key], a[i]
        print("after %d change:"%i, a)
    return a

def main():
    Array = list(map(int,input("please input the array(split by space):").split()))
    print("input is: ",Array)
    SortedArray = selection_sort(Array)
    print("result is: ", SortedArray)


if __name__ == "__main__":
    main()
