# calcluate the averge height from list of student given 

def average_height():
    student_list = [180, 124, 165, 173, 189, 169, 146]
    total_height = 0
    total_students = 0

    for h  in student_list:
        total_height = total_height + h
        total_students = total_students + 1
    
    average_student_height = total_height/total_students
    print(f"The sum of heights {total_height}")
    print(f"Total students {total_students}")

    print(f"The average height of of all student {round(average_student_height)}")



#calling the function 
average_height()