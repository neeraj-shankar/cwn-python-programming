alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']

text = input("Type your message: \n").lower()
print(f"Input Message {text}")
text_list = []
shift = int(input("Type the shift number:\n"))
total_length = len(alphabet)
def encrypt(plain_text, shift_amount):
    cypher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        if position >= len(alphabet)-shift_amount:
            new_position = position - len(alphabet)+shift_amount
            print(f"when new position is greater than list {new_position}")
        else:
            new_position = position +shift_amount
            print(f"new position {new_position}")
        new_letter = alphabet[new_position]
        cypher_text += new_letter
    print(f"The cypher text {cypher_text}")

def decrypt(encrypted_text, shift_amount):
    decrypted_text = ""
    for letter in encrypted_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        new_letter = alphabet[new_position]
        decrypted_text += new_letter
    print(f"The cypher text {decrypted_text}")

# calling the function
direction = input("Type 'encode' to encrypt, type 'decode' to decode. \n")
if direction == 'encode':
    encrypt(text, shift)

elif direction == 'decode':
    decrypt(encrypted_text=text, shift_amount=shift)
else:
    print(f"Chosen Option does not exists")