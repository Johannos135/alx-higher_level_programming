#!/usr/bin/python3
""" Module Class Rectangle """

from models.base import Base


class Rectangle(Base):
    """ Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Class constructor

            Parameters:
                width: represents rectangle width
                height: represents rectangle height
                x: attribute x
                y: attribute y
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """ Get the value of width """
            return self.__width

        @width.setter
        def width(self, value):
            """ Set a value to width """
            self.__width = value

        @property
        def height(self):
            """ Get the value of height """
            return self.__height

        @height.setter
        def height(self, value):
            """ Set a value to height """
            self.__height = value

        @property
        def x(self):
            """ Get the value of x """
            return self.__x

        @x.setter
        def x(self, value):
            """ Set a value to x """
            selft.__x = value

        @property
        def y(self):
            """ Get the value of y """
            return self.__y

        @y.setter
        def y(self, value):
            """ Set a value to y """
            self.__y = value
