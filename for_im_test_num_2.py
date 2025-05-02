T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    player = list(map(int,input().split()))

    ans = 0

    for i in range(N):
        team = 0
        for j in range(N):
            if player[i]-K <= player[j] <= player[i]:
                team += 1
        ans = max(team,ans)
    print(f'#{tc} {ans}')