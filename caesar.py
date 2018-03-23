from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    new_text = ""
    for char in text:
        new_text = new_text + rotate_character(char, rot)
    return new_text

def main():
    from sys import argv, exit
    if len(argv) != 2 or not argv[1].isdigit():
        print("usage: python caesar.py n")
        exit() 
    text = input("Type a message:\n")
    rot = int(argv[1])
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()