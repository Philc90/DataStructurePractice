# https://leetcode.com/problems/remove-k-digits/

def removeOne(s):
    if len(s) < 2:
        return ''
    if int(s[0]) > int(s[1]): # starts at peak
        iPeak = 0
    else: # find the peak
        iPeak = 0
        for i in range(len(s)):
            if i < len(s) - 1 and int(s[i]) > int(s[i+1]):
                iPeak = i
                break
            elif i == len(s) - 1:
                iPeak = i
    s = s[:iPeak] + s[iPeak+1:]
    iLeadingZero = 0
    for i in range(0, len(s)):
        if int(s[i]) == 0:
            iLeadingZero+=1
        else:
            break
    return s[iLeadingZero:]

k = 3
s = '1432219'
print(s)
for i in range(k):
    s = removeOne(s)
    print(s)

k = 1
s = '10200'
print(s)
for i in range(k):
    s = removeOne(s)
    print(s)

k = 2
s = '10'
print(s)
for i in range(k):
    s = removeOne(s)
    print(s)

k = 2
s = '12345'
print(s)
for i in range(k):
    s = removeOne(s)
    print(s)