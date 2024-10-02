#Creating a dictionary and performing operations
my_dict = {'a':1, 'b':2, 'c': 3}
print("Intial Dictionary:", my_dict)

#Adding a new key-value pair
my_dict['d']=4
print("After adding 'd':", my_dict)

#Updating a value
my_dict['b']= 20
print("After updating value of 'b':", my_dict)

#Remove a key-value pair 
removed_value = my_dict.pop('a',None)
print("After Removing 'a' (Value was {removed_value}):, my_dict")

# Iterating over dictory items
for key, value in my_dict.items():
    print(f"Key: {key}, Value: {value}")

#Checking for existence of a key
if 'b' in my_dict:
    print("'b' exists in the dicitonary")