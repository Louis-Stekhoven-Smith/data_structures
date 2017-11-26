

def merge_sort(input_array):

    arraySize = len(input_array)

    # Break out statement
    if(arraySize < 2):
        return

    midPoint  = int(arraySize / 2)

    left_array = []
    right_array = []

    for i in range(0, midPoint):
        left_array.append(input_array[i])

    for i in range(midPoint, arraySize):
        right_array.append(input_array[i])

    merge_sort(left_array)
    merge_sort(right_array)
    merge(left_array,right_array,input_array)



def merge(left_array,right_array,input_array):

    i = j = k = 0
    # print('Merging')
    # print(left_array)
    # print(right_array)

    # Start merging left and right arrays
    while(i < len(left_array) and j < len(right_array)):
        if left_array[i] < right_array[j]:
            input_array[k] = left_array[i]
            i += 1

        elif right_array[j] < left_array[i]:
            input_array[k] = right_array[j]
            j += 1

        k += 1

    # Merge remaining data in either the left or right array
    while(i < len(left_array)):
        input_array[k] = left_array[i]
        i += 1
        k += 1

    while(j < len(right_array)):
        input_array[k] = right_array[j]
        j += 1
        k += 1

    # print('Merged')
    # print(input_array)




input = [3,5,7,10,2,1]

merge_sort(input)

print(input)