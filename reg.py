def add(data):
    name=str(input("Enter ur name:"))
    id=int(input("Enter id:"))
    age=int(input("Enter your age:"))
    place=str(input("Enter ur place:"))
    data.append({"name":name,"id":id,"age":age,"place":place})

