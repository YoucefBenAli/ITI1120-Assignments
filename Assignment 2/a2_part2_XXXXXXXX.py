#Course: ITI1120
#Assignment number 2
#Ben Ali, Youcef
#XXXXXXXX

#Question 2.1 ~~~~~~~~~~~~~~~~~~~~
def min_enclosing_rectangle(radius,x,y):
    '''(Number, Number, Number) ->(Number, Number)
Function will provide coordinates of bottom-left corner of a rectangle that can enclose a circle of radius parameter radius and with the coordinates of parameters x and y
Preconditions: Radius must be a positive number'''
    if radius < 0:
        return None
    else:
        rec = (x-radius, y-radius)
        return rec
#Question 2.2 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def series_sum():
    '''(None) -> (Number)
Function will calculate the equation 1000 + 1=1**2 + 1=2**2 + 1=3**2 + 1=4**2 + ::: + 1=n**2 Where n is a number the user provides
Preconditions: N must be a integer'''
    number = int(input("Please enter a non-negative integer: "))
    if number<0:
        return None
    else:
        series = 1000
        for i in range(number):
            series += 1/(i+1)**2
        return series

#Question 2.3 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def pell(n):
    '''(Integer) -> (Integer)
Calculates Pell's number with the parameter n
Preconditions: N must be an integer'''
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n>1:
        return 2*(pell(n-1))+pell(n-2)
    else:
        return None

#Question 2.4 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def countMembers(s): #WORK ON THIS LATER
    '''(String) -> (Integer)
Function will find how many special characters are in the parameter s. Special characters are efghijFGHIJKLMNOPQRSTUVWX23456\!
Preconditions: s must be a string'''
    extra = 0
    condition = 'efghijFGHIJKLMNOPQRSTUVWX23456\!,'
    for i in s:
        if i in condition:
            extra += 1
    return extra

#Question 2.5 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def casual_number(s):
    '''(String) -> (Integer)
Function will convert casual numbers into an integer processable by computers
Preconditions: s must be a string'''
    number = False
    for i in s:
        if i not in "1234567890-, ":
            return None
        if i in "1234567890":
            number = True
    if s.find("--") != -1:
        return None
    if not number:
        return None
    s = int(s.strip().replace(", ", "").replace(",", "").replace(" ", ""))
    return s

#Question 2.6 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def alienNumbers(s):
    '''(String) -> (Integer)
Function will calculate the sum of a string where each special symbol holds a certain value
Preconditions: s must be a string'''
    return s.count("T")*1024 + s.count("y")*598 + s.count("!")*121 + s.count("a")*42 + s.count("N") *6 + s.count("U")*1

#Question 2.7 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
def alienNumbersAgain(s):
        '''(String) -> (Integer)
Function will calculate the sum of a string where each special symbol holds a certain value
Preconditions: s must be a string'''
        total = 0
        for i in s:
            if i == "T":
                total += 1024
            elif i =="y":
                total += 598
            elif i =="!":
                total += 121
            elif i == "a":
                total += 42
            elif i == "N":
                total += 6
            elif i == "U":
                total += 1
        return total

#Question 2.8 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def encrypt(s): #To be worked on
    '''(String) -> (String)
Function will encrypt a given string
Preconditions: s must be a string'''
    condition = 0
    condition2 = True
    news = ""
    s = s[::-1]
    length = len(s)
    while condition == 0:
        for x in s:
            if condition2:         
                news = news + x
                s = s.replace(x,"",1)
                s = s[::-1]
                condition2 = False
        condition2 = True
        if len(news) == length:
            condition = 1
    return news

#Question 2.9 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def oPify(s):
    '''(String) -> (String)
Function will add op between each alphabetical character of the string and capitalize them according to how the characters are capitalized
Preconditions: s must be a string'''
    news = ""
    for i in range(len(s)):
        if i == len(s)-1:
            news = news+ s[i]
        elif s[i].isalpha() and s[i+1].isalpha():
            if s[i] == s[i].upper() and s[i+1] == s[i+1].lower():
                news = news + s[i] + "Op"
            elif s[i] == s[i].lower() and s[i+1] == s[i+1].upper():
                news = news + s[i] + "oP"
            elif s[i] == s[i].lower() and s[i+1] == s[i+1].lower():
                news = news + s[i] + "op"
            elif s[i] == s[i].upper() and s[i+1] == s[i+1].upper():
                news = news + s[i] + "OP"
        else:
            news = news + s[i]
    if news == "":
        news = s
    return news

#Question 2.10 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def nonrepetitive(s):
    '''(String) -> (Boolean)
Function will check if the string has any repeating characters.
Preconditions: S must be a string'''
    for i in s:
        if s.count(i)>1:
            reference = s.find(i)
            if s[reference+1] == i:
                return False
            else:
                s_excluding_repeat = s[(reference+1):]
                FirstSet = s[reference:(s_excluding_repeat.find(i)+1)]
                SecondSet = s[(s_excluding_repeat.find(i)): ((s_excluding_repeat.find(i))+len(FirstSet))]
                if FirstSet == SecondSet:
                    return False
    if len(s) == 0:
        return True
    return True
        
