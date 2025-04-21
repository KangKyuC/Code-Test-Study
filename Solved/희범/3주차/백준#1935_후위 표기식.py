"""
메모리: 33432 KB, 시간: 36 ms
https://www.acmicpc.net/submit/1935/93425649
"""

import sys
import operator # 사칙연산자
input = sys.stdin.readline


input_num = int(input()) # 입력된 변수의 개수   
stack_num = 0 # 입력된 변수의 개수를 확인
input_expr = list(input().strip()) # 후위 표기식
stack = [] # 후위 표기식을 리스트로 변환
stack_dict = {}

for idx, i in enumerate(input_expr):
    if i not in ["+", "-", "*", "/"] and i not in stack_dict: # 사칙연산자가 아닌 경우, 그리고 stack_dict에 없는 경우
        stack_dict[i] = int(input())
        stack_num += 1
        if stack_num == input_num: # 입력된 변수가 N개와 같으면
            break # 종료

# 사칙연산 operator 모듈
ops_dict = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

for i in input_expr: # 후위 표기식을 계산
    if i in ops_dict: # 사칙연산자인 경우
        next_num = stack.pop() # 후위 표기식에서 다음 요소
        prev_num = stack.pop() # 후위 표기식에서 이전 요소
        stack.append(ops_dict[i](prev_num, next_num)) # 계산된 결과를 stack에 추가
    else:
        stack.append(stack_dict[i]) # 후위 표기식에서 피연산자인 경우


print(f"{stack[0]:.2f}") # 최종 결과
