'''
- 100*100 차원 배열 [0]으로 만들어버리기
- 입력값으로 덮어씌우기 (어떻게 받지?)

- 2 도착점부터 시작
- 양옆 > 위 로 방향 전환하면서 1인 지점따라 이동
    > 델타
- 0행 까지 이동
- 끝나고 나서 X값 추출
'''
T = 10
ladder = []
x = 0
y = 0
nx = [1, -1, 0]
ny = [0, 0, 1]

for _ in range(T):
    tc = int(input())
    ladders = [list(map(int, input().split())) for _ in range(100)]
    
    for i in range(100):
        if ladders[99][i] == 2:
            start = i
            break
    # 인덱스
    ci = 99
    cj = start
    # 양쪽으로 진입할 때 끝까지 가라. >>>
    
    
    while ci>0:
        if cj-1>=0 and ladders[ci][cj-1] == 1:
            while cj-1>=0 and ladders[ci][cj-1] == 1:
                cj -= 1
        
        elif cj+1<=99 and ladders[ci][cj+1] == 1:
            while cj+1<=99 and ladders[ci][cj+1] == 1:
                cj += 1

        ci -= 1
    
    print(f'#{tc}', cj)
    



    # if ladders[][start-1] == 1 :         #왼쪽

    # if:         #오른쪽
    #     pass
    # if:         #위로가기
    #     pass


    