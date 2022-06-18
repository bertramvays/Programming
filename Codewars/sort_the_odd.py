"""
You will be given an array of numbers. You have to sort
the odd numbers in ascending order
while leaving the even numbers at their original positions.
"""


def sort_array(source_array):
    result_array = []
    odd_array = []
    for i in source_array:
        if i % 2 == 0:
            result_array.append(i)
        else:
            result_array.append(None)
            odd_array.append(i)
    odd_array.sort()
    for i, el in enumerate(result_array):
        if el is None:
            result_array[i] = odd_array.pop(0)
    print(result_array)
    return result_array


sort_array([])
