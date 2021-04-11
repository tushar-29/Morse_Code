MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-', " ": '|'}


def head(error_message=""):
    print(error_message, end="")
    print("MORSE CODE ENCODE AND DECODE")
    choice = input("Enter 1 to Encode the normal String  or 2 to Decode Morse Code (0 for EXIT) : ")
    choice = choice.strip(" ")
    if not choice.isdigit():
        message = "ERROR : Incorrect Input, Enter the Numeric value \n"
        head(message)
    else:
        choice = int(choice)
        return choice


def encode(error_message=""):
    print(error_message)
    encode_input = input("Enter the String to be converted : ")
    excape_charter = "!@#$%^&*()~`_+-=<>?/.,\":';}{]["
    encode_output = ""
    if excape_charter in encode_input:
        message = "ERROR: Wrong Character is Entered (only ',' '.' '/' '?' '-' '(' ')' are allowed)\n\t" \
                  "Try Again\n"
        encode(message)
    for i in encode_input:
        if i != " ":
            # one space seperating letters
            encode_output += MORSE_CODE_DICT[i.upper()] + " "
        else:
            # two space for seperating words
            encode_output += MORSE_CODE_DICT[" "] + " "
    return encode_output


def get_key(val):
    for key, value in MORSE_CODE_DICT.items():
        if val == value:
            return key
    else:
        print(f"INCORRECT MORSE CODE : {val}\n")
        return False


def decode(error_message=""):
    print(error_message)
    decode_input = input("Enter the Morse Code to decode : ").strip().split(" ")
    decode_output = ""
    for i in decode_input:
        if i != '|':
            val = get_key(i)
            if not val:
                decode()
            decode_output += get_key(i)
        else:
            decode_output += " "
    return decode_output


class Morse:
    def body(self):
        option_selected = head()
        if option_selected == 1:
            encoded_output = encode()
            print(f"Encode Morse Code is : \n\t{encoded_output}\n")
            input("'press enter to go back'")
            self.body()
        elif option_selected == 2:
            decoded_output = decode()
            print(f"Decode Morse Code is : \n\t{decoded_output}\n")
            input("'press enter to go back'")
            self.body()
        elif option_selected == 0:
            exit(1)
        else:
            print("ERROR: Wrong Input has been given\n")
            self.body()


if __name__ == '__main__':
    converter = Morse()
    converter.body()
