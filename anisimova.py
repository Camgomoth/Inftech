#this is for test
def bubble_sort():
    a = [1, 8, 3, 5, 7, 4]

    print(a)
    j = 1
    while j < len(a):
        k = 0
        while k < (len(a) - 1):
            if a[k] > a[k+1]:
                a[k], a[k+1] = a[k+1], a[k]
            k += 1
        j += 1
    
    return a

def selection_sort():
    arr = [1,2,3,4,5,6]
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)): 
            if arr[j] < arr [minimum]:
                minimum = j
        
        arr [minimum], arr[i] = arr[i], arr [minimum]
    
    return arr

def insertion_sort(): 
    array = [22,56,73,11,12,9,67,105,2]
    length = len(array) 
    for i in range(1, length):
        key = array[i]
        j = i
        while (j - 1 >= 0) and (array[j - 1] > key):
            array[j - 1], array[j] = array[j], array[j - 1]
            j = j - 1
        array[j] = key
    return array


