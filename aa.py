
class Node:
    def __init__(self, roll, name):
        self.roll = roll
        self.name = name
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def height(self, node):
        return node.height if node else 0

    def balance(self, node):
        return self.height(node.left) - self.height(node.right)

    def right_rotate(self, y):
        x = y.left
        t = x.right
        x.right = y
        y.left = t
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        return x

    def left_rotate(self, x):
        y = x.right
        t = y.left
        y.left = x
        x.right = t
        x.height = 1 + max(self.height(x.left), self.height(x.right))
        y.height = 1 + max(self.height(y.left), self.height(y.right))
        return y

    def insert(self, root, roll, name):
        if root is None:
            return Node(roll, name)

        if roll < root.roll:
            root.left = self.insert(root.left, roll, name)
        elif roll > root.roll:
            root.right = self.insert(root.right, roll, name)
        else:
            root.name = name
            return root

        root.height = 1 + max(self.height(root.left),
                              self.height(root.right))
        b = self.balance(root)

        if b > 1 and roll < root.left.roll:
            return self.right_rotate(root)
        if b < -1 and roll > root.right.roll:
            return self.left_rotate(root)
        if b > 1 and roll > root.left.roll:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if b < -1 and roll < root.right.roll:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def display(self, root):
        if root:
            self.display(root.left)
            print(root.roll, root.name)
            self.display(root.right)

    def search(self, root, roll):
        if root is None or root.roll == roll:
            return root
        if roll < root.roll:
            return self.search(root.left, roll)
        return self.search(root.right, roll)


tree = AVLTree()
root = None

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Enter roll number: "))
    name = input("Enter student name: ")
    root = tree.insert(root, roll, name)

print("\nStudent records in ascending order:")
tree.display(root)

for roll in [108, 107]:
    result = tree.search(root, roll)
    if result:
        print("Roll number", roll, "found:", result.name)
    else:
        print("Roll number", roll, "not found")
