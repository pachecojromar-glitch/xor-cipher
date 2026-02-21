import random

def text_to_binary(text):
    binary = ""
    for char in text:
        binary += format(ord(char), '08b')
    return binary

def binary_to_text(binary):
    text = ""
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        text += chr(int(byte, 2))
    return text

def generate_key(length):
    key = ""
    for _ in range(length):
        key += random.choice(["0", "1"])
    return key

def xor_operation(data, key):
    result = ""
    for i in range(len(data)):
        if data[i] == key[i]:
            result += "0"
        else:
            result += "1"
    return result



if __name__ == "__main__":
    print("=== XOR Cipher Program ===")

    message = input("Enter your message: ")

    
    binary_message = text_to_binary(message)
    print("Binary message:", binary_message)


    key = generate_key(len(binary_message))
    print("Generated key:", key)

    encrypted = xor_operation(binary_message, key)
    print("Encrypted binary:", encrypted)

    decrypted_binary = xor_operation(encrypted, key)
    decrypted_message = binary_to_text(decrypted_binary)
    print("Decrypted message:", decrypted_message)