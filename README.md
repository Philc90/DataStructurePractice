# DataStructurePractice

# Python Cheatsheet

## Common Operations

### String Operations
- reverse: `s[::-1]`

### Ternary operator format
*value_if_true* `if` *condition* `else` *value_if_false*

### ASCII char val conversion
- `ord()`: convert char to num
- `chr()`: convert back

### Bit Manipulation
- generate *n* 1's
    - `bin((1 << n + 1) - 1)`
    - approach: shift 1 left by *n + 1* bits, then subtracting 1 will remove the leftmost 1 and flip all the remaining (*n*) zeros to 1

### Fixed Array
- initialize a list like this: `[None] * FIXED_LEN`

## Implementations of Data Structures

### List
- append elements of another list to current list: `myList.extend(otherList)`
- sorting a list:
    - `sorted(myList)` -> returns a **copy**
        - Options
            - `reverse=True`: descending order instead of ascending order
            - `key=...`: sort by a different key
                - e.g. sort tuple by second item: `key=lambda x:x[1]`
    - `myList.sort()` -> sorts **in-place**

### Stack
- use a list & built-in methods
    - isEmpty(): `not stack`
    - size(): `len(stack)`
    - top(): `stack[-1]`
    - push(): `stack.append()`
    - pop(): `stack.pop()`

### Queue
- simplest: use a list & built-in methods (perhaps less efficient? look into this)
    - enqueue(): `q.append()`
    - dequeue(): `q.pop(0)`
- other options in Python:
    - collections.deque:
        - initialize: `q = deque()`
        - enqueue(): `q.append()`
        - dequeue(): `q.popleft()`
    - queue.Queue: this one is meant for concurrency

### Binary Tree
```python3
class TreeNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
```
- array representation of a complete binary tree:
    - use list
    - for node at index `i`:
        - left child is at `2i + 1`
        - right child is at `2i + 2`
        - parent is at `(i-1)/2`

### Hash Map
- use the built-in dictionary
- Other useful dictionary types from the collections library:
    - Counter: constructor takes an iterable, constructs an object that counts occurrences of each item
    - OrderedDict: guarantees order of insertion of keys
        - methods:
            - `od[key] = value`
            - `od.pop(key)`
    - defaultdict: returns a user-specified default value if non-existent key is retrieved

### Set
- initialize empty set: `s = set()`
- initialize with values: `s = { 'one', 'two' }`
- methods:
    - `s.add(elem)`
    - `s.remove(elem)`
    - `s.clear()`

### Min Heap
- built-in library: `import heapq`
    - transform list to heap: `heapq.heapify(array)`
    - push: `heapq.heappush(array, item)`
    - pop: `heapq.heappop(array)`
    - extra - more efficient methods
        - push then pop: `heapq.heappushpop(array, item)`
        - pop then push: `heapq.heapreplace(array, item)`

### Max Heap
- built-in heapq is a min heap by default. One way to still use it is to multiply nums by -1 before pushing, then multiply by -1 when popping to restore val.

### Trie
```python3
class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.visitedCount = 0
```

---

# Algorithms / techniques

## Two pointer technique
- [Floyd's cycle-finding algorithm](https://en.wikipedia.org/wiki/Cycle_detection#Tortoise_and_hare)
- implementation note: easier to remember/write when fast pointer is checked to be None instead of checking fast.next to be none
    - e.g. `while fast and fast.next:` instead of `while fast.next and fast.next.next:`

## Sliding Window

## Boyer-Moore Voting Algorithm

---

# other stuff

### To do:
- **LinkedList** ???
- **BinaryTree** ???
    - dfs ???
    - bfs ???
- Stack ???
- Queue ???
- HashMap ???
- Heap
    - heapify
- Graph
    - dfs
    - bfs
- Sorting algorithms

---

from reddit comment
> I know I'm a little late to the party, but I really want to give my advice since I struggled with this for a really long time as well. I think one of the first things anyone preparing for the interview game should read the intro chapters of CTCI (up until chapter 1). The reason for this is that it goes over the actual strategy behind solving coding problems. For those who don't know it, I'll talk about the importance of it here. When you're first given a problem, ask about it! Ask for what the valid inputs are and clarify just everything about the problem, then go over the test case(s) that they provide with you. This will help get you more comfortable with the problem and better suited to get into possible solutions, also this should all be spoken OUT LOUD.
> 
> A lot of people sort of just go into test taking mode for interviews, and it is the COMPLETE OPPOSITE for coding problems. On a test, you would usually just write down the correct solution and erase all your wrong work. However, it is in your advantage to talk as much as possible and communicating how you are thinking along the way despite if you are wrong. There are people who emphasize this but not enough, this is what your interviewer is looking for! (most of them at least).
> 
> Once you understand your problem, try to make a brute force solution. You can typically do it pretty quickly but it's more important to NOT code it. The reason for this is that the brute force solution maybe obvious, but you should at least let your interviewer know "hey, I can actually SOLVE this if I encountered somehow in my school or work". From here, we can optimize and try to find the optimal solution. Coding out the brute force solution is in general, just time consuming and doesn't help you in the mind of the interviewer. You acknowledging the brute force solution is good enough to them. Mind you, I try to aim for that entire thing to be in under 5 minutes, you need a lot of time to come up with these solutions!
> 
> To get these solutions, I think you should do a number of problems each dealing with an individual topic. For data structures, it's important to know when to use them and for algorithms, it's pretty obvious when they're used it's just a matter of actually implementing them.
> 
> For string, array based questions and hash-table questions, the first chapter of CTCI will do just fine. Try to work at each problem like I've done before and actually talk out loud when doing it (I know sounds dumb but it works. That's why it's really important to do mock interviews with another).
> 
> LinkedList questions are also very common and are strangely loved by companies. They are strangely niche and each solution is quite different from each other imo. You should do each LinkedList problem in CTCI, that will be a really good base knowledge on LinkedLists. Also, you should know when to use a linkedlist as a data structure! The best one for this is LRU Cache on leetcode in my opinion. By drawing out how it works with a linkedlist vs. another structure like a vector, it makes it very clear on when linkedlists are great!
> 
> For queues and stacks, I think the best way to learn them is to implement iterative traversals of binary search trees. Speaking of which, recursion is important too and CTCI has good problems on it. My personal preference on recursion problems is to actually get comfortable with recursion by doing basic binary tree problems before moving on to bigger ones. Some basic tree questions are: find height of a binary tree, print out all nodes in a certain order binary tree, level order traversal of a binary tree (important!!) and more.
> 
> Finally, with BFS and DFS questions, it's important to first learn how to implement them, then to use them in a problem. For me, I learned the best when doing the "number of islands" leetcode problem. Also, make sure to work with a few priority queue problems! These ones are always hiding and can catch you off guard. I don't believe there's a dedicated section to it in CTCI so try to find problems using them. I personally like "merge k linkedlists" for this one.
> 
> There are a final few notes I'd like to give. First, if a problem involves intervals, it usually depends on having to sort it by begin and end points in some way before actually doing the work on the intervals. Second, don't forget your sorts! You will use sorts in many array and string based problems, but make sure you know your time complexities (covered in CTCI). Finally, I'd like to reiterate my paragraphs about speaking out loud. I think this trait of interviewing really makes you stand out among the rest. I have passed interviews without even getting the optimal solution, just because I was communicative. I even had an onsite with Microsoft once and the guy gave me a second chance at the end of the day to re-interview because he thought I had a lot of potential (I got the problem completely wrong the first time around). The re-interview I had, I absolutely killed it and moved on in the process. So, speaking from experience I believe it's very very important to not just do problems, but to approach it the same way you would approach the real thing.
> 
> Best of luck! If you read through it all, I appreciate it :)


Things to cover:
- Big O
- Arrays
- LinkedLists
- BFS
- DFS
- stack
- queue
- binary tree
- binary search tree
- binary search
- graphs
- topological sort
- heap
- hash map
- collision
- merge sort
- divide and conquer
- selection sort
- logarithms
