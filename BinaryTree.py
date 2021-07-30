import collections

class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# Implementation from: https://youtu.be/oz9cEqFynHU?t=525
# DFS == Preorder
def dfs(root):
    if root == None:
        return
    stack = [root]
    while stack: # len(stack) > 0
        current = stack.pop() # pop top
        print(current.data, end='')
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    print('')

def inorder(root):
    stack = []
    current = root
    while True:
        if current:
            stack.append(current)
            current = current.left
        elif stack: # current is None and stack not empty
            current = stack.pop()
            print(current.data, end='')
            current = current.right
        else: # current is None and stack is empty
            break
    print('')

def postorder(root):
    stack = []
    current = root
    while True:

# Implementation from: https://youtu.be/oz9cEqFynHU?t=549
def bfs(root):
    if root == None:
        return
    queue = [root]
    while queue: # len(queue) > 0
        current = queue.pop(0) # pop front
        print(current.data, end='')
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    print('')

c = TreeNode(3, None, None)
d = TreeNode(4, None, None)
a = TreeNode(1, c, d)
b = TreeNode(2, None, None)
root = TreeNode(0, a, b)
"""
    0
   / \
  1   2
 / \
3   4
"""

print('dfs:')
dfs(root)
print('inorder:')
inorder(root)
print('bfs:')
bfs(root)

# def turnToArray(node, treeArr, idx):
#     if node == None:
#         return idx

#     treeArr[idx] = node
#     idx += 1
#     idx = turnToArray(node, treeArr, idx)
#     idx = turnToArray(node, treeArr, idx)

#     return idx

# print(turnToArray(root, [None] * 2000, 0))