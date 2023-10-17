#time out

import sys

input = sys.stdin.readline

N = input()
lstN = input().split()

M = input()
lstM = input().split()

lstN.sort()
card_count_str = ""
for card in lstM:
    cnt = 0
    if card in lstN:
        idx = lstN.index(card)
        cnt += 1
        while(lstN[idx+1] == card):
            cnt += 1
            idx += 1
        card_count_str += str(cnt)+" "
    else:
        card_count_str += "0"+" "

print(card_count_str)


#time out

import sys

input = sys.stdin.readline

N = input()
lstN = input().split()

M = input()
lstM = input().split()

card_count_str = ''
for card in lstM:
    card_count_str += str(lstN.count(card)) + ' '

print(card_count_str)


#성공

import sys
input = sys.stdin.readline

N = input()
lstN = input().split()

M = input()
lstM = input().split()

cntDict = dict()

for card in lstN:
    if card in cntDict:
        cntDict[card] += 1
    else:
        cntDict[card] = 1

for hisCard in lstM:
    if hisCard in cntDict:
        print(cntDict[hisCard], end = ' ')
    else:
        print(0, end = ' ')