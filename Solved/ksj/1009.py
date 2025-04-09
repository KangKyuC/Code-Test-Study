#data case number = t
#a,b = int(input())
#지수 형태. 지수를 10으로 나눈 나머지로 경우의 수를 따질것 
# a = 1 나머지 1
# a = 2 나머지 2, 4, 8, 6
# a = 3 나머지 3, 9, 7, 1
# a = 4 나머지 4, 6
# a = 5 나머지 5
# a = 6 나머지 6
# a = 7 나머지 7, 9, 3, 1
# a = 8 나머지 8, 4, 2, 6
# a = 9 나머지 9, 1
# a = 10 나머지 0

#1,5,6 은 몇 제곱해도 자기자신
#a**b b = 0 -> 10으로 나눠떨어지거나 0 -> 
import sys
t= int(input())
a,b = map(int,sys.stdin.readline().split())
num = (a**b)%10
for _ in range(t):
    if num == 0:
        print('10')
        
    elif num in [1,5,6]:
        print(num)
        
    elif num in [4,9]:
        