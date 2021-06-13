import random
import string
from itertools import cycle

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
        print(f"{self.name} WINS!!!")
        
p1 = Player('p1')
p2 = Player('p2')

def declare_winner(p):
    p.win()

def invalid_character(letter):
    # Player enters more than one letter.
    if len(letter) != 1:
        return True
    
    # Player enters non-alphabetical character.
    elif letter not in string.ascii_lowercase:
        return True
    
    return False
    
def validate_letter(letter, string_1):
    # Create current sequence.
    string_1 = string_1 + letter
    
    # There aren't any words in the dictionary that start with the given sequence. Using set instead of list.
    if len({word for word in word_dict[string_1[0]] if word.startswith(string_1)}) == 0:
        return False
    
    # Validation complete.
    return True

def setup():
    #39143 words
    with open("wordlist_kevin_atkinson.txt") as f:
        lst = [line.rstrip() for line in f]
    a_list = [letter for letter in string.ascii_lowercase]
    word_dict = dict.fromkeys(a_list, set())
    for k,_ in word_dict.items():
        word_dict[k] = {elem for elem in lst if elem.startswith(k)}
    return word_dict

if __name__ == "__main__":
    word_dict = setup()
    print("Welcome to GHOST: The Word Game!")    
    game_on = True
    letter_seq = ''
    # Determine start order
    starter = random.choice([p1,p2])
    if starter.name == 'p1':
        player_pool = cycle([p1, p2])
    else:
        player_pool = cycle([p2, p1])

    while game_on:
        for player in player_pool:
            next_letter = input(f"{player.name} enter the next letter: ").lower()
            # no turn loss.
            while invalid_character(next_letter):
                print(f"'{next_letter}' is invalid. Try again!")
                next_letter = input(f"{player.name} enter the next letter: ").lower()
                
            if validate_letter(next_letter, letter_seq):
                letter_seq = letter_seq+next_letter
                wordset = {word for word in word_dict[letter_seq[0]] if word.startswith(letter_seq)}

                if len(letter_seq) > 3 and letter_seq in wordset:
                    # The other player is the winner.
                    declare_winner(next(player_pool))
                    game_on = False
                    break  
            else:
                player.add_strike()
                if player.show_strikes() == 3:
                    print(f"Player {player.name} has {player.show_strikes()} strikes!")
                    # The other player is the winner.
                    declare_winner(next(player_pool))
                    game_on = False
                    break
                print(f"Player {player.name} has {player.show_strikes()} strike(s).")
                # Stay with same player (i.e. skip next player in line.)
                next(player_pool)