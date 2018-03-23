def alphabet_position(letter):
    letter = letter.upper()
    num_pos = ord(letter) - 65
    return num_pos

def rotate_character(char, rot):
    upper = True
    new_char_pos = 0
    new_char = ""    
    if char.isupper():
        upper = True
    elif char.islower():
        upper = False
    else:
        return char
    new_char_pos = (alphabet_position(char) + rot)%26+97
    new_char = new_char + chr(new_char_pos)
    if upper:
        return new_char.upper()
    else:
        return new_char