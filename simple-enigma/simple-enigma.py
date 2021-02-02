# A "simple" implementation of Enigma, using an alphabet of 6 characters.
# Author: Gabriel De Jesus

def main():
    keyboard = ['a','b','c','d','e','f']
    scramblers = []
    # Define Initial Wire Positions for Scrambled Alphabet
    scramble = ['B', 'A', 'D', 'F', 'E', 'C']
    # Re-using code built for Vigenere to build a matrix of
    # Scramblers that Rotates 1 Position per Input
    # Which means it takes 6 iterations to get a duplicate encoding of a character
    # With a single scrambler.
    # If we add a second or third Scrambler, we can increase the variation and reduce
    # Likelihood of frequency analysis being successful.
    for r in range(0, len(keyboard)):
        scramblers.append([0 for c in range(0,len(keyboard))])
    for i in range(0, len(keyboard)):
        for j in range(0, len(keyboard)):
            scramblers[i][j] = scramble[(scramble.index(scramble[j]) + i) % 6]
    
    ch = ''
    while True:
        for ind in range(0,len(keyboard)):
            ch = input("Enter Letter to Encode:")
            if ch not in keyboard:
                print("Only Working with 'a-f' for now")
                return
            print("Input Character:" + ch)
            out = scramblers[ind][keyboard.index(ch)]
            print("Encoded: " + out)
# in case we want to take in args
if __name__ == "__main__":
    main() # sys.argv[1:]

