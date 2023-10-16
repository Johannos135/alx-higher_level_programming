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
        super().__init(id)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, width):
            self.__width = width

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, height):
            self.__height = height

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, x):
            selft.__x = x

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, y):
            self.__y = y
