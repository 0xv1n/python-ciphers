# Author: Gabriel De Jesus

def main():
    # generate base matrix for vigenere cipher
    BASE_ALPH = r'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vigenere = []
    for r in range(0, len(BASE_ALPH)):
        vigenere.append([0 for c in range(0, len(BASE_ALPH))])

    for i in range(0,len(BASE_ALPH)):
        for j in range(0,len(BASE_ALPH)):
            # each iteration, we need to shift the base alphabet by 1
            # we can conveniently repurpose code I wrote for the caesar cipher
            vigenere[i][j] = BASE_ALPH[(BASE_ALPH.index(BASE_ALPH[j]) + i) % 26]
        print()

    # Define a Key and the Message Plaintext (for testing)
    # Eventually, take Key in as script arg, and message parsed from text file.
    BASE_KEY = r'TAMPA'
    PLAINTEXT = r'THIS MESSAGE IS ENCRYPTED USING THE VIGENERE CIPHER.'
    # Strip any punctuation or whitespace from the plaintext.
    PLAINTEXT_STRIP = ''.join(c for c in PLAINTEXT if c.isalnum())

    # We need to Repeat the Key to match the length of the plaintext
    #   e.g. TAMPATAMPATA ... until the key reaches "KEY_LEN" in size.
    BASE_KEY_LEN = len(BASE_KEY)
    KEY_LEN = len(PLAINTEXT_STRIP)
    keyIndex = 0
    expandedKey = ""
    for i in range(0,KEY_LEN):
        for j in range(0,BASE_KEY_LEN):
            if keyIndex < KEY_LEN:
                expandedKey += str(BASE_KEY[j])
                keyIndex += 1
    # In order to encrypt the plaintext, we need to first get the Row index based on the current position within the key
    # then we need to get the column index of the plaintext letter.
    #
    #   e.g. Second letter of Key is 'A', and Second Letter of Plaintext is 'H', so Arr[A][H] would be the Encrypted Character
    #       which in this case would be 'H', so H -> H in this case.
    #
    #       Third letter of Key is 'M', Third Letter of Plaintext is 'I', so Arr[M][I] would be the Encrypted Char, I -> U
    #   And So on.
    # Eventually, our encrypted message will be: Mhuh mxsepgx ie tnvrketxd ghigg fwe Oistnxrq Riihqg.
    encoded = ''
    for i in range(0,KEY_LEN):
        encoded += vigenere[BASE_ALPH.index(expandedKey[i])][BASE_ALPH.index(PLAINTEXT_STRIP[i])]
    print("Original Message:" + PLAINTEXT)
    print("Encoded Message: " + encoded)
if __name__ == "__main__":
    main()
