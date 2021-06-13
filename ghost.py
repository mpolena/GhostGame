import random, string
from itertools import cycle
from player import Player
from helpers import declare_winner, validate_letter, invalid_character

def setup():
    # Import valid words.
    with open("wordlist_kevin_atkinson.txt") as f:
        lst = [line.rstrip() for line in f]
    # Create list of keys from alphabet letters.
    a_list = [letter for letter in string.ascii_lowercase]
    word_dict = dict.fromkeys(a_list, set())
    # Populate dictionary with sets of words.
    for k,_ in word_dict.items():
        word_dict[k] = {elem for elem in lst if elem.startswith(k)}
    return word_dict

if __name__ == "__main__":
    
    p1 = Player('p1')
    p2 = Player('p2')
    
    word_dict = setup()
    print("\nWelcome to GHOST: The Word Game!\n")    
    letter_seq = ''
    # Determine start order
    starter = random.choice([p1,p2])
    if starter.name == 'p1':
        player_pool = cycle([p1, p2])
    else:
        player_pool = cycle([p2, p1])

    for player in player_pool:
        next_letter = input(f"{player.name} enter the next letter: ").lower()
        # Avoids loss of turn.
        while invalid_character(next_letter):
            print(f"'{next_letter}' is invalid. Try again!")
            next_letter = input(f"{player.name} enter the next letter: ").lower()
            
        if validate_letter(next_letter, letter_seq, word_dict):
            letter_seq = letter_seq+next_letter
            wordset = {word for word in word_dict[letter_seq[0]] if word.startswith(letter_seq)}

            if len(letter_seq) > 3 and letter_seq in wordset:
                # The other player is the winner.
                declare_winner(next(player_pool))
                break  
        else:
            player.add_strike()
            if player.show_strikes() == 3:
                print(f"Player {player.name} has {player.show_strikes()} strikes!")
                # The other player is the winner.
                declare_winner(next(player_pool))
                break
            print(f"Player {player.name} has {player.show_strikes()} strike(s).")
            # Enables continuation with same player.
            next(player_pool)