import os
import time

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def insert(node, key):
    if node is None:
        return Node(key)
    if key > node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

def search(root, key):
    if root is None or root.key == key:
        return root
    if root.key < key:
        return search(root.left, key)
    return search(root.right, key)

def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root
    if key > root.key:
        root.left = deleteNode(root.left, key)
    elif key < root.key:
        root.right = deleteNode(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        temp = minValueNode(root.right)
        root.key = temp.key
        root.right = deleteNode(root.right, temp.key)
    return root

def print_tree(node, level=0, side='ROOT'):
    if node != None:
        print(f'({side} ) |' + '_' * (level + 1) + str(node.key))
        print_tree(node.left, level + 1, 'LEFT')
        print_tree(node.right, level + 1, 'RIGHT')

def search_path(root,key,path=[]):
    if not root:
        return []
    path.append(root.key)
    if root.key == key:
        return path
    left_path=search_path(root.left,key,path[:])
    right_path=search_path(root.right,key,path[:])
    if left_path!=[]:
        return left_path
    if right_path!=[]:
        return right_path
    return []

def main():
    root = None
    keys = input("Enter a sequence of strings (space-delimited):").split()
    if not keys:
        print("Error: Input cannot be empty")
        return
    for key in keys:
        if not key.isalpha():
            print(f"Error: Invalid character in input: {key}")
            return
        root = insert(root, key)
    print()
    print_tree(root)
    while True:
        print()
        print("[1] Search string")
        print("[2] Delete string")
        print("[3] Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            clear_screen()
            search_key = input("Enter string to search for in the tree: ")
            path = search_path(root, search_key)
            if path:
                print(f"Path from {path[0]} to {search_key}: {' -> '.join(path)}")
            else:
                print(f"{search_key} not found in the tree")
                time.sleep(1)
        elif choice == '2':
            clear_screen()
            delete_key = input("Enter string to delete in the tree: ")
            if search(root, delete_key):
                root = deleteNode(root, delete_key)
                print()
                print_tree(root)
            else:
                print(f"{delete_key} not found in the tree")
                time.sleep(1)
        elif choice == '3':
            clear_screen()
            time.sleep(2)
            break
        else:
            print("Invalid choice")
            time.sleep(1)
            clear_screen()

def main():
    root = None
    keys = input("Enter a sequence of strings (space-delimited):").split()
    if not keys:
        print("Error: Input cannot be empty")
        return
    keys_set = set()
    for key in keys:
        if not key.isalpha():
            print(f"Error: Invalid character in input: {key}")
            return
        if key in keys_set:
            print(f"Error: Duplicate string in input: {key}")
            return
        keys_set.add(key)
        root = insert(root, key)
    if root:
        print_tree(root)
    else:
        print("No strings left in the tree")
    input("Press Enter to continue...")
    while True:
        clear_screen()
        print("[1] Search string")
        print("[2] Delete string")
        print("[3] Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            search_key = input("Enter string to search for in the tree: ")
            path = search_path(root, search_key)
            if path:
                print(f"Path from {path[0]} to {search_key}: {' -> '.join(path)}")
            else:
                print(f"{search_key} not found in the tree")
        elif choice == '2':
            delete_key = input("Enter string to delete in the tree: ")
            if search(root, delete_key):
                root = deleteNode(root, delete_key)
                if root:
                    print_tree(root)
                else:
                    print("No strings left in the tree")
                input("Press Enter to continue...")
            else:
                print(f"{delete_key} not found in the tree")
        elif choice == '3':
            break
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()




