def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Would you like to (e)ncrypt or (d)ecrypt a message? ")
        message = input("Enter your message: ")
        shift = int(input("Enter the shift value(an integer): "))

        if choice.lower() == 'e':
            encrypted_message = encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice.lower() == 'd':
            decrypted_message = decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")
        else:
            print("Invalid choice. Please choose 'e' to encrypt or 'd' to decrypt.")

        another = input("Do you want to encrypt or decrypt another message? (yes/no): ")
        if another.lower() != 'yes':
            print("Thank you for using the Caesar Cipher program!")
            break

if __name__ == "__main__":
    main()
