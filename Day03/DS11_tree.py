# 이진 탐색 트리 구현

# 전역변수 선언
memory = []
root = None
nameAry = ['블랙핑크','레드벨벳','마마무','에이핑크','걸스데이','트와이스'] # 정렬은 앞 글자 국어사전 숫자 순서대로

class TreeNode:
    def __init__(self) -> None:
        self.left = None
        self.data = None
        self.right = None


if __name__ == '__main__':
    node = TreeNode()
    node.data = nameAry[0]
    root = node
    memory.append(node)

    for name in nameAry[1:]:
        node = TreeNode()
        node.data = name
        
        current = root
        
        while True:
            if name < current.data: # Root 노드의 왼쪽
                if current.left == None:
                    current.left = node
                    break
                current = current.left
            else: # Root 노드의 오른쪽
                if current.right == None:
                    current.right = node
                    break
                current = current.right
        memory.append(node)

    print('이진 탐색 트리 완료')    
    print('%20s' %  root.data )
    print('%20s'%'／＼')
    print('%13s'%root.left.data,'%8s'%root.right.data)
    print('%13s'%'／＼','%10s'%'＼')
    print('%8s'%root.left.left.data,'%5s'%root.left.right.data,'%9s'%root.right.right.data)

# 검색
search = '데이식스'

current = root
while True:
    if search == current.data:
        print(search,'을(를) 찾음')
        break
    elif search < current.data:
        if current.left == None:
            print(search,'못 찾음!')
            break
        else:
            current = current.left
    else:
        if current.right == None:
            print(search,'못 찾음!')
            break
        else:
            current = current.right        
