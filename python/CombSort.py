import datetime

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

def comb_sort_ascended(a):
    step = len(a)
    t = 0
    while (step > 1):
        t = t + 1
        k = int(step)
        for i in range(0, len(a)-k):
            if(a[i] > a[i+k]):
                a[i], a[i+k] = a[i+k], a[i]
        step = step/1.3
        print("after %d comb change: "%t, a)
    
    print("before bubble: ", a)

    bubble_sort_ascended(a)
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

def comb_sort_dascended(a):
    step = len(a)
    t = 0
    while (step > 1):
        t = t + 1
        k = int(step)
        for i in range(0, len(a)-k):
            if(a[i] < a[i+k]):
                a[i], a[i+k] = a[i+k], a[i]
        step = step/1.3
        print("after %d comb change: "%t, a)
    
    print("before bubble: ", a)

    bubble_sort_dascended(a)
    return a

def main():
    start = datetime.datetime.now()
    Array = list(map(int,input("please input the array(split by space):").split()))
    print("input is: ", Array)
    SortedArrayAscend = comb_sort_ascended(Array)
    print("ascend result is: ", SortedArrayAscend)

    SortedArrayDascend = comb_sort_dascended(Array)
    print("dascend result is: ", SortedArrayDascend)
    end = datetime.datetime.now()
    print(end - start)

if __name__ == "__main__":
    main()