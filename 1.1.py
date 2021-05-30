def isUniqueChars(theString):
    if len(theString) > 128:
        return False

    charSet = [None] * 128
    for i in range(len(theString)):
        asciiVal = ord(theString[i])
        if charSet[asciiVal]:
            return False
        else:
            charSet[asciiVal] = True
    return True

print(isUniqueChars('abc'))
print(isUniqueChars('aardvark'))
print(isUniqueChars('hello'))