def selectionSort(ary):
    n = len(ary)
    for i in range(0,n-1): # 첫번째 인덱스 값부터 마지막 인덱스 까지 
        minIdx = i
        for k in range(i+1,n): # 바깥 for문에서 지정된 인덱스의 값과 지정된 인덱스 보다 뒤에 정렬된 데이터의 값을 비교하여 최솟값 찾기
            if (ary[minIdx] > ary[k]):
                minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]                
        ary[minIdx]  = tmp

    return ary

dataAry = [188,162,168,120,50,150,177,105]

print('정렬 전 --> ',dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 --> ',dataAry)