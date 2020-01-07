# Course: IT1 1120
# Assignment number 5
# Youcef Ben Ali
# XXXXXXXX
# Part 1

import string

def printing(coexistance, query):
    '''(Set, String) -> None
Prints the lines in the set
'''
    query = query.strip()
    coexistance = list(coexistance)
    if len(coexistance) == 0:
        print(f"The word/words '{query}' are/is not in the file")
    else:
        print("The one or more words you entered coexisted in the following lines of the file:")
        for i in range(len(coexistance)):
            if i == len(coexistance)-1:
                print(coexistance[i])
            else:
                print(coexistance[i], end=" ")

def wordprocess(word):
    '''(String)->(String)
Removes any punctuation in the word.'''
    for i in string.punctuation:
        word.replace(i,"")
    return word

def alphaorunder2(words):
    '''(list) -> (list)
Removes non alphanumerical words and words under 2 characters long. Returns the list of words.'''
    for i in words:
        for j in set(i):
            if not j.isalpha() or len(j)<2:
                i.remove(j)
    return words

def open_file():
    '''None->file object
    This function continously asks for the user to input a valid text file'''
    # YOUR CODE GOES HERE
    condition = True
    while condition:
        try:
            name = input("Please enter the name of your file").strip()
            x = open(name)
            return x
        except:
            print("That file does not exist, please try again.")
   

def read_file(fp):
    '''(file object)->dict
    Processes the file and makes a dictionary connecting each word with the lines it appears in'''
    # YOUR CODE GOES HERE
    text = fp.read().lower().splitlines()
    words = list()
    for i in text:
        temp = i.replace("'","")
        for x in string.punctuation:
            temp = temp.replace(x,"")
        words.append(set(temp.split()))
    words = alphaorunder2(words)
    d = {}
    for i in words:
        for j in i:
            if j not in d.keys():
                d[j] = {words.index(i)+1}
            else:
                d[j].add(words.index(i)+1)
    return d
    

def find_coexistance(D, query):
    '''(dict,str)->list
    Finds which common lines a list of words appear in'''
    # YOUR CODE GOES HERE
    query = query.lower().split()
    sets = []
    for i in query:
        if i not in D.keys():
            return {}
        else:
            sets.append(D[i])
    common = sets[0]
    for i in sets:
        common = common.intersection(i)
    return common
    

##############################
# main
##############################
file=open_file()
d=read_file(file)
query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
# YOUR CODE GOES HERE
if query != "q":
    printing(find_coexistance(d,query), query)

while query !="q":
    query=input("Enter one or more words separated by spaces, or 'q' to quit: ").strip().lower()
    query = wordprocess(query)
    if query !="q":
        printing(find_coexistance(d,query), query)




