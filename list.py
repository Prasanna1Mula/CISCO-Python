my_list = [1,2,3,4,5]
print("Initial List:", my_list)

#Appending elements
my_list.append(6)
print("After appending 6:",my_list)

#Removing elements in the list 
try:
    my_list.remove(10)
except ValueError:
    print("10 is not in the list")

#Reversing the List
my_list.sort()
print("Sorted List:", my_list)

#Checking if an element exits in the list
if 4 in my_list:
    print("4 is int he list")

#Inserting an element at specif position 
my_list.insert(2,208)
print("After inserting 208 at index 2:", my_list)

#List length and slicing
print("Length of list", len(my_list))
print("Sliced list (First 3 elements):", my_list[:3])