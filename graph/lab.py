class Node:
    def __self__(self, vertex, weight =0):
        self.vertex = vertex
        self.weight = weight
        self.next = None

vertices = 7
edge =[
    (0,1,5),(0,2,10),(1,3,2),(1,4,4),
    (2,3,7), (2,5,1), (3,6,3), (3,0,8), 
    (4,5,6), (4,6,9), (5,1,2), (6,2,5)
]

#0a
adj_matrix = [None]* vertices
for i in range(vertices):
    adj_matrix[i] = [0]*vertices

for i in range(12):
    u, v, w = edge[i]
    adj_matrix[u][v] = w 

#0b
adj_list = [None]*vertices
for i in range(12):
    u, v, w = edge[i]
    newNode = Node(v,w)
    if adj_list[u] is None:
        adj_list[u] = newNode
    else:
        temp = adj_list[u]
        while temp:
            temp = temp.next
        temp.next = newNode

#Task1a
def max_degree_matrix(matrix):
    v_count = len(matrix)
    max_degree = -1
    best_v = -1
    for i in range(v_count):
        degree = 0
        for j in range(v_count):
            if matrix[i][j] !=0:
                degree +=1

        if degree > max_degree:
            max_degree = degree
            best_v = i 
    return best_v, max_degree

def maxDegreeList(lst):
    v_count = len(lst)
    max_degree = -1
    v_count = -1

    for i in range(v_count):
        degree = 0 
        temp = lst[i]
        while temp:
            degree +=1 
            temp = temp.next 
        if degree > max_degree:
            max_degree = degree
            v_count = i
    return v_count, max_degree

