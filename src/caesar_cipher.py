import re

string = input("enter your string>>>")

for i in range(1,26):
    result = ""
    for c in string:
        if bool(re.match(r'[A-Z]', c)):
                result += chr((ord(c) + i - ord('A')) % 26 + ord('A'))
        elif bool(re.match(r'[a-z]', c)):
                result += chr((ord(c) + i - ord('a')) % 26 + ord('a'))
        else:
                result += c

    print("ROT"+str(i)+">>>"+result)





