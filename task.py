# import random,string
# string=string.ascii_letters+string.digits+string.punctuation
# n=int(input("enter length of the password:"))
# password=""
# for i in range(n):
#     password+=random.choice(string)
# print(password)
# import getpass
# balance=0
# p1=int(getpass.getpass("enter your pin:"))
# if len(str(p1))!=4:
#     print("The length of the pin must be 4 values")
#     exit()
# p2=int(getpass.getpass("re-enter your pin:"))
# if p1!=p2:
#     print("the pin you entered does not match,try again")
#     exit()
# pin=p1
# while True:
#     print("1.balance")
#     print("2.deposit amount")
#     print("3.withdraw amount")
#     print("4.exit")
#     opt=int(input("enter your choice:"))
#     if opt==1:
#         p=int(getpass.getpass('enter your pin:'))
#         if p!=pin:
#             print("Invalid pin ")
#             continue
#         else:
#             print(f"The balance {balance}")

#     elif opt==2:
#         p=int(getpass.getpass('enter your pin:'))
#         if p!=pin:
#             print("Invalid pin ")
#             continue
#         else:
#             amount=int(input('enter your amount:'))
#             balance+=amount
#         print(f'{amount} is succesfully deposited and our current balance is {balance}')
#     elif opt==3:
#         p=int(getpass.getpass('enter your pin:'))
#         if p!=pin:
#             print("Invalid pin ")
#             continue
#         else:
#             withdraw=int(input("enter your amount:"))
#             if withdraw>balance:
#                 print("Insufficent Balance")
#             else:
#                 balance-=withdraw
#                 print(f'{withdraw} is successfully withdrawn and your current balance is {balance}')
#     elif opt==4:
#         print("Thankyou")
#         break

# def merge_expenses(expenses):
#     total={}  
    
#     for category,amount in expenses:
#         if category in total:
#             total[category]+=amount
#         else:
#             total[category]=amount
#     large=float('-inf')
#     cat=None
#     for k,v in total.items():
#         if v>large:
#             large=v
#             cat=k
#     return total, cat,large
        

# expenses=[("travel",500),("food",200),("travel",300)]
# print(merge_expenses(expenses))




       