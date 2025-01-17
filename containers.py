# a_tuple = (1, 2, 3, 'a string')
# a_list = [1, 2, 3, 'a string']
# # print(len(a_list)) # will return the number of items inside the list 

# a_list.append('another word') # adds an item at the end of the list
# print(a_list)

# container setup
a_tuple = (1, 2, 3, 'a string')
a_list = [1, 2, 3, 'a string', 2]
a_set = {1, 2, 3, 4}
print(set(a_list)) # set() function will convert any container into a set container
a_dictionary = {'key': 'value', 123: [1, 2, 3]}
a_dictionary['new key'] = 1.5 # this will add a new key and value in the dictionary
print(a_dictionary)

# how to get values from a container 
user_list = ('Lisa', 'Bob', 'Alex', 'Anna', 'John')
print(user_list[-1]) # will display from right to left
print(user_list[0:4:2]) # start at index 0 and stop before the 3rd index and will display the 2nd index after 
print(a_dictionary[123])

# Exercise 

ex_list = (1, 2, 3, 4, 5, 6, 7, 8, 9 ,10)
new_list = ex_list[7::-2] # kinda understand this
print(new_list)

