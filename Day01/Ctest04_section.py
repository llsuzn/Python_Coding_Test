import sys
input = sys.stdin.readline
N,M = map(int,input().split())
numbers = list(map(int,input().split()))
sums = [0] # 0번째 인덱스
temp = 0

for i in numbers:
    temp += i
    sums.append(temp)

for i in range(M):
    x,y = map(int,input().split())
    print(sums[y]-sums[x-1]) 