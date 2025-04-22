'''
최대점수 = 최대 팡 - 최소 팡

팡 = 가로세로합 = 팡 되는 부분의 열값합 + 행값합 - 그 해당좌표값.

1. 입력값 받기

2. 함수만들기 _ 열 합+ 행합-두번더해지는값 , 그리고 반환함.

3. 구하기 _ 함수에집어넣어서 구하기, 그다음 score 빈리스트에 집어넣기

3. 각 차이값을 비교한 뒤 제일 큰 값 꺼내기 (if else로 분기)
'''

#입력값받기
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    balloonmap = [list(map(int, input().split())) for _ in range(N)]
# 함수만들기
    def pang(y,x, balloonmap):
        row_sum = sum(balloonmap[y])
        col_sum = sum(balloonmap[r][x] for r in range(N))
        score = row_sum + col_sum - balloonmap[y][x]
        # print(score)
        return score
    
#  score에 집어넣기
    scores = []
    for y in range(N):
        for x in range(N):         
                scores.append(pang(y,x, balloonmap))


# 제일 큰 값 꺼내기 < 최댓값? 최솟값? 차이를 일일이 구해서 최대값?
    ans = max(scores) - min(scores)

print(f'#{tc} {ans}')
