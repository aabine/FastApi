from typing import List, Tuple
from collections import defaultdict

#list is a dynamic array it is a collection of items in a particular order
begin_list = [1,2,3,4,5,8,17,87]
print(begin_list)
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

#rotate a list to the k step
def rotate_list(lst, k):
    return lst[k:] + lst[:k]

print(rotate_list(begin_list, 3))

#Find all pair in a list whose sum is equal to the given value
def find_pairs(lst: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Find all unique pairs in the list `lst` that sum up to the target value.
    """
    if not isinstance(lst, list) or not all(isinstance(x, int) for x in lst):
        raise ValueError("Input must be a list of integers.")
    if not isinstance(target, int):
        raise ValueError("Target must be an integer.")

    seen = set()
    pairs = set()
    
    for num in lst:
        complement = target - num
        if complement in seen:
            pairs.add((min(num, complement), max(num, complement)))
        seen.add(num)
    
    return list(pairs)

#merge two sorted list
def merge_sorted_list(lst1: List[int], lst2: List[int]) -> List[int]:
    """
    Merge two sorted lists into a single sorted list.
    """
    merged = []
    i = j = 0
    len1, len2 = len(lst1), len(lst2)
    
    while i < len1 and j < len2:
        if lst1[i] <= lst2[j]:
            merged.append(lst1[i])
            i += 1
        else:
            merged.append(lst2[j])
            j += 1
    
    merged.extend(lst1[i:] or lst2[j:])
    
    return merged

# Example Usage
result = find_pairs(begin_list, 87)
if result:
    print("Pairs found:", result)
else:
    print("No pairs found")

new_list = [1,2,3,4,5,6,7,8,9,10]
new_list2 = [11,12,13,14,15,16,17,18,19,20]
print(merge_sorted_list(new_list, new_list2))







#remove all elements from the list
begin_list.clear()

