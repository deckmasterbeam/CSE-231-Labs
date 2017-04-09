import cards

def hand_initilization():
    the_deck = cards.Deck()
    the_deck.shuffle()
    
    p1_hand = []
    p2_hand = []
    i = 0
    while i < 10:
        card = the_deck.deal()
        if i%2 == 0:
            p1_hand.append(card)
        elif i%2 == 1:
            p2_hand.append(card)
        i += 1
    return p1_hand, p2_hand
    
def war_game(p1_hand, p2_hand):     
    while True:
        p1_card = p1_hand.pop(0)
        p2_card = p2_hand.pop(0)
        print()
        p1_card_rank = p1_card.rank()
        p2_card_rank = p2_card.rank()
        if p1_card_rank == 1:
            p1_card_rank = 20
        if p2_card_rank == 1:
            p2_card_rank = 20
        
        if p1_card_rank == p2_card_rank:
            print( "Tie:", p1_card, "and", p2_card, "of equal rank" )
            p1_hand.append(p1_card)
            p2_hand.append(p2_card)
            
        elif p1_card_rank > p2_card_rank:
            print( "Player #1 wins:", p1_card, "of higher rank than", p2_card )
            p1_hand.append(p1_card)
            p1_hand.append(p2_card)
        else:
            print( "Player #2 wins:", p2_card, "of higher rank than", p1_card )
            p2_hand.append(p1_card)
            p2_hand.append(p2_card)
        #For testing purposes    
        print(p1_hand)
        print(p2_hand)
            
        if len(p1_hand) == 0:
            break
        elif len(p2_hand) == 0:
            break
        
        user_input = input("Would you like to continue? (type 'quit' to quit, press enter to continue): ")
        if user_input.lower() == "quit":
            break
        else:
          continue
    return p1_hand, p2_hand

def win_cons(p1_hand, p2_hand):
    if len(p1_hand) == len(p2_hand):
        print("It's a tie!!!")
    elif len(p1_hand) > len(p2_hand):
        print("Player One Wins!!!")
    else:
        print("Player Two Wins!!!")
    
    
player1, player2 = hand_initilization()
player1, player2 = war_game(player1, player2)
win_cons(player1, player2)

    