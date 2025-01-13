alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']




def ceaser(original_text, shift_amount, encode_or_decode):
    cipher_text = ""
    if direction == 'decode':
        shift_amount *= -1
    for x in original_text:
        shifted_amount = alphabet.index(x) + shift_amount
        shifted_amount = shifted_amount%len(alphabet)
        cipher_text += alphabet[shifted_amount]
    print(f"The {encode_or_decode}d text is {cipher_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrpyt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(original_text=text, shift_amount=shift, encode_or_decode=direction)

    yes_or_no = input("Type 'yes' to run again and 'no' to stop.").lower()
    if yes_or_no == 'no':
        should_continue = False
        print("Goodbye")
