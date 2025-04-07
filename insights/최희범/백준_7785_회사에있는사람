1차 시도 - 맞았긴했으나 시간이 너무걸림 2620ms
---
commute_dic = {}

result = []

num_input = int(input()) # 시행 횟수 입력

def record_status(name, status):
    commute_dic[name] = status # 이름과 상태를 나타낼 딕셔너리 작성

for _ in range(num_input): # name, status 입력하기 위한 for 문
    name, status = [str for str in input().split()]
    record_status(name, status)

for name, status in commute_dic.items(): # commute_dic의 key, values 순회
    if status == "enter": # status가 "enter"이면
        result.append(name) # name을 result에 넣어라

result.sort(reverse=True)

for enter in result:
    print(enter)

----
ChatGPT 힌트 : 자료구조를 바꿔볼 수도 있어.
→ 딕셔너리 대신 set을 활용하면, 'enter' 상태인 사람만 추적하고 불필요한 삭제나 상태 변경 연산을 줄일 수 있어.
----

2차 시도 - 시간은 거의 유사하다

commute_dic = set()

num_input = int(input()) # 시행 횟수 입력

result = []

for _ in range(num_input): # name, status 입력하기 위한 for 문
    name, status = [str for str in input().split()]
    if status == "enter": # 입력에 "enter"가 있으면 dic에 name을 추가하고
        commute_dic.add(name)
    elif status == "leave": # 입력에 "leave"가 있으면 dic에 name을 제거
        commute_dic.remove(name)

result = list(commute_dic) # set인 commute_dic을 result에서 리스트화 
result.sort(reverse=True) # 알파벳 역순으로 재정렬

for enter in result:
    print(enter)
