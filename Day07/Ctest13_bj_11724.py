# 백준 11724번_ 연결 요소의 개수
import sys
sys.setrecursionlimit(10 ** 6)
# 파이썬에선 재귀 최대깊이 제한 1000번 까지 가능
# 따라서 재귀호출 제한을 10 ** 6 번으로 바꾸어줌
input = sys.stdin.readline
n,m = map(int, input().split())
A = [[] for i in range(n+1)]
visited = [False] * (n+1)

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)


for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)