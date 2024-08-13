def encrypt(text, shift):
    result = ""

    for char in text:
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
    while True:
        choice = input("Do you want to (E)ncrypt, (D)ecrypt, or (Q)uit? ").strip().upper()
        if choice == 'Q':
            print("Goodbye!")
            break
        elif choice not in ['E', 'D']:
            print("Invalid choice. Please choose 'E' for encryption, 'D' for decryption, or 'Q' to quit.")
            continue

        text = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'E':
            encrypted_text = encrypt(text, shift)
            print(f"Encrypted message: {encrypted_text}")
        else:
            decrypted_text = decrypt(text, shift)
            print(f"Decrypted message: {decrypted_text}")


if __name__ == "__main__":
    main()
