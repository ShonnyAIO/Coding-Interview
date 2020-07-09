class TreeNode {
    constructor(val) {
    this.val = val
    this.right = null
    this.left = null
    }
    }
    
    const isValidBST = (root) => {
    const helper = (node, lower, upper) => {
    if (!node) return true
    const { val } = node
    
    if (val <= lower || val >= upper) return false
    if (!helper(node.right, val, upper)) return false
    if (!helper(node.left, lower, val)) return false
    return true
    }
    
    return helper(root, -Infinity, Infinity)
    }
    
    const node = new TreeNode(10)
    node.left = new TreeNode(5)
    node.right = new TreeNode(15)
    
    /// True
    console.log(isValidBST(node))
    
    node.right.left = new TreeNode(9)
    
    /// False
    console.log(isValidBST(node))