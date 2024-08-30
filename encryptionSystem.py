import string
import config


def create_matrix(key, shift=config.SHIFT):
    alphabet = string.ascii_uppercase
    extended_alphabet = alphabet + string.punctuation + string.digits + string.whitespace

    key = ''.join(sorted(set(key.upper()), key=lambda x: key.upper().index(x)))
    key += ''.join(sorted(set(extended_alphabet) - set(key), key=lambda x: extended_alphabet.index(x)))

    shifted_alphabet = extended_alphabet[shift:] + extended_alphabet[:shift]
    matrix = ''.join(shifted_alphabet[extended_alphabet.index(char)] for char in key)

    return matrix


def encrypt_block(block, matrix):
    extended_alphabet = string.ascii_uppercase + string.punctuation + string.digits + string.whitespace

    encrypted_block = ''.join(
        matrix[extended_alphabet.index(char)] if char in extended_alphabet else char for char in block)

    return encrypted_block


def decrypt_block(block, matrix):
    extended_alphabet = string.ascii_uppercase + string.punctuation + string.digits + string.whitespace
    reverse_matrix = ''.join(sorted(set(matrix), key=lambda x: matrix.index(x)))

    decrypted_block = ''.join(
        extended_alphabet[reverse_matrix.index(char)] if char in reverse_matrix else char for char in block)

    return decrypted_block


def encrypt(text, key):
    matrix = create_matrix(key)
    text = text.upper()
    block_size = config.BLOCK_SIZE
    padding = config.PADDING
    encrypted_text = ''

    for i in range(0, len(text), block_size):
        block = text[i:i + block_size].ljust(block_size, padding)
        encrypted_text += encrypt_block(block, matrix)

    return encrypted_text


def decrypt(text, key):
    matrix = create_matrix(key)
    block_size = config.BLOCK_SIZE
    padding = config.PADDING
    decrypted_text = ''

    for i in range(0, len(text), block_size):
        block = text[i:i + block_size]
        decrypted_text += decrypt_block(block, matrix)

    return decrypted_text.strip(padding)
