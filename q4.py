class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrderTraversal(root):
    result = []
    if not root:
        return result

    queue = [root]

    while queue:
        current = queue.pop(0)
        result.append(current.val)

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return result


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)


level_order_result = levelOrderTraversal(root)
print("Level-order traversal of the binary tree:", level_order_result)
