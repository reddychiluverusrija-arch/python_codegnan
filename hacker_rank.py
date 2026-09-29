# https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
def is_leap(year):
    if year%4 ==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False
year = int(input())
print(is_leap(year))
# https://www.hackerrank.com/challenges/py-if-else/problem?isFullScreen=true
n = int(input().strip())
if n%2!=0:
    print("Weird")       
elif 2<=n<=5:
    print("Not Weird")
elif 6<=n<=20:
    print("Weird")
else:
    print("Not Weird")
