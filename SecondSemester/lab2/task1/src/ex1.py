import time
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../..')))
from SecondSemester.lab1.utils.utils import time_memory_tracking, printResult



def read_input_lines(file_path="../txtf/input.txt"):
    """Чтение данных"""
    with open(file_path, "r") as inp:
        n = int(inp.readline())
        list_of_lines = []
        for line in inp:
            if line != "":
                list_of_lines.append(list(map(int, line.split())))
        print("==========Входные данные========== ")
        # print(f"n = {n}, arr = {list_of_lines}")
        return n, list_of_lines


class Node:  # создали класс узел
    def __init__(self, key, left, right):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):  # Делаем объекты читаемыми
        return f"Node({self.key}, left={self.left}, right={self.right})"


def read_tree(n, arr):  # заполняем словарь узлами, считывая наши данные
    tree = {}
    for i in range(len(arr)):
        key, left, right = arr[i]
        tree[i] = Node(key, left, right)

    return tree


def in_order(tree, root):
    stack = []
    result = []
    node = root

    while stack or node != -1:
        if node != -1:
            stack.append(node)
            node = tree[node].left  # идём влево
        else:
            node = stack.pop()
            result.append(tree[node].key)  # записываем узел
            node = tree[node].right  # переходим вправо

    return result


def pre_order(tree, root):
    if root == -1:
        return []

    stack = [root]
    result = []

    while stack:
        node = stack.pop()
        result.append(tree[node].key)  # записываем узел

        if tree[node].right != -1:
            stack.append(tree[node].right)  # сначала добавляем правого ребёнка
        if tree[node].left != -1:
            stack.append(tree[node].left)  # затем левого (чтобы он был первым в обходе)

    return result


def post_order(tree, root):
    if root == -1:
        return []

    stack, result = [root], []
    visited = set()

    while stack:
        node = stack[-1]

        if (tree[node].left != -1 and tree[node].left not in visited):
            stack.append(tree[node].left)  # сначала идём влево
        elif (tree[node].right != -1 and tree[node].right not in visited):
            stack.append(tree[node].right)  # затем вправо
        else:
            result.append(tree[node].key)  # только когда нет детей — записываем
            visited.add(stack.pop())  # убираем узел из стека

    return result


if __name__ == "__main__":
    time_start = time.perf_counter()
    n, arr = read_input_lines("../txtf/input.txt")
    tree = read_tree(n, arr)
    in_res, pre_res, post_res = [], [], []

    print(*in_order(tree, 0))
    print(*pre_order(tree, 0))
    print(*post_order(tree, 0))
    file_name = os.path.basename(__file__)
    # printResult(result, file_name)
    time_memory_tracking(time_start)

# 5
# 4 1 2
# 2 3 4
# 5 -1 -1
# 1 -1 -1
# 3 -1 -1
