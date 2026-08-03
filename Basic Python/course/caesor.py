def caesar(text, shift, encrypt=True):
    # 1. Validation: Shift integer hunu parchha
    if not isinstance(shift, int):
        return 'Shift must be an integer value'
    
    # 2. Validation: Shift 1 dekhi 25 ko bhitra hunu parchha
    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25'

    # 3. Handle Decryption: encrypt False chha bhane shift lai ulto banaune
    if not encrypt:
        shift = -shift

    # 4. Alphabet mapping setup
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    
    # Capital ra Small letters dubai ko lagi translation table
    translation_table = str.maketrans(
        alphabet + alphabet.upper(), 
        shifted_alphabet + shifted_alphabet.upper()
    )
    
    return text.translate(translation_table)

# 5. Helper function for Encryption
def encrypt(text, shift):
    return caesar(text, shift)

# 6. Helper function for Decryption
def decrypt(text, shift):
    return caesar(text, shift, False)

# --- Final Testing ---

# Encrypted message jaslai decrypt garnu chha
encrypted_text = 'Pbhentr vf sbhaq va hayvxryl cynprf.'

# Decryption process call gareko (shift 13 use garera)
decrypted_text = decrypt(encrypted_text, 13)

# Terminal ma result print garne
print(decrypted_text)