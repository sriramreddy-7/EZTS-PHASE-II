import heapq
def prims(graph,start):
    parents={}
    weights={} 
    queue=[]
    visited=set()
    for vertex in graph:
        weights[vertex]=6969696969
    weights[start]=0
    print(weights)
    heapq.heappush(queue,(0,start))
    while len(queue) !=0:
        cur_weight,cur_node=heapq.heappop(queue)
        if cur_node in visited:
            continue
        for weight,node in graph[cur_node]:
            if node not in visited and weight < weights[node]:
                weights[node]=weight
                parents[node]=cur_node
                heapq.heappop(queue,(weight,node))
            visited.add(cur_node)
        
        


graph={
    'A':[(1,'B'),(3,'E')],
    'B':[(1,'A'),(2,'E'),(1,'D'),(4,'C')],
    'C':[(4,'B'),(1,'D')],
    'D':[(1,'B'),(1,'C'),(2,'E')],
    'E':[(3,'A'),(2,'B'),(2,'D')]
}

mst=prims(graph,'A')