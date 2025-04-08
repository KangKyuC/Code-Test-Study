# 시간 32ms
# 문자열 비교를 이용한 방식/방법

number = input()

while int(number):
    length = len(number)
    for idx in range(length//2):
        if number[idx] != number[length-idx-1]:
            print("no")
            break
    else:
        print("yes")
    number = input()