# 백준 1260번_DFS와 BFS
from queue import Queue
N,M,Start = map(int, input().split())
A = [[] for _ in range(N + 1)]

for _ in range(M):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N + 1):
    A[i].sort()

def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)                     

visited = [False] * (N + 1)
DFS(Start)

def BFS(v):
    Qu = Queue()
    Qu.put(v)
    visited[v] = True
    while Qu.empty() != True:
        now_None = Qu.get()
        print(now_None,end=' ')
        for i in A[now_None]:
            if not visited[i]:
                visited[i] = True
                Qu.put(i)

print()
visited = [False] * (N + 1)
BFS(Start)                