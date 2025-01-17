# if statements
# if 3 > 4:
#     print('correct result') # false
# elif 0 > 1:
#     print('some other result') # false
# elif 0 == 0 and 5 > 1:
#     print('some other result') # true so one will display
#     if len([1, 2, 3 ]) > 2:
#         print('list is long enough')
# else:
#     print('incorrect result')

# while loop
# counter = 0

# while counter <= 10:
#     print(counter)
#     counter += 1
#     if counter == 5:
#         print('counter is 5')
# print('while loop is finished')

# for loop
# test_list = {1, 2, 3, 3}
# test_list = {1:2, 3:4, 5:6}
# for x in test_list.keys(): loops through the dictionary's keys
# for x in test_list.values(): # loops through the dictionary's values
# for x, y in test_list.items(): # loops through the dictionary's items
#     print(x)
#     print(y)

# truthy and falsy
# if 'a':
#     print('truthy')
# else:
#     print('falsy')

# Exercise

ex_list = (1, 2, 3, 4, 5)
ex_counter = 0
for x in ex_list:
    if x == 2:
        print('the value is 2')
    else:
        print('the value is not 2')
while ex_counter <= 6:
            print('last item')
            ex_counter += 1
