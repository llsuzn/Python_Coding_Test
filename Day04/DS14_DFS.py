# 깊이 우선 탐색의 구현
class Graph:
    def __init__(self,size) -> None:
        self.SIZE = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)] # 2차원 배열

G1 = None
stack = [] # DFS 를 위한 스택
visitedAry = [] # 방문한 정점   
A,B,C,D = 0,1,2,3             

if __name__ == '__main__':
    # 그래프 생성
    G1 = Graph(4)
    # A 출발
    G1.graph[0][2] = 1 ; G1.graph[0][3] = 1 # (A,C) edge(간선) # (A,D) edge(간선)
    # B 출발
    G1.graph[1][2] = 1 # (B,C) edge(간선)
    # C 출발
    G1.graph[2][0] = 1; G1.graph[2][1] = 1; G1.graph[2][3] = 1 # (C,A) edge(간선)  # (C,B) edge(간선) # (C,D) edge(간선)
    # D 출발
    G1.graph[3][0] = 1; G1.graph[3][2] = 1 # (D,A) edge(간선) # (D,C) edge(간선)
    for item in G1.graph:
        print(item)

    current = A # 시작정점
    stack.append(current)
    visitedAry.append(current)

    while (len(stack) != 0): # 스택이 다 빌 때까지
        next = None
        for vertex in range(G1.SIZE):
            if G1.graph[current][vertex] == 1: # edge 가 있다면
                if vertex in visitedAry: # 이미 방문한 적이 있다면 탈락
                    pass
                else:
                    next = vertex # 방문한 적이 없다면 다음 정점으로
                    break
                    
        if next != None: # 다음 방문 할 정점이 있다면
            current = next
            stack.append(current)
            visitedAry.append(current)
        else: # 다음 방문할 정점이 없다면
            current = stack.pop()    

    print('방문순서 --> ',end=' ')
    for i in visitedAry:
        print(chr(ord('A')+i),end=' ')                