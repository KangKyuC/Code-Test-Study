'''
INPUT:
8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1

OUTPUT:
9 (흰색 종이 개수)
7 (파란색 종이 개수)

재귀 함수

1. 해당 영역이 모두 같은 색인지 확인
2. 만일 모두 같은 색이면, 해당 색의 종이 개수를 하나 증가 -> 함수 종료
3. 다른 색이 섞여 있으면(크기가 1X1이 아니면) 그 영역을 4개의 작은 영역으로 나누기
3-1. 각각의 작은 영역에 대해 다시 1번 작업부터 시작

예시:
cut_paper(0,0,8)
'''

N= int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

white_papers = 0
blue_papers = 0


def cut_paper(row, col, size):
    # print(f"--- Processing region: row={row}, col={col}, size={size} ---")
    # 첫 번째 칸 색 확인
    first_cell_color = paper[row][col]
    # print(f"  First cell color in this region: {first_cell_color}")
    all_color_same = True

    # 1단계: 현재 영역 색상 통일성 검사 단계
    for i in range(row, row+size): # 현재 영역의 행 범위
        for j in range(col, col+size): # 현재 영역의 열 범위
            if paper[i][j] != first_cell_color:
                all_color_same = False # 다른 색 발견
                # print(f"  Mismatch found at paper[{i}][{j}] (value: {paper[i][j]}).")
                break 
        if not all_color_same: # 안쪽 루프를 돌면서 all_color_same이 False로 바뀐 적이 있을 경우
            break # 바깥쪽 루프도 탈출


    # 2단계: 판단 및 다음 행동 결정 단계
    if all_color_same: #종이가 모두 같은 색일 때
        # print(f"  Region ({row},{col},{size}) is ALL SAME COLOR: {first_cell_color}.")
        if first_cell_color == 0:
            global white_papers
            white_papers += 1
            # print(f"  Incremented white_papers. Current white: {white_papers}")
        else:
            global blue_papers
            blue_papers += 1
            # print(f"  Incremented blue_papers. Current white: blue: {blue_papers}")
        
        return
    else:
        # all_color_same이 False일 때(색이 섞여 있을 때)
        new_size = size//2
        # print(f"  Region ({row},{col},{size}) is MIXED. Dividing into 4 sub-regions of size {new_size}.")
        # print(f"    -> Calling for TL: ({row}, {col}, {new_size})")
        cut_paper(row, col, new_size) # 왼쪽 위
        # print(f"    -> Calling for TR: ({row}, {col + new_size}, {new_size})")
        cut_paper(row, col+new_size, new_size) # 오른쪽 위
        # print(f"    -> Calling for BL: ({row + new_size}, {col}, {new_size})")
        cut_paper(row+new_size, col, new_size) # 왼쪽 아래
        # print(f"    -> Calling for BR: ({row + new_size}, {col + new_size}, {new_size})")
        cut_paper(row+new_size, col+new_size, new_size) # 오른쪽 아래
    return 

cut_paper(0, 0, N)

# 결과
print(white_papers)
print(blue_papers)