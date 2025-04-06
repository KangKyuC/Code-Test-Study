#10진법 기준으로 데이터 끊음.
#10 대 정해짐.
#데이터 갯수 = a^b

#T의 갯수에 해당하는 a,b 쌍의 갯수가 존재한다. -> 
# 리스트 컴프리핸션으로 쓰면 간단하지 않을까
# 리스트 컴프리핸션 쓰는 법
# numbers = []
# for n in range(1, 10+1):
#     numbers.append(n)
    
# [n for n in range(10)]


t = int(input())
a,b =map(int,input().split())
numbers = a,b
print(numbers)


anum = [numbers for _ in range(t) ((a**b)//10)]

print(anum)
