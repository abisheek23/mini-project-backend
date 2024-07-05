books=['harry potter','the hobbit','game of thrones','lord of the rings']
users=[['a','b',22,'c']]
while True:
    print('\n1.register\n2.login')
    ch=int(input())
    if ch==1:
        name=(input('enter user name'))
        email=(input('enter your email'))
        ph=int(input('enter your phone number'))
        password=(input('enter your password'))
        users.append([name,email,ph,password,])
        print('registration sucessful')
    elif ch==2:
        email=(input('enter your email'))
        password=(input('enter your password'))
        f=0
        for i in users:
            if i[1]==email and i[3]==password:
                f=1
                print('login successful')
                while True:
                    print('\n1.borrow book\n2.return book\n3.check available books\n4.logout')
                    c=int(input('enter your choice'))
                    if c==1:
                        h=int('enter the number of books to borrow')
                        for i in range(h):
                            bk=input('enter the book you want to borrow')
                            if bk in books:
                                books.remove(bk)
                                print(f'You have borrowed "{bk}".')
                            else:
                                print('book not available')
                    elif c==2:
                        bk=(input('enter the book to return'))
                        books.append(bk)
                        print(f'You have returned "{bk}".') 
                    elif c==3:
                        for i in books:
                            print(i)
                    elif c==4:
                        print('logged out')
                        break
        if f==0:                            
            print('invalid email or password') 