import sched


class PlaceBet():
    def __init__(self):
        self.bet = 0
        self.place = 0
        
    def set_bet(self, bet):
        self.bet = bet
        return self.bet
    
    def set_place(self, pl):
        self.place = pl
   
        return self.place
        
    