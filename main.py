from tkinter import *
from design import *
from card import Card, collect_cards
from deal import Deal


root = Tk()
root.geometry('1280x720')
root.title('JimShapedCasino - Blackjack')
root.configure(bg = background_color)

#####
#UI Frames
####

#Player:
player_frame = Frame(root, bg = background_color, ** hightlight_frame_with_white )
player_frame.pack(side = BOTTOM, fill = X)

player_cards_frame = Frame(player_frame, bg = background_color)
player_cards_frame.pack(side = RIGHT, fill = Y)

player_options_frame = Frame(player_frame,bg = background_color)
player_options_frame.pack(**pack_left_and_fill_y)



#Dealer:
dealer_frame = Frame(root, bg = background_color, **hightlight_frame_with_white)
dealer_frame.pack(side = TOP,fill = X)

dealer_cards_frame = Frame(dealer_frame, bg = background_color)
dealer_cards_frame.pack(side = TOP, fill = Y)


#Score Board:
scoreboard = Frame(root, bg = background_color, **hightlight_frame_with_white)
scoreboard.pack(side = LEFT, fill = Y)

dealer_score = Frame(scoreboard,bg = background_color)
dealer_score.pack(side = TOP, fill = BOTH)

player_score = Frame(scoreboard,bg = background_color)
player_score.pack(side = BOTTOM, fill = BOTH)


player_score_label = Label(player_score, bg = background_color, text = 'Player Score: ', **button_args)
player_score_label.pack()

dealer_score_label = Label(dealer_score, bg = background_color, text = "Dealer Score: ", **button_args)
dealer_score_label.pack()
#Score Board END

#player options in the game:
deal = Button(player_options_frame, text = 'DEAL', **button_args, bg = "#34CA3A")
deal.pack(**pack_left_and_fill_y)


player_game_options_frame = Frame(player_options_frame, bg = background_color)
player_game_options_frame.pack(**pack_left_and_fill_y)


#player options in the deal:
hit     = Button(player_game_options_frame, text = 'HIT', bg = '#FF3300', **button_args, state = DISABLED, name = 'hit')
stand   = Button(player_game_options_frame, text = 'STAND', bg = '#B5BD18', **button_args, state = DISABLED, name = 'stand')
double  = Button(player_game_options_frame, text = 'DOUBLE', bg = '#CC00CC', **button_args, state = DISABLED, name = 'double')
split   = Button(player_game_options_frame, text = 'SPLIT', bg = '#66FFFF', **button_args,state = DISABLED, name = 'split')

hit.pack(side = TOP, fill = X)
stand.pack(side = TOP, fill = X)
double.pack(side = TOP, fill = X)
split.pack(side = TOP, fill = X)

#player options END

#Player Cards:
#Set their images:

#PLAYER:
player_card1_image = Card.hidden_card()
player_card1_label = Label(player_cards_frame, image = player_card1_image, bg = background_color,name = 'dealcard1_player')
player_card1_label.pack(side = RIGHT)

player_card2_image = Card.hidden_card()
player_card2_label = Label(player_cards_frame, image = player_card2_image, bg = background_color,name = 'dealcard2_player')
player_card2_label.pack(side = RIGHT)

#DEALER:
dealer_card1_image = Card.hidden_card()
dealer_card1_label = Label(dealer_cards_frame, image = dealer_card1_image, bg = background_color,name = 'dealcard1_dealer')
dealer_card1_label.pack(side = LEFT)

dealer_card2_image = Card.hidden_card()
dealer_card2_label = Label(dealer_cards_frame, image = dealer_card2_image, bg = background_color,name = 'dealcard2_dealer')
dealer_card2_label.pack(side = LEFT)

#Busted Text:
player_busted_message = Label(player_cards_frame, text = 'BUSTED', font = font_medium, fg = '#FF0000', bg = background_color)
dealer_busted_message = Label(dealer_cards_frame, text = 'BUSTED', font = font_medium, fg = '#FF0000', bg = background_color)



#Table Frame for displaying result of the deal (WON OR LOST)
deal_results_frame = Frame(root, bg = background_color)
deal_results_frame.pack(fill = BOTH,side = LEFT)


#Deal a game:
def deal_init():
    ########
    #Clean player frame from the hit cards:
    Deal.clean_table(frames = [player_cards_frame,dealer_cards_frame,deal_results_frame])
    ########

    ########
    #Initialize Card Instances so this way i will have a new deck each time deal is pressed
    cards_instances = []
    for card in collect_cards():
        cards_instances.append(Card(name = card)) # (Card instance)
        print(f'{card} added to deck')
    ########


    #Initialize Game:
    game  = Deal(
        deck = cards_instances,
        master = root,
        player_cards_frame = player_cards_frame,
        player_game_options_frame = player_game_options_frame,
        player_card1_label = player_card1_label,
        player_card2_label = player_card2_label,
        dealer_card1_label = dealer_card1_label,
        dealer_card2_label = dealer_card2_label,
        player_score_label = player_score_label,
        dealer_score_label = dealer_score_label,
        dealer_cards_frame = dealer_cards_frame,
        deal_results_frame = deal_results_frame,
        player_busted_message = player_busted_message,
        dealer_busted_message = dealer_busted_message,
        split = split
    )

    # Starting operations in real game:

    #deal player:
    game.deal_player()


    #deal for dealer:
    #handle all dealt cards for dealer for here so we can keep one undisplayed
    dealer_1 = game.get_card(dealer_card1_label, is_player = False)
    dealer_2 = game.get_card(dealer_card2_label, is_player = False, display=False)

    #fill the score board:
    game.set_scoreboard()

    #See if split should be disabled or enabled:
    game.set_split_button_state()


    #Set the Buttons click function <Button-1> Stand for left click
    hit.bind('<Button-1>', lambda event: game.hit(dealer_2))
    stand.bind('<Button-1>', lambda event: game.finish_player_turn(dealer_2))



deal.bind('<Button-1>', lambda event: deal_init())
root.mainloop()