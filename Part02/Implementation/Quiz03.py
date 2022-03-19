# p.118 실전문제 03 - 게임 개발
  # 22.03.13 함수화하여 코드 정리 필요

N, M = map(int, input().split())
# print(N, M)

A, B, d = map(int, input().split())

# map Setting (육지: True, 바다: False)
map_list = []
for i in range(N):
  data = list(map(int, input().split()))
  temp = []
  for j in data:
    if (j == 0):
      temp.append(True)
    else:
      temp.append(False)
  map_list.append(temp)
# print(map_list)
map_list[A][B] = 0

cnt = 1  # 캐릭터가 방문한 칸의 개수
dA = [-1, 0, 1, 0]  # 북 동 남 서 , 세로
dB = [0, 1, 0, -1]  # 북 동 남 서 , 가로

while True:
  nA = A + dA[d]
  nB = B + dB[d]
  print("nA, nB", nA, nB)

  # map 벗어나면 아무일도 일어나지 않음, 방향만 전환한다.
  if (nA < 0) or (nB < 0) or (nA > N) or (nB > M):
    d -= 1
    if (d < 0): d = 3
    print("d", d)
  else:
    print("오긴오니?")
    if (map_list[nA][nB]):  # 육지이면서 안가본 곳
      map_list[nA][nB] = 0  # 이제 가본 곳으로 check
      A, B = nA, nB
      cnt += 1
    elif (map_list[nA][nB] == 0):  # 육지이면서 가본 곳
      flag = d
      if (d + 2 > N): flag = 0
      mA = A + dA[d + 2]  # 한 칸 뒤로 back

      if (map_list[mA][B] == False or 0):
        # 가본 데나 바다이면 stop
        break

      map_list[A][B] = 0  # 뒤로 이동한 곳도 가본 곳으로 check
      cnt += 1
    else:  # 바다
      break  # 그냥 break 말고 뒤로 가기 함수를 호출해야지 cnt가 제대로 될 듯
    d -= 1
    print("d", d)
    if (d < 0): d = 3
print("cnt", cnt)