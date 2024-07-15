import datetime

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Room:
    def __init__(self, room_number, capacity, price_per_night):
        self.room_number = room_number
        self.capacity = capacity
        self.price_per_night = price_per_night
        self.is_booked = False
        self.guest_name = None
        self.check_in_date = None
        self.check_out_date = None
    
    def book_room(self, guest_name, check_in_date, check_out_date):
        self.is_booked = True
        self.guest_name = guest_name
        self.check_in_date = check_in_date
        self.check_out_date = check_out_date
        print(f"Room {self.room_number} booked for {guest_name} from {check_in_date} to {check_out_date}")

    def display_info(self):
        print(f"Room Number: {self.room_number}")
        print(f"Capacity: {self.capacity}")
        print(f"Price per Night: ${self.price_per_night}")
        if self.is_booked:
            print(f"Status: Booked for {self.guest_name}")
            print(f"Check-in Date: {self.check_in_date}")
            print(f"Check-out Date: {self.check_out_date}")
        else:
            print("Status: Available")
        print("--------------------")

class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.users = []  # List to store registered users

    def add_room(self, room):
        self.rooms.append(room)

    def display_rooms(self):
        for room in self.rooms:
            room.display_info()

    def find_room_by_number(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def register_user(self, username, password):
        # Check if username already exists
        for user in self.users:
            if user.username == username:
                print("Username already exists. Please choose a different username.")
                return False
        
        # If username doesn't exist, create a new user
        new_user = User(username, password)
        self.users.append(new_user)
        print("Registration successful. You can now login.")
        return True

    def login_user(self, username, password):
        for user in self.users:
            if user.username == username and user.password == password:
                print(f"Welcome, {username}!")
                return True
        
        print("Invalid username or password. Please try again.")
        return False

    def book_room(self, room_number, guest_name, check_in_date, check_out_date):
        room = self.find_room_by_number(room_number)
        if room and not room.is_booked:
            room.book_room(guest_name, check_in_date, check_out_date)
        elif room and room.is_booked:
            print(f"Room {room_number} is already booked for {room.guest_name} from {room.check_in_date} to {room.check_out_date}.")
        else:
            print(f"Room {room_number} does not exist.")

# Creating a hotel instance
hotel = Hotel("Py Hotel")

# Adding rooms to the hotel
room1 = Room(101, 2, 100)
room2 = Room(102, 3, 150)
room3 = Room(103, 4, 200)

hotel.add_room(room1)
hotel.add_room(room2)
hotel.add_room(room3)

# Function to handle user registration
def register():
    print("----- Register -----")
    username = input("Enter username: ")
    password = input("Enter password: ")
    hotel.register_user(username, password)

# Function to handle user login
def login():
    print("----- Login -----")
    username = input("Enter username: ")
    password = input("Enter password: ")
    return hotel.login_user(username, password)

# Function to display room details
def display_rooms():
    print(f"{hotel.name} Rooms Available:")
    hotel.display_rooms()

# Function to handle room booking
def book_room():
    print("----- Book Room -----")
    room_number = int(input("Enter room number to book: "))
    guest_name = input("Enter guest name: ")
    check_in_date = input("Enter check-in date (YYYY-MM-DD): ")
    check_out_date = input("Enter check-out date (YYYY-MM-DD): ")

    # Validate dates
    try:
        check_in_date = datetime.datetime.strptime(check_in_date, "%Y-%m-%d").date()
        check_out_date = datetime.datetime.strptime(check_out_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    hotel.book_room(room_number, guest_name, check_in_date, check_out_date)

# Main program loop
while True:
    print("\n----- Welcome to Py Hotel -----")
    print("1. Register")
    print("2. Login")
    print("3. View Rooms")
    print("4. Book Room")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        register()
    elif choice == '2':
        if login():
            # User logged in successfully
            while True:
                print("\n----- Menu -----")
                print("1. View Rooms")
                print("2. Book Room")
                print("3. Logout")

                user_choice = input("Enter your choice (1-3): ")

                if user_choice == '1':
                    display_rooms()
                elif user_choice == '2':
                    book_room()
                elif user_choice == '3':
                    print("Logging out...")
                    break
                else:
                    print("Invalid choice. Please enter a valid option.")
    elif choice == '3':
        display_rooms()
    elif choice == '4':
        book_room()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-5).")