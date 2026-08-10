students = []
subjects_offered = set()

print("welcome to student data organizer")

while True:
    print("\n select an option")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Update Student Information")
    print("4. Delete Student")
    print("5. Display Subjects Offered")
    print("6. Exit")
    choice = int(input("enter the choice: "))

    if choice == 1:

        print("enter students detail")
        student_id = int(input("enter the studnet id: "))
        name = str(input("enter the name of students: "))
        age = int(input("enter the age of students: ")) 
        grade = input("enter grade of students: ")
        dob = input("enter the bdate in YYYY-MM-DD: ")
        subjects = input("enter the subject choose: ").split(",")

        student_info = (student_id, dob)

        student = {"info" : student_info,
                   "name": name,
                   "age" : age,
                   "grade" : grade,
                   "dob" : dob,
                   "subjects" : subjects }
        students.append(student)

        for subject in subjects:
            subjects_offered.add(subject)
        print("student added successfully")


    elif choice == 2:
        print()
        for student in students:
            
            print()
            print("Name: ", student["name"])
            print("Age: ", student["age"])
            print("Grade: ", student["grade"])
            print("Id: ", student["info"][0])
            print("DOB: ", student["info"][1])
            print("Subjects: ", student["subjects"])
            print()
    elif choice == 3:
        print("update inforamtion")

        student_id = int(input("enter student id: "))

        for student in students:
            if student["info"][0] == student_id:

                print("choose what to update")
                print("1. age")
                print("2.. subject")

                choice_update = int(input("enter your choice: "))
                if choice_update == 1:
                    new_age = int(input("enter new age: "))
                    student["age"] = new_age

                elif choice_update == 2:
                    new_subjects = str(input("enter new subjects(comma seprated): ")).split(",")
                    student["subjects"] = new_subjects

                else:
                    print("invalid choice")
                break

            else:
                print("invalid studnet id :)")

    elif choice == 4:
        student_id = int(input("enter student id: "))
        for i in range(len(students)):
            if students[i]["info"][0] == student_id:
                del students[i]
                print("student deleted")
                break


    elif choice == 5:
        subjects_offered = set()

        for  student in students:
            subjects_offered.update(student["subjects"])

        print("subjects offered to students are:")
        for subject in subjects_offered:
            print(subject)
            
    elif choice == 6:
        print("thank you for using stuent data organizer")
        break
    else:
        print("invalid choice")
            


        
