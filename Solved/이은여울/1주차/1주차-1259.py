while True:
    s = input()
    # input이 0이면 루프 탈출
    if s == '0':
        break
    # string의 가운데 부분까지만 반복
    for i in range(len(s)//2):
        # string의 앞 부분과 뒷 부분이 같은지 확인
        if s[i] != s[-1-i]:
            print('no')
            break
    else:
        print('yes')


    
            