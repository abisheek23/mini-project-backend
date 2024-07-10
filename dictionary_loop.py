"example"
# std=[]
# for i in range(2):
#     name=input('enter the name:')
#     age=int(input('enter the age:'))
#     place=input('enter the place:')
#     # ph_no=int(input('enter the phone no:'))
#     std.append({'name':name,'age':age,'place':place,})
# print(std)
# print("{:<10}{:<10}{:<10}".format('name','age','plase',))
# print('_'*25)
# for i in std:
#     print("{:<10}{:<10}{:<10}".format (i["name"],i["age"],i["place"]))
# print('age>30')
# print("{:<10}{:<10}{:<10}".format('name','age','plase',))
# for i in std:
#    if i['age']>=30:
#         print("{:<10}{:<10}{:<10}".format (i["name"],i["age"],i["place"]))
# print('age<30')
# print("{:<10}{:<10}{:<10}".format('name','age','plase',))
# for i in std:
#      if i['age']<30:
#         print("{:<10}{:<10}{:<10}".format (i["name"],i["age"],i["place"]))
# number={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
# a=[(input('number'))]
# a=str(a)
# result=""
# for char in a:
#     digit=int(char)
#     if digit in number:
#         result +=number[digit]+""
# print(result.strip())

number = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
a = int(input('Enter a number: '))
result = ''
while a > 0:
    digit = a % 10  
    word = number[digit]  
    result = word + ' ' + result 
    a = a // 10 
result = result
print(result)

