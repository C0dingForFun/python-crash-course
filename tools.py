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
simple_list = [f'{j}{i}' for i in range(0, 11, 1) for j in ('a', 'b', 'c')]
# for i in range(0, 11, 1):
#     simple_list.append(i)
print(simple_list)


