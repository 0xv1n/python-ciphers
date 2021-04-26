# A "simple" implementation of Enigma, using an alphabet of 6 characters.
# Author: Gabriel De Jesus

def main():
    keyboard = ['a','b','c','d','e','f']
    scramblers = []
    # Define Initial Wire Positions for Scrambled Alphabet
    scramble = ['B', 'A', 'D', 'F', 'E', 'C']
    for r in range(0, len(keyboard)):
        scramblers.append([0 for c in range(0,len(keyboard))])
    for i in range(0, len(keyboard)):
        for j in range(0, len(keyboard)):
            scramblers[i][j] = scramble[(scramble.index(scramble[j]) + i) % 6]
            
    ch = ''
    while True:
        for ind in range(0,len(keyboard)):
            ch = input("Enter Letter to Encode:").lower()
            if ch not in keyboard:
                print("Only Working with 'A-F' for now")
                return
            print("Input Character:" + ch)
            out = scramblers[ind][keyboard.index(ch)]
            print("Encoded: " + out)

            
if __name__ == "__main__":
    main() # sys.argv[1:]

