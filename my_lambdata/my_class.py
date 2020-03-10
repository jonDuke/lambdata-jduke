# my_lambdata/my_class.py

import random


class My_Class():
    """
    an example class
    """

    def __init__(self, name, fav_color, fav_number):
        """
        Initializes my_class

        name (string) - the name of this object
        fav_color (string) - this object's favorite color
        fav_number (int) - this object's favorite number
        """
        self.name = str(name)
        self.fav_color = str(fav_color)
        self.fav_number = int(fav_number)

    def introduce_self(self):
        """
        says hello
        """
        print('Hi!  My name is ' + self.name +
              '.  My favorite color is ' + self.fav_color +
              ' and my favorite number is ' + str(self.fav_number) + '.')

    def pick_new_number(self):
        """
        randomly picks a new favorite number between 0 and 100 (inclusive)
        """
        self.fav_number = random.randrange(101)

    def pick_new_color(self):
        """
        randomly picks a new favorite color
        """
        colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
        choice = random.randrange(len(colors))
        self.fav_color = colors[choice]
