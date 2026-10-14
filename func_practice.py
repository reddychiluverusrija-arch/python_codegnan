# def check_even(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# n=int(input("enter:"))
# result=check_even(n)
# print(result)
# def square(n):
#     return n*n
# n=int(input("enter:"))
# result=square(n)
# print(result)
# def maximum(a,b):
#     if a>b:
#         return a
#     else:
#         return b
# a=int(input("enter:"))
# b=int(input("enter:"))
# result=maximum(a,b)
# print(result)
# def check_num(n):
#     if n>0:
#         return "positive"
#     elif n<0:
#         return "negative"
#     else:
#         return "zero"
# n=int(input())
# result=check_num(n)
# print(result)
# def add(a,b):
#     return a+b
# a=int(input())
# b=int(input())
# result=add(a,b)
# print(result)
# def sum_n(n):
#     add=0
#     for i in range(1,n+1):
#         add+=i
#     return add
# n=int(input())
# result=sum_n(n)
# print(result)
def count_even(n):
    count=0
    for i in range(n):
        if i%2==0:
            count+=1
    return count
n=int(input())
result=count_even(n)
print(result)