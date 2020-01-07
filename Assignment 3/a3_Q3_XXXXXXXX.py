#Course: ITI1120
#Assignment number 3
#Ben Ali, Youcef
#XXXXXXXX

def longest_run(l):
    """(List) -> (Integer)
Function will determine the longest run inside the list
Preconditions: None"""
    if len(l) == 0:
        return 0
    if len(l) == 1:
        return 1
    for i in range(len(l)):
        l[i] = float(l[i])
    top = 0
    for i in range(len(l)):
        if i< len(l)-1:
            if l[i] == l[i+1]:
                condition = True
                x = 0
                count = 0 #How much times l[i] is repeated consecutively
                while condition:
                    if i+x <= len(l)-1:
                        if l[i] == l[i+x]:
                            count+= 1
                        else:
                            if top<count:
                                top = count
                            condition = False
                        x+= 1
            else:
                if top<1:
                    top = 1
    return top

print(longest_run(input("Please input a list of numbers seperated by a space: ").strip().split()))
