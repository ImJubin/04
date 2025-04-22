'''
입력값
i부터 j개의 돌을 i번째 돌 색으로 바꾸기

i번째 돌 색 저장
바꾸는 범위 지정

'''


T = int(input())
for tc in range(1,T+1):
    N,M = map(int, input().split())
    stones = list(map(int, input().split()))

    for _ in range(M):
        i,j = map(int, input().split())
        
        color = stones[i - 1]  # 기준 색 (0번째부터 인덱스)

        for k in range(j):
            idx = i - 1 +k
            if idx<N:
                stones[idx] = color                
            else:
                break
    print(f'#{tc}', *stones)