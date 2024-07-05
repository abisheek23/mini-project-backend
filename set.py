
python=set()
php=set()

# len(python)==a
# len(php)==b
# print("total available seat",a+b)
while True:
    c=int(input("choose the cource\n1.python\n2.php\n:"))
    if c==1:
        a=int(input ("enter the limit python:"))
        for i in range(a):
            name=str(input ("enter the name of student:"))
            python.add(name)
    elif c==2:
            b=int(input("enter the limmit php:"))
            for i in range(b):
                name=str(input ("enter the name of student:"))
                php.add(name)
    d=int(input("1.view students in python\n2.view students in php\n3.view students in both python and php\n:"))
    if d==1:
       print(python)
    elif d==2:
        print(php)
    elif d==3:
        print(python.intersection(php))  
    # print(php)
    # print(python)
    # for a in name:
    #     print(python)
    # for b in name:
    #     print(php)

    

    # print(python)
    # print(php)

    # print(input("enter the subject ,1.python/2.php:"))
    # c=input("enter the subject")
    # if c==1:
    #     python.add()
    # elif c==2:
    #     php.add() 





