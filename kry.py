from collections import Counter

# Dekódovaný text ZP3
decoded_zp3 = "tjpuuzuuiuuleoibulii"

# 1. Caesarova šifra - vyzkoušíme posun od 1 do 25
def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

# Vyzkoušíme všechny posuny pro Caesarovu šifru
caesar_shifts = {shift: caesar_cipher(decoded_zp3, shift) for shift in range(1, 26)}

# 2. Frekvenční analýza
letter_frequencies = Counter(decoded_zp3)

# 3. Reverzní hledání běžných slov
common_words = ["the", "is", "this", "that", "crypto", "message", "cipher", "code", "text"]

# Výstupy
print(caesar_shifts, letter_frequencies)
