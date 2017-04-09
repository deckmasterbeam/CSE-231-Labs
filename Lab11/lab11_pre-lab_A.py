##
## Demonstrate some of the operations of the Deck and Card classes
##

import cards

# Seed the random number generator to a specific value so every execution
# of the program uses the same sequence of random numbers (for testing).

import random
random.seed( 25 )


# Create a deck of cards

my_deck = cards.Deck()


# Display the deck (unformatted)
# print( "===== initial deck =====" )
# print()
# print( my_deck )
# print()


# Display the deck in 13 columns

print( "===== initial deck =====" )
print(my_deck)
my_deck.display()


# Shuffle the deck, then display it in 13 columns


# Deal first card from the deck and display it (and info about the deck)
loop_counter = 0
card2 = my_deck.deal()

while loop_counter < 51:
    
    card1 = my_deck.deal()
    print( "===== shuffled deck =====" )
    my_deck.display()

    print( "First card dealt from the deck:", card1 )
    print()
    print( "Card suit:", card1.suit() )
    print( "Card rank:", card1.rank() )
    print( "Card value:", card1.value() )
    print()
    print( "Deck empty?", my_deck.is_empty() )
    print( "Number of cards left in deck:", len(my_deck) )
    print()
    if card1.suit() == card2.suit():
        print( card1, "same suit as", card2 )
    else:
        print( card1, "and", card2, "are from different suits" )
    
    if card1.rank() == card2.rank():
        print( card1, "and", card2, "of equal rank" )
    elif card1.rank() > card2.rank():
        print( card1, "of higher rank than", card2 )
    else:
        print( card2, "of higher rank than", card1 )
    
    if card1.value() == card2.value():
        print( card1, "and", card2, "of equal value" )
    elif card1.value() > card2.value():
        print( card1, "of higher value than", card2 )
    else:
        print( card2, "of higher value than", card1 )
    card2 = card1
    loop_counter += 1
    
# Deal second card from the deck and display it (and info about the deck)



# Compare the two cards



