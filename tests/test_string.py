import encryptionSystem

key = "HALLO"

text_to_encrypt = "I'm Jonas"
print("RAW Text: " + text_to_encrypt)

encrypted = encryptionSystem.encrypt(text_to_encrypt, key)
print("Encrypted Text: " + encrypted)

decrypted_wrong = encryptionSystem.decrypt(encrypted, "asdasd")
print("Decrypted Text with wrong key: " + decrypted_wrong)

decrypted_correct = encryptionSystem.decrypt(encrypted, key)
print("Decrypted Text with correct key: " + decrypted_correct)
