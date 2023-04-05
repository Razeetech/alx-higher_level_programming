#!/usr/bin/python3
"""Class that defines a rectangle"""


class Rectangle:
    """A rectangle with size, position, and methods to calculate more"""

    number_of_instances = 0
    """Tracks the number of instances that still exist"""

    print_symbol = '#'
    """The symbol used when drawing the string representation of rectangles"""

    def __del__(self):
        """Print a message when this rectangle is deleted"""

        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    def __init__(self, width=0, height=0):
        """
        Initialize a rectangle with optional size
        Args:
            height (int): height of rectangle
            width (int): width of rectangle
        """

        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __repr__(self):
        """
        Get a representation of this rectangle in Python code
        Returns:
            str: a representation of this rectangle that can be used by eval
        """

        return '{:s}({:d}, {:d})'.format(
            type(self).__name__,
            self.__width,
            self.__height
        )

    def __str__(self):
        """
        Draw this rectangle as a rectangle made of # characters
        Returns:
            str: string representation of this rectangle
        """

        if self.__height == 0 or self.__width == 0:
            return ''
        return '\n'.join(
            str(self.print_symbol) * self.__width
            for _ in range(self.__height)
        )

    @property
    def height(self):
        """
        The height of this rectangle
        The setter ensures that this value is an integer and >= 0
        """

        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise TypeError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        """
        The width of this rectangle
        The setter ensures that this value is an integer and >= 0
        """

        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise TypeError('width must be >= 0')
        self.__width = value

    def area(self):
        """
        Return this rectangle's area
        Returns:
            int: area
        """

        return self.__height * self.__width

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the largest of two rectangles
        Args:
            rect_1 (Rectangle): left operand
            rect_2 (Rectangle): right operand
        Returns:
            Rectangle: rect_1 if its area >= rect_2, rect_2 otherwise
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def perimeter(self):
        """
        Return the rectangle's perimeter
        Returns:
            int: perimeter
        """

        if self.__height == 0 or self.__width == 0:
            return 0
        return self.__height * 2 + self.__width * 2

    @classmethod
    def square(cls, size=0):
        """
        Create a new Rectangle representing a square with given size
        Args:
            size (int): length of sides of new square
        Returns:
            Rectangle: new Rectangle with given side lengths
        """

        return cls(size, size)