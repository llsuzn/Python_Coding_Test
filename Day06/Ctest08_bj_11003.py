# 백준 11003번 최솟값 찾기

from collections import deque
N, L = map(int, input().split())
mydeque = deque()
now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i],i))
    if mydeque[0][1] <= i - L: # 범위에서 벗어난 인덱스 값은 덱에서 제거한다
        # mydeque[0][1] : 덱의 1번째 데이터의 인덱스 값
        mydeque.popleft()
    print(mydeque[0][0], end=' ')   