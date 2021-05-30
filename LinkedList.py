class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

    def __str__(self):
        return '{' + self.val + '}'

class LinkedList:
    def __init__(self, head):
        self.head = head

    def __str__(self):
        formattedStr = ''
        current = self.head
        while current != None:
            formattedStr += str(current) + ' --> '
            current = current.next
        formattedStr += '|||'
        return formattedStr

n0 = Node('0', None)
n1 = Node('1', None)
n2 = Node('2', None)

ll = LinkedList(n0)
n0.next = n1
n1.next = n2
print(ll)

l2 = LinkedList(None)
print(l2)

l2.head = Node('test', None)
print(l2)