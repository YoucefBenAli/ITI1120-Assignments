
#Course: ITI1120
#Assignment number 3
#Ben Ali, Youcef
#XXXXXXXX


# In this implementation a card (that is not a 10) is represented
# by a 2 character string, where the 1st character represents a rank and the 2nd a suit.
# Each card of rank 10 is represented as a 3 character string, first two are the rank and the 3rd is a suit.

import random

def wait_for_player():
    '''()->None
    Pauses the program until the user presses enter
    '''
    try:
         input("\nPress enter to continue. ")
         print()
    except SyntaxError:
         pass


def make_deck():
    '''()->list of str
        Returns a list of strings representing the playing deck,
        with one queen missing.
    '''
    deck=[]
    suits = ['\u2660', '\u2661', '\u2662', '\u2663']
    ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    for suit in suits:
        for rank in ranks:
            deck.append(rank+suit)
    deck.remove('Q\u2663') # remove a queen as the game requires
    return deck

def shuffle_deck(deck):
    '''(list of str)->None
       Shuffles the given list of strings representing the playing deck    
    '''
    random.shuffle(deck)

#####################################

def deal_cards(deck):
     '''(list of str)-> tuple of (list of str,list of str)

     Returns two lists representing two decks that are obtained
     after the dealer deals the cards from the given deck.
     The first list represents dealer's i.e. computer's deck
     and the second represents the other player's i.e user's list.
     '''
     dealer=[]
     other=[]

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE
     x = 1
     for i in deck:
        if x%2 != 0:
             dealer.append(i)
             x+= 1

        else:
            other.append(i)
            x+= 1
     return (dealer, other)
 


def remove_pairs(l):
    '''
     (list of str)->list of str

     Returns a copy of list l where all the pairs from l are removed AND
     the elements of the new list shuffled

     Precondition: elements of l are cards represented as strings described above

     Testing:
     Note that for the individual calls below, the function should
     return the displayed list but not necessarily in the order given in the examples.

     >>> remove_pairs(['9♠', '5♠', 'K♢', 'A♣', 'K♣', 'K♡', '2♠', 'Q♠', 'K♠', 'Q♢', 'J♠', 'A♡', '4♣', '5♣', '7♡', 'A♠', '10♣', 'Q♡', '8♡', '9♢', '10♢', 'J♡', '10♡', 'J♣', '3♡'])
     ['10♣', '2♠', '3♡', '4♣', '7♡', '8♡', 'A♣', 'J♣', 'Q♢']
     >>> remove_pairs(['10♣', '2♣', '5♢', '6♣', '9♣', 'A♢', '10♢'])
     ['2♣', '5♢', '6♣', '9♣', 'A♢']
    '''

    no_pairs=[]

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    # YOUR CODE GOES HERE
    
    no_pairs=[]
    exeptions = []
    copy = l[:]
    pairs = []
    for i in copy:
        num1 = str(i)[0]
        condition = True
        x = 0
        if i not in exeptions:
            while x<len(copy) and condition:
                num2 = str(copy[x])[0]
                if num1 == num2 and x != copy.index(i) and copy[x] not in exeptions:
                    exeptions.append(i)
                    exeptions.append(copy[x])
                    l.remove(i)
                    l.remove(copy[x])
                    condition = False
                x+= 1
    no_pairs = l
    random.shuffle(no_pairs)
    return no_pairs

def print_deck(deck):
    '''
    (list)-None
    Prints elements of a given list deck separated by a space
    '''

    # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
    for i in deck:
        if deck.index(i) != len(deck)-1:
            print(i, end=" ")
        else:
            print(i, end="\n")


def get_valid_input(n):
     '''
     (int)->int
     Returns an integer given by the user that is at least 1 and at most n.
     Keeps on asking for valid input as long as the user gives integer outside of the range [1,n]
     
     Precondition: n>=1
     '''

     # COMPLETE THE BODY OF THIS FUNCTION ACCORDING TO THE DESCRIPTION ABOVE
     # YOUR CODE GOES HERE

     condition = True
     while condition:
         try:
             num = int(input(f"Please provide an integer between 1 and {n}: ").strip())
             if num < 1 or num > n:
                 raise ValueError
             else:
                condition = False
         except ValueError:
             print("That is not a valid integer, please try again")
     return num

def which_card(card):
    '''(int) -> (String)
Function will format an integer into a "position", example: 2 -> 2nd, 3-> 3rd
Preconditions: card must be a valid integer and card >0'''
    if card == 1:
        return "1st"
    elif card ==2:
        return "2nd"
    elif card == 3:
        return "3rd"
    elif card >3:
        return str(card)+"th"

def take_card(l):
    '''(List) -> (Integer, listitem)
Function will randomly return which card to take from the human's deck as well as what is the card's position in his deck'''
    if len(l) > 0:        
        randomnumber = random.randint(0,len(l)-1)
        randomcard = l[randomnumber]
        return (randomnumber+1,randomcard)
    else:
        return (None, None)
def win(l):
    '''(List) -> (Boolean)
Function will check if the list is empty or not'''
    if len(l)==0:
        return True
    else:
        return False
def play_game():
     '''()->None
     This function plays the game'''
    
     deck=make_deck()
     shuffle_deck(deck)
     tmp=deal_cards(deck)

     dealer=tmp[0]
     human=tmp[1]

     print("Hello. My name is Robot and I am the dealer.")
     print("Welcome to my card game!")
     print("Your current deck of cards is:")
     print_deck(human)
     print("Do not worry. I cannot see the order of your cards")

     print("Now discard all the pairs from your deck. I will do the same.")
     wait_for_player()
     
     dealer=remove_pairs(dealer)
     human=remove_pairs(human)

     # COMPLETE THE play_game function HERE
     # YOUR CODE GOES HERE
     print("After discarding the pairs from your deck, your deck is now: \n")
     print_deck(human)
     wait_for_player()
     condition = True
     
     while condition:
         print("*************************************************\nYour turn: \n")
         print("Your current deck of cards is: \n")
         print_deck(human)
         print(f"I have {len(dealer)} cards, if 1 represents the first card and {len(dealer)} represents my last card, which of my cards would you like?\n")
         card = get_valid_input(len(dealer))
         print(f"You have asked for my {which_card(card)} card\n")
         card2 = dealer[card-1]
         print(f"Here it is. It is: {card2}\n")
         human.append(card2)
         dealer=remove_pairs(dealer)
         print(f"With {card2} added your deck is now: \n")
         print_deck(human)
         print(f"And after discarding any pairs, the deck is now: \n")
         human=remove_pairs(human)
         print_deck(human)

         if win(human) == True:
             condition = False

         elif win(human) == False:
             wait_for_player()
             print("*************************************************\nMy turn: \n")
             x,y = take_card(human)
             print(f"I have taken your {which_card(x)} card")
             dealer.append(y)
             human.remove(y)
             wait_for_player()
             if win(dealer) == True:
                 condition = False
     if win(human):
         print("*************************************************\nUps. You do not have any more cards\nCongratulations! You, Human, win")
     elif win(dealer):
         print("*************************************************\nUps. I do not have any more cards\nCongratulations! You lost! I, Robot, win")
         
# main
play_game()
