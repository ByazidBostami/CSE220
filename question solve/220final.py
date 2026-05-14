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