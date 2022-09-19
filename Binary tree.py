class node:
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data

def print_inorder(root):
    if root:
        print_inorder(root.left)
        print(root.data)
        print_inorder(root.right)
def print_preorder(root):
    if root:
        print(root.data)
        print_inorder(root.left)
        print_inorder(root.right)
def print_postorder(root):
    if root:
        print_inorder(root.left)
        print_inorder(root.right)
        print(root.data)


root=node(1)

root.left=node(2)
root.right=node(3)
root.left.left=node(4)

print_postorder(root)
print('')
print_preorder(root)
print('')
print_inorder(root)