class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid+1:])

    return root

def inorderTraversal(root):
    result = []
    if root:
        result.extend(inorderTraversal(root.left))
        result.append(root.val)
        result.extend(inorderTraversal(root.right))
    return result


sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]


balanced_bst = sortedArrayToBST(sorted_array)


inorder_result = inorderTraversal(balanced_bst)
print("In-order traversal of the balanced BST:", inorder_result)
