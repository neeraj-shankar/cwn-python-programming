# Python3 program to reverse string without
# affecting it's special character
def rev(s, l, r):
    while l < r:
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        l += 1
        r -= 1


# creating character array of size
# equal to length of string
def reverse(s):
    temp = [''] * len(s)
    x = 0

    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z' or s[i] >= 'A' and s[i] <= 'Z':
            # storing elements in array
            temp[x] = s[i]
            x += 1

    # reversing the character array
    rev(temp, 0, x)

    lst = list(s)
    x = 0

    for i in range(len(s)):
        if s[i] >= 'a' and s[i] <= 'z' or s[i] >= 'A' and s[i] <= 'Z':
            # updating the origional string
            lst[i] = temp[x]
            x += 1

    revStr = ""
    for i in range(len(s)):
        revStr += lst[i]

    print("reverse string is :", revStr);


# Driver Code
if __name__ == "__main__":
    s = "abcdaefj@r#j"

    reverse(s)

# This code is contributed by aditya942003patil
