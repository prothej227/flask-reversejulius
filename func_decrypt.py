#Upper -> 65 - 90
#Lower -> 97 - 122

def Decrypt(msg, key):
    nkey = int()
    li = []
    MSG = map(lambda x:x, msg)
    for c in MSG:
        #Check if UpperCase:
        if c.isupper():
            if (ord(c) - key) < 65:
                nKey = (ord(c) - key) + 26
            else:
                nKey = (ord(c) - key)
            li.append(nKey)
        elif c.islower():
            if (ord(c) - key) < 97:
                nKey = (ord(c) - key) + 26
            else:
                nKey = (ord(c) - key)
            li.append(nKey)
        else:
            nKey = ord(c)
            li.append(nKey)   
    DecryptMessage = "".join([chr(char) for char in li])
    return DecryptMessage

