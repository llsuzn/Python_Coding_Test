# 중복된 값을 허용하는 퀵정렬
def quickSort(ary):
    n = len(ary)
    if n <= 1:
        return ary
    
    pivot = ary[n // 2] # 퀵 정렬의 기준값을 중간값으로 선택
    leftAry, midAry, rightAry = [],[],[]

    for num in ary:
        if num < pivot:
            leftAry.append(num)
        elif num > pivot:
            rightAry.append(num)
        else:
            midAry.append(num)
    return quickSort(leftAry) + midAry + quickSort(rightAry)

dataAry = [120,120,188,150,168,50,50,162,120,50]

print('정렬 전 --> ', dataAry)
dataAry = quickSort(dataAry)
print('정렬 후 --> ', dataAry)    