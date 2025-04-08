# 틀렸습니다!
# 최초 제출 시 print를 한 줄씩 하지 않은 문제로 틀렸음.
# 이에 Unpacking Opertator * 를 사용하고, print seperate를 사용해 출력
# 두 번째 제출 시에는 사람이 "한 번만 출퇴근" 하는 걸로 오판하며 문제를 풀이한 것이 문제가 되었음.
# 현재의 코드에서는 1회 입출근은 정말 잘 처리하지만, 복수번의 출퇴근 시, 처리가 안 됨.
# 즉, 한 번 출근한 사람이 퇴근 후 다시 출근하면 set 집합 연산에 따라 그냥 퇴근한 걸로만 판단됨.

''' Edge Case
3
John enter
John leave
John enter
'''

import sys
input = sys.stdin.readline

comm_dict = {"enter": [], "leave": []}

for _ in range(int(input())):
    cmd = input().split()
    comm_dict[cmd[1]].append(cmd[0])

print(*sorted((set(comm_dict["enter"])- set(comm_dict["leave"])), reverse = True), sep='\n')