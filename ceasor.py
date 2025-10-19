# Encryption part
def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

# Dedcryption part
def decrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = 65 if char.isupper() else 97
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

# Main program loop
while True:
    print("\nEncryption-Decryption Program")
    print("1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")
    
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a number (1-3).")
        continue

    if choice == 1:
        plain_text = input("Enter the plain text: ")
        try:
            key = int(input("Enter the key value: ")) % 26
        except ValueError:
            print("Invalid key. Must be an integer.")
            continue
        cipher_text = encrypt(plain_text, key)
        print("Cipher Text:", cipher_text)
    elif choice == 2:
        cipher_text = input("Enter the cipher text: ")
        try:
            key = int(input("Enter the key value: ")) % 26
        except ValueError:
            print("Invalid key. Must be an integer.")
            continue
        plain_text = decrypt(cipher_text, key)
        print("Decrypted Text:", plain_text)
    elif choice == 3:
        print("Exiting program...")
        break
    else:
        print("Invalid choice! Try again.")
