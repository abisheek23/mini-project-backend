# # # # books=['harry potter','the hobbit','game of thrones','lord of the rings']
# # # # users=[['a','b',22,'c']]
# # # # while True:
# # # #     print('\n1.register\n2.login')
# # # #     ch=int(input())
# # # #     if ch==1:
# # # #         name=(input('enter user name'))
# # # #         email=(input('enter your email'))
# # # #         ph=int(input('enter your phone number'))
# # # #         password=(input('enter your password'))
# # # #         users.append([name,email,ph,password,])
# # # #         print('registration sucessful')
# # # #     elif ch==2:
# # # #         email=(input('enter your email'))
# # # #         password=(input('enter your password'))
# # # #         f=0
# # # #         for i in users:
# # # #             if i[1]==email and i[3]==password:
# # # #                 f=1
# # # #                 print('login successful')
# # # #                 while True:
# # # #                     print('\n1.borrow book\n2.return book\n3.check available books\n4.logout')
# # # #                     c=int(input('enter your choice'))
# # # #                     if c==1:
# # # #                         h=int('enter the number of books to borrow')
# # # #                         for i in range(h):
# # # #                             bk=input('enter the book you want to borrow')
# # # #                             if bk in books:
# # # #                                 books.remove(bk)
# # # #                                 print(f'You have borrowed "{bk}".')
# # # #                             else:
# # # #                                 print('book not available')
# # # #                     elif c==2:
# # # #                         bk=(input('enter the book to return'))
# # # #                         books.append(bk)
# # # #                         print(f'You have returned "{bk}".') 
# # # #                     elif c==3:
# # # #                         for i in books:
# # # #                             print(i)
# # # #                     elif c==4:
# # # #                         print('logged out')
# # # #                         break
# # # #         if f==0:                            
# # # #             print('invalid email or password') 

# # # data=[{'op':1,'uname':'cab1','pswd':987,'email':'cab1@gmail.com','pno':'123456700','livloc':'ekm','tno':'kl5b123'},
# # #       {'op':1,'uname':'cab2','pswd':876,'email':'cab2@gmail.com','pno':'998766789','livloc':'ktm','tno':'kl6b123'},
# # #       {'op':1,'uname':'cab3','pswd':765,'email':'cab3@gmail.com','pno':'123467812','livloc':'vkm','tno':'kl7b123'},
# # #       {'op':2,'uname':'user1','pswd':123,'email':'u1@gmail.com','pno':'123456789','livloc':'ktm','headloc':'vkm','time':'1pm'},
# # #       {'op':2,'uname':'user2','pswd':234,'email':'u2@gmail.com','pno':'987654321','livloc':'vkm','headloc':'ekm','time':'2pm'},
# # #       {'op':2,'uname':'user3','pswd':345,'email':'u3@gmail.com','pno':'123454321','livloc':'ekm','headloc':'ktm','time':'3pm'},]

# # # while True:
# # #     # Display the menu
# # #     print("1.Regester \n2.Login \n3.Cancle")
# # #     choice = int(input("Enter your choice: "))

# # #     if choice == 1:
# # #         #regestration
# # #         op=int(input("Are you intrested in working as uber driver : \n1.Yes \n2.No"))
# # #         data.append({'op':op})
# # #         #cab regestration
# # #         if choice == 1:
# # #             uname=str(input("Enter the name : "))
# # #             pswd=int(input("Enter password : "))
# # #             email=str(input("Enter your place : "))
# # #             pno=int(input("Enter your phone number : "))
# # #             tno=str(input("Enter your taxi regestration number : "))
# # #             data.append({'name':uname,'pswd':pswd,'email':email,'pno':pno,'tno':tno})
# # #         #user regestration
# # #         elif choice == 2:
# # #             uname=str(input("Enter the name : "))
# # #             pswd=int(input("Enter password : "))
# # #             email=str(input("Enter your place : "))
# # #             pno=int(input("Enter your phone number : "))            
# # #             data.append({'name':uname,'age':pswd,'place':email,'pno':pno})
# # #         else:
# # #             print("Invalid input")
# # #     elif choice == 2:
# # #         uname = input("Enter your name : ")
# # #         pswd = int(input("Enter password : "))
       
        
# # #         found = False
# # #         for s in data:
# # #             if s['op'] == 2 and uname == s['uname'] and pswd == s['pswd']:
# # #                         found = True
# # #                         print("You have successfully logged in.")
                        
# # #                         while True:
# # #                             u_choice=int(input("1.Book taxi \n2.View details \n3.Logut \nEnter your choice : "))
# # #                             if u_choice == 1:                                
# # #                                 livloc=str(input("Share your current location : "))
# # #                                 headloc=str(input("Where do you want to go : "))     
# # #                                 time=str(input("Enter the time you want taxi to arive"))   
# # #                                 data.append({'livloc':livloc,'headloc':headloc,'time':time})
# # #                             elif u_choice == 2:
# # #                                 print('details&price') #booking details

# # #                             elif u_choice == 3:
# # #                                 print("You had logouted")
# # #                                 break
# # #                             else:
# # #                                  print("Invalid input")

                            
                        
        
# # #             elif s['op'] == 1 and uname == s['uname'] and pswd == s['pswd']:
# # #                         found = True
# # #                         print("You have successfully logged in.")
# # #                         while True:
# # #                             cab_choice = int(input("1.View booking \n2.Add details \n3.Logout \nEnter your choice : "))  
# # #                             if cab_choice == 1:
# # #                                 print('details&price') #booking details

# # #                             elif cab_choice == 2:
# # #                                 livloc=str(input("Share your current location : "))
# # #                                 data.append({'livloc':livloc})
# # #                             elif cab_choice == 3:
# # #                                 print("You had logouted")
# # #                                 break
# # #                             else:
# # #                                  print("Invalid input")


# # #     elif choice == 3:
# # #         print("You had exited")
# # #         break

# # # Complex structure with lists and dictionaries
# # company = {
# #     "name": "TechCorp",
# #     "departments": [
# #         {"name": "Engineering", "employees": ["Alice", "Bob"]},
# #         {"name": "HR", "employees": ["Charlie", "Diana"]}
# #     ]
# # }

# # # Access the name of the first department
# # print(company["departments"][0]["name"])  # Output: Engineering

# # # List all employees in the HR department
# # hr_employees = company["departments"][1]["employees"]


# # List to store student records
# students = []
# # Adding new students
# students.append({"name": "Alice", "grade": 85, "id": 1})
# students.append({"name": "Bob", "grade": 90, "id": 2})
# students.append({"name": "Charlie", "grade": 78, "id": 3})

# print("Students added:")
# print(students)
# print("\nView all students:")
# for student in students:
#     print(f"ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}")
# search_name = "Bob"
# print(f"\nSearching for student named '{search_name}':")
# for student in students:
#     if student["name"].lower() == search_name.lower():
#         print(f"Found - ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}")
#         break
# else:
#     print(f"No student named '{search_name}' found.")
# remove_id = 2
# print(f"\nRemoving student with ID '{remove_id}':")
# students = [student for student in students if student["id"] != remove_id]
# print(students)
# # Student Grade Management System

# # List to store student records
# students = []

# # Adding new students
# students.append({"name": "Alice", "grade": 85, "id": 1})
# students.append({"name": "Bob", "grade": 90, "id": 2})
# students.append({"name": "Charlie", "grade": 78, "id": 3})

# print("Students added:")
# print(students)

# # View all students
# print("\nView all students:")
# for student in students:
#     print(f"ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}")

# # Search for a student by name
# search_name = "Bob"
# print(f"\nSearching for student named '{search_name}':")
# for student in students:
#     if student["name"].lower() == search_name.lower():
#         print(f"Found - ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}")
#         break
# else:
#     print(f"No student named '{search_name}' found.")

# # Remove a student by ID
# remove_id = 2
# print(f"\nRemoving student with ID '{remove_id}':")
# students = [student for student in students if student["id"] != remove_id]
# print(students)

# # View all students after removal
# print("\nView all students after removal:")
# for student in students:
#     print(f"ID: {student['id']}, Name: {student['name']}, Grade: {student['grade']}")

