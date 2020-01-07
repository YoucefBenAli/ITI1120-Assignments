#Course: ITI1120
#Assignment number 2
#Ben Ali, Youcef
#XXXXXXXX

def split_tester(N, d):
    '''(String, String) ->(Boolean)
This function will split the string D into groups of d characters.
Preconditions: Strings N and D must only be composed of positive integers'''
    if not N.isdigit() or not d.isdigit():
        return False
    if len(N)%int(d) != 0:
        return False
    else:
        numberlist = ""
        d = int(d)
        beginning = 0
        ending = d
        increasing = True
        if len(N) == 1 or len(N)//d == 1:
            numberlist = N
        else:
            for i in range(len(N)//d):
                if i == (len(N)//d -1): #Checking if this is the last loop
                    numberlist += N[beginning:ending]
                    if int(N[beginning:ending]) <= int(N[beginning-d:ending-d]):
                           increasing = False
                else:
                    numberlist += N[beginning:ending]+", "
                    if int(N[beginning:ending]) >= int(N[beginning+d:ending+d]):
                           increasing = False
                    beginning += d
                    ending += d
        
    print(numberlist)
    return increasing

def plaque(name):
    chars = " __" + name + ", Welcome to my increasing-splits tester.__ "
    print("*" * (len(chars)+2))
    print("*" + " "*len(chars) + "*")
    print("*" + chars + "*")
    print("*" + " "*len(chars) + "*")
    print("*" * (len(chars)+2))

def goodbyeplaque(name):
    chars = " __Good Bye " + name + "!__"
    print("*" * (len(chars)+2))
    print("*" + " "*len(chars) + "*")
    print("*" + chars + "*")
    print("*" + " "*len(chars) + "*")
    print("*" * (len(chars)+2))
plaque("")

name = input("What is your name? ").strip()
plaque(name)

flag=True
while flag:
    Posint1 = False
    Breakit = True
    Posint2 = False
    question=input(name+", would you like to test if a number admits an increasing-split of give size? ")
    question=(question.strip()).lower()
    if question=='no':
        flag=False
        goodbyeplaque(name)
    elif question == "yes":
        print("Good choice!")
        string1 = input("Enter a positive integer: ").strip()
        if string1.replace("-","").isdigit():
            if int(string1)>0:
                Posint1 = True
            else:
                print("The input has to be a positive integer. Try again.")
                Breakit = False
        else:
            print("The input can only contain digits. Try again.")
            Breakit = False
        if Breakit:
            string2 = input("Input the split. The split has to divide the length of " + string1 + " i.e " + str(len(string1)) + "\n").strip()
            if string2.isdigit():
                if int(string2)>0:
                    Posint2 = True
                else:
                    print("The input has to be a positive integer. Try again.")
                    Breakit = False
            else:
                print("The input has to be a positive integer. Try again.")
                Breakit = False
            if Breakit:
                
                if len(string1)%int(string2) != 0:
                    print(str(string2) + " does not divide " + str(len(string1)))
                else:
                    if split_tester(string1,string2):
                        print("The sequence is increasing")
                    else:
                        print("The sequence is not increasing")
    else:
        print("Please enter yes or no. Try again")

    
