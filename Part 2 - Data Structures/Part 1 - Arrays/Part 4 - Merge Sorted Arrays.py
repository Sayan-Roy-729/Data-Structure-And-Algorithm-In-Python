# mergeSortedArrays([0, 3, 4, 31], [4, 6, 30])
# [0, 3, 4, 4, 6, 30, 31]

def mergeSortedArrays(array1, array2):
    if len(array1) == 0 or len(array2) == 0:
        return array1 + array2
        
    mylist=[]
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):

        if array1[i] <= array2[j]:
            mylist.append(array1[i])
            i += 1

        elif array2[j] < array1[i]:
            mylist.append(array2[j])
            j += 1

    return mylist + array1[i:] + array2[j:]

if __name__ == "__main__":
    print(mergeSortedArrays([0, 3, 4, 31], [4, 6, 30]))
