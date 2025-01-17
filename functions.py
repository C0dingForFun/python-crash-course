# create a function
# def print_x_times(parameter = 'loop', loop_amount = 5):
#     counter = 0
#     print(global_var)
#     while counter < loop_amount:
#         print(counter, parameter)
#         counter += 1
#     return 'something else'

def hypotenuse_calculator(a = 1, b = 2):
    c = (a ** 2 + pow(b, 2)) ** (1/2)
    return round(c, 2)

# Exercise
def print_string(word = 'Hello World', loop_amount = 3):
    if loop_amount <= 10:
        for i in range(loop_amount):
            print(word.upper())
    else:
        print('You are too loud')
    return 'done'
# call
# print('print') 
# global_var = 'global variable'
# test = print_x_times('something', 4)
# print(test)

# print(hypotenuse_calculator())

status = print_string('Mkbk', 10)
print(status)
