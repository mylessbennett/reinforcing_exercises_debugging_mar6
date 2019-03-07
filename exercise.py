def select_cards(possible_cards, hand):

    cards = 0
    while len(hand) != 3:
        print("Do you want to pick up {}?".format(possible_cards[cards]))
        answer = input()
        if answer.lower() == 'y':
            hand.append(possible_cards[cards])
        cards += 1
    return hand

# Switched to while loop and took return statement out of loop

#   for current_card in possible_cards:
#     print("Do you want to pick up {}?".format(current_card))
#     answer = input()
#     if answer.lower() == 'y':
#       hand.append(current_card)
#     return hand


available_cards = ['queen of spades', '2 of clubs', '3 of diamonds', 'jack of spades', 'queen of hearts']

new_hand = select_cards(available_cards, [])

display_hand = "\n".join(new_hand)

print("Your new hand is: \n{}".format(display_hand))
