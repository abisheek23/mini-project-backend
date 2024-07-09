data=[]
depart=['project manager','network engineer','software tester',]
while True:
    print("1. Add \n2. View \n3.Delete")
    ch = int(input("Enter your choice: "))
    if ch==1:
        name=str(input("enter your name:"))
        id=int(input("enter id:"))
        age=int(input("enter your age:"))
        print(depart)
        department=(input("enter the deparment:",depart=[]))
        data.append({"name":name,"id":id,"age":age,"department":depart})
    print (data)
    # print("{:<10}{:<10}{:<10}{:<10}".format('name','id','age','department',))
    # print('_'*30)
    # for i in data:
    #     print("{:<10}{:<10}{:<10{:<10}}".format(i["name"],i["id"],i["age"],i["department"]))

    if ch==2:
        print(depart)
        print("view employe:\n1.project manager,\n2.network engineer,\n3.software tester")
        dp=int(input("enter your choice:"))
        if dp==1:
            for i in data:
                f=0
                data({'department':'a'})==('project manager')
                f==1
                print(data)
        if dp==2:
            for i in data:
                f=0
                i[3]=={'deparment':'network engineer'}
                f==1
                print(data)
        if dp==3:
            for i in data:
                f=0
                i[3]=={'deparment':'software tester'}
                f==1
                print(data)
