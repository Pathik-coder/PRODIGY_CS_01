def caesar_cipher(text, shift, mode):
    result = ""

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char   # keep spaces & symbols

    return result


print("Caesar Cipher Program")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice (1 or 2): ")
message = input("Enter message: ")
shift = int(input("Enter shift value: "))

if choice == "1":
    print("Encrypted Message:", caesar_cipher(message, shift, "encrypt"))

elif choice == "2":
    print("Decrypted Message:", caesar_cipher(message, shift, "decrypt"))

else:
    print("Invalid choice")
