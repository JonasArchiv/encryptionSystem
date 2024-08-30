import string
import random
import os
from encryptionSystem.encryptionSystem import encrypt, decrypt


def generate_random_key(length=16):
    return ''.join(random.choices(string.ascii_uppercase + string.digits + string.punctuation, k=length))


def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)


def main():
    print("Encryption/Decryption Tool by JonasHeilig")
    print("1. Encrypt text")
    print("2. Decrypt text")
    print("3. Encrypt text from a file")
    print("4. Decrypt text from a file")
    choice = input("Please select an option: ").strip()

    if choice not in ['1', '2', '3', '4']:
        print("Invalid option.")
        return

    if choice in ['1', '3']:
        print("Encryption key options:")
        print("1. Own key")
        print("2. Random key")
        key_choice = input("Please select an option: ").strip()

        if key_choice == '1':
            key = input("Enter the encryption key: ").strip()
        elif key_choice == '2':
            key = generate_random_key()
            print(f"Your generated key: {key}")
        else:
            print("Invalid option.")
            return

        if choice == '1':
            text = input("Enter the text to encrypt: ").strip()
            encrypted_text = encrypt(text, key)
            print(f"Encrypted text: {encrypted_text}")

        elif choice == '3':
            input_file_path = input("Enter the path to the text file: ").strip()
            if not os.path.isfile(input_file_path):
                print("File does not exist.")
                return
            text = read_file(input_file_path)
            encrypted_text = encrypt(text, key)
            print(f"Encrypted text: {encrypted_text}")

            save_choice = input("Save encrypted text to file (y/n)? ").strip().lower()
            if save_choice == 'y':
                output_file_path = input("Enter the path to save the encrypted text: ").strip()
                write_file(output_file_path, encrypted_text)
                print(f"Encrypted text saved to {output_file_path}")

    elif choice in ['2', '4']:
        key = input("Enter the decryption key: ").strip()
        if not key:
            print("Key is required.")
            return

        if choice == '2':
            text = input("Enter the text to decrypt: ").strip()
            decrypted_text = decrypt(text, key)
            print(f"Decrypted text: {decrypted_text}")

        elif choice == '4':
            input_file_path = input("Enter the path to the text file: ").strip()
            if not os.path.isfile(input_file_path):
                print("File does not exist.")
                return
            text = read_file(input_file_path)
            decrypted_text = decrypt(text, key)
            print(f"Decrypted text: {decrypted_text}")

            save_choice = input("Save decrypted text to file (y/n)? ").strip().lower()
            if save_choice == 'y':
                output_file_path = input("Enter the path to save the decrypted text: ").strip()
                write_file(output_file_path, decrypted_text)
                print(f"Decrypted text saved to {output_file_path}")


if __name__ == "__main__":
    main()
