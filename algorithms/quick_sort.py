
def quick_sort(input_array, start, end):

    if start >= end:
        return

    partition_index = partition(input_array, start, end)
    quick_sort(input_array, start, partition_index - 1)
    quick_sort(input_array, partition_index + 1, end)


def partition(input_array, start, end):

    pivot = input_array[end]

    pivot_index = start
    for i in range(start, end):
        if input_array[i] <= pivot:
            print('swapping')
            print(input_array)
            temp = input_array[i]
            input_array[i] = input_array[pivot_index]
            input_array[pivot_index] = temp

            print(input_array)

            pivot_index += 1

    print(pivot_index)
    print('swap pivot')
    print(input_array)
    temp = input_array[pivot_index]
    input_array[pivot_index] = pivot
    input_array[end] = temp

    print(input_array)
    return pivot_index


test = [2, 54, 4, 1, 9]
quick_sort(test, 0, len(test) - 1)

print('Result')
print(test)
