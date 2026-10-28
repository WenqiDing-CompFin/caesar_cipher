# caesar_cipher.py

def encrypt(text, shift):
    result = ""
    for char in text:
        if ('A' <= char <= 'Z') or ('a' <= char <= 'z'):  # 只移位 ASCII 英文字母
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)  # 解密就是加密反向操作

if __name__ == "__main__":
    message = "information security"
    shift_value = 3  # 移动位数
    encrypted = encrypt(message, shift_value)
    print("Encrypted:", encrypted)

    decrypted = decrypt(encrypted, shift_value)
    print("Decrypted:", decrypted)
