class Player():
    def __init__(self, name):
        self.name = name
        self.strikes = 0
        # Best of 3 mode - not implemented
        self.wins = 0
        
    def show_strikes(self):
        return self.strikes
    
    def add_strike(self):
        self.strikes += 1
    
    def win(self):
        #self.wins += 1
        print(f"\n{self.name} WINS!!!\n")  