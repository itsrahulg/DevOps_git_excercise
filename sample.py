def sort(array):
    n = len(array)-1
    for i in range(n):
        for j in range(0,n-i):
            if array[j+1] < array[j]:
                array[j+1],array[j] = array[j],array[j+1]
            
    print(array)


array = [2,8,4,9,6,1]
sort(array)