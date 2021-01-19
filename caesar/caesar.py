# Implementation of traditional 3 shift Caesar cipher
# Author: Gabriel De Jesus

import sys, getopt

def main(argv):
    inputfile = ''
    try:
        opts, args = getopt.getopt(argv, "p:c:", ["ifile="])
    except getopt.GetoptError:
        print ('caesar.py -p <plaintextfile> or caesar.py -c <ciphertextfile>')
        sys.exit(2)
    for opt, arg in opts:
        high_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        low_alphabet = high_alphabet.lower()
        shift = 3
        inputfile = arg
        # encrypt plaintext with caesar
        if opt == '-p':
            f = open(inputfile, 'r')
            plaintext = f.read()
            f.close()
            crypt = []
            with open(inputfile, 'r') as f:
                for c in f.read():
                    if c.strip() and c in low_alphabet:
                        crypt.append(low_alphabet[(low_alphabet.index(c) + shift) % 26])
                    elif c.strip() and c in high_alphabet:
                        crypt.append(high_alphabet[(high_alphabet.index(c) + shift) % 26])
                    else:
                        crypt.append(c)
                f.close()
            message = ''.join(crypt)
            print()
            print('Original Text: ' + plaintext)
            print('Encrypted: ' + message)
            sys.exit()
        # decrypt ciphertext
        if opt == '-c':
            f = open(inputfile, 'r')
            ciphertext = f.read()
            f.close()
            crypt = []
            with open(inputfile, 'r') as f:
                for c in f.read():
                    if c.strip() and c in low_alphabet:
                        crypt.append(low_alphabet[(low_alphabet.index(c) - shift) % 26])
                    elif c.strip() and c in high_alphabet:
                        crypt.append(high_alphabet[(high_alphabet.index(c) - shift) % 26])
                    else:
                        crypt.append(c)
                f.close()
            message = ''.join(crypt)
            print()
            print('Original Text: ' + ciphertext)
            print('Decrypted: ' + message)
            sys.exit()

if __name__ == "__main__":
    main(sys.argv[1:])
