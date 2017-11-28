
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
        if input_array[i] <=  pivot:

            # Avoid unnecessary swaps
            if(pivot_index is not i):
                print('Swapping')
                print(input_array[pivot_index])
                print('with')
                print(input_array[i])
                print(input_array)
                input_array[i], input_array[pivot_index] = input_array[pivot_index], input_array[i]
                print(input_array)

            pivot_index += 1


    print('Swap pivot')
    print(input_array)
    input_array[end], input_array[pivot_index] = input_array[pivot_index], pivot
    print(input_array)

    return pivot_index


test = [2, 54, 4, 1, 9, 10, 22]
quick_sort(test, 0, len(test) - 1)

print('Result')
print(test)
