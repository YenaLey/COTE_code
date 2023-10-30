import sys

N, M = map(int, sys.stdin.readline().split())

set1 = set()
set2 = set()
answer = set()

for _ in range(N):
    set1.add(sys.stdin.readline().strip()) #\n 제거

for _ in range(M):
    set2.add(sys.stdin.readline().strip())

answer = sorted(set1.intersection(set2))

print(len(answer))
for name in answer:
    print(name)