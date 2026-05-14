import numpy as np
class Node:
    def __init__(self, elem, next = None):
        self.elem = elem
        self.next = next


n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)

n1.next = n2
n2.next = n3
n3.next = n4

head = n1

def iteration(head):
    temp = head
    while temp:
        print(temp.elem, end ="-->")
        temp = temp.next

    print()

iteration(head)

def arrTOlinkList(arr):
    if len(arr) == 0:
        return None 
    
    head = Node(arr[0])
    tail = head 

    for i in range(1, len(arr)):
        newNode = Node(arr[i])
        tail.next = newNode
        tail = tail.next

    return head
arr = np.array([10, 20, 30, 40])
arrL = arrTOlinkList(arr)
iteration(arrL)
    
def countNode(head):
    count = 0
    temp = head 
    while temp:
        
        temp = temp.next 
        count+=1

    return count 
print(countNode(arrL))

def traverse_all(head):
    count = 0 
    temp = head 
    while temp:
        print(temp.elem, end= "-->")
        temp = temp.next 
        count +=1

    print(f"\nTotal loop run: {count}")
    print(f"Total comparison in while: {count + 1}")
    print(f"Stopped at Null/None: {temp}")
    print("-------------------------------------")
traverse_all(arrL)

def get_tail(head):
    temp = head 
    while temp.next:
        temp = temp.next
    return temp

tail = get_tail(arrL)
print(tail.elem)

def appendLL(head, data):
    newNode = Node(data)
    if head == None:
        head = newNode
        return
    tail = get_tail(head)
    print(tail.elem)
    tail.next = newNode

appendLL(arrL, 199)
iteration(arrL)

def prependLL(head, d):
    newNode = Node(d)
    newNode.next = head
    return newNode

nw = prependLL(arrL, 299)
iteration(nw)

def indexOf(head, target):
    temp = head 
    cr_index = 0
    while temp:
        if temp.elem == target:
            return cr_index ,temp.elem , temp #temp for get node 
            
        temp = temp.next 
        cr_index +=1 

    return -1
index = indexOf(arrL, 199)
print(index)
def getNode(head, index):
    current_node = head
    count = 0 # index
    while current_node != None:
        if count == index:
            return current_node # Returning the Node
        current_node = current_node.next # moving forward
        count += 1
    return None

def setNode(head, idx, newElem):
    temp = getNode(head, idx)
    if temp:
        temp.elem = newElem
        print("Updated")
    else:
        print("Invalid idx")

def setNodeWgetNode(head,idx, newE):
    temp = head 
    newidx = 0
    isUpdate = False
    while temp:
        if newidx == idx:
            temp.elem = newE
            isUpdate = True
        temp = temp.next
        newidx += 1 
    if isUpdate:
        print("successfull")
    else:
        print("Invalid index")
setNodeWgetNode(arrL, 2, 200)
iteration(arrL)

def insertAt(head, idx, elem):
    size = countNode(head)

    if idx<0 or idx> size :
        return "Invalid index"
    elif idx == 0:
        newNode = Node(elem)
        newNode.next = head 
        head = newNode

    else:
        newNode = Node(head)
        predecessor = getNode(head, idx-1)
        successor = predecessor.next #getNode(head, idx)
        predecessor.next = newNode
        newNode.next = successor

        return head
    
def removeAt(head, idx):
    size = countNode(head)
    if size == 0:
        head = head.next 
    else:
        pres = getNode(head, idx-1)
        rmNode = pres.next
        suc = getNode(head, idx+1)
        pres.next = suc 

    return head
        
        
def copyList(head):
    if head == None:
        return None 
    copy_head = Node(head.elem)
    copy_tail = copy_head
    
    temp = head.next 
    while temp:
        newNode = Node(temp.elem)
        copy_tail.next = newNode
        copy_tail = copy_tail.next
        temp = temp.next 

    return copy_head