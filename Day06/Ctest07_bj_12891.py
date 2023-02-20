# # 백준 12891번_DNA비밀번호 

# checklist = [0] * 4 # ACGT 
# mylist = [0] * 4 # 부분 문자열의 ACGT개수
# checkSecret = 0

# def myadd(c): # 새로 들어온 문자를 처리
#     global checklist, mylist, checkSecret
#     if c == 'A':
#         mylist[0] += 1
#         if mylist[0] == checklist[0]: checkSecret += 1
#     elif c == 'C':
#         mylist[1] += 1
#         if mylist[1] == checklist[1]: checkSecret += 1
#     elif c == 'G':
#         mylist[2] += 1
#         if mylist[2] == checklist[2]: checkSecret += 1
#     elif c == 'T':
#         mylist[3] += 1
#         if mylist[3] == checklist[3]: checkSecret += 1

# def myremove(c): # 제거되는 문자를 처리
#     global checklist, mylist, checkSecret
#     if c == 'A':
#         mylist[0] += 1
#         if mylist[0] == checklist[0]: checkSecret -= 1
#         mylist[0] -= 1
#     elif c == 'C':
#         mylist[1] += 1
#         if mylist[1] == checklist[1]: checkSecret += 1
#         mylist[1] -= 1
#     elif c == 'G':
#         mylist[2] += 1
#         if mylist[2] == checklist[2]: checkSecret += 1
#         mylist[2] -= 1
#     elif c == 'T':
#         mylist[3] += 1
#         if mylist[3] == checklist[3]: checkSecret += 1
#         mylist[3] -= 1

# S, P = map(int, input().split())
# Result = 0
# A = list(input())
# checklist = list(map(int, input().split()))

# for i in range(4):
#     if checklist[i] == 0:
#         checkSecret += 1

# for i in range(P):
#     myadd(A[i])

# if checkSecret == 4:
#     Result += 1

# for i in range(P,S):
#     j = i - P
#     myadd(A[i])
#     myremove(A[j])
#     if checkSecret == 4:
#         Result += 1

# print(Result)

import sys
input = sys.stdin.readline

S,P = map(int, input().split())
A = list(map(str,input().rstrip()))
a,c,g,t = map(int, input().split())

result = 0

start = A[:P]
tmp = {"A" : 0, "C" : 0, "G" : 0, "T" : 0}
for i in start:
    tmp[i] += 1

cnt = 0
if tmp["A"] >= a and tmp["C"] >= c and tmp["G"] >= g and tmp["T"] >= t:
    cnt += 1

start_idx = 0
end_idx = start_idx + P

for i in range(len(A)-P):
    tmp[A[start_idx+i]] -= 1 # 슬라이딩 : 1번째 데이터를 지우고
    tmp[A[end_idx+i]] += 1 # 마지막 데이터 추가하기
    if tmp["A"] >= a and tmp["C"] >= c and tmp["G"] >= g and tmp["T"] >= t:
        cnt +=1

print(cnt)