

class DealerAI():
    def __init__(self,dealer_score):
        self._dealer_score = dealer_score # Need to know what is the dealer score for playing

    @property
    def dealer_score(self):
        return self._dealer_score

    @dealer_score.setter
    def dealer_score(self,value):
        self._dealer_score = value

    ########
    #This is the Mind of the Dealer
    #Will decide if to hit or not
    ########
    def is_hit(self):
        if int(self._dealer_score) > 17:
            return False
        else:
            return True
