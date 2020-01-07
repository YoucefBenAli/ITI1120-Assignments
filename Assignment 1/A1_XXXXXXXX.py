#Course: ITI1120
#Assignment number 1
#Ben Ali, Youcef
#XXXXXXXX

import math
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question 1:
def pythagorean_pair(a,b):
    '''(integer, integer) -> (boolean)
    This function returns True if the a and b are a pythagorean pair
    Preconditions: a and b, must be integers'''
    c = math.sqrt(a**2 + b**2)
    return c%1 == 0
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question 2:
def mh2kh(s):
    '''(number) -> (float)
    Function will take your value in miles per hour and return it in kilometers per hour
    Preconditions: s must be a real number'''
    return s*1.609344
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question3:
def in_out(xs,ys,side):
    '''(Number, Number, Number) -> (Boolean)
    This function will take two coordinates (for the bottom left corner of a square) and the length of the square,
    and will ask prompt the user for two x,y coordinates and will print True if those coordinates are in the square and false if not
    Preconditions: Side must be a positive number, xs ys and side must be real numbers, x and y inputs must be real numbers'''
    x = float(input("Enter a number for the x coordinate of a query point: "))
    y = float(input("Enter a number for the y coordinate of a query point: "))
    print(x<= (xs+side) and x>=xs and y<= (ys+side) and y>=ys)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question 4:
def safe(n):
    '''(number) -> (boolean)
    Function will determine if the number is safe or not, it's safe if it doesnt contain the digit 9 and if it isnt divisible by 9
    Preconditions: n must be a real number'''
    div = n%9
    smallnum = n%10
    bignum = n//10
    return div != 0 and smallnum != 9 and bignum != 9
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question5:
def quote_maker(quote,name,year):
    '''(String, String, String/Integer) -> (String)
    Function will take your strings and return a string of format In year, a person called name said: “quote”
    Preconditions: Quote and name must be strings, year can be a positive integer or a string'''
    sentence = 'In ' +str(year) + ' a person called ' + str(name) + ' said: "' + str(quote) + '"'
    return sentence
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question6:
def quote_displayer():
    '''(None) -> (None)
    Allows user to input the quote,name and year and print a line with format: "In year, a person called name said: “quote”"
    Preconditions: None'''
    q = input("Please enter the quote: ")
    n = input("Please enter a name: ")
    y = input("Please enter a year: ")
    print(quote_maker(q,n,y))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question 7:
def rps_winner():
    '''(None) -> (None)
    The function will simulate a game of rock paper scissors
    Preconditions: Must type one of the following three - "rock" - "paper" - "scissors"'''
    choice1 = input("Player 1 please choose:\nrock\npaper\nscissors\n")
    choice2 = input("Player 2 please choose:\nrock\npaper\nscissors\n")
    tie = choice1 == choice2
    player1win = choice1=="rock" and choice2 =="scissors" or choice1 == "paper" and choice2 =="rock" or choice1=="scissors" and choice2 =="paper"
    print("This is a tie. That is not " + str(not tie))
    print("Player 1 wins. This is " + str(player1win))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question8:
def fun(x):
    '''(number) -> (number)
    Returns the value of y in the function 10**4y = x+3 where x is the parameter x
    Preconditions: x>=-3'''
    y = math.log(x+3, 10)/4
    return y
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question 9
def ascii_name_plaque(name):
    '''(String) - > (None)
Function will print a "drawing" of your name plaque
Preconditions: name must be a string'''
    print("*"*(len(name)+4))
    print("*", " "*(len(name)+2), "*", sep="")
    print("*", name, "*")
    print("*", " "*(len(name)+2), "*", sep="")
    print("*"*(len(name)+4))
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question 10
def draw_train():
    '''(None) -> (None)
Function will draw a train with turtle
Preconditions: None'''
    import turtle
    #BigBox1
    turtle.speed(0)
    turtle.penup()
    turtle.setposition(50,50)
    turtle.fillcolor("Dark Green")
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(100)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(130)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
    turtle.forward(140)
    turtle.end_fill()

    #Wheel1
    turtle.setpos(0,0)
    turtle.pendown()
    turtle.fillcolor("black")
    turtle.begin_fill()
    turtle.circle(50)
    turtle.end_fill()
    turtle.penup()
    turtle.setpos(0,30)
    turtle.fillcolor("gray")
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(20)
    turtle.end_fill()
    #CurrentPosition = 0,30

    #SmallRoof
    turtle.penup()
    turtle.setpos(90,250)
    turtle.left(90)
    turtle.fillcolor("Gray")
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(220)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(200)
    turtle.end_fill()
    turtle.penup()

    #Train Window
    turtle.setpos(0,230)
    turtle.fillcolor("Light Blue")
    turtle.begin_fill()
    turtle.pendown()
    turtle.forward(80)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(160)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
    turtle.forward(80)
    turtle.end_fill()
    turtle.penup()

    #Turtle BixBox2
    turtle.setpos(-90,160)
    turtle.right(180)
    turtle.pendown()
    turtle.fillcolor("Light Green")
    turtle.begin_fill()
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(110)
    turtle.left(90)
    turtle.forward(180)
    turtle.left(90)
    turtle.forward(110)
    turtle.end_fill()
    turtle.penup()

    #TurtleBumb1
    turtle.setpos(-110,160)
    turtle.pendown()
    turtle.fillcolor("Light Green")
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(20)
    turtle.end_fill()
    turtle.penup()
    turtle.setpos(-110,210)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(90)
    turtle.circle(10,180)
    turtle.end_fill()
    turtle.penup()
    turtle.right(180)

    #TurtleBumb2
    turtle.setpos(-160,160)
    turtle.pendown()
    turtle.fillcolor("Light Green")
    turtle.begin_fill()
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(25)
    turtle.left(90)
    turtle.forward(10)
    turtle.end_fill()
    turtle.penup()
    turtle.setpos(-160,185)
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(90)
    turtle.circle(5,180)
    turtle.end_fill()
    turtle.penup()
    turtle.right(180)
    #Wheel2
    turtle.setpos(-140,75)
    turtle.pendown()
    turtle.left(90)
    turtle.fillcolor("Black")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()
    turtle.setpos(-140,55)
    turtle.fillcolor("Gray")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()

    #Wheel3
    turtle.setpos(-200,75)
    turtle.pendown()
    turtle.fillcolor("Black")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()
    turtle.penup()
    turtle.setpos(-200,55)
    turtle.fillcolor("Gray")
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()

    #WheelBar
    turtle.setpos(turtle.xcor()-5,turtle.ycor()-5)
    turtle.left(180)
    turtle.pendown()
    turtle.fillcolor("Dark Gray")
    turtle.begin_fill()
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(10)
    turtle.right(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(10)
    turtle.end_fill()
    turtle.penup()

    #LightBulb
    turtle.setpos(-270,160)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor("Light Blue")
    turtle.begin_fill()
    turtle.circle(20,180)
    turtle.end_fill()
    turtle.right(90)

    #TriangleThingInfront
    turtle.forward(30)
    turtle.pendown()
    turtle.fillcolor("Gray")
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(270)
    turtle.forward(50*3**0.5)
    turtle.right(150)
    turtle.forward(100)
    turtle.end_fill()
    turtle.penup()

    #Chimney Thing I think???
    #~~Positioning
    turtle.setpos(-210,160)
    turtle.fillcolor("Light Green")
    turtle.left(60)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(10)
    #~Positioning
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(5)
    turtle.right(90)
    turtle.backward(10)
    #~Triangle
    turtle.begin_fill()
    turtle.pendown()
    turtle.right(30)
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(30)
    turtle.left(120)
    turtle.forward(30)
    turtle.end_fill()
    turtle.penup()
    turtle.right(210)
    #~Rectangle
    turtle.setpos(-210,160)
    turtle.pendown()
    turtle.begin_fill()
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(10)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(10)
    turtle.end_fill()
    #~Positioning
    turtle.setpos(-210,160)
    turtle.penup()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(30)
    turtle.forward(18)
    #Drawing
    turtle.pendown()
    turtle.begin_fill()
    turtle.left(60)
    turtle.forward(10)
    turtle.left(60)
    turtle.forward(20)
    turtle.left(60)
    turtle.forward(10)
    turtle.left(120)
    turtle.forward(30)
    turtle.end_fill()
    turtle.penup()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question 11:
def alogical(n):
    '''(number) -> (Integer)
    Takes a number and returns how many times the number must be devided by 2 in order to become less than 1
    Preconditions: n must be a real positive number and cannot be zero'''
    x = math.log(n,2)
    return math.ceil(x)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question 12:
def time_format(h,m):
    '''(integer, integer) -> (string)
    Takes time in hour and minute format and returns time in a neatly formatted string
    Preconditions: h and m must be positive integers'''
    roundedm = 5*(round(m/5))
    if roundedm == 60:
        roundedm = 0
        h = h+1
    if h == 24:
        h = 0
    if roundedm == 0:
        return "It is " + str(h) + " o'clock"
    elif roundedm == 30:
        return "it is half passed " + str(h) + " o'clock"
    elif 0< roundedm < 30:
        return "It is " + str(roundedm) + " minutes past " + str(h) + " o'clock" 
    elif 30< roundedm<60:
        if h == 23:
            h = 0
            return str(60-roundedm) + " minutes to " + str(h) + " o'clock" 
        else:
            return str(60-roundedm) + " minutes to " + str(h+1) + " o'clock"
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question 13:
def cad_cashier(price,payment):
    '''(number, number) -> (float)
    Function will return the change after a transaction costing parameter price and with a payment of parameter payment
    Preconditions: Price and payment are positive real, payment's second decimal place is always 0 or 5 and payment is above or equal to price'''
    return round(round((price-payment)/5,2)*-5, 2)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#Question 14
def min_CAD_coins(price,payment):
    '''(number,number) -> (integer,integer,integer,integer,integer)
    Function will call cad_cashier to determine amount of change, and will then divide change into coins optimizing for the least amount of coins
    Preconditions: Price and payment are positive real, payment's second decimal place is always 0 or 5 and payment is above or equal to price'''
    OwedMoneyInCents = cad_cashier(price,payment)*100
    toonies = int(OwedMoneyInCents//200)
    OwedMoneyInCents = round(OwedMoneyInCents - toonies*200)
    loonies = int(OwedMoneyInCents//100)
    OwedMoneyInCents = round(OwedMoneyInCents - loonies*100)
    quarters = int(OwedMoneyInCents//25)
    OwedMoneyInCents = round(OwedMoneyInCents-quarters*25)
    dimes = int(OwedMoneyInCents//10)
    OwedMoneyInCents = round(OwedMoneyInCents- dimes*10)
    nickels = int(OwedMoneyInCents//5)
    OwedMoneyInCents = round(OwedMoneyInCents-nickels*5)
    return(toonies,loonies,quarters,dimes,nickels)
draw_train()
