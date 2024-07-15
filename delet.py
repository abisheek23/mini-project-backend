def dele(data):
    id = input("Enter User ID to delete: ")
    for i in data:
            if i["id"] == id:
                data.remove(i)
                print("User deleted successfully!\n")
                break
    else:
            print("ID not found!\n")