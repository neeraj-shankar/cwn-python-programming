def is_beautiful(s):
    n = len(s)
    
    # Iterate through possible lengths of the first number in the sequence
    for i in range(1, n // 2 + 1):
        first_num = s[:i]
        print(f"First Number --> {first_num}")
        if first_num.startswith('0'):
            # Skip if the first number has a leading zero
            continue

        seq = [int(first_num)]
        j = i
        while j < n:
            next_num = seq[-1] + 1
            print(f"Next Num: {next_num}")
            next_num_str = str(next_num)
            if s.startswith(next_num_str, j):
                # Append the next number to the sequence
                seq.append(next_num)
                j += len(next_num_str)
            else:
                # If we can't continue the sequence, break the loop
                break

        if j == n and len(seq) >= 2:
            # If we successfully split the string into a sequence of positive integers
            return "YES"

    return "NO"

# Example usage:
numeric_string = "1234"
result = is_beautiful(numeric_string)
print(result)  # Output: "YES"
