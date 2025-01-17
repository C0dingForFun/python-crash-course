# f strings 
# user_name = 'Paul'
# user_age = 16
# user_informaion = f'{user_name} is {user_age} years old.'
# bad_approach = user_name + ' is '+ str(user_age) +'10 years old' # bad approach
# print(user_informaion)

# single line if statements
# user_name = 'Gwiba'
# user_age = 17
# user_status = '
# if user_age < 18:
#     user_status = 'Child'
# else:
#     user_status ='Adult'
# print(f'{user_name} is {user_age} years old. The person is a {'Adult' if user_age >= 18 else 'Child'}.')

# list comprehension
# simple_list = [f'{j}{i}' for i in range(0, 11, 1) for j in ('a', 'b', 'c') if j == 'a']
# for i in range(0, 11, 1):
#     simple_list.append(i)
# print(simple_list)

# lambda functions
# def double_value(num):
#     return num * 2

double_value = lambda num: num * 2 # lambda turns this into a function
print(double_value(10))

# some functions want a function as an argument
random_list = [0, 5, 2, 4, 1, 123, 523]
# random_list2 = ['w', 's', 'a', 'b']
random_list3 = [('Anna', 25), ('Paul', 40), ('Lisa', 10)]

sorted_list = sorted(random_list) # arranges numbers to ascending order
# sorted_list2 = sorted(random_list2) # arranges letters to alphabetical order
sorted_list3 = sorted(random_list3, key = lambda user_tuple: user_tuple[1])

print(sorted_list3)

# Exercise
battleship_list = [f'{y}{x}' for x in range(0, 6, 1) for y in ('A', 'B', 'C', 'D', 'E') if f'{y}{x}' != 'C3']
print(battleship_list)
