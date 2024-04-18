def main():

    student = {}

    num_student = int(input('enter the number of students:'))

    for i in range(num_student):
        reg_number = input('enter the registration numbers: ')
        first_name = input('enter the first name: ')
        student[reg_number] = first_name

    print('student_dict:', student)

