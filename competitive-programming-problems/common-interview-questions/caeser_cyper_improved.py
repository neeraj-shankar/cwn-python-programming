alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decode. \n")
text = input("Type your message: \n").lower()
shift = int(input("Type the shift number:\n"))
total_length = len(alphabet)
def caser_cipher(input_text, shift_amount):
    caeser_text = ""
    if direction == 'encode':
        for letter in input_text:
            position = alphabet.index(letter)
            if position >= len(alphabet)-shift_amount:
                new_position = position - len(alphabet)+shift_amount
            else:
                new_position = position +shift_amount
            new_letter = alphabet[new_position]
            caeser_text += new_letter
        print(f"The encrypted text is {caeser_text}")
    elif direction == 'decode':
        for letter in input_text:
            position = alphabet.index(letter)
            new_position = position - shift_amount
            new_letter = alphabet[new_position]
            caeser_text += new_letter
        print(f"The decrytpted text is {caeser_text}")
    else:
        print(f"Sorry! You selected wrong option.")

# calling the function
caser_cipher(input_text=text, shift_amount=shift)
