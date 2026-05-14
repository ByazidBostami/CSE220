class TNode:
    def __init__(self, val, left=None, right=None):
        self.parent = None
        self.val = val 
        self.left = left 
        self.right = right 

def insert(root, key):
    newNode = TNode(key)
    if root is None:
        return newNode

    temp = root
    parent = None 
    while temp:
        parent = temp
        if key < temp.val:
            temp = temp.left
        elif key > temp.val:
            temp = temp.right
        else:
            return root # Key already exists
            
    # Connect the parent and the new node
    newNode.parent = parent
    if key < parent.val:
        parent.left = newNode
    else:
        parent.right = newNode
    
    return root

def inOrder(root):
    if root:
        inOrder(root.left)
        print(root.val, end=" ")
        inOrder(root.right)

def preOrder(root):
    if root:
        # FIX: Use print() to display the value, not the function name
        print(root.val, end=" ") 
        preOrder(root.left)
        preOrder(root.right)

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        # FIX: Use print() to display the value
        print(root.val, end=" ")

# Testing
root = None
values_to_insert = [20, 10, 30, 5, 15, 25, 35]

for i in values_to_insert:
    root = insert(root, i)

print("In-Order:")
inOrder(root)
print("\nPre-Order:")
preOrder(root)
print("\nPost-Order:")
postOrder(root)

def getMinRec(x):
    if x == None:
        return None
    if x.left == None:
        return x
    return getMinRec(x.left)

def getMin(x):
    while x.left:
        x = x.left

    return x


def getMax(cr_node):
    while cr_node.right:
        cr_node = cr_node.right 

    return cr_node

def searchBst(root, key):
    if root == None:
        return root 
    temp = root
    if key < root.val:
        searchBst(root.left, key)
    else:
        searchBst(root.right, key)

def sorted_arr_to_bst(arr, left, right):
    if left> right:
        return None
    mid = (left+right) //2
    root = TNode(arr[mid])
    root.left = sorted_arr_to_bst(arr , left , mid -1)
    root.right = sorted_arr_to_bst(arr, mid+1, right)

    return root

def arrToTree(arr, i =1 , parent = None):
    if i >= len(arr) or arr[i] is None:
        return None 
    root = TNode(arr[i])
    root.parent = parent

    root.left = arrToTree(arr, 2*i, root)
    root.right = arrToTree(arr, 2*i+1, root)

    return root

def inOrderSucc(x):
    if x.right:
        return getMin(x.right)
    y = x.parent
    while y is not None and x == y.right:
        x = y 
        y = y.parent
    return y

def inOrderpre(root, x):
    if x.left:
        return getMax(x.left)
    y = x.left
    while y is not None and x == y.left:
        x = y 
        y = y.parent

    return y 

def deleteWithSucce(root,key):
    if root is None:
        return root
    if key < root.val:
        deleteWithSucce(root.left, key)
    elif key > root.val:
        deleteWithSucce(root.right, key)

    else:
        if root.left is None and root.right is None:
            return None
        
        elif root.left is None:
            root.right.parent = root.parent
            return root.right

        elif root.right is None:
            root.left.parent = root.parent 
            return root.left 
        else:
            succ = getMin(root.right)
            root.val = succ.val
            root.right = deleteWithSucce(root.right, succ.val)
    return root

def delete_with_predecessor(root, key):
    if root is None:
        return root  # Base case: Tree is empty or node not found

    # Traverse to the left subtree if key is smaller
    if key < root.val:
        root.left = delete_with_predecessor(root.left, key)

    # Traverse to the right subtree if key is larger
    elif key > root.val:
        root.right = delete_with_predecessor(root.right, key)

    else:
        # ==== Case 1 | No subtree or children ====
        if root.left is None and root.right is None:
            return None  # Simply delete the node

        # ==== Case 2 | One subtree (one child) ====
        elif root.left is None:
            root.right.parent = root.parent
            return root.right
        elif root.right is None:
            root.left.parent = root.parent
            return root.left

        # ==== Case 3 | Two subtrees (two children) ====
        else:
            # Find in-order predecessor (rightmost node in left subtree)
            pred = getMax(root.left)
            root.val = pred.val  # Replace value with predecessor's value
            # Delete the in-order predecessor node recursively
            root.left = delete_with_predecessor(root.left, pred.val)

    return root