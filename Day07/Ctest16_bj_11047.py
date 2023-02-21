# 백준 11047번_동전 0
N, K = map(int,input().split())
A = [0] * 10

for i in range(N):
    A[i] = int(input())

count = 0
for i in range(N-1,-1,-1):
    if A[i] <= K:
        count += K // A[i]
        K = K % A[i]

print(count)        