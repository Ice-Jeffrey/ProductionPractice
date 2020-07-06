def main():
    new_string = ''
    string = input()
    for letter in string:
        if ord(letter) >= 65 and ord(letter) < 91:
            new_string += chr((ord(letter) + 4 - 65) % 26 + 65)
        elif ord(letter) >= 97 and ord(letter) < 123:
            new_string += chr((ord(letter) + 4 - 97) % 26 + 97)
        
    print(new_string)

if __name__ == "__main__":
    main()