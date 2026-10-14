
array=[10,20,30]
print(array)
print(len(array))
print(array[0])
print(array[-1])
array.append(40)
array.insert(11,7)
print(array)
array.remove(7)
array.pop()
array.pop(2)
print(array)
#traversing:
##access by value
for i in array:
    print(i)
## acess by index
for i in range(len(array)):
    print(array[i])
#reverse acess
#acess by value
for i in reversed(array):
    print(i)
#Acess by indexfor i in range(len(array)-1,-1,-1):
    # print(array[i])