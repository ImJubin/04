'''

범위 체크, 범위 밖에 있으면 break

같은색이면> 뒤집고
다른 색이면 그대로

하나를 기준으로

'''
T = int(input())
for tc in range(1, T+1):
    
    N, M = map(int, input().split())
    stones = list(map(int, input().split()))

    for _ in range(M):
        i, j = map(int, input().split())
        c_c = i-1

        k = 0
        for k in range(1, j+1):
            c_l = i-k-1
            c_r = i+k-1
            if 0<= c_l < N and 0 <= c_r < N:
                if stones[c_l] == stones[c_r]:
                    stones[c_l] = (stones[c_l]+1)%2
                    stones[c_r] = (stones[c_r]+1)%2

            else:
                break

    print(f'#{tc}', *stones)


             