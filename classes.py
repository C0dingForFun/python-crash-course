# # a basic class
# class TestClass:
#     test_var = (1, 2, 3 )
#     another_var = 'something'

#     def test_func(self):
#         print('function in a class')
#         print(self.test_var)
#         self.another_func()

#     def another_func(self, test_param):
#         print(test_param)


# # create an instance
# test = TestClass()
# # print(test.test_var)
# test.another_var = 'new value' # reassigning the varible from the class
# # print(test.another_var)

# test2 = TestClass()
# print(test2.another_var)
# test2.test_func()

# test3 = TestClass()
# test3.another_func()

class Mage:
    def __init__(self, health, mana):

        print('the mage class was created')

mage = Mage()
