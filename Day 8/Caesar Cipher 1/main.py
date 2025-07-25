alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.
def encrypt(original_text, shift_amount):
    encrypted_message = ""
    for letter in original_text:
        # Check if letter is special character, if so, do not encrypt
        if not alphabet.count(letter):
            encrypted_message += letter
            continue
        current_index = alphabet.index(letter)
        new_index = current_index + shift_amount
        #Check if new index goes out of range
        if new_index > len(alphabet)-1:
            new_index = new_index % len(alphabet)
            encrypted_message += alphabet[new_index]
        else:
            encrypted_message += alphabet[new_index]
    print(encrypted_message)
# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.

# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

encrypt(text, shift)

