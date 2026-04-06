"""
Python Coding Interview Preparation Guide
==========================================
A hands-on reference with runnable examples covering the most commonly
tested topics in Python coding interviews.
"""

# =============================================================================
# 1. DATA STRUCTURES
# =============================================================================

# --- Lists, Stacks, Queues ---------------------------------------------------

# List as a stack (LIFO)
stack = []
stack.append(1)
stack.append(2)
stack.append(3)
top = stack.pop()  # 3

# List as a queue (use collections.deque for O(1) popleft)
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
front = queue.popleft()  # 1

# --- Dictionary / HashMap ----------------------------------------------------

# Count character frequencies (classic interview pattern)
def char_frequency(s: str) -> dict:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

assert char_frequency("banana") == {'b': 1, 'a': 3, 'n': 2}

# collections.Counter shortcut
from collections import Counter
assert Counter("banana") == {'a': 3, 'n': 2, 'b': 1}

# --- Sets ---------------------------------------------------------------------

# Remove duplicates while preserving order
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

assert remove_duplicates([3, 1, 2, 1, 3, 4]) == [3, 1, 2, 4]

# --- DefaultDict & OrderedDict -----------------------------------------------

from collections import defaultdict

# Group anagrams (very common interview question)
def group_anagrams(words: list[str]) -> list[list[str]]:
    groups = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())

result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
# [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

# --- Heaps (Priority Queues) -------------------------------------------------

import heapq

# Find k largest elements
def k_largest(nums: list[int], k: int) -> list[int]:
    return heapq.nlargest(k, nums)

assert k_largest([3, 1, 5, 12, 2, 11], 3) == [12, 11, 5]

# Min-heap usage
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 1)
heapq.heappush(heap, 3)
smallest = heapq.heappop(heap)  # 1


# =============================================================================
# 2. STRING MANIPULATION
# =============================================================================

# --- Reverse a string ---------------------------------------------------------
def reverse_string(s: str) -> str:
    return s[::-1]

assert reverse_string("hello") == "olleh"

# --- Check palindrome ---------------------------------------------------------
def is_palindrome(s: str) -> bool:
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    return cleaned == cleaned[::-1]

assert is_palindrome("A man, a plan, a canal: Panama")

# --- Longest substring without repeating characters ---------------------------
def longest_unique_substring(s: str) -> int:
    """Sliding window approach - O(n)."""
    seen = {}
    left = 0
    max_len = 0
    for right, ch in enumerate(s):
        if ch in seen and seen[ch] >= left:
            left = seen[ch] + 1
        seen[ch] = right
        max_len = max(max_len, right - left + 1)
    return max_len

assert longest_unique_substring("abcabcbb") == 3  # "abc"

# --- Valid anagram ------------------------------------------------------------
def is_anagram(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)

assert is_anagram("anagram", "nagaram")


# =============================================================================
# 3. CLASSIC ALGORITHM PATTERNS
# =============================================================================

# --- Two Pointers -------------------------------------------------------------
def two_sum_sorted(nums: list[int], target: int) -> tuple[int, int]:
    """Given a SORTED array, find two numbers that add up to target."""
    left, right = 0, len(nums) - 1
    while left < right:
        total = nums[left] + nums[right]
        if total == target:
            return (left, right)
        elif total < target:
            left += 1
        else:
            right -= 1
    return (-1, -1)

assert two_sum_sorted([2, 7, 11, 15], 9) == (0, 1)

# --- Sliding Window -----------------------------------------------------------
def max_sum_subarray(nums: list[int], k: int) -> int:
    """Maximum sum of a subarray of size k."""
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum += nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)
    return max_sum

assert max_sum_subarray([1, 4, 2, 10, 2, 3, 1, 0, 20], 4) == 24

# --- Binary Search ------------------------------------------------------------
def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

assert binary_search([1, 3, 5, 7, 9], 5) == 2

# --- Two Sum (HashMap approach) -----------------------------------------------
def two_sum(nums: list[int], target: int) -> list[int]:
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

assert two_sum([2, 7, 11, 15], 9) == [0, 1]


# =============================================================================
# 4. SORTING
# =============================================================================

# --- Merge Sort (commonly asked to implement) ---------------------------------
def merge_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

assert merge_sort([38, 27, 43, 3, 9, 82, 10]) == [3, 9, 10, 27, 38, 43, 82]

# --- Quick Sort ---------------------------------------------------------------
def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

assert quick_sort([3, 6, 8, 10, 1, 2, 1]) == [1, 1, 2, 3, 6, 8, 10]

# --- Custom sorting with key --------------------------------------------------
intervals = [(1, 3), (2, 6), (8, 10), (15, 18)]
sorted_by_start = sorted(intervals, key=lambda x: x[0])
# Sort by second element descending
sorted_desc = sorted(intervals, key=lambda x: -x[1])


# =============================================================================
# 5. RECURSION & DYNAMIC PROGRAMMING
# =============================================================================

# --- Fibonacci (memoized) -----------------------------------------------------
from functools import lru_cache

@lru_cache(maxsize=None)
def fib(n: int) -> int:
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

assert fib(10) == 55

# --- Fibonacci (bottom-up DP) -------------------------------------------------
def fib_dp(n: int) -> int:
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

assert fib_dp(10) == 55

# --- Climbing Stairs (DP classic) ---------------------------------------------
def climb_stairs(n: int) -> int:
    """Number of distinct ways to climb n stairs (1 or 2 steps at a time)."""
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b

assert climb_stairs(5) == 8

# --- 0/1 Knapsack ------------------------------------------------------------
def knapsack(weights: list[int], values: list[int], capacity: int) -> int:
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
    return dp[n][capacity]

assert knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7) == 9

# --- Longest Common Subsequence -----------------------------------------------
def lcs(text1: str, text2: str) -> int:
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

assert lcs("abcde", "ace") == 3


# =============================================================================
# 6. LINKED LISTS
# =============================================================================

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_list(values):
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def list_to_array(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# --- Reverse a linked list ----------------------------------------------------
def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

assert list_to_array(reverse_list(build_list([1, 2, 3, 4, 5]))) == [5, 4, 3, 2, 1]

# --- Detect cycle in linked list (Floyd's algorithm) --------------------------
def has_cycle(head: ListNode) -> bool:
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

# --- Merge two sorted lists ---------------------------------------------------
def merge_two_lists(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

merged = merge_two_lists(build_list([1, 3, 5]), build_list([2, 4, 6]))
assert list_to_array(merged) == [1, 2, 3, 4, 5, 6]


# =============================================================================
# 7. TREES & GRAPHS
# =============================================================================

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# --- Tree Traversals ----------------------------------------------------------
def inorder(root: TreeNode) -> list[int]:
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)

def preorder(root: TreeNode) -> list[int]:
    if not root:
        return []
    return [root.val] + preorder(root.left) + preorder(root.right)

def level_order(root: TreeNode) -> list[list[int]]:
    """BFS level-order traversal."""
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level)
    return result

# --- Max depth of binary tree -------------------------------------------------
def max_depth(root: TreeNode) -> int:
    if not root:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))

# --- Validate BST -------------------------------------------------------------
def is_valid_bst(root: TreeNode, lo=float('-inf'), hi=float('inf')) -> bool:
    if not root:
        return True
    if root.val <= lo or root.val >= hi:
        return False
    return is_valid_bst(root.left, lo, root.val) and is_valid_bst(root.right, root.val, hi)

# --- Lowest Common Ancestor ---------------------------------------------------
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if not root or root is p or root is q:
        return root
    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    if left and right:
        return root
    return left or right

# --- Graph BFS ----------------------------------------------------------------
def bfs(graph: dict, start) -> list:
    visited = set()
    queue = deque([start])
    visited.add(start)
    order = []
    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return order

# --- Graph DFS ----------------------------------------------------------------
def dfs(graph: dict, start) -> list:
    visited = set()
    order = []
    def _dfs(node):
        visited.add(node)
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                _dfs(neighbor)
    _dfs(start)
    return order

# --- Number of Islands (classic grid DFS) ------------------------------------
def num_islands(grid: list[list[str]]) -> int:
    if not grid:
        return 0
    rows, cols = len(grid), len(grid[0])
    count = 0

    def sink(r, c):
        if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
            grid[r][c] = "0"
            sink(r + 1, c)
            sink(r - 1, c)
            sink(r, c + 1)
            sink(r, c - 1)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                count += 1
                sink(r, c)
    return count


# =============================================================================
# 8. PYTHON-SPECIFIC FEATURES (frequently tested)
# =============================================================================

# --- List Comprehensions ------------------------------------------------------
squares = [x ** 2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]
flat = [x for row in [[1, 2], [3, 4], [5]] for x in row]  # flatten

# --- Dict Comprehension -------------------------------------------------------
word_lengths = {w: len(w) for w in ["hello", "world", "python"]}

# --- Generators ---------------------------------------------------------------
def fibonacci_gen():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = fibonacci_gen()
first_10 = [next(gen) for _ in range(10)]

# --- Enumerate & Zip ----------------------------------------------------------
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
for i, (name, score) in enumerate(zip(names, scores)):
    pass  # i=0, name="Alice", score=85 ...

# --- *args and **kwargs -------------------------------------------------------
def flexible_func(*args, **kwargs):
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

# --- Decorators ---------------------------------------------------------------
def timer(func):
    import time
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.4f}s")
        return result
    return wrapper

# --- Context Managers ---------------------------------------------------------
from contextlib import contextmanager

@contextmanager
def managed_resource():
    print("Acquiring resource")
    try:
        yield "resource"
    finally:
        print("Releasing resource")

# --- Lambda, Map, Filter, Reduce ---------------------------------------------
from functools import reduce

doubled = list(map(lambda x: x * 2, [1, 2, 3]))     # [2, 4, 6]
odds = list(filter(lambda x: x % 2, [1, 2, 3, 4]))  # [1, 3]
total = reduce(lambda a, b: a + b, [1, 2, 3, 4])     # 10

# --- Walrus Operator (Python 3.8+) -------------------------------------------
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered = [y for x in data if (y := x ** 2) > 20]  # [25, 36, 49, 64, 81, 100]

# --- Dataclasses --------------------------------------------------------------
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float

    def distance_to(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

p1, p2 = Point(0, 0), Point(3, 4)
assert p1.distance_to(p2) == 5.0


# =============================================================================
# 9. COMPLEXITY CHEAT SHEET
# =============================================================================
"""
Operation                   | Time         | Space
----------------------------+--------------+--------
Array access by index       | O(1)         |
Array append                | O(1) amort.  |
Array insert/delete at i    | O(n)         |
Dict get/set/delete         | O(1) avg     |
Set add/remove/lookup       | O(1) avg     |
Sorting (Timsort)           | O(n log n)   | O(n)
Binary search               | O(log n)     | O(1)
BFS / DFS                   | O(V + E)     | O(V)
Heap push/pop               | O(log n)     |
Heap build                  | O(n)         |
"""


# =============================================================================
# 10. COMMON INTERVIEW TIPS
# =============================================================================
"""
1. CLARIFY before coding: ask about edge cases, input size, constraints.
2. THINK ALOUD: explain your approach before writing code.
3. START with brute force, then optimize.
4. TEST your code with examples and edge cases.
5. KNOW YOUR COMPLEXITIES: always state time & space complexity.
6. PRACTICE these patterns:
   - Two pointers
   - Sliding window
   - HashMap / frequency counting
   - BFS / DFS
   - Dynamic programming (top-down vs bottom-up)
   - Binary search
   - Backtracking
"""


if __name__ == "__main__":
    print("All assertions passed! You're ready for your interview.")
