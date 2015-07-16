class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None




def hasPathSum(root, sum):
    return helper(root,sum,0)


def helper(root, sum, preSum):
    if (root == None):
        return False
    elif ((preSum + root.val) == sum and root.left == None and root.right == None):
        return True
    elif ((preSum + root.val) != sum and (root.right == None and root.left == None)):
        return False
    elif (root.right != None and root.left == None):
        return helper(root.right, sum, preSum + root.val)
    elif (root.left != None and root.right == None):
        return helper(root.left, sum, preSum + root.val)
    else:
        return helper(root.right, sum, preSum + root.val) or helper(root.left, sum, preSum + root.val)

if __name__ == "__main__":
    root = TreeNode(1)
    left = TreeNode(2)
    root.left = left
    print(hasPathSum(root,1))


