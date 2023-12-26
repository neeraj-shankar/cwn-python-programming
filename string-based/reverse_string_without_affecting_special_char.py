def rev(input_string, left, right):
    while left < right:
        temp = input_string[left]
        input_string[left] = input_string(right)
        input_string[right] = temp
        left += 1
        right -= 1


