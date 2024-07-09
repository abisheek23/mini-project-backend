# student=[]
# class1=[]
# class2=[] 
# while True:
#                 print("0.registeration\n1.view total students joined this year,\n2.view students joineed in class1,\n3.view students joined in class2,\n4.view details of a student,\n5.exit ")
#                 ad=int(input("enter your chais:"))
#                 if ad==0:
#                      name=(input("enter the name:"))
#                      admition_no=(input(" admition no:"))
#                      age=int(input("enter the age:11 to 14"))
#                      if age<10 or age>15:
#                           print("not eligible")
#                           break
#                      gender=input("gender:M or F:")
#                      guardian=(input("guardian name:"))
#                      PH_NO=int(input("guardian phone number:"))
#                      choose_class=(input("choose the class1 or class2:"))
#                      student.append([name,admition_no,age,gender,guardian,PH_NO, choose_class,])     
#                 elif ad==1:
#                     for i in student:
#                         print(i[0],i[1],i[6])
#                 elif ad==2:
#                     for i in student:
#                             if i[6]=='class1':
#                                 print(i[0])
#                                 class1.append(student)
#                 elif ad==3:
#                      for i in student:
#                             if i[6]=='class2':
#                                 print(i[0])
#                                 class2.append(student)
#                 elif ad==4:
#                         print("1.from class1\n2.from class2")
#                         det=int(input("enter your chais"))
#                         if det==1 :
#                             if i[6]==class1:
                                  
#                                 a=(input("enter the name :"))
#                                 b=(input("enter the admition_no :"))
#                                 f=0
#                                 for i in student:
#                                         f==1
#                                         if a==i[0] and b==i[1]:
#                                             print("student found:", i[student])
#                         elif det==2 :
#                                 a=(input("enter the name :"))
#                                 b=(input("enter the admition_no :"))
#                                 f=0
#                                 for i in class2:
#                                     f==1
#                                     if a==i[0] and b==i[1]:
#                                      print("student found:",i[0],i[6])
#                                     else:
#                                         print("student not found , check the detils")
                     
                     
#                 elif ad==5:
#                     print('exit')
#                     break
    
#         # a=(input("enter the name :"))
#         # b=(input("enter the admition_no :"))
#         # for i in student:
#         #     if a==i[0] and b==i[1]:
#         #         print("student found:",student)
#         #     else:
#         #         print("student not found , check the detils")
#     # elif c==3:
#     #     for i in student:
#     #         if student[5]==class2:
#     #             class1.append(student[0])
#     # print(class1)


#     # while True:
#     #     print("1.view class1\n 2.view view class2")
#     #     d=int(input("enter your chois:"))
#     #     if d==1:
#     #        if student[6]==class1:
#     #     #     class1.append(student[0])
#     #           for i in student:
#     #                 if student[6]==class1:
#     #                     print(class1)
#     #     if d==2:
#     #        if student[6]==class2:
#     #     #     class2.append(student[0])
#     #             for i in student:
#     #              if student[6]==class2:
#     #                 print(class2)

# # student = []
# # class1 = []
# # class2 = []

# # while True:
# #     print("1. Registration\n2. View Details\n3. Exit")
# #     c = int(input("Enter your choice: "))

# #     if c == 1:
# #         name = input("Enter the name: ")
# #         admission_no = int(input("Admission No: "))
# #         age = int(input("Enter the age: "))
# #         gender = input("Gender (M or F): ")
# #         guardian = input("Guardian name: ")
# #         ph_no = input("Guardian phone number: ")  # Phone number should be stored as string
# #         choose_class = input("Choose the class (class1 or class2): ")
        
# #         student_data = [name, admission_no, age, gender, guardian, ph_no, choose_class]
# #         student.append(student_data)
        
# #         if choose_class == 'class1':
# #             class1.append(student_data)
# #         elif choose_class == 'class2':
# #             class2.append(student_data)
        
# #         print("Student Registered:", student_data)

# #     elif c == 2:
# #         name = input("Enter the name: ")
# #         admission_no = int(input("Enter the admission number: "))
        
# #         found = False
# #         for s in student:
# #             if name == s[0] and admission_no == s[1]:
# #                 print("Student found:", s)
# #                 found = True
# #                 break
        
# #         if not found:
# #             print("Student not found, check the details")

# #     elif c == 3:
# #         print("Exiting...")
# #         break

# #     else:
# #         print("Invalid choice, please try again.")

# #     while True:
# #         print("1. View class1\n2. View class2\n3. Back to main menu")
# #         d = int(input("Enter your choice: "))
        
# #         if d == 1:
# #             print("Class1 Students:", class1)
# #         elif d == 2:
# #             print("Class2 Students:", class2)
# #         elif d == 3:
# #             break
# #         else:
# #             print("Invalid choice, please try again.")


students = []
class1 = []
class2 = []

while True:
    print("\n0. Registration\n1. View total students joined this year\n2. View students joined in class1\n3. View students joined in class2\n4. View details of a student\n5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 0:
        name = input("Enter the name: ")
        admission_no = input("Enter the admission no: ")
        age = int(input("Enter the age (11 to 14): "))
        if age < 11 or age > 14:
            print("Not eligible")
            continue
        gender = input("Gender (M or F): ")
        guardian = input("Guardian name: ")
        phone_no = input("Guardian phone number: ")
        chosen_class = input("Choose the class (class1 or class2): ")
        if chosen_class == 'class1':
            class1.append(admission_no)
        elif chosen_class == 'class2':
            class2.append(admission_no)
        else:
            print("Invalid class choice")
            continue
        students.append([name, admission_no, age, gender, guardian, phone_no, chosen_class])
        print("Student registered successfully!")

    elif choice == 1:
        print("\nTotal students joined this year:")
        for student in students:
            print(student[0], student[1], student[6])

    elif choice == 2:
        print("\nStudents joined in class1:")
        for student in students:
            if student[6] == 'class1':
                print(student[0])

    elif choice == 3:
        print("\nStudents joined in class2:")
        for student in students:
            if student[6] == 'class2':
                print(student[0])

    elif choice == 4:
        print("1. From class1\n2. From class2")
        det = int(input("Enter your choice: "))
        if det == 1:
            name = input("Enter the name: ")
            admission_no = input("Enter the admission_no: ")
            found = False
            for student in students:
                if student[0] == name and student[1] == admission_no and student[6] == 'class1':
                    print("Student found:", student)
                    found = True
                    break
            if not found:
                print("Student not found, check the details.")
        elif det == 2:
            name = input("Enter the name: ")
            admission_no = input("Enter the admission_no: ")
            found = False
            for student in students:
                if student[0] == name and student[1] == admission_no and student[6] == 'class2':
                    print("Student found:", student)
                    found = True
                    break
            if not found:
                print("Student not found, check the details.")
        else:
            print("Invalid choice")

    elif choice == 5:
        print("Exit")
        break

    else:
        print("Invalid choice. Please try again.")
