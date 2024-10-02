my_tuple = (10,20,30,40,50)
print("Initial Tuple:", my_tuple)

#Accessing the tuple elements using indexing and slicing
print("Element at index 2:", my_tuple[2])
print("Slicing Tuple from index 1 to 3:",my_tuple[1:4])

#Finding length of the tuple
print("Length of the tuple:", len(my_tuple))

#Concatenating two tuples
new_tuple = (60,100)
concatenated_tuple = my_tuple + new_tuple
print("Concatenated Tuple:", concatenated_tuple)

#Checking if the current element exists in the tuple
if 30 in my_tuple:
    print("30 is in the tuple")

#Tuple unpacking 
a,b,c,d,e = my_tuple
print("Unpacked Tuple Values:", a,b,c,d,e)