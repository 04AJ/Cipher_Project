key = {'A': '!', 'B': '@', 'C': '#', 'D': '$', 'E': '%',  'F': '^',  'G': '&', 'H': '*',  'I': '(', 'J': ')', 'K': '-', 'L': '=',
       'M': '_', 'N': '+', 'O': '{',  'P': '}', 'Q': '[',  'R': ']',  'S': '|', 'T': ':',  'U': ';',  'V': '<',  'W': '>',  'X': '?',  'Y': '/',  'Z': '~', ' ': '`', ',': '?', '?': '.'}


# reversing dictionary
invr = {a: b for b, a in key.items()}


def encrypt(input):
    secret = ''
    for word in input:
        secret += key[word]

    return secret


def decrypt(input):
    answer = ''
    for word in input:
        answer += invr[word]
    return answer


# getting user input
loop = True
while(loop):
    usr = input("Enter text: ")
    usr = usr.upper()
    inp = list(usr)
    func = input("Enter A to Encrypt or Enter B to Decrypt: ").upper()
    if func == 'A':
        print(encrypt(inp))
    elif func == 'B':
        print(decrypt(inp))
    else:
        print("INVALID INPUT")
    p = input("Press C to continue or Q to quit: ").upper()
    if p == 'Q':
        loop = False
