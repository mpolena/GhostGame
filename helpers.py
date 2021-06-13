import string

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
    
def validate_letter(letter, string_1, word_dict):
    # Create current sequence.
    string_1 = string_1 + letter
    
    # There aren't any words in the dictionary that start with the given sequence. Using set instead of list.
    if len({word for word in word_dict[string_1[0]] if word.startswith(string_1)}) == 0:
        return False
    
    # Validation complete.
    return True
