import time
import sys
import os
from collections import deque

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from SecondSemester.lab1.utils.utils import time_memory_tracking


def read_input_lines(file_path="../txtf/input.txt"):
    """Чтение данных"""
    with open(file_path, "r") as inp:
        n = int(inp.readline())
        list_of_lines = []
        for line in inp:
            if line.strip():
                list_of_lines.append(list(map(int, line.split())))
        print("==========Входные данные========== ")
        print(f"n: {n}, arr: {list_of_lines}")
        return n, list_of_lines


class Node:
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Node({self.key}, left={self.left}, right={self.right})"


def read_tree(n, arr):
    tree = {}
    for i in range(len(arr)):
        key, left, right = arr[i]
        tree[i] = Node(key, left - 1 if left else -1, right - 1 if right else -1)
    return tree


def tree_height(tree, root):
    if root == -1:
        return 0

    queue = deque([(root, 1)])
    max_height = 0

    while queue:
        node, height = queue.popleft()
        max_height = max(max_height, height)

        if tree[node].left != -1:
            queue.append((tree[node].left, height + 1))
        if tree[node].right != -1:
            queue.append((tree[node].right, height + 1))

    return max_height


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input_lines("../txtf/input.txt")
    tree = read_tree(n, arr)
    height = tree_height(tree, 0)
    print("Ответ")
    print(height)
    file_name = os.path.basename(__file__)
    time_memory_tracking(time_start)
