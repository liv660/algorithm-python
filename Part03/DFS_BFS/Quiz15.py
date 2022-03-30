# p.339 기출문제 15 - 특정 거리의 도시 찾기
from sys import stdin

# 1. 입력
N, M, K, X = map(int, stdin.readline().split())

map_list = [[] for _ in range(N+1)]
for i in range(M):
    temp_list = list(map(int, stdin.readline().split()))
    map_list[temp_list[0]].append(temp_list[1])
# print("map_list:", map_list)

# 2. 도시 X부터 거리가 K인 도시 찾기
shortest_list = []
all_list = []
def goToCity(x, d): # d = 거리
    # 거리 K만큼 온 경우 return
    if d == K:
        all_list.append(x)
        return

    # 최단 경로 check
    if d != 0:
        shortest_list.append((x, d))

    # +1 만큼 도시로
    for i in map_list[x]:
        goToCity(i, d+1)

goToCity(X,0)
# print("최단 check:", shortest_list)

# 3. 최단거리가 아닌 경우 제외
for i in shortest_list:
    if i[0] in all_list:
        all_list.remove(i[0])

# 4. 출력
if len(all_list) == 0:
    print(-1)
else:
    for i in all_list:
        print(i)