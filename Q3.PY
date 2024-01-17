class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def arrayToCompleteBinaryTree(arr):
    if not arr:
        return None

    n = len(arr)
    root = TreeNode(arr[0])
    queue = [root]
    i = 1

    while i < n:
        current = queue.pop(0)

        if i < n and arr[i] is not None:
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1

        
        if i < n and arr[i] is not None:
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1

    return root

def inorderTraversal(root):
    result = []
    if root:
        result.extend(inorderTraversal(root.left))
        result.append(root.val)
        result.extend(inorderTraversal(root.right))
    return result

input_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

complete_binary_tree = arrayToCompleteBinaryTree(input_array)
 
inorder_result = inorderTraversal(complete_binary_tree)
print("In-order traversal of the complete binary tree:", inorder_result)
