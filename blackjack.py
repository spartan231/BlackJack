from p1_random import P1Random
# outside of the loop
# brings in the function P1Random from the p1_random file
rng = P1Random()

# sets the continue variable to be initially true
game_continue = True
# sets the number of games played to zero
game_num = 0
# sets the number of player wins to zero
player_wins = 0
# sets the numebr of dealer wins to zero
deals_wins = 0
# sets the number of ties to zero
num_ties = 0

# control the number of games the player will play
while game_continue:
    # 1. print game number message
    game_num += 1
    print(f"START GAME #{game_num}")
    print()

    # 2. deal a card to the player automatically
    player_hand = 0
    # [0,12] => [1,13]
    # deal a card to the player
    card = rng.next_int(13) + 1

    # "#" of the card has a value of 1 than the card is an ACE
    # the player hand increases by 1
    # print card and player hand values
    if card == 1:
        print("Your card is a ACE!")
        player_hand += 1
        print(f"Your hand is: {player_hand}")

    # the card that are not face or ace cards
    # the player hand increases by the value of the card
    # print card and player hand values
    elif 2 <= card <= 10:
        print(f"Your card is a {card}!")
        player_hand += card
        print(f"Your hand is: {player_hand}")

    # represents the jack
    # the player hand increases by 10
    # print card and player hand values
    elif card == 11:
        print(f"Your card is a JACK!")
        player_hand += 10
        print(f"Your hand is: {player_hand}")

    # represents the queen
    # the player hand increases by 10
    # print card and player hand values
    elif card == 12:
        print(f"Your card is a QUEEN!")
        player_hand += 10
        print(f"Your hand is: {player_hand}")

    # represents the king
    # the player hand increases by 10
    # print card and player hand values
    elif card == 13:
        print(f"Your card is a KING!")
        player_hand += 10
        print(f"Your hand is: {player_hand}")

    # within the game it sets there to be no winner to true
    no_winner = True

    while no_winner:
        # print four menu options
        print()
        print("1. Get another card")
        print("2. Hold hand")
        print("3. Print statistics")
        print("4. Exit")
        print()

        # gets the user choice from the menu options
        user_choice = int(input("Choose an option: "))

        # if user chocies 1
        # gives the user a card
        if user_choice == 1:
            card = rng.next_int(13) + 1

            # if the card is a 1 it's an ace
            # increase player hand to plus one
            # prints the card name and your hand value
            if card == 1:
                #print()
                print("Your card is a ACE!")
                player_hand += 1
                print(f"Your hand is: {player_hand}")

            # if the card is in the range of 2 and 10 inclusive
            # increase the player hand to plus the value of the card
            # prints the card name and your hand value
            elif 2 <= card <= 10:
                # print out the card value
                #print()
                print(f"Your card is a {card}!")
                player_hand += card
                print(f"Your hand is: {player_hand}")

            # if the card is 11 its a JACK
            # increase the player hand to plus 10
            # prints the card name and your hand value
            elif card == 11:
                #print()
                print("Your card is a JACK!")
                player_hand += 10
                print(f"Your hand is: {player_hand}")

            # if the card is 12 its a queen
            # increase the player hand to plus 10
            # prints the card name and your hand value
            elif card == 12:
                #print()
                print("Your card is a QUEEN!")
                player_hand += 10
                print(f"Your hand is: {player_hand}")

            # if the card is 13 its a king
            # increase the player hand to plus 10
            # prints the card name and your hand value
            elif card == 13:
                #print()
                print("Your card is a KING!")
                player_hand += 10
                print(f"Your hand is: {player_hand}")

            # if the player hand is equal to 21
            # player automatically wins
            # a new game is started
            # player wins increases by 1
            if player_hand == 21:
                #print()
                print("BLACKJACK! You win!")
                print()
                no_winner = False
                player_wins += 1

            # if the player hand is greater than 21
            # player automatically loses
            # new game started
            # dealer wins increases by 1
            elif player_hand > 21:
                print()
                print("You exceeded 21! You lose.")
                print()
                no_winner = False
                deals_wins += 1
        # if the user choice is 2
        elif user_choice == 2:
            # deals a card to the dealers hand
            dealer_hand = rng.next_int(11) + 16
            # prints dealer and player hand
            print(f"Dealer's hand: {dealer_hand}")
            print(f"Your hand is: {player_hand}")
            print()

            # checks to see if player hand is greater than dealer hand
            # prints "you win" and sets no winner to false
            # also increases the number of player wins by 1
            # sets no_winner to false
            if player_hand > dealer_hand:
                print("You win!")
                print()
                no_winner = False
                player_wins += 1

            # checks to see if the dealer hand is greater than 21
            # if true prints "you win"
            # increases the number of player wins by 1
            # sets no_winner to false
            elif dealer_hand > 21:
                print("You win!")
                print()
                no_winner = False
                player_wins += 1

            # checks to see if the dealer hand is greater than the player hand
            # deal wins increases by 1
            # sets no_winner to false
            # dealer wins
            # increases number of dealer wins by one
            elif dealer_hand > player_hand:
                print("Dealer wins!")
                print()
                no_winner = False
                deals_wins += 1

            # this is a tie
            # increases number of times by 1
            elif dealer_hand == player_hand:
                print("It's a tie! No one wins!")
                print()
                no_winner = False
                num_ties += 1

            # prints out the stats from the game
        elif user_choice == 3:
            print()
            print(f"Number of Player wins: {player_wins}")
            print(f"Number of Dealer wins: {deals_wins}")
            print(f"Number of tie games: {num_ties}")
            print(f"Total # of games played is: {game_num-1}")
            print(f"Percentage of Player wins: {round((player_wins / (game_num-1))*100, 1)}%")

            # exits the program
        elif user_choice == 4:
            no_winner = False
            game_continue = False

        # if the user_choice isn't 1-4
        # sets the game continue to be true
        elif (not (not (user_choice != 1) and not 2) or 3 or 4):
            print("Invalid input!")
            print("Please enter an integer value between 1 and 4.")

            game_continue = True

        # sets the player hand to 0
        # stops the game
        else:
            player_hand = 0
            no_winner = True
