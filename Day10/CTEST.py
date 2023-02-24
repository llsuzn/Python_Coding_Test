def solution(n, lost, reserve):
    people = []
    studentN = n - len(lost)
    for i in range(1,n+1):
        people.insert(i-1,i)

    for i in lost:
        num1 = i+1
        num2 = i-1
        if num1 in reserve:
            studentN += 1
            reserve.remove(num1)
            continue
        elif num2 in reserve:
            studentN += 1            
            reserve.remove(num2)
            continue
    return studentN


n = 5
lost = [2, 4]
reserve = [1,3,5]

print(solution(n, lost, reserve)) # return 5


n = 5
lost = [2, 4]
reserve = [3]

print(solution(n, lost, reserve)) # return 4


n = 3
lost = [3]
reserve = [1]

print(solution(n, lost, reserve)) # return 2