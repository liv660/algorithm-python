# p.149 실전문제 03 - 음료수 얼려 먹기

# CASE: N = 4, M = 5
# 0 0 1 1 0
# 0 0 0 1 1
# 1 1 1 1 1
# 1 0 0 0 0

N, M = map(int, input().split())
# print("세로:", N, "\t가로:", M)
d
# 1. 2차원 배열로 입력 저장
ice = []

for i in range(N):
    ice.append(list(map(int, input().split())))

# 2. DFS 방식? 으로 탐색하기
def getIce(x,y):
    if(x == N or y == M): return

    p = ice[x][y]
    if(p == 0 and ice[x][y+1] == 0): # p, p+1 두 요소가 모두 0일 때
        ice[x][y+1] = -1
        getIce(x, y+1)
    else: getIce(x+1, y)


getIce(0,0)
print("ice:", ice)
print("result:", ice.count(0)) # ice 에서 0인 요소 개수 세기