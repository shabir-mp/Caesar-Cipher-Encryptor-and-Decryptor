def encrypt(message, key):
    encrypted = ""
    for char in message:
        if char.isalpha():
            if char.islower():
                encrypted += chr((ord(char) - ord('a') + key) % 26 + ord('a'))
            else:
                encrypted += chr((ord(char) - ord('A') + key) % 26 + ord('A'))
        else:
            encrypted += char
    return encrypted

def decrypt(encrypted_message, key):
    decrypted = ""
    for char in encrypted_message:
        if char.isalpha():
            if char.islower():
                decrypted += chr((ord(char) - ord('a') - key) % 26 + ord('a'))
            else:
                decrypted += chr((ord(char) - ord('A') - key) % 26 + ord('A'))
        else:
            decrypted += char
    return decrypted

def main():
    print("Text Encrypt and Decrypt Converter - copyright @shabirmp")
    print()
    message = input("Enter the message: ")
    key = int(input("Enter the key (0-25): "))
    encrypted_message = encrypt(message, key)
    print("Encrypted message:", encrypted_message)
    decrypted_message = decrypt(encrypted_message, key)
    print("Decrypted message:", decrypted_message)

main()
