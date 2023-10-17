# 큐에 넣기
# count가 1,2이면 dequeue > enqueue
# count가 3이면 dequeue 출력

import sys
from collections import deque

N, K = list(map(int, sys.stdin.readline().split()))

queue = deque([num+1 for num in range(N)]) #1부터 N까지 초기화

cnt = 1
answer_lst = []

while(len(queue)): #큐가 빌 때까지
    if cnt == K:
        answer_lst.append(queue.popleft()) #큐에서 dequeue만
        cnt = 1 #1로 초기화
    elif cnt < K:
        queue.append(queue.popleft()) #큐에서 dequeue 후 enqueue까지
        cnt += 1

print('<', end = '')
answer_lst = list(map(str, answer_lst)) #모든 요소를 문자로 바꾸기
print(', '.join(answer_lst), end = '')
print('>')