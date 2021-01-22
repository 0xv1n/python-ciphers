# Author: Gabriel De Jesus

def main():
    # generate base matrix for vigenere cipher
    BASE_ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    print('This is the Base Vigenere Cipher Alphabet Matrix:')
    for i in range(0,len(BASE_ALPH)):
        for j in range(0,len(BASE_ALPH)):
            # each iteration, we need to shift the base alphabet by 1
            # we can conveniently repurpose code I wrote for the caesar cipher
            print(BASE_ALPH[(BASE_ALPH.index(BASE_ALPH[j]) + i) % 26], end="")
        print()

    # Define a Key and the Message Plaintext (for testing)
    # Eventually, take Key in as script arg, and message parsed from text file.
    BASE_KEY = 'TAMPA'
    PLAINTEXT = 'This message is encrypted using the Vigenere Cipher.'

    # We need to Repeat the Key to match the length of the plaintext
    #   e.g. TAMPATAMPATA ... until the key reaches "KEY_LEN" in size.
    BASE_KEY_LEN = len(BASE_KEY)
    KEY_LEN = len(PLAINTEXT)
    # expandedKey = ''
    key_index = 0
    print('\nThis is our expanded cipher key:')
    for i in range(0,KEY_LEN):
        for j in range(0,BASE_KEY_LEN):
            if key_index < KEY_LEN:
                print(BASE_KEY[j], end="")
                key_index += 1
            else:
                return
    # In order to encrypt the plaintext, we need to first get the Row index based on the current position within the key
    # then we need to get the column index of the plaintext letter.
    #
    #   e.g. Second letter of Key is 'A', and Second Letter of Plaintext is 'H', so Arr[A][H] would be the Encrypted Character
    #       which in this case would be 'H', so H -> H in this case.
    #
    #       Third letter of Key is 'M', Third Letter of Plaintext is 'I', so Arr[M][I] would be the Encrypted Char, I -> U
    #   And So on.
    # Eventually, our encrypted message will be: Mhuh mxsepgx ie tnvrketxd ghigg fwe Oistnxrq Riihqg.
if __name__ == "__main__":
    main()
