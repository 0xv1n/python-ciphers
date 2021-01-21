# Author: Gabriel De Jesus

def main():
    # generate base matrix for vigenere cipher
    BASE_ALPH = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(0,len(BASE_ALPH)):
        print()
        for j in range(0,len(BASE_ALPH)):
            # each iteration, we need to shift the base alphabet by 1
            # we can conveniently repurpose code I wrote for the caesar cipher
            print(BASE_ALPH[(BASE_ALPH.index(BASE_ALPH[j]) + i) % 26], end=" ")

if __name__ == "__main__":
    main()
