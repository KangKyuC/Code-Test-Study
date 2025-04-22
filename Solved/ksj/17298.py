#오큰수
#NGE(i)라는 수열이 존재한다. a[i]에 있는 수에 대해 오른쪽에 있는 가장 큰수
#없으면 return -1

    
#1. 리스트 형태로 선언
#2. 리스트 첫번째(리스트에서0번째) 수부터 -1번째 숫자랑 비교해서 크냐 작냐 같냐
#3. 작으면 다음번째 수열로 넘어가서 진행
#4. 비교하고자 하는 애보다 크면 리턴으로 멈춰
#5. 비교하려는 애 수열을 더해서 진행
#6. 비교하려는 애랑 같은 수여도 다음거로 진행해야함
#7. for문으로 범위 안에서 계속 비교하게끔 해줘
#8. if 문으로 비교하려는 애보다 크면 리턴으로 포문 break
#9. 근데 그냥 while문으로 진행시키는게 낫지 않나?
# import sys
# n = int(sys.stdin.readline()) #수열의 갯수
# number = list(map(int,sys.stdin.readline().split())) #그 안에서 수열로 넣어 
# answer = [-1]*n #더 큰수 없으면 -1로 나와야함
# for i in range(n):
#     j = i + 1
#     while j < n: #수열 안에서
#         if number[j] > number[i]:
#             answer[i] = number[j]
#             break
#         j += 1

# print(*answer)




#1트트
# for s in range (1, n):
#     i = number.index(0)
#     while i < number[s]:
#         answer.append(number[s])
    
# print(answer)

#아예 틀린 접근이었음
# 문제는 스택으로 접근해야함
#(*answer)는 리스트를 한줄로 출력할때 사용

#2트 
#그러면 리스트 인덱스를 두가지로 만들어서 비교해서 넣어보자.
#근데 너무 오래 걸림 결과는 동일. 시간초과

#3트
#해당문제는 O(N)으로 풀어야하는 문제.
#한마디로 리스트 첫번째부터 -1번 인덱스까지 비교하면서
#스택 문제 -> 선입후출
import sys
n = int(sys.stdin.readline())
a = list(map(int,sys.stdin().readline().split()))
NGE = [-1]*n
stack = [0]

for i in range(1,n):
    while stack and a[stack[-1]] < a[i]:
        NGE[stack.pop()] = a[i]
        
    stack.append(i)
    
print(*NGE)