import re

def genKey(string, key):
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) - len(key)):
            key += key[i % len(key)]
        return(key)

def encryption(string, key):
    encrypt_text = ""
    upperKey = key.upper()
    lowerKey = key.lower()
    for i in range(len(string)):
        if bool(re.match(r'[A-Z]',string[i])):
           encrypt_text += chr((ord(string[i]) + (ord(upperKey[i]) - ord('A')) -ord('A')) % 26 + ord('A'))
        elif bool(re.match(r'[a-z]',string[i])):
           encrypt_text += chr((ord(string[i]) + (ord(lowerKey[i]) - ord('a')) -ord('a')) % 26 + ord('a'))
        else:
           encrypt_text += string[i]

    return(encrypt_text)

if __name__=="__main__":      
    string = input("Enter the text>>>")
    key = input("Enter the key>>>")
    encKey = genKey(string, key)
    encText = encryption(string, encKey)

    print("cipher: ", encText)
           

