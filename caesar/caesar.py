# Caesar Cipher
# Author: Gabriel De Jesus
# Usage:
#   -s <#> to specify shift amount
#   -p <fileName> to specify plaintext file to encrypt
#   -c <fileName> to specify ciphertext to decrypt
#
#   example: `python caesar.py -s 3 -p samplefile.txt`

import sys, getopt

def main(argv):
    inputfile = ''
    shift = 3
    try:
        opts, args = getopt.getopt(argv, "s:p:c:")
    except getopt.GetoptError:
        print ('caesar.py -p <plaintextfile> or caesar.py -c <ciphertextfile>')
        sys.exit(2)
    for opt, arg in opts:
        crypt = []
        # if user specifies shift amount, we'll use it, else we default to 3 character shift
        if opt == '-s':
            shift = int(arg)
        elif opt == '-p':
            inputfile = arg
            with open(inputfile, 'r') as f:
                orig = f.read()
                f.seek(0)
                for c in f.read():
                    cryptor(c,'encrypt',crypt,shift)
                f.close()
            message = ''.join(crypt)
            output(orig,message,'enc')
        # decrypt ciphertext
        elif opt == '-c':
            inputfile = arg
            with open(inputfile, 'r') as f:
                orig = f.read()
                f.seek(0)
                for c in f.read():
                    cryptor(c,'decrypt',crypt,shift)
                f.close()
            message = ''.join(crypt)
            output(orig,message,'dec')

def cryptor(ch,func,msg,shamt):
    high_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    low_alphabet = high_alphabet.lower()
    if func == 'encrypt':
        if ch.strip() and ch in low_alphabet:
            msg.append(low_alphabet[(low_alphabet.index(ch) + shamt) % 26])
        elif ch.strip() and ch in high_alphabet:
            msg.append(high_alphabet[(high_alphabet.index(ch) + shamt) % 26])
        else:
            msg.append(ch)
    elif func == 'decrypt':
        if ch.strip() and ch in low_alphabet:
            msg.append(low_alphabet[(low_alphabet.index(ch) - shamt) % 26])
        elif ch.strip() and ch in high_alphabet:
            msg.append(high_alphabet[(high_alphabet.index(ch) - shamt) % 26])
        else:
            msg.append(ch)
    return

def output(orig,out,type):
    if type == 'enc':
        tx_t = 'En'
    elif type == 'dec':
        tx_t = 'De'
    print(f"{'Original Text:':<20}{orig:<40}")
    print(f"{'{}crypted Text:'.format(tx_t):<20}{out:<40}")
    pass

if __name__ == "__main__":
    main(sys.argv[1:])
