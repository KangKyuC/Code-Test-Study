# 가독성 및 네이밍 리펙토링
## senior_dict > senior_info
## 7 > DAYS_PER_WEEK = 7 전역변수 선언
## 재사용성이 높은 Senior에 대한 객체화 > 재사용성 높은 함수를 활용
## sorted() 에 집합을 넘기면 반드시 리스트를 반환해 주기 때문에 list로 묶을 필요가 없음.
import sys

# 상수
DAYS_PER_WEEK = 7

# 각 요소에 대한 명시가 됨. 기존은 idx 기반 호출 [0], [1], [2]
# 타입에 대한 안전성도 부족했음.
# 유지보수도 어렵고
# 단일 책임 원칙(SRP)에 의거
# 데이터와 데이터에만 의미가 있는 로직을 한 곳에 모음.
## 가독성이 올라가고, 버그 위험이 내려가고, 유지보수성이 늘어남.

class Senior:
    def __init__(self, week, day, cost):
        self.week = week
        self.day = day
        self.cost = cost

    def day_index(self):
        return (self.week - 1) * DAYS_PER_WEEK + (self.day - 1)

    def can_afford(self, money):
        return money >= self.cost


def read_seniors(n, input):
    seniors = {}
    for _ in range(n):
        name, w, d, p = input().split()
        seniors[name] = Senior(int(w), int(d), int(p))
    return seniors


def read_balances(n, input):
    balances = {}
    for _ in range(n):
        name, m = input().split()
        balances[name] = int(m)
    return balances


def get_affordable_days(seniors, balances):
    days = set()
    for name, money in balances.items():
        senior = seniors.get(name)
        if senior and senior.can_afford(money):
            days.add(senior.day_index())
    return sorted(days)


def longest_consecutive(days):
    if not days:
        return 0
    max_run = curr_run = 1
    prev = days[0]
    for d in days[1:]:
        if d == prev + 1:
            curr_run += 1
        else:
            curr_run = 1
        prev = d
        if curr_run > max_run:
            max_run = curr_run
    return max_run


def main():
    input = sys.stdin.readline
    count = int(input())

    seniors = read_seniors(count, input)
    balances = read_balances(count, input)

    days = get_affordable_days(seniors, balances)
    print(longest_consecutive(days))


if __name__ == '__main__':
    main()
