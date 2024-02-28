import string
az = string.ascii_uppercase
strings = []

def main():
    # Ask for cipher input
    cipher = input("Please input the code: ").upper()
    shift_letters(cipher)


def shift_letters(cipher):
    #loop through each letter shifting it in the alphabet x places
    #starting at 0 places and incrementing up to length of alphabet
    #
    places_to_shift = 0

    while places_to_shift <= len(az):
        broken_cipher = ''

        for letter in cipher:
            #checks for a space, ignores if so
            if letter !=' ' :
                new_char = az[az.index(letter)-places_to_shift] 
                broken_cipher += new_char
            else:
                broken_cipher += ' '
        strings.append(broken_cipher)
        places_to_shift += 1
    

# Check if this script is being run directly
if __name__ == "__main__":
    main()