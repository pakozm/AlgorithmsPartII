import heapq
import sys

def loadGraph(filename):
    f = open(filename)
    V,E = map(int,f.readline().rstrip().split())
    graph = [ [] for x in range(V) ]
    for i in range(E):
        u,v,w = map(int,f.readline().rstrip().split())
        u-=1
        v-=1
        graph[u].append((v,w))
        graph[v].append((u,w))
    return graph

def heapPush(Q, x, w):
    heapq.heappush(Q, (w, x))

def heapPop(Q):
    w,x = heapq.heappop(Q)
    return x,w

def MSTCost(g):
    def process(Tv, Q, g, u):
        Tv.add(u)
        for v,w in g[u]:
            if v not in Tv:
                heapPush(Q, (u,v), w)
    Tv = set() # vertices of MST
    Q = []
    cost = 0
    process(Tv, Q, g, 0)
    for i in range(len(g)-1):
        u,v,w = 0,0,None
        while v in Tv:
            x,w = heapPop(Q)
            u,v = x
        cost += w
        process(Tv, Q, g, v)
    return cost

graph = loadGraph(sys.argv[1])
print MSTCost(graph)
