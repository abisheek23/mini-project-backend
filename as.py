
employees = []

while True:
    print("\nEmployee Management System")
    print("1. Register Employee")
    print("2. View Employee Details")
    print("3. Update Employee Details")
    print("4. Exit")
    choice =(input("Enter your choice: "))

    if choice == '1':
        employee = {}
        employee['ID'] = input("Enter Employee ID: ")
        employee['Name'] = input("Enter Employee Name: ")
        employee['Department'] = input("Enter Department: ")
        employee['Position'] = input("Enter Position: ")
        employee['Salary'] = input("Enter Salary: ")
        employees.append(employee)
        print("Employee registered successfully!")

    elif choice == '2':
        if not employees:
            print("No employees registered yet.")
        else:
            print("\nEmployee Details:")
            for emp in employees:
                print(f"ID: {emp['ID']}, Name: {emp['Name']}, Department: {emp['Department']}, Position: {emp['Position']}, Salary: {emp['Salary']}")

    elif choice =='3':
        emp_id = input("Enter Employee ID to update: ")
        found = False
        for emp in employees:
            if emp['ID'] == emp_id:
                print("Enter new details (leave blank to keep current value):")
                new_department = input(f"Enter Department (current: {emp['Department']}): ")
                new_position = input(f"Enter Position (current: {emp['Position']}): ")
                new_salary = input(f"Enter Salary (current: {emp['Salary']}): ")
                

                if new_department:
                    emp['Department'] = new_department
                if new_position:
                    emp['Position'] = new_position
                if new_salary:
                    emp['Salary'] = new_salary
                
                print("Employee details updated successfully!")
                found = True
                break
        if not found:
            print("Employee ID not found.")

    elif choice == '4':
        print("Exiting the system.")
        break

    else:
        print("Invalid choice. Please try again.")

