# Function to handle admin login
def admin_login():
   
    print("----- Admin Login -----")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user =(username, password)
    if user and user["is_admin"]:
        return True
    else:
        print("Access denied. Only admins can access this feature.")
        return False