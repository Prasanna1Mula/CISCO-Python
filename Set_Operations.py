# Creating a set, performing various operations including handling duplicate set
my_set = {1,2,3,4,5}
print("Initial Set:", my_set)

#Adding elements to the set
my_set.add(6)
print("After adding 6:", my_set)

#Trying to add duplicate element (won't affect the set)
my_set.add(3)
print("After attempting to add duplicate 3:", my_set)

#Removing elements from the set 
my_set.discard(10)
print("After discarding 10 ( not present):", my_set)

#Set operatins: Union, intersection, difference
set2 = {4,5,6,7}
print("Union of sets:", my_set.union(set2))
print("Intersection of sets:", my_set.intersection(set2))
print("Difference between sets:", my_set.difference(set2))

#Checking if an element exists in the text
if 5 in my_set:
    print("5 is in the set")
