'''
집합은 내부 C언어 처리를 통해 해시테이블로 구조화되어 있음.
리스트는 포인터 리스트를 관리하고 있고, 해당 포인터는 객체를 지칭하고 있어 각 데이터를 지칭하고 있는 구조임.
이 때,
'''

import sys

input = sys.stdin.readline
num_input = int(input()) # 시행 횟수 입력

result = []
result_app = result.append
result_rem = result.remove

def people_remain(name, status):
    if status == "enter": # 입력에 "enter"가 있으면 dic에 name을 추가하고
        result_app(name)
    elif status == "leave": # 입력에 "leave"가 있으면 dic에 name을 제거
        result_rem(name)

for _ in range(num_input): # name, status 입력하기 위한 for 문
    name, status = [str for str in input().split()]
    people_remain(name, status)

result.sort(reverse=True)

for enter in result:
    print(enter)

