# encoding: utf-8

def quick_sort(arr,first,last):
    if first<last:
       splitpoint = partition(arr,first,last)
       quick_sort(arr,first,splitpoint-1)
       quick_sort(arr,splitpoint+1,last)
    return arr

def partition(arr,first,last):
   pivotvalue = arr[first]

   leftmark = first+1
   rightmark = last

   while not rightmark < leftmark:

       while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
           leftmark = leftmark + 1
       while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       else:
           arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]

   arr[first], arr[rightmark] = arr[rightmark], arr[first]
   return rightmark
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    leftlist = arr[:mid]
    rightlist = arr[mid:]

    L = merge_sort(leftlist)
    R = merge_sort(rightlist)

    i = j = 0
    result = []
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            result.append(L[i])
            i+=1
        else:
            result.append(R[j])
            j+=1

    # 정렬하고 나머지를 결과에 붙여준다.
    result += L[i:]
    result += R[j:]
    return result

def insertion_sort(arr):
    # i: unsorted array의 index
    # j: sorted array의 index
    for i in range(1, len(arr)): # 첫번째는 sorted array라고 가정, i는 unsorted array의 첫번째 값
        j = i
        while (j > 0 and arr[i] < arr[j-1]): # sorted array에서 가장 마지막 값과 비교
            j -= 1
        temp = arr[i]
        k = i # unsorted array의 첫번째 값 부터 시작해서 앞으로 쉬프트
        while (k > 0 and k >= j): # 선택한 값을 왼쪽으로 쉬프트 
            arr[k] = arr[k-1]
            k -= 1
        arr[j] = temp
    return arr

def selection_sort(arr):
    for i in range(len(arr)-1): # 마지막 배열의 값은 자동으로 정렬되기 때문에 -1
        least_idx = i
        # 최소값을 찾는
        for j in range(i+1, len(arr)):
            if arr[least_idx] > arr[j]:
                least_idx = j
        temp = arr[least_idx]
        arr[least_idx] = arr[i]
        arr[i] = temp
    return arr

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
    return arr

def main():
    arr = [56,8,45,2,42,7,34,3]
    print (bubble_sort(arr))
    arr = [56,8,45,2,42,7,34,3]
    print (selection_sort(arr))
    arr = [56,8,45,2,42,7,34,3]
    print (insertion_sort(arr))
    arr = [56,8,45,2,42,7,34,3]
    print (merge_sort(arr))
    arr = [56,8,45,2,42,7,34,3]
    print (quick_sort(arr))

if __name__ == "__main__":
    main()
