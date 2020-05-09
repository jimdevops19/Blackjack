from PIL import ImageTk, Image
import os
import random
import ctypes


cards_location = './images_demo/cards/'
hidden_card_location = './images_demo/hidden.png'

def collect_cards():
    cards = os.listdir(cards_location)

    cards = [card.split('.')[0] for card in cards]

    return cards


class Card():
    def __init__(self,name, value = 11, is_displayed = True):
        self.name = name #always will remain the same
        self._is_displayed = is_displayed #could be change during the program
        self._value = value # could be change only in ACE card

    @property
    def is_displayed(self):
        return self._is_displayed

    @is_displayed.setter
    def is_displayed(self, value):
        self._is_displayed = value

    @property
    def value(self):
        if str(self.name)[0] in ['J','Q','K']: # testing if the card is Queen,King,Jack
            self._value = 10
        elif str(self.name)[0] == 'A':
            pass # Overriding in the game it self
        else:
            self._value = int(self.name.split('-')[0]) # will return its own value 2 - 9
        return self._value


    @value.setter
    def value(self,value ):
        self._value = value

    #####
    #This will return hearts,spades and so on...
    #####
    def shape(self):
        return self.name.split('-')[1]

    #####
    #Created in order to pick a random card
    #####

    @staticmethod
    def random_card(instances):
        cards = instances
        random.shuffle(cards) # will shuffle the order of the cards so like real life ;)

        dealed_card = cards[0] # After shuffling just give the first card
        return dealed_card     # And return it

    ########
    # Created in order to get card image from main file
    ########
    @staticmethod
    def get_card_image(card):
        try:
            card_file_location = f"{cards_location}/{getattr(card,'name')}.png"
            card_image = Image.open(card_file_location)
            card_image_shaped = card_image.resize((159,225), Image.ANTIALIAS) # this will reshape the card because its actual size its huge!
            card_image = ImageTk.PhotoImage(card_image_shaped)

            return card_image

        except:
            ctypes.windll.user32.MessageBoxW(0,
                                             "Could not find cards. Missing images_demo folder with all the card images",
                                             "Cards Images are missing!", 1)

    @staticmethod
    def hidden_card():
        try:
            card_image = Image.open(hidden_card_location)
            card_image_shaped = card_image.resize((159,225), Image.ANTIALIAS) # this will reshape the card because its actual size its huge!
            card_image = ImageTk.PhotoImage(card_image_shaped)

            return card_image

        except:
            ctypes.windll.user32.MessageBoxW(0,
                                             "Could not find cards. Missing images_demo folder with all the card images",
                                             "Cards Images are missing!", 1)




