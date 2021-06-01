# assume ASCII string only, no empty string, and really basic hash function. using a linked list for collisions

from LinkedList import *

class KeyValuePair:
    def __init__(self, key=None, val=None):
        self.key = key
        self.val = val

    def __str__(self):
        if self.key and self.val:
            return str(self.key) + '::' + str(self.val)
        else:
            return 'NULL'

    def __eq__(self, other):
        if isinstance(other, KeyValuePair):
            return True if (self.key == other.key) else False
        else:
            return True if (self.key == other) else False

# This class used for implementing set or map depending on whether key is string or KeyValuePair
class HashTable:
    def __init__(self):
        self.hashTable = [None] * 128

    def __str__(self):
        formattedStr = ''
        for ll in self.hashTable:
            if ll:
                formattedStr += str(ll) + '\n'
            else:
                formattedStr += 'vacant\n'
        return formattedStr

    def hashFunction(self, input) -> int:
        if isinstance(input, str):
            return ord(input[0])
        elif isinstance(input, KeyValuePair):
            return ord(input.key[0])
        else:
            return -1

    def insert(self, input):
        hashIdx = self.hashFunction(input)
        if self.hashTable[hashIdx]: # collison. insert to end of LL
            self.hashTable[hashIdx].addLast(Node(input))
        else:
            self.hashTable[hashIdx] = LinkedList(Node(input))

    def containsKey(self, input:str):
        hashIdx = self.hashFunction(input)
        if self.hashTable[hashIdx]:
            if self.hashTable[hashIdx].contains(input):
                return True
            else:
                return False
        else:
            return False

if __name__ == '__main__':
    hashSet = HashTable()
    hashSet.insert('cat')
    hashSet.insert('dog')
    hashSet.insert('caterpillar')
    hashSet.insert('cupid')
    print(hashSet)

    print('cat in list? ' + str(hashSet.containsKey('cat')))
    print('cow in list? ' + str(hashSet.containsKey('cow')))
    print('===================================\n')

    wordAssocHashMap = HashTable()
    wordAssocHashMap.insert(KeyValuePair('cat', 'dog'))
    wordAssocHashMap.insert(KeyValuePair('george', 'costanza'))
    wordAssocHashMap.insert(KeyValuePair('man', 'hack'))
    print(wordAssocHashMap)

    print('cat in list? ', str(wordAssocHashMap.containsKey('cat')))
    print('dog in list? ', str(wordAssocHashMap.containsKey('dog')))