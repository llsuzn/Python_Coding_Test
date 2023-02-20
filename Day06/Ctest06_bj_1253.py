# 백준 1253번
import sys
input = sys.stdin.readline
N = int(input())
Count = 0
A = list(map(int, input().split()))
A.sort()

for k in range(N):
    find = A[k]
    i,j = 0,N-1
    while i < j: 
        if A[i] + A[j] == find:
            if i != k and j != k:
                Count += 1
                break
            elif i == k: i += 1
            elif j == k: j -= 1
        elif A[i] + A[j] < find:
            i += 1
        elif A[i] + A[j] > find:
            j -= 1
print(Count)                                            

