def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            base = 65 if char.isupper() else 97
            result += chr((ord(char) + shift - base) % 26 + base)
        else:
            result += char
    return result

message = input("Enter message: ")
shift_amount = int(input("Enter shift: "))
print("Encrypted:", caesar_cipher(message, shift_amount))
