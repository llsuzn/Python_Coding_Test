# 큐 구현

# queue full 확인
def isqueuefull():
    global SIZE, queue, front, rear
    if (rear == SIZE -1):
        return True
    else:
        return False
        
# queue empty 확인
def isqueueempty():
    global front, rear
    if (front == rear):
        return True
    else:
        return False 

# enqueue
def enqueue(data):
    global queue, rear
    if (isqueuefull()):
        print('큐가 꽉 찼습니다.')
    else:
        rear += 1
        queue[rear] = data

# dequeue
def dequeue():
    global queue, front, rear,SIZE
    if (isqueueempty()):
        print('큐가 비었습니다.')
        return None
    else:
        front += 1
        data = queue[front]
        queue[front] = None
        for i in range(front+1,SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1        
        return data

# 큐에서 front+1 위치 데이터 확인
def peek():
    global queue, front
    if (isqueueempty()):
        print('큐가 비었습니다.')
        return None
    else:
        return queue[front+1]

# 메인 코드 부분
if __name__ == '__main__':
    # 전역변수 선언 부분
    SIZE = int(input("큐의 크기를 입력하세요 ==> "))
    queue = [None for _ in range(SIZE)]
    front = rear = -1

    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 : ')

        if select.lower() == 'x':
            break
        elif select.lower() == 'i':
            data = input('입력할 데이터 ==> ')
            enqueue(data)
            print('큐 상태 : ',queue)
        elif select.lower() == 'e':
            data = dequeue()
            print('추출된 데이터 ==> ',data)
            print('큐 상태 : ',queue)
        elif select.lower() == 'v':
            data = peek()
            print('확인된 데이터 ==> ',data)
            print('큐 상태 : ',queue)
        else:
            print('입력이 잘못됨')

    print('프로그램 종료!')

