# 단순 연결리스트 구현
# https://docs.google.com/presentation/d/1cvNArbuAhtvtsdOhoSHz5JV4dNBM4xHS/edit#slide=id.p30
# 전역변수
memory = []
head,current, pre = None,None,None
dataArray = ['다현','쯔위','사나','정연','지효']

class Node:
    def __init__(self) -> None:
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return

    print(current.data,end=' -> ')
    while current.link != None:
        current = current.link
        if current.link == None:
            print( current.data)
        else:
            print(current.data,end=' -> ')

def insertNode(findData,insertData):
    global memory, pre, current, head

    # 첫 번째 노드 삽입
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return

    # 중간 노드 삽입
    current = head # current를 제일 앞으로
    while current.link != None:
        pre = current
        current = current.link

        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return
    
    # 마지막 노드 삽입
    node = Node()
    node.data = insertData
    current.link = node

def deleteNode(deleteData):
    global memory, head, current, pre

    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        return
    
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

# 노드 검색
def findNode(finddata):
    global memory, pre, current, head

    current = head
    if current.data == finddata:
        return current
    while current != None:
        current = current.link
        if current.data == finddata:
            return current
    else: 
        return Node() # 빈 노드 반환

if __name__ == '__main__':
    node = Node()
    node.data = dataArray[0]
    head = node
    memory.append(node)

    for data in dataArray[1:]: # 두 번쨰 노드 이후
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)

    printNodes(head)

    insertNode("다현","화사")
    printNodes(head)

    deleteNode("다현")
    printNodes(head)

    result = findNode("정연")
    print(result.data) 