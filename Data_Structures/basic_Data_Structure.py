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

from typing import List, Tuple
from collections import defaultdict

def find_pairs(lst: List[int], target: int) -> List[Tuple[int, int]]:
    """
    Find all unique pairs in the list `lst` that sum up to the target value.

    Args:
    lst (List[int]): The list of integers.
    target (int): The target sum for which pairs are to be found.

    Returns:
    List[Tuple[int, int]]: A list of tuples, each containing a pair of numbers that add up to the target.
    """
    # Input validation
    if not isinstance(lst, list) or not all(isinstance(x, int) for x in lst):
        raise ValueError("Input must be a list of integers.")
    if not isinstance(target, int):
        raise ValueError("Target must be an integer.")

    seen = defaultdict(int)
    pairs = []
    
    for num in lst:
        complement = target - num
        # Check if the complement exists in the dictionary
        if seen[complement] > 0:
            pairs.append((complement, num))
            seen[complement] -= 1  # Decrement to avoid using the same element multiple times
        else:
            seen[num] += 1
    
    return pairs


# Example Usage
result = find_pairs(begin_list, 87)
if result:
    print("Pairs found:", result)
else:
    print("No pairs found")







#remove all elements from the list
begin_list.clear()

