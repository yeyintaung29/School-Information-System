# Author: Ye Yint Aung
# Admin No/Grp: 222905W/BA2203

import time

students_total = 0  # Total Number of Students

#  Lists used for storing information
student_admission_no = []
student_list = []
module_names = []
module_scores = []


def main():  # Main Function for the Menu
    global students_total

    while True:
        print(f"""***** Welcome to SIT Mini Student Information System *****
Number of student in the system: {students_total}
These are the functions available:
Enter 1 to Add a new student
Enter 2 to Update an existing student info
Enter 3 to Remove an existing student info
Enter 4 to Display all student information in the system
Enter 5 to Search for student(s)
Enter -1 to Exit the application""")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            add_student()
            break

        elif choice == 2:
            if students_total == 0:

                print("\nThere is no student information currently in the system!")
                time.sleep(2)
                continue

            else:
                update_student()
                break

        elif choice == 3:
            if students_total == 0:
                print("\nThere is no student information currently in the system!")
                time.sleep(2)
                continue

            else:
                remove_student()
                break
        elif choice == 4:
            if students_total == 0:
                print("\nThere is no student information currently in the system!")
                time.sleep(2)
                continue

            else:
                display()
                break
        elif choice == 5:
            if students_total == 0:
                print("\nThere is no student information currently in the system!")
                time.sleep(2)
                continue

            else:
                search()
                break
        elif choice == -1:
            break
        else:
            print("Invalid choice!")
            time.sleep(2)
            continue


def add_student():  # Add Student Function
    global students_total
    global student_admission_no
    global student_list
    global module_names
    global module_scores

    print("\n== Add a new student ==")

    admission_number = input("Please enter the admission number: ")

    while True:
        if admission_number in student_admission_no:
            print("Admission number already exists in the system.")
            admission_number = input("Please enter a new admission number or enter 0 to return to main menu: ")
            if admission_number == '0':
                print('')
                main()
                break
            elif admission_number in student_admission_no:
                continue
            else:
                student_name = input("Please enter the student name: ")
                module_name = input("Please enter the module name: ")
                module_score = int(input("Please enter the score: "))

                students_total += 1

                student_admission_no.append(admission_number)
                student_list.append(student_name)
                module_names.append(module_name)
                module_scores.append(module_score)
                print("Student added!\n")
                time.sleep(1)
                main()
                break

        else:
            student_name = input("Please enter the student name: ")
            module_name = input("Please enter the module name: ")
            module_score = int(input("Please enter the score: "))

            students_total += 1

            student_admission_no.append(admission_number)
            student_list.append(student_name)
            module_names.append(module_name)
            module_scores.append(module_score)
            print("Student added!\n")
            time.sleep(1)
            main()
            break


def update_student():  # Update Student Function
    global student_admission_no
    global student_list
    global module_names
    global module_scores

    print("\n== Update student ==")

    while True:
        student_no = input("Please enter the admission number of the student you would like to update: ")
        if student_no not in student_admission_no:
            print("No such student found.")
            time.sleep(2)
            continue

        else:
            list_index = student_admission_no.index(student_no)

            print(f"""\nAdmission Number: {student_admission_no[list_index]}
Student Name: {student_list[list_index]}
Module Name: {module_names[list_index]}
Score: {module_scores[list_index]:.1f}
Student Exist!
Enter 1 to Update Name
Enter 2 to Update Module Name
Enter 3 to Update Score
Enter 0 to return to Main Menu""")

            choice = int(input("What would you like to update? "))

            if choice == 1:
                new_name = input("Enter the new student name: ")

                student_list[list_index] = new_name

                print("Student Name Updated!\n")
                time.sleep(1)
                main()
                break

            elif choice == 2:
                new_module = input("Enter the new module name: ")

                module_names[list_index] = new_module

                print("Module Name Updated!\n")
                time.sleep(1)
                main()
                break

            elif choice == 3:
                new_score = input("Enter the new score: ")

                module_scores[list_index] = int(new_score)

                print("Score Updated!\n")
                time.sleep(1)
                main()
                break

            elif choice == 0:
                print('')  # Space
                main()
                break

            else:
                print("Invalid choice!")
                time.sleep(2)
                continue


def remove_student():  # Remove Student Function
    global students_total
    global student_admission_no
    global student_list
    global module_names
    global module_scores

    while True:
        print("\n== Remove student ==")
        student_no = input("Please enter the admission number you want to remove: ")
        if student_no not in student_admission_no:
            print("No such student found.")
            time.sleep(2)
            continue

        else:
            list_index = student_admission_no.index(student_no)
            print(f"""\nAdmission Number: {student_admission_no[list_index]}
Student Name: {student_list[list_index]}
Module Name: {module_names[list_index]}
Score: {module_scores[list_index]:.1f}""")

            choice = input("Is this the student you want to remove? (Yes/No)").upper()

            if choice == 'YES':
                student_admission_no.pop(list_index)
                student_list.pop(list_index)
                module_names.pop(list_index)
                module_scores.pop(list_index)

                print("Student info removed!\n")
                students_total -= 1
                time.sleep(2)
                main()
                break

            elif choice == 'NO':
                print("Student info was not removed!\n")
                time.sleep(2)
                main()
                break

            else:
                print("Invalid choice!")
                time.sleep(2)
                continue


def display():  # Display Function
    global student_admission_no
    global student_list
    global module_names
    global module_scores

    print("\n== Display all students ==")

    list_index = 0

    while list_index < len(student_admission_no):  # While initial of 0 is less than 0, all lists are printed
        print(f"""\nAdmission Number: {student_admission_no[list_index]}
Student Name: {student_list[list_index]}
Module Name: {module_names[list_index]}
Score: {module_scores[list_index]:.1f}""")

        list_index += 1

    print("")  # Space

    time.sleep(2)
    main()


def search():  # Search Function
    global student_admission_no
    global student_list
    global module_names
    global module_scores

    while True:
        print("\n== Search Student ==")
        print("""Search By:
Enter 1 to search by Admission Number
Enter 2 to search by Module Name
Enter 3 to search by Score Range
Enter 0 to return to Main Menu""")

        choice = int(input("Your choice: "))
        if choice == 1:
            student_no = input("Please enter the admission number you wish to search by: ")
            if student_no not in student_admission_no:
                print("No student with this admission number found!")
                time.sleep(2)
                continue

            else:
                list_index = student_admission_no.index(student_no)
                print(f"""\nAdmission Number: {student_admission_no[list_index]}
Student Name: {student_list[list_index]}
Module Name: {module_names[list_index]}
Score: {module_scores[list_index]:.1f}\n""")
                time.sleep(2)
                main()
                break

        elif choice == 2:
            module_name = input("Please enter the module name you wish to search by: ")
            if module_name not in module_names:
                print("No student with this module name found!")
                time.sleep(2)
                continue

            else:
                for index, value in enumerate(module_names):
                    if value == module_name:
                        print(f"""\nAdmission Number: {student_admission_no[index]}
Student Name: {student_list[index]}
Module Name: {module_names[index]}
Score: {module_scores[index]:.1f}""")
                time.sleep(2)
                main()
                break

        elif choice == 3:
            range_list = []  # List for range of numbers (min + max) that are in the module scores

            print("Please enter the range of score you wish to search by: ")
            minimum = int(input("Minimum score: "))
            maximum = int(input("Maximum score: "))

            for score in module_scores:
                if minimum - 1 < score < maximum + 1:
                    range_list.append(score)

            if not range_list:  # Comparison between the range list and the original list
                print("No student within this range found!")
                time.sleep(2)
                continue

            else:
                for index, value in enumerate(module_scores):
                    if minimum - 1 < value < maximum + 1:
                        print(f"""\nAdmission Number: {student_admission_no[index]}
Student Name: {student_list[index]}
Module Name: {module_names[index]}
Score: {module_scores[index]:.1f}\n""")

            time.sleep(2)
            main()
            break

        elif choice == 0:
            print('')  # Space
            main()
            break

        else:
            print("Invalid choice!")
            time.sleep(2)
            continue


main()
