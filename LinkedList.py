class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return '{' + str(self.val) + '}'

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def __str__(self):
        formattedStr = ''
        current = self.head
        while current != None:
            formattedStr += str(current) + ' --> '
            current = current.next
        formattedStr += '|||'
        return formattedStr

    def addLast(self, node):
        head = self.head
        while head.next:
            head = head.next
        head.next = node

    def contains(self, val):
        head = self.head
        while head and head.val != val:
            head = head.next
        return False if head == None else True

if __name__ == '__main__':
    n0 = Node('0')
    n1 = Node('1')
    n2 = Node('2')

    ll = LinkedList(n0)
    n0.next = n1
    n1.next = n2
    print(ll)

    l2 = LinkedList()
    print(l2)

    l2.head = Node('test')
    print(l2)