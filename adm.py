import datetime

# Hotel Data
hotel_name = "Py Hotel"
rooms = []
users = []
booked_rooms = []

# Room 
def create_room(room_number, capacity, price_per_night):
    return {
        "room_number": room_number,
        "capacity": capacity,
        "price_per_night": price_per_night,
        "is_booked": False,
        "guest_name": None,
        "check_in_date": None,
        "check_out_date": None
    }

# User 
def create_user(username, password, is_admin=False):
    return {
        "username": username,
        "password": password,
        "is_admin": is_admin
    }

# room information
def display_room_info(room):
    print(f"Room Number: {room['room_number']}")
    print(f"Capacity: {room['capacity']}")
    print(f"Price per Night: ${room['price_per_night']}")
    if room['is_booked']:
        print(f"Status: Booked for {room['guest_name']}")
        print(f"Check-in Date: {room['check_in_date']}")
        print(f"Check-out Date: {room['check_out_date']}")
    else:
        print("Status: Available")
    print("--------------------")

#  add room
def add_room(room):
    rooms.append(room)

# display all rooms
def display_rooms():
    for room in rooms:
        display_room_info(room)

#  find a room by its number
def find_room_by_number(room_number):
    for room in rooms:
        if room["room_number"] == room_number:
            return room
    return None

#   user registration
def register_user(username, password, is_admin=False):
    for user in users:
        if user["username"] == username:
            print("Username already exists. Please choose a different username.")
            return False
    new_user = create_user(username, password, is_admin)
    users.append(new_user)
    print("Registration successful.")
    return True

# user login 
def login_user(username, password):
    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"Welcome, {username}!")
            return user
    print("Invalid username or password. Please try again.")
    return None

# booking a room
def book_room(room_number, guest_name, check_in_date, check_out_date):
    room = find_room_by_number(room_number)
    if room and not room["is_booked"]:
        room["is_booked"] = True
        room["guest_name"] = guest_name
        room["check_in_date"] = check_in_date
        room["check_out_date"] = check_out_date
        booked_rooms.append(room)
        print(f"Room {room_number} booked for {guest_name} from {check_in_date} to {check_out_date}")
    elif room and room["is_booked"]:
        print(f"Room {room_number} is already booked for {room['guest_name']} from {room['check_in_date']} to {room['check_out_date']}.")
    else:
        print(f"Room {room_number} does not exist.")

# to display booked rooms
def display_booked_rooms():
    if not booked_rooms:
        print("No rooms are currently booked.")
    else:
        print("Booked Rooms:")
        for room in booked_rooms:
            display_room_info(room)


room1 = create_room(101, 2, 100)
room2 = create_room(102, 3, 150)
room3 = create_room(103, 4, 200)

add_room(room1)
add_room(room2)
add_room(room3)

register_user("admin", "adminpass", is_admin=True)

#  admin login
def admin_login():
    print("----- Admin Login -----")
    username = input("Enter username: ")
    password = input("Enter password: ")
    user = login_user(username, password)
    if user and user["is_admin"]:
        return True
    else:
        print("Access denied. Only admins can access this feature.")
        return False

# to add a new room
def add_new_room():
    print("----- Add Room -----")
    room_number = int(input("Enter room number: "))
    capacity = int(input("Enter room capacity: "))
    price_per_night = float(input("Enter price per night: "))
    new_room = create_room(room_number, capacity, price_per_night)
    add_room(new_room)
    print(f"Room {room_number} added successfully.")

# Main program 
while True:
    print("\n----- Welcome to Py Hotel -----")
    print("1. Admin Login")
    print("2. Register")
    print("3. Login")
    print("4. View Rooms")
    print("5. Book Room")
    print("6. View Booked Rooms")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        if admin_login():
            while True:
                print("\n----- Admin Menu -----")
                print("1. Add Room")
                print("2. View Booked Rooms")
                print("3. Logout")

                admin_choice = input("Enter your choice (1-3): ")

                if admin_choice == '1':
                    add_new_room()
                elif admin_choice == '2':
                    display_booked_rooms()
                elif admin_choice == '3':
                    print("Logging out as admin...")
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")
        register_user(username, password)
    elif choice == '3':
        username = input("Enter username: ")
        password = input("Enter password: ")
        user = login_user(username, password)
        if user and not user["is_admin"]:
            while True:
                print("\n----- User Menu -----")
                print("1. View Rooms")
                print("2. Book Room")
                print("3. Logout")

                user_choice = input("Enter your choice (1-3): ")

                if user_choice == '1':
                    display_rooms()
                elif user_choice == '2':
                    room_number = int(input("Enter room number: "))
                    guest_name = input("Enter guest name: ")
                    check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
                    check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
                    book_room(room_number, guest_name, check_in_date, check_out_date)
                elif user_choice == '3':
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
    elif choice == '4':
        display_rooms()
    elif choice == '5':
        room_number = int(input("Enter room number: "))
        guest_name = input("Enter guest name: ")
        check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
        check_out_date = input("Enter check-out date (YYYY-MM-DD): ")
        book_room(room_number, guest_name, check_in_date, check_out_date)
    elif choice == '6':
        display_booked_rooms()
    elif choice == '7':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-7).")
