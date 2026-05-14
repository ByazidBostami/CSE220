def build_key(root):
    def traverse(Node, level):
        if Node is None:
            return 
        
        if Node.left is None and Node.right is None:
            if level%2 == 0:
                return Node.elem 
            return 
        right_key = traverse(root.right, level+1)
        left_key = traverse(root.left, level+1)

        return right_key+left_key
    return traverse(root, 0)


def cpuscheduler(tasks, k):
    max_heap = MaxHeap()
    for task in tasks:
        max_heap.insert(task)

    for i in range(1, k+1):
        highest_priority = max_heap.extract()

        print("Highest", highest_priority)
        print("highest",i)

def iscomplete(network):
    n = len(network)

    for i in range(n):
        met_participants = set()
        temp = network[i]
        while temp:
            dest = int(temp.destination)
        if dest != i:
            met_participants.add(dest)

        if len(met_participants) < n-1:
            return False
    return True

def getEncoding(root, st):
    def findPath(node, chr, path):
        if node is None:
            return None 
        
        if node.left is None and node.right is None:
            if node.value == chr:
                return path
            return None 
        left_search = findPath(node.left, chr, path +"0")
        if left_search is not None:
            return left_search
        return findPath(node.right, chr , path +"1" )
    result = ""
    for chr in st:
        char_path = findPath(root, chr, "")
        result += char_path    
    return result

def mergeLL(h1,h2):
    def getLength(head):
        length = 0
        while head:
            length +=1
            head = head.next 
        return length
    
    len1 = getLength(h1)
    len2 = getLength(h2)
    ptr1 = h1 
    ptr2 = h2 
     
    if len1> len2: 
        for _ in range(len1-len2):
            ptr1 = ptr1.next 

    elif len2> len1:
        for _ in range(len2-len1):
            ptr2 = ptr2.next 
    intersecNode = None 
    while ptr1 and ptr2:
        if ptr1 == ptr2:
            intersecNode = ptr1
            break
        ptr1 = ptr1.next 
        ptr2 = ptr2.next
    
    if intersecNode is None:
        return None 
    if h1 == intersecNode:
        return h2
    curr = h1 
    while curr.next != intersecNode:
        curr = curr.next 
    curr.next = h2 

    return h1


def second_max(root):
    # arr[0] stores the maximum, arr[1] stores the second maximum
    # Initialize with negative infinity
    arr = [float('-inf'), float('-inf')]
    
    # Helper function to traverse the tree
    def traverse(node, arr):
        if node is None:
            return
            
        val = node.elem
        
        # If current value is greater than the max
        if val > arr[0]:
            arr[1] = arr[0] # Demote old max to second max
            arr[0] = val    # Set new max
        # If current value is greater than second max (and strictly less than max)
        elif val > arr[1] and val < arr[0]:
            arr[1] = val
            
        # Traverse left and right children
        traverse(node.left, arr)
        traverse(node.right, arr)
        
    # Start traversal
    traverse(root, arr)
    
    # Return the second highest value
    return arr[1]