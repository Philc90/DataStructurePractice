import collections

class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def dfs(root):
    stack = [root]
    while len(stack) > 0:
        current = stack.pop()
        print(current.data, end='')
        if current.right != None:
            stack.append(current.right)
        if current.left != None:
            stack.append(current.left)
    print('')

def bfs(root):
    queue = collections.deque()
    queue.append(root)
    while len(queue) > 0:
        current = queue.popleft()
        print(current.data, end='')
        if current.left != None:
            queue.append(current.left)
        if current.right != None:
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
print('bfs:')
bfs(root)

def turnToArray(node, treeArr, idx):
    if node == None:
        return idx

    treeArr[idx] = node
    idx += 1
    idx = turnToArray(node, treeArr, idx)
    idx = turnToArray(node, treeArr, idx)

    return idx

print(turnToArray(root, [None] * 2000, 0))