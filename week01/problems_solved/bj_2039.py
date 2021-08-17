# https://www.acmicpc.net/problem/2309

import sys

dwarfs = []

for t in range(0, 9):
    dwarfs.append(int(sys.stdin.readline()))

total = 0
for dwarf in dwarfs:
    total += dwarf

diff = total - 100
answer = []

for i in range(0, 8):
    for j in range(i+1, 9):
        if dwarfs[i] + dwarfs[j] == diff:
            answer.append(dwarfs[i])
            answer.append(dwarfs[j])

dwarfs.remove(answer[0])
dwarfs.remove(answer[1])

for dwarf in sorted(dwarfs):
    print(dwarf)