# Find the highest scores from list of scores given.

def highest_score():
    # Taking the student scores 
    students_scores = list(map(int, input("Please enter the student scores").split()))

    top_score = 0

    for score in students_scores:
        if(score>top_score):
            top_score = score
    
    print(f"The highest score is {top_score}")



# calling the function
highest_score()