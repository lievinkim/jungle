from typing import MutableSequence

def heap_sort(a: MutableSequence) -> None:

    # 루트에 값을 넣고 힙 구조를 맞추는 함수
    def down_heap(a: MutableSequence, left:int, right:int) -> None:

        temp = a[left] 
        
        parent = left 
        while parent < (right+1)//2: 
            cl = parent * 2 + 1 
            cr = cl + 1 
            
            if cr <= right and a[cr] > a[cl]:
                child = cr 
            else:
                child = cl
            
            print("child: {0}".format(child))
            print("a[child]: {0}".format(a[child]))

            if temp >= a[child]:
                break
            a[parent] = a[child] 
            parent = child 
        a[parent] = temp 

    n = len(a)

    # 자식이 있는 부모 노드부터 힙정렬 차근 차근히 진행
    for i in range(((n-1)-1)//2, -1, -1):
        down_heap(a, i, n-1)

    # 루트에 있는 애를 빼고 다시 힙 정렬하기
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        down_heap(a, 0, i-1)

print('힙 정렬을 수행합니다.')
num = int(input('원소 수를 입력하세요 : '))
x = [None]*num

for i in range(num):
    x[i] = int(input('x[{index}]: '.format(index=i)))

heap_sort(x)

print('오름차순으로 정렬했습니다.')
print(x)