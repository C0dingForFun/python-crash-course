# a basic class
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

# class Mage:
#     def __init__(self, health, mana):
#         self.health = health
#         self.mana = mana
#         print('the mage class was created')
#         # print(self.health)

#     def attack(self, target):
#         target.health -= 10

# class Monster:
#     health = 40

# mage = Mage(100, 200)
# monster = Monster()

# print(monster.health)
# mage.attack(monster)
# print(monster.health)

# Inheritance

class Warrior:
    def __init__(self, health):
        self.health = health

    def attack(self):
        print('attack')

class Barbarian:
        def __init__(self, health):
            self.health = health

        def attack(self):
            print('Attack')
     
