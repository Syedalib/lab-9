class TreeNode:
    def _init_(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_bst(root, prev=[None]):
    if root is None:
        return True
    if not is_bst(root.left, prev):
        return False
    if prev[0] is not None and root.value <= prev[0].value:
        return False
    prev[0] = root
    return is_bst(root.right, prev)