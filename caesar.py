def alphabet_position(letter):
    low_list = "abcdefghijklmnopqrstuvwxyz"
    up_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letter.isalpha():
        if letter.islower():
            return low_list.find(letter)
        elif letter.isupper():
            return up_list.find(letter)


def rotate_character(char, rot):
    low_list = "abcdefghijklmnopqrstuvwxyz"
    up_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if char.isalpha():
        char_val = (alphabet_position(char) + rot) % 26
        if char.islower():
            return low_list[char_val]
        elif char.isupper():
            return up_list[char_val]
    else:
        return char


def encrypt(text, rot):
    new_text = ""
    for letter in text:
        new_letter = rotate_character(letter, rot)
        new_text = new_text + new_letter
    return new_text
