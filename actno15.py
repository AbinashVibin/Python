def result(*marks):
    # Calculate the average
    avg = sum(marks) / len(marks)


    #determine if the student has passed or failed
    if avg >= 50:
        print(avg)

        print('passed')

    else:

        print('failed')


result(56,61,73)







