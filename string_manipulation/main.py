custom_input = input("Input Text to Encrypt / Decrypt \n")
custom_key = input("Input Key \n")
custom_dir = input("Input 1 to Encrypt / 2 to Decrypt \n")

def main(input, key, direction):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    key_index = 0
    final_message = ""
    for char in input.lower():
        if char in alphabet:
            key_char = key[key_index % len(key)]
            key_index += 1
            offset = alphabet.index(key_char)
            old_index = alphabet.index(char) # use index function here
            new_index = (old_index + offset * direction) % len(alphabet)
            final_message += alphabet[new_index]
        else:
            final_message += char
    return final_message

def encrypt(input, key):
    return main(input, key, 1)

def decrypt(input, key):
    return main(input, key, -1)

if custom_dir == "1":
    result = encrypt(custom_input, custom_key)
    print("\nEncrypted: " + result)
elif custom_dir == "2":
    result = decrypt(custom_input, custom_key)
    print("\nDecrypted: " + result)
else:
    print("Invalid Input, try again \n")
    quit()

print ("\nCustom Input: " + custom_input)
print("\nCustom Key: " + custom_key)