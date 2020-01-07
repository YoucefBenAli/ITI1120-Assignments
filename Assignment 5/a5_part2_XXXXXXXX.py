# Course: IT1 1120
# Assignment number 5
# Youcef Ben Ali
# XXXXXXXX
# Part 2

class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord

    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle:
    "Class that represents a rectangle in the place"
    def __init__(self,p1,p2,color):
        """
        (Point, Point, str) -> None
        Initializes the rectangle to (point1coord, point2coord, color)
        """
        self.p1 = p1
        self.p2 = p2
        self.color = color
        
    def __repr__(self):
        """
        (Rectangle) -> str
        Returns canonical string representation Rectangle(Point1(x, y), Point2(x, y), color)
        """
        return f"Rectangle(Point({self.p1.x},{self.p1.y}), Point({self.p2.x},{self.p2.y}), '{self.color}')"
    
    def __str__(self):
        """
        (Rectangle) -> str
        Returns nice string representation Rectangle(Point1(x, y), Point2(x, y), color).
        """
        return f"I am a {self.color} rectangle with bottom left corner at ({self.p1.x}, {self.p1.y}) and top right corner at ({self.p2.x}, {self.p2.y})."

    def __eq__(self, other):
        """
        (Rectangle, Rectangle) -> bool
        Returns True if self and other have the same bottom left corner and top right corner coordinates
        """
        return self.p1 == other.p1 and self.p2 == other.p2 and self.color == other.color
    def get_color(self):
        """
        () -> str
        Returns the color the rectangle
        """
        return self.color
    
    def get_bottom_left(self):
        """
        () -> str
        Returns the coordinates of p1 (the bottom left corner)
        Preconditions: bottom left corner exists
        """
        return self.p1
    
    def get_top_right(self):
        """
        () -> str
        Returns the coordinates of p2 (the top right corner)
        Preconditions: top right corner exists
        """
        return self.p2
    
    def reset_color(self,color):
        """
        (str) -> None
        Changes the color of the rectangle to new_color
        Preconditions: new_color is a string
        """
        self.color = color
        
    def get_perimeter(self):
        """
        () -> number
        Returns the perimeter of the rectangle
        Preconditions: p1 and p2 exist
        """
        difx = self.p1.x-self.p2.x
        dify = self.p1.y-self.p2.y
        return 2*abs(dify) + 2*abs(difx)
    
    def move(self,x,y):
        """
        (number, number) -> None
        Changes the x and y coordinates of p1 and p2 by dx and dy, which moves the whole rectangle
        """
        self.p1.move(x,y)
        self.p2.move(x,y)
    def get_area(self):
        """
        () -> number
        Returns the area of the rectangle
        Preconditions: p1 and p2 exist
        """
        difx = self.p1.x-self.p2.x
        dify = self.p1.y-self.p2.y
        return abs(difx)*abs(dify)
    def intersects(self,rectangle):
        """
        (Rectangle) -> boolean
        Returns True if Rectangles 1 and 2 intersect and False otherwise
        Preconditions: rectangles is an object of class rectangle
        """
        if self.p1.x > rectangle.p2.x or self.p2.x < rectangle.p1.x:
            return False
        if self.p1.y > rectangle.p2.y or self.p2.y < rectangle.p1.y:
            return False
        else:
            return True
        
    def contains(self,x,y):
        """
        (number, number) -> boolean
        Returns True if point with coordinates (xcoord, ycoord) is in object Rectangle
        Preconditions: xcoord and ycoord are numbers
        """
        if not (x >= self.p1.x and x <= self.p2.x):
            return False
        if not (y >= self.p1.y and y <= self.p2.y):
            return False
        else:
            return True
    
class Canvas:
    "Class that represents a canvas in the plane"
    def __init__(self):
        """
        () -> None
        Initializes the canvas
        """
        self.rectangles = list()
        
    def __len__(self):
        """
        () -> int
        Returns the amount of rectangles in the canvas
        """
        return len(self.rectangles)
    def __repr__(self):
        """
        (Canvas) -> str
        Returns string Canvas(ListOfRectangles)
        """
        return f"Canvas({self.rectangles})"
    def add_one_rectangle(self, rectangle):
        """
        (Rectangle) -> None
        Adds the parameter rectangle to the canvas
        Precondition: "rectangle" is a object of class rectangle
        """
        self.rectangles.append(rectangle)
    def total_perimeter(self):
        """
        () -> Number
        Returns the sum of perimeters
        """
        total = 0
        for i in self.rectangles:
            total += i.get_perimeter()
        return total
    def min_enclosing_rectangle(self):
        """
        () -> str
        Returns a string that includes the coordinates of the canvas (rectangles enclosed)
        Precondition: canvas has atleast one rectangle
        """
        minx = None
        maxx = None
        miny = None
        maxy = None
        for i in self.rectangles:
            tempminx = i.get_bottom_left().x
            tempminy = i.get_bottom_left().y
            tempmaxx = i.get_top_right().x
            tempmaxy = i.get_top_right().y
            if minx == None:
                minx = tempminx
                miny = tempminy
                maxx = tempmaxx
                maxy = tempmaxy
            else:
                if minx>tempminx:
                    minx = tempminx
                if miny>tempminy:
                    miny = tempminy
                if maxx<tempmaxx:
                    maxx = tempmaxx
                if maxy<tempmaxy:
                    maxy = tempmaxy
        return Rectangle(Point(minx,miny),Point(maxx,maxy),"green")
    def common_point(self):
        """
        () -> boolean
        Returns true if the rectangles in the canvas share a common point, and false otherwise
        Precondition: canvas has alteast one rectangle
        """
        for i in self.rectangles:
            for j in self.rectangles:
                if i!=j:
                    if not(i.intersects(j)):
                        return False
        return True
    def count_same_color(self, color):
        """
        (str) -> int
        Returns the amount of rectangles with this color
        Precondition: desired_color is a string
        """
        colors = {}
        for i in self.rectangles:
            if i.get_color() not in colors.keys():
                colors[i.get_color()] = 1
            else:
                colors[i.get_color()] += 1
        if color not in colors.keys():
            return 0
        else:
            return colors[color]
        
