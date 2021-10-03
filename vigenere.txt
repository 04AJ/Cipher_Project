# creating vars and library

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
           'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
alph = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4,  'F': 5,  'G': 6, 'H': 7,  'I': 8, 'J': 9, 'K': 10, 'L': 11,
        'M': 12, 'N': 13, 'O': 14,  'P': 15, 'Q': 16,  'R': 17,  'S': 18, 'T': 19,  'U': 20,  'V': 21,  'W': 22,  'X': 23,  'Y': 24,  'Z': 25}

rows = 26
cols = 26

# creating empty 2D array
arr = [[0 for i in range(cols)] for j in range(rows)]
arr = [' ' for i in range(rows)]
arr[0] = letters

# creating 2d array that has every possible caesar cipher
shift = 1
for j in range(1, 26):
    temp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    for i in range(0, shift):
        temp.append(letters[i])
        temp.pop(0)

    arr[j] = temp
    shift += 1


# Creating functions


def encrypt(input, key):
    keyword = []
    length = 0
    index = 0
    while length < len(input):
        if(index > len(key)-1):
            index = 0
            keyword.append(key[index])
            length += 1
            index += 1
        else:
            keyword.append(key[index])
            length += 1
            index += 1

    encr = []
    for i in range(0, len(input)):
        encr.append(arr[alph[keyword[i]]][alph[input[i]]])
    secret = ''
    for letter in encr:
        secret += letter

    return secret


def decrypt(input, key):
    keyword = []
    length = 0
    index = 0
    while length < len(input):
        if(index > len(key)-1):
            index = 0
            keyword.append(key[index])
            length += 1
            index += 1
        else:
            keyword.append(key[index])
            length += 1
            index += 1

    answer = ''
    for i in range(0, len(input)):
        loc = 0
        for let in arr[alph[keyword[i]]]:
            if input[i] == let:
                break
            else:
                loc += 1
        answer += letters[loc]

    return answer


# getting user input
loop = True
while(loop):
    usr = input("Enter text (No spaces!): ")
    usr = usr.upper()
    inp = list(usr)
    KEY = list(input("Enter a key: ").upper())
    func = input("Enter A to Encrypt or Enter B to Decrypt: ").upper()
    if func == 'A':
        print(encrypt(inp, KEY))
    elif func == 'B':
        print(decrypt(inp, KEY))
    else:
        print("INVALID INPUT")
    p = input("Press C to continue or Q to quit: ").upper()
    if p == 'Q':
        loop = False
