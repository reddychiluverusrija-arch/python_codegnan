# def add(a, b):
#     print('add function')
#     c = a + b 
#     return c 
#     pirnt('HI')
# def sub(a, b):
#     print('sub function')
#     c = a - b
#     return 
# def div(a, b):
#     print('div function')
#     c = a / b 
# x = add(10, 15)   
# y = sub(20, 10)   
# z = div(25, 10)   
# print(x)#add function
# print(y)#sub function
# print(z)#div function
# print()#25
# #None
# #None
#Type of arguments
# def detail(name, age, rollno):
#     print(f'My name is {name}')# my name is rakesh
#     print(f'My age is {age}')#my age is 20
#     print(f'My rollno is {rollno}')#my rollno is A101
# detail('rakesh', 20, 'A101')
# detail(20, 'A101', 'rakesh')# my name is 20 ,my age is A101,my rollno is rakesh
# detail(age=20, rollno='A101', name='rakesh')#key word argument my name is rakesh
# detail(rollno='A101', age=20, name='rakesh')#keyword argument my age is 20
# detail(rollno='A101', age=20, name='rakesh')#keyword argument my rollno is A101
# def add(a, b=10, c=20):
#     return a + b + c 
# print(add(1))#1+10+20=31
# print(add(1,2))#1+2+20=23
# print(add(1,2,3))#1+2+3=6
# print(add(c=3, a=1, b=2))#keyword argument 1+2+3=6

# #order of = in function def
# # def sub(a=10, b, c):#error keyword argument must  be after position argument
# #     pass 
# #order of = in function call.
# # add(a=10, b, c)#error keyword argument must  be after position argument

# def f1(*a):
#     print(a)#(1,2,3,4)
#     print(type(a))#<class 'tuple'>
# f1(1,2,3,4)

# def f2(**a):
#     print(a)#{a:1,b:2,c:3,d:4}
#     print(type(a))#<class 'dict'>
# # f2(1,2,3,4)
# f2(a=1, b=2, c=3, d=4)