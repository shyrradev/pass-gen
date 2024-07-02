#!/usr/bin/env python3

import json
import random
import sys

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
alphabet = 'abcdefghijklmnopqrstuvwxyz'

print("Welcome to the PyPassword Generator!")
try:
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))
    pass_category = input("What kind of password is this? Social, business, or personal? ")
    website = input("What is the name of the website/app for which password is generated? ")
except ValueError:
    print("Error: Please enter valid integer values.")
    sys.exit(1) 

password_list = []

for _ in range(nr_letters):
    password_list.append(random.choice(letters))
for _ in range(nr_symbols):
    password_list.append(random.choice(symbols))
for _ in range(nr_numbers):
    password_list.append(random.choice(numbers))
    
random.shuffle(password_list)

password = ''.join(password_list)
print(f"The most secure password for your choice is: {password}")

def cipher(plain_text, shift_amount, direction):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = (position + shift_amount) % 26  # Wrap around using modulus
            elif direction == "decode":
                new_position = (position - shift_amount) % 26  # Wrap around using modulus
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter  # Preserve non-alphabet characters
    return cipher_text

cipher_password = input("Do you want to cipher your password and save it in the storage? (y/n): ").lower()
shift = 0
if cipher_password == 'y':
    while True:
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction in ["encode", "decode"]:
            shift = int(input("Type the shift number:\n"))
            break  # Exit the loop if input is valid
        else:
            print("Please input valid choice: 'encode' or 'decode'")

    encrypted_message = cipher(password, shift, direction)
    print(f"The {direction}d text is: {encrypted_message}")
elif cipher_password == 'n':
    sys.exit(1)
else:
    print("Please input valid choice: 'y' or 'n'")
    sys.exit(1)

data = {
    "category": pass_category,
    "password": password,
    "website": website,
}

if cipher_password == 'y':
    data["Ciphered_password"] = encrypted_message
    data["shift_number"] = shift

file_path = 'data.json'
with open(file_path, 'w') as file:
    json.dump(data, file, indent=4)

print(f"Data saved to {file_path}")
