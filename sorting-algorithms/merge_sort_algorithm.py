""" 
"""


def merge(custom_list, left_index, middle_index, right_index):
    n1 = middle_index - left_index + 1
    n2 = right_index - middle_index

    # Create two sub arrays
    left_array = [0] * n1
    right_array = [0] * n2

    # Divide the elements of the custom list into two sub arrays
    for i in range(0, n1):
        left_array[i] = custom_list[left_index + i]

    for j in range(0, n2):
        right_array[j] = custom_list[middle_index + 1 + j]

    # Merge the two sub arrays
    i = 0
    j = 0
    k = left_index
    while i < n1 and j < n2:
        if left_array[i] <= right_array[j]:
            custom_list[k] = left_array[i]
            i += 1
            k += 1
        else:
            custom_list[k] = right_array[j]
            j += 1
            k += 1

    # Handling the remaining element of the left and right arrays
    while i < n1:
        custom_list[k] = left_array[i]
        i += 1
        k += 1

    while j < n2:
        custom_list[k] = right_array[j]
        j += 1
        k += 1


# writing the merger sort method
def merge_sort(custom_list, left_index, right_index):
    if left_index < right_index:
        middle_index = (left_index + (right_index - 1)) // 2
        merge_sort(custom_list, left_index, middle_index)
        merge_sort(custom_list, middle_index + 1, right_index)
        merge(custom_list, left_index, middle_index, right_index)
    return custom_list


""" 
"""
if __name__ == "__main__":
    custom_list = [2, 4, 12, 7, 6, 18]
    l = 0
    r = len(custom_list) - 1
    result = merge_sort(custom_list, l, r)
    print(f"The sorted array --> {result}")
