# 백준 1717_집합의 표현
import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
N, M = map(int,input().split())
parent = [0] * (N + 1)

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a]) # 경로 압축함으로써 실행 시간 단축됨 
        return parent[a]
    
def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        if a < b: # 값이 더 작은 쪽을 부모로
            parent[b] = a
        else:
            parent[a] = b

def checkSame(a,b):
    a = find(a)
    b = find(b)
    if a == b:
        return True
    return False

for i in range(0,N+1):
    parent[i] = i

for i in range(M):
    question, a, b = map(int, input().split())
    if question == 0:
        union(a,b)
    else:
        if checkSame(a,b):
            print("YES")
        else:
            print("NO")                                 