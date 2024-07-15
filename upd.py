def up(data):
    id = input("Enter user ID to update: ")
    for i in data:
        if i["id"] == id:
            print("Current Name : " + i['name'])
            new_name = input("Enter new name (leave blank to keep current): ")
            i["name"] = new_name or i["name"]
            
            print("Current Age : " + i['age'])
            new_age = input("Enter new age (leave blank to keep current): ")
            i["age"] = new_age or i["age"]
            
            print("Current Place : " + i['place'])
            new_place = input("Enter new place (leave blank to keep current): ")
            i["place"] = new_place or i["place"]
            
            print("Profile updated successfully!\n")
            break
    else:
        print("Id not found!\n")