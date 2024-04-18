def calculate_average(*args):
    total_marks = sum(args)
    num_subjects = len(args)
    average = total_marks / num_subjects
    print("The average is:", average)
    if average >= 50:
         print("pass")
    else:
        print("fail")

calculate_average(20,40,30)