def findInsertIdx(ary,data):
    findIdx = -1
    for i in range(0,len(ary)):
        if (ary[i] > data):
            findIdx = i
            break
            
    if findIdx == -1:
        return len(ary)
    else:
        return findIdx

testAry = []
insPos = findInsertIdx(testAry, 55)
print('삽입할 위치 --> ',insPos)

testAry = [33,44,99]
insPos = findInsertIdx(testAry, 55)
print('삽입할 위치 --> ',insPos)

testAry = [33,55,44,99,1111]
insPos = findInsertIdx(testAry, 100)
print('삽입할 위치 --> ',insPos)
