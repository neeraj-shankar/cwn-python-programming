
'''
---------------------------------------------------------------------------------------------------
Problem Statement:
-----------------------------------------------------------
Maria plays college basketball. Each season she maintains a record of her play. She tabulates the number
of times she breaks her season record for most points and least points in a game. Points scored in the
first game establish her record for the season, and she begins counting from there.

Example Input: 
scores = [12, 24, 10, 24]

Example Output:
1 1

Explanation:
-----------------------------------------------------------
   Game  Score  Minimum  Maximum   Min Max
     0      12     12       12       0   0
     1      24     12       24       0   1
     2      10     10       24       1   1
     3      24     10       24       1   1

-----------------------------------------------------------

'''

def break_the_records(scores):
    minimum = maximum = scores[0]
    max_count = min_count = 0
    for score in scores[1:]:
        if score < minimum:
            minimum = score
            min_count += 1
        
        elif score > maximum:
            maximum = score
            max_count += 1
    record = [max_count, min_count]
    return record

if __name__ == '__main__':
    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    result = break_the_records(scores)
    print(f"Final Result: {result}")


# Attempt to solve the problem using list comprehension.
def breaking_records(scores):
    highest_score, lowest_score = scores[0], scores[0]

    # Calculate the counts using list comprehension
    highest_count, lowest_count = sum(score > (highest_score := max(highest_score, score)) for score in scores[1:]), \
                                 sum(score < (lowest_score := min(lowest_score, score)) for score in scores[1:])

    return highest_count, lowest_count

if __name__ == '__main__':
    scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
    scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
    result = break_the_records(scores)
    print(f"Final Result: {result}")


