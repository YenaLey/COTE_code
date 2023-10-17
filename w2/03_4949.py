# 1. 왼쪽 괄호 만나면 스택에 push
# 2. 오른쪽 괄호 만나면 pop해서 비교
# NO 조건
# 1. 마지막에 스택에 남아있다면
# 2. 오른쪽 괄호 만났을 때 pop한 괄호와 다를 때

from collections import deque

while(1):

    str = input()

    if str == '.': #종료 조건
        break

    stack = deque()

    answer = True # true로 초기화
    
    for s in str:

        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if len(stack) == 0 or stack.pop() != '(':
                answer = False
                break
        elif s == ']':
            if len(stack) == 0 or stack.pop() != '[':
                answer = False
                break

    if len(stack):
        answer = False

    if answer:
        print("yes")
    else:
        print("no")