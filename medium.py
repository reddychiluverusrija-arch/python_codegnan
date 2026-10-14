# # l=list(map(int,input("enter:").split()))
# # large=float('-inf')
# # second=float('-inf')
# # third=float('-inf')
# # for i in l:
# #     if i >large:
# #         third=second
# #         second=large
# #         large=i
# #     elif  i>second and i!=large:
# #         third=second
# #         second=i
        
# #     else:
# #         if i >third and i !=large and i!=second:
# #             third=i
# # print(third)
# l=list(map(int,input("enter:").split()))
# large=float('-inf')
# second=float('-inf')
# third=float('-inf')
# fourth=float('-inf')
# fifth=float('-inf')

# for i in l:
#     if i >large:
#         fifth=fourth
#         fourth=third
#         third=second
#         second=large
#         large=i
#     elif i>second and i!=large:
#         fifth=fourth
#         fourth=third
#         third=second
#         second=i
#     elif  i>third and i!=large and i!=second:
#         fifth=fourth
#         fourth =third
#         third=i
#     elif i>fourth and i !=large and i!=second and i!=third:
#         fifth=fourth
#         fourth=i
        
#     else:
#         if i >fifth and i!=fourth and i !=large and i!=second and i!=third:
#             fifth=i
# if fifth==float('-inf'):
#     print("No element fifth distinct number")
# else:
#     print(fifth)

# n=map(int,input().split())
# large=float('-inf')
# second=float('-inf')
# for i in n:
#     if i>large:
#         second=large
#         large=i
#     elif i>second and i!=large:
#         second=i
# if second==float('-inf'):
#     print("not found")
# else:
#     print(second)
# n=input("enter").lower().strip()
# freq={}
# for i in n:
#     if i==" ":
#         continue
#     if i  in freq:
#         freq[i]+=1
#     else:
#         freq[i]=1
# print(freq)
# n=list(map(int,input("enter:").split()))
# zero=[]
# non_zero=[]
# for i in n:
#     if i ==0:
#         zero.append(i)
#     else:
#         non_zero.append(i)
# n[:]=non_zero+zero
# print(n)
# k=int(input())
# n=list(map(int,input("enter:").split()))
# expected=0
# for i in range(1,k+1):
#     expected+=i
# sum=0
# for i in n:
#     sum+=i
# print(expected-sum)
# n=input("enter:")
# freq={}
# for i in n:
#     if i  not in freq:
#         freq[i]=1
#     else:
#         freq[i]+=1
# for i in freq:
#     if freq[i]==1:
#         print(i)
#         break
# else:
#     print("-1")
# n=list(map(int,input().split()))
# large=float('-inf')
# second=float('-inf')
# third=float('-inf')
# for i in n:
#     if i >large:
#         third=second
#         second=large
#         large=i
#     elif i>second and i!=large:
#         third=second
#         second=i
#     elif i>third and i!=second and i!=large:
#         third=i
# if third==float('-inf'):
#     print("no third element found")
# else:
#     print(third)
# n=input("enter:")
# k=input("enter:")
# m={}
# l={}
# for i in n:
#     if i in m:
#         m[i]+=1
#     else:
#         m[i]=1
# for i in k:
#     if i in l:
#         l[i]+=1
#     else:
#         l[i]=1

# if m==l:
#     print("anagaram")
# else:
#     print("not an anagram")
n=list(map(int,input("enter:").split()))
left=0
right=len(n)-1
large=float('-inf')
sum=right+left
for right in n:
    sum+=right
    right-=1
else:
    left+=1
for i in sum:
    if sum>large:
        large=sum
print(left[n],right[n])
