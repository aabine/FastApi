#list is a dynamic array it is a collection of items in a particular order
begin_list = [1,2,3,4,5,8,17,87]
#print the middle of the list
print(begin_list[len(begin_list) // 2])
#print in reverse
print(begin_list[::-1])
#modify the list
begin_list[3] = 87
#add and remove elements from the list
begin_list.append(100)
begin_list.remove(87)
#insert element at a specific index
begin_list.insert(3, 100)
#remove element at a specific index
begin_list.pop(2)
#search the list for an element
num = 0
if num not in begin_list:
    print("not found")
else:
    print("found")
try:
    print(begin_list.index(0))
except ValueError:
    print("0 is not in the list")
#count the number of times an element appears in the list
print(begin_list.count(5))
#sort the list
begin_list.sort()
#reverse the list
begin_list.reverse()









print(begin_list)

#remove all elements from the list
begin_list.clear()

