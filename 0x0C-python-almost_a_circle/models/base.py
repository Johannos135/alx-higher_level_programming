#!/usr/bin/python3
""" Base class module """


class Base:
    """ Class base """
    __nb_objects = 0


    def __init__(self, id=None):
        """ Class Base COnstructor
            
            Args:
                id: Public instance of class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
