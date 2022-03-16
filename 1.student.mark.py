course_list = []
student_list = []


def student_input():
    num_stu = int(input("Enter the number of students: "))
    for i in range(0, num_stu):
        print("Enter the information of student number", i + 1,)
        student_id = input("ID: ")
        student_name = input("Name: ")
        student_dob = input("DoB: ")
        student_list.append({"ID": student_id, "Name": student_name, "DoB": student_dob})


def course_input():
    num_course = int(input("Enter the number of courses: "))
    for i in range(0, num_course):
        print("Enter the information of course number", i + 1,)
        course_id = input("ID: ")
        course_name = input("Name: ")
        course_list.append({"ID": course_id, "Name": course_name})


def marks_input():
    select_course = input("Select the student to enter mark: ")
    for i in range(0, len(student_list)):
        student = student_list[i]
        if select_course == str(student["Name"]):
            student_mark = float(input("Enter the mark for this student: "))
            student["Mark"] = student_mark
        else:
            print("This student doesn't exist")


def list_course():
    print("\nHere is the course list:\n")
    print("ID\tName\n")
    for i in range(0, len(course_list)):
        course = course_list[i]
        print(str(course["ID"]) + "\t" + str(course["Name"]))
    print("\n")


def list_students():
    print("Here is the student list:\n")
    print("ID\tName\tDate of birth\n")
    for i in range(0, len(student_list)):
        student = student_list[i]
        print(str(student["ID"]) + "\t" + str(student["Name"]) + "\t" + str(student["DoB"]))
    print("\n")


def show_mark():
    open_mark = input("Select the student to show mark: ")
    for i in range(0, len(student_list)):
        student = student_list[i]
        if open_mark == str(student["Name"]):
            print(str(student["Mark"]))


student_input()
course_input()
list_course()
list_students()
marks_input()
show_mark()