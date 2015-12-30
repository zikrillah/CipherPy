#Python 3
#Aythor : Zikri
#This expanded code from caesarCipher.py, using 2 methods toEncrypt and toDecrypt


key = 13

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

translated = ''

mode = ''


def toEncrypt(key, translated): 

    #message = input('Message to encrypt> ')
    #message = message.upper()

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)

            num = num + key

            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]

        else:

            translated = translated + symbol
            
    print(translated)


def toDecrypt(key, translated):

    #message = input('Message to decrypt> ')
    #message = message.upper()

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)

            num = num - key

            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)

            translated = translated + LETTERS[num]

        else:

            translated = translated + symbol
            
    print(translated)

while True:
    
    mode = input('Choose mode > ')
    mode = mode.lower()

    if (mode == 'encrypt') or (mode == 'decrypt'):
        prompt = str('Message to %s ' % (mode))
        message = input(prompt + ' > ') 
        message = message.upper()
        break
    

if mode == 'encrypt':
    toEncrypt(key, translated)
elif mode == 'decrypt':
    toDecrypt(key, translated)
