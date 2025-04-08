#a = input()
#if enter -> append()
#if leave -> pop
# n = int(input())
# for i in range (n) :
#     a = input().split()
#     b=[]
#     if a == 'enter':
#         b.append(a)
#         print(b)
#     elif a == 'leave':
#         b.remove(a)
#         print(b)
#     i += 1
    
# print(b)

#반복문으로 출입 , 퇴근 기록
# pop으로 스택 관리

#두 글자가 같이 들어감 사람, 출입 여부
#키값으로 같이 매칭이 되는 딕셔너리가 더 용이

import sys
# n = int(sys.stdin.readline()) #출입기록의 수
n =int(input())
temp = dict()

for _ in range(n):
    a,b = map(str,sys.stdin.readline().split())
    
    if b == 'enter':
        temp[a] = b
        
    else:
        del temp[a]
        
temp = sorted(temp.keys(),reverse = True)

for i in temp:
    print(i)