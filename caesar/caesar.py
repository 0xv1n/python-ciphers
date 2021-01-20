# Caesar Cipher
# Author: Gabriel De Jesus
# Usage:
#   -s <#> to specify shift amount
#   -p <fileName> to specify plaintext file to encrypt
#   -c <fileName> to specify ciphertext to decrypt
#
#   example: `python caesar.py -s 3 -e -f sampletext.txt`
#       will encrypt sampletext.txt with 3 character shift

import sys, getopt

def main(argv):
    inputfile = ''
    func = ''
    shift = 3
    try:
        opts, args = getopt.getopt(argv, "hs:edf:")
    except getopt.GetoptError:
        print ('caesar.py -h for help using this script')
        sys.exit(2)
    for opt, arg in opts:
        crypt = []
        if opt == '-h':
            print('Usage: caesar.py -s <#> -e/-d -f <filename> \n-s <#>: specify shift amount\n-e: encrypt\n-d: decrypt')
        # if user specifies shift amount, we'll use it, else we default to 3 character shift
        elif opt == '-s':
            shift = int(arg)
        elif opt == '-e':
            func = 'En'
        elif opt == '-d':
            func = 'De'
        elif opt == '-f':
            inputfile = arg
            with open(inputfile, 'r') as f:
                orig = f.read()
                orig = orig.upper()
                f.seek(0)
                for c in orig:
                    cryptor(c,func,crypt,shift)
                f.close()
            message = ''.join(crypt)
            output(orig,message,func)

def cryptor(ch,func,msg,shamt):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if func == 'En':
        if ch.strip() and ch in alphabet:
            msg.append(alphabet[(alphabet.index(ch) + shamt) % 26])
        else:
            msg.append(ch)
    elif func == 'De':
        if ch.strip() and ch in alphabet:
            msg.append(alphabet[(alphabet.index(ch) - shamt) % 26])
        else:
            msg.append(ch)
    return

def output(orig,out,func):
    print(f"{'Original Text:':<20}{orig:<40}")
    print(f"{'{}crypted Text:'.format(func):<20}{out:<40}")

if __name__ == "__main__":
    main(sys.argv[1:])
