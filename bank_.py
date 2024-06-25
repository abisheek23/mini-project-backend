
bank=[]
while True:
    print("1.registration\n 2.login")
    c=int(input("enter your chois:"))
    if c==1:
        name=(input("enter the name:"))
        email=(input("enter the email:"))
        PH_NO=(input("enter the phone number:"))
        password=(input("enter the password:"))
        bank.append([name,email,PH_NO,password,0])   
    elif c==2:
        a=(input("enter the email :"))
        b=(input("enter the password :"))
        f=0
        for i in bank:
            if a==i[1] and b==i[3]:
                f=2
                print("login successful")
                while True:
                    print("1.balance\n2.deposit\n.3.withdraw\n4.lotout")
                    d=int(input("enter your chaic:"))
                    if d==1:
                        print("balance :",i[4])
                    elif d==2:
                        amount=int(input("enter the amount:"))
                        i[4]+=amount

                        print("current balance",i[4])
                    elif d==3:
                        amount=int(input("enter the amount:"))
                        
                        if i[4]<amount:
                            print("insufficiant fund")
                        else :
                            i[4]-=amount
                            print("transaction succeseful")
                    elif d==4:
                        break
                    else:
                        print("invalid choise")
        if f==0:
            print("user not found")


                        



                



