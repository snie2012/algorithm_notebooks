from .TreeNode import TreeNode

def buildTree():
        root = TreeNode(0)
        root.left = TreeNode(1)
        root.right = TreeNode(2)

        root.left.left = TreeNode(3)
        root.left.right = TreeNode(4)

        root.right.left = TreeNode(5)
        root.right.right = TreeNode(6)

        return root
