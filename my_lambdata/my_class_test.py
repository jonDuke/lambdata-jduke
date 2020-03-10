# my_lambdata/my_class.py

# script to test out my_class

from my_lambdata.my_class import My_Class

obj1 = My_Class('Bob', 'red', 14)
obj2 = My_Class('Sally', 'blue', 42)

obj1.introduce_self()
obj2.introduce_self()

print('\nPicking a new number')
obj1.pick_new_number()
print(obj1.name, 'picked', obj1.fav_number)

print('\nPicking a new color')
obj2.pick_new_color()
print(obj2.name, 'picked', obj2.fav_color)