# n=int(input("enter num:"))
# if n>0:
#     print(n,"positive")
# elif n<0:
#     print(n,"negative")
# else:
#     print(n,"zero")
# n=int(input("enter:"))
# if n%2==0:
#     print(n,"even number")
# else:
#     print(n,"odd number")
# k=list(map(int,input("enter:").split()))
# large=0
# for i in k:
#     if i>large:
#         large=i
# print(large)
# n=int(input("enter:"))
# if n>90 and n<100:
#     print(n,"Grade A")
# elif n>75 and n<89:
#     print(n,"Grade B")
# elif n>60 and n<74:
#     print(n,"Grade C")
# elif n>40 and n<59:
#     print(n,"Grade D")
# else:
#     print(n,"Fail")
# n=int(input("enter:"))
# if n%4==0 and n%100!=0 or n%400==0:
#     print(n,"leap year")
# else:
#     print(n,"not a leap year")
# n=int(input("enter :"))
# for i in range(1,n+1):
#     print(i)
# n=int(input("enter n:"))
# for i in range(1,n+1):
#     if i%2==0:
#         print(i,"even")
#     # else:
#     #     print(i,"odd")
# else:
#     print("loop executed")
# n=int(input("enter:"))
# add=0
# for i in range(1,n+1):
#     add+=i
# print(add)
# n=int(input("enter n:"))
# product=1
# for i in range(1,n+1):
#     product*=i
# print(product)
# n=(input("enter:"))
# k=str(n)
# m=""
# for i in range(len(k)-1,-1,-1):
#     m+=k[i]
# if k==m:
#     print("palindrome")
# else:
#     print("not a palindrome")
# n=int(input("enter:"))
# count=0
# for i in range(2,n):
#     if n%i==0:
#         count+=1
# if count==0:
#     print(n," prime")
# else:
#     print(n,"not prime")
# n=int(input("enter:"))
# for i in range(1,11):
#     print(n,"*",i,"=",n*i)
# n=int(input("enter n:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print("*",end=" ")
#     print()
# n=int(input("enter:"))
# for i in range(n,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()
# n=int(input("enter:"))
# for i in range(1,n+1):
#     for  j in range(1,i+1):
#         print(j,end="")
#     print()
# n=int(input("enter:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end="")
#     print()
# n=int(input("enter:"))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()                                                                                 
# n=int(input("enter:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(j,end="")
#     print()
# n=int(input("enter:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(i):
#         print("*",end="")
#     print()
# n=int(input("enter:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for j in range(1,1+i):
#         print(j,end=" ")
#     print()
# n=int(input("enter:"))
# for i in range(1,n+1):
#     for j in range(n-i):
#         print("",end=" ")
#     for j in range(i):
#         print(i,end="")
#     print()
# n=int(input("enter:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(i,end="")
#     print()
# n=int(input("enter :"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()
# n=int(input("enter:"))
# for i in range(1,n+1):
#     for j in range(i,0,-1):
#         print(j,end="")
#     print()
# m=input("enter:")
# vowels="aeiouAEIOU"
# count=0
# for i in m:
#     if i in vowels:
#         count+=1
# print(count)
# n=input("enter:")
# count_upper=0
# count_lower=0
# for i in n:
#     if i.isupper():
#         count_upper+=1
#     elif i.islower():
#         count_lower+=1
# print(count_upper)
# print(count_lower)
# n=input("enter:")
# k=""
# for i in range(len(n)-1,-1,-1):
#     k+=n[i]
# if n==k:
#     print("palindrome")
# else:
#     print("not palindrome")
# n=input("enter:")
# k=""
# for i in range(len(n)-1,-1,-1):
#     k+=n[i]
# print(k)
# n=input("enter:")
# count=0
# for i in n:
#     if i=="a":
#         count+=1
# print(count)
# n=input("enter")
# for i in n:
#     if i!=" ":
#         print(i,end="")
# arr=list(map(int,input("enter:").split()))
# large=arr[0]
# second=arr[0]
# for i in arr:
#     if i<large:
#         second=large
#         large=i
#     else:
#         if i<second and i!=large:
#             second=i
# print(second)

# print(large)
# arr=list(map(int,input("enter:").split()))
# small=arr[0]
# for i in arr:
#     if i<small:
#         small=i
# print(small)
