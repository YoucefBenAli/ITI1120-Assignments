#Course: ITI1120
#Assignment number 3
#Ben Ali, Youcef
#XXXXXXXX


def number_divisible(l,n):
    '''(List, Integer) -> (Integer)
Function will count how many integers inside parameter l are divisble by parameter n
Preconditions: l must have atleast one element'''
    divisible = 0
    if len(l) == 0:
        return divisible #Returns zero
    else:
        for i in l:
            if i%n == 0:
                divisible += 1
    return divisible

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

raw_input = input("Please input a list of numbers seperated by spaces").strip().split()
for i in range(0,len(raw_input)):
    raw_input[i] = int(raw_input[i])

integer = int(input("Please enter an integer").strip())

print(f"The number of elements divisible by {integer} is {number_divisible(raw_input,integer)}")
