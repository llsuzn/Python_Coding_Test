# 
def solution(numbers):
    answer = 0
    for i in numbers:
        answer += 1

    return answer / len(numbers)

if __name__ == '__main__':
    numbers = [1,2,3,4,5,6,7,8,9,10]
    print(solution(numbers))
    numbers = [89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    print(solution(numbers))