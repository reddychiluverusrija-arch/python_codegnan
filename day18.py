#List Comprehension
#for
a = []
for x in range(1, 11):
    a.append(x)
print(a)#[1,2,3,4,5,6,7,8,9]
#create with list comprehension

#for-if
a = []
for x in range(1,11):
    if x % 2 == 0:
        a.append(x) 
print(a)#[2,4,6,8,10]
#create with list comprehension

#for-if-for-if 
a = []
for x in range(1,5):
    if x % 2 == 0:
        for y in range(1,4):
            if x + y == 5:
                a.append((x,y))
print(a)# (2,3),(4,1)
#create with list comprehension

#set comprehension: create a set with even numbers from 1 to 20
#dict comprehension: create a dict with numbers and their squares from 1 to 10 

#function
def numbers():
    return 1 
    return 2 
n = numbers()
print(n)#$1
print(type(n))#  int

#generators
def numbers():
    yield 1 
    yield 2 
    yield 3 
    yield 4 
n = numbers() 
print(n)
print(type(n))#generator
print(next(n))#1
print(next(n))#2
print(n.__next__())#3
print(n.__next__())#4
# print(next(n)) #error stop iteration

def evennumbers():
    for x in range(1, 10):
        if x % 2 == 0:
            yield x 
n = evennumbers()
print(next(n))#2
print(n.__next__())#4
for x in n:
    print(x)# 6 8
