# 스택 전체 구현

# 스택이 꽉 찼는지 확인하는 함수
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1):
        return True
    else:
        return False
# 스택이 비어있는지 확인하는 함수
def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False
# 스택에 데이터를 삽입하는 함수        
def push(data):
    global SIZE, stack, top
    if isStackFull():
        print('스택이 꽉 찼습니다.')
    else:
        top += 1
        stack[top] = data
# 스택에서 데이터를 추출하는 함수
def pop():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택이 비었습니다.')
        return None
    else:
        data = stack[top]
        stack[top] = None
        top -= 1
        return data
# 스택에서 top 위치의 데이터를 확인하는 함수
def peek():
    global SIZE, stack, top
    if isStackEmpty():
        print('스택이 비었습니다.')
        return None
    else:
        return stack[top]

top = -1

if __name__ == '__main__':
    SIZE = int(input("스택 크기를 입력하세요: "))
    stack = [None for _ in range(SIZE)]
    while True:
        select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 : ')
        if select.lower() == 'x': # 종료
            print('프로그램 종료')
            break
        elif select.lower() == 'i':
            data = input('입력할 데이터: ')
            push(data)
            print(f'스택상태 : {stack}')
        elif select.lower() == 'e':
            data = pop()
            print(f'추출된 데이터 : {data}')
        elif select.lower() == 'v':
            data = peek()
            print(f'확인된 데이터 : {data}')
            print(f'스택 상태 : {stack}')
        else:
            print('입력이 잘못됨')

    print('프로그램 종료')     
