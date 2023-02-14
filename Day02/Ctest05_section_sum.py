# 백준 11660번 
# 구간 합 구하기 5
import sys
input = sys.stdin.readline
n,m = tuple(map(int, input().split()))
A = [[0]*(n+1)] # 배열 크기 할당A[n]
D = [[0]*(n+1)for _ in range(n+1)] #2차원 배열 D[n+2][n+2] 크기 할당
#2차원 배열 입력받기
for i in range(n):
    rows = list(map(int, input().split()))
    A_row = [0] + rows
    A.append(A_row)
#2차원 합 배열 만들기(D)
for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]
print(A)
#구간 합
for _ in range(m):
    x1,y1,x2,y2 = map(int,input().split())
    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
    print(result)
