import math


# Should the area method be moved into the shape class and inherited by circle, square, and rectangle? If so, what issues would result?
# No, each subclass will have their own area code as different shapes can require different equations to calculate area, makes code more messy if superclass has the area equation.
# Shape is superclass, rectangle, square, and circle will be subclasses and will apply inheritance only for sake of assignment instructions. ,
# "use Assert where possible and write your own exception inherited from the BaseException to manage errors." - Not covered well at all in edube, doing best to answer question


class excep(BaseException):
    def __init__(self, err, message):
        Exception.__init__(self, message)
        message = "this program does not run properly"
        self.err = err


class shape:
   pass


#subclasses of shape, (shape) applies inheritance to rectangle, square, and circle classes
#subclass rectangle, area width * height
class rectangle(shape):
    def __init__(self, width, height):
        assert width != height, "Width and height must be different for a rectangle"
        self.wid = width
        self.hgth = height

    def area(self):
        return self.wid * self.hgth

#subclass square, area width * height
class square(shape):
    def __init__(self, width, height):
        assert width == height, "Width and height must be the same for a square"
        self.wid = width
        self.hgth = height

    def area(self):
        return self.wid * self.hgth

#subclass circle, area for circle is = pi * radius(squared)
class circle(shape):
    def __init__(self, radius):
        self.rad = radius
        self.pi = 3.14159

    def area(self):
        return self.pi * self.rad ** 2

#calculate area of each shape
rectangle = rectangle(4, 5)
square = square(4,4)
circle = circle(3)


print("rectangle area:", rectangle.area())
print("square area:", square.area())
print("circle area:", circle.area())


