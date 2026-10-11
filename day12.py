# #FOR LOOP PROBLEMS
# #basic understanding
# #1. print numbers from 1 to 10 in one line
# n=int(input("enter:"))
# for i in range(1,n+1):
#     print(i,end=" ")
# print()
# #2. print even numbers from 5 to 30 in one line
# n=int(input("enter even:"))
# for i in range(5,n+1):
#     if i%2==0:
#         print(i,end=" ")
# print()

# #3. print odd numbers from 5 to 30 in one line
# n=int(input("enter odd:"))
# for i in range(5,n+1):
#     if i%2!=0:
#         print(i,end=" ")
# print()
# #4. print numbers divisible by 5 from 1 to 30 in one line
# n=int(input("enter num:"))
# for i in range(1,n+1):
#     if i%5==0:
#         print(i,end=" ")
# print()
# #5. print numbers divisible by both 5 and 7 from 1 to 100 in one line
# n=int(input("enter numbers:"))
# for i in range(1,n+1):
#     if i%5==0 and i%7==0:
#         print(i,end=" ")
# print()
# # #6. sum of numbers from 10 to 25
# n=int(input("enter sum:"))
# add=0
# for i in range(10,n+1):
#     add+=i
# print(add)
# print() 
# #7. sum of numbers in any list
# k=list(map(int,input("enter list:").split()))
# sum=0
# for i in k:
#     sum+=i
# print(sum)
# print()
#8. multiplication table of a number 
# m=int(input("enter mul:"))
# for i in range(1,11):
#     print(m,"*",i,"=",m*i)
# print()
#interview problems
#9. factorial 
# n=int(input("enter:"))
# p=1
# for i in range(1,n+1):
#     p*=i
# print(p)
# print()
#10. fibonacci 
# n=int(input("enter m:"))
# a=0
# b=1
# for i in range(n+1):
#     print(a,end=" ")
#     a,b=b+a,a
#11. reverse a string
# a=input("enter:")
# rev=""
# for i in range(len(a)-1,-1,-1):
#     rev+=a[i]
# print(rev)
#12. count vowels in a string
# a=input("enter:")
# vowels="aeiouAEIOU"
# count=0
# for i in a:
#     if i in vowels:
#         count+=1
# print(count)
#13. count z's and y's in a string
# s=input("enter")
# v="zZYy"
# count=0
# for i in s:
#     if i in v:
#         count+=1
# print(count)
#14. check whether a number is prime number or not 
# l=int(input("enter:"))
# for i in range(2,l):
#     if l%i==0:
#         print(i,"prime number")
# else:
#     print(i,"not prime number")




#WHILE LOOP PROBLEMS
#basic understanding
#print 1 to 10 with while loop
# a=1
# while a<=11:
#     print(a,end=" ")
#     a+=1
# print()
#print even numbers from 1 to 10
# a=1
# while a<=10:
#     if a%2==0:
#         print(a)
#     a+=1
# print()
#print numbers divisible by both 5 and 7 from 1 to 500 
# a=1
# while a <=500:
#     if a%5==0 and a%7==0:
#         print(a)
#     a+=1  
# print()

#interview problems
#count digits

#reverse a number
#palindrome number 
# a=input("enter:")
# k=a[::-1]
# if a==k:
#     print("palindrome")
# else:
#     print("not")
#palindrome string (without slicing, built in function)
# a=input("enter:")
# k=""
# for i in range(len(a)-1,-1,-1):
#     k+=a[i]
# if a==k:
#     print("palindrome")
# else:
#     print("not palindrome")
#armstrong number
# n=int(input("enter:"))
# sum=0
# original=n
# while n>0:
#     digit = n % 10
#     sum += digit ** 3
#     n = n // 10
# if sum==original:
#     print("arm strong")
# else:
#     print("no")

