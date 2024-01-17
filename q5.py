class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_operator(char):
    return char in {'+', '-', '*', '/'}

def constructExpressionTree(postfix):
    stack = []

    for symbol in postfix:
        node = TreeNode(symbol)

        if not is_operator(symbol):
            stack.append(node)
        else:
          
            operand2 = stack.pop()
            operand1 = stack.pop()

            node.right = operand2
            node.left = operand1

            stack.append(node)

    
    return stack[0]

def inorderTraversal(root):
    result = []
    if root:
        result.extend(inorderTraversal(root.left))
        result.append(root.value)
        result.extend(inorderTraversal(root.right))
    return result

postfix_expression = "23*5+"


expression_tree = constructExpressionTree(postfix_expression)


inorder_result = inorderTraversal(expression_tree)
