def bubbleSort(ary):
    n = len(ary)
    num = 1
    for end in range(n-1, 0,-1):
        changeYN = False
        print(f' 사이클{num} -->{ary}')
        num += 1
        for cur in range(0, end):
            if (ary[cur]> ary[cur+1]):
                ary[cur],ary[cur+1] = ary[cur+1],ary[cur]
                changeYN = True
        if not changeYN:
            break
    return ary

dataAry = [55,88,11,33,22,44,99,66,77]

print('정렬 전 --> ',dataAry)
dataAry = bubbleSort(dataAry)
print('정렬 후 --> ',dataAry)