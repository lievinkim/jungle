import sys

lst = []
max_num = 0
index_num = 0

for i in range(0, 9):
    lst.append(int(sys.stdin.readline()))

for i in lst:
    if i > max_num:
        max_num = i
        index = lst.index(i)+1

print(max_num)
print(index)