#Course: ITI1120
#Assignment number 3
#Ben Ali, Youcef
#XXXXXXXX

def two_length_run(l):
    """(List) -> (Boolean)
Function will return True if there is a run of atleast 2 and false otherwise
Preconditions: l must be a list"""
    for i in range(len(l)):
        l[i] = float(l[i])
    if len(l) < 2:
        return False
    for i in range(len(l)):
        if i == len(l)-1:
            return False
        if l[i] == l[i+1]:
            return True

print(two_length_run(input("Please input a list of numbers seperated by a space: ").strip().split()))
