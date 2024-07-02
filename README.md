# pass-gen
 - Generates a random password with specified number of letters, symbols, and numbers. - Encrypts the generated password using a substitution cipher if requested. - Saves the generated password and optional encrypted password to a JSON file along with other metadata like category and website.
# Password Generator and Cipher

This Python script generates a random password based on user specifications and optionally encrypts it using a simple substitution cipher.

## Features

- Generates a random password with specified number of letters, symbols, and numbers.
- Encrypts the generated password using a substitution cipher if requested.
- Saves the generated password and optional encrypted password to a JSON file along with other metadata like category and website.

## How to Use

1. **Setup:**
   - Make sure you have Python 3 installed on your system.
   - Clone or download the repository to your local machine.

2. **Running the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory where the script (`password_generator.py`) is located.

3. **Execution:**
   - Run the script using Python:
     ```bash
     python password_generator.py
     ```
   - Follow the prompts to specify the number of letters, symbols, and numbers for the password, and provide additional details like password category and website.

4. **Encryption (Optional):**
   - You can choose to encrypt the generated password using a substitution cipher.
   - Enter 'y' when prompted if you want to encrypt the password.
   - Choose whether to 'encode' or 'decode' the password and specify a shift number.

5. **Saving Data:**
   - After generating or encrypting the password, the script saves the data to a JSON file (`data.json`) in the same directory.
   - The JSON file includes details such as password category, website, generated password, and optionally the encrypted password.

## Example Usage

Here's an example scenario using the script:

- User inputs:
  - 10 letters, 3 symbols, 2 numbers for the password.
  - Password category: Personal
  - Website: example.com
- The script generates a password, allows the user to encrypt it if desired, and saves all relevant information to `data.json`.

## Notes

- This script is intended for educational purposes and should not be used for securing sensitive information without further enhancements (e.g., stronger encryption methods).

## License

This project is licensed under the MIT License - see the LICENSE file for details.
