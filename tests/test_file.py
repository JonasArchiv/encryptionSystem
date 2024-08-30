import encryptionSystem

key = "HALLO"

input_file = "input.txt"
encrypted_file = "encrypted.txt"
wrong_file = "wrong.txt"
decrypted_file = "decrypted.txt"

with open(input_file, 'w', encoding='utf-8') as file:
    file.write("This is a test file. Let's encrypt and decrypt it!")

encryptionSystem.encrypt_file(input_file, encrypted_file, key)
print(f"Text in {input_file} was encrypted saved in {encrypted_file}")

with open(encrypted_file, 'r', encoding='utf-8') as file:
    encrypted_file_text = file.read()

print("Encrypted text:", encrypted_file_text)


encryptionSystem.decrypt_file(encrypted_file, wrong_file, "ddasdasd")
print(f"Encrypted text in {encrypted_file} was decrypted and saved in {wrong_file}.")

with open(wrong_file, 'r', encoding='utf-8') as file:
    wrong_decrypted_text = file.read()

print("Wrong decrypted Text:", wrong_decrypted_text)


encryptionSystem.decrypt_file(encrypted_file, decrypted_file, key)
print(f"Encrypted text in {encrypted_file} was decrypted and saved in {decrypted_file}.")

with open(decrypted_file, 'r', encoding='utf-8') as file:
    decrypted_text = file.read()

print("Decrypted Text:", decrypted_text)
