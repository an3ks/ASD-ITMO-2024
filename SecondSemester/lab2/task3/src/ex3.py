import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from SecondSemester.lab1.utils.utils import time_memory_tracking, printResult


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if not self.root:
            self.root = BSTNode(key)
            return
        node = self.root
        while True:
            if key < node.key:
                if node.left:
                    node = node.left
                else:
                    node.left = BSTNode(key)
                    return
            elif key > node.key:
                if node.right:
                    node = node.right
                else:
                    node.right = BSTNode(key)
                    return
            else:
                return  # Уже есть в дереве

    def find_min_greater(self, key):
        node = self.root
        res = None
        while node:
            if node.key > key:
                res = node
                node = node.left
            else:
                node = node.right
        return res.key if res else 0


def data_reading(file_path="../txtf/input.txt"):
    bst = BST()
    results = []

    with open(file_path, "r") as f:
        for line in f:
            op, x = line[0], int(line[2:])
            if op == '+':
                bst.insert(x)
            elif op == '>':
                results.append(str(bst.find_min_greater(x)))

    return results


if __name__ == "__main__":
    time_start = time.perf_counter()
    results = data_reading("../txtf/input.txt")
    print("\n".join(results))
    file_name = os.path.basename(__file__)
    time_memory_tracking(time_start)
