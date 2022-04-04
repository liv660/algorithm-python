# p.360 기출문제 24 - 안테나
import sys

# 1. 입력
N = int(sys.stdin.readline())
house = list(map(int, sys.stdin.readline().split()))

# 2. 집이 있는 곳 check
isHouse = ['' for _ in range(max(house) + 1)]
for i in house:
    isHouse[i] = True

# 3. 퀵정렬? (피벗 사용)
def isLocHouse(loc):
    if isHouse[loc]: return True
    return False

def setAntenna(left_loc, right_loc):  # 최소 위치값(loc)에 집이 없는 경우
    isLeftHouse = isLocHouse(left_loc)
    isRightHouse = isLocHouse(right_loc)

    if isLeftHouse and not isRightHouse: # 왼쪽으로 갔을 때의 위치만 집인 경우
        return print(left_loc)
    elif isRightHouse and not isLeftHouse: # 오른쪽으로 갔을 때의 위치만 집인 경우
        return print(right_loc)
    elif isLeftHouse and isRightHouse: # 양방향 모두 집인 경우
        return print(min(left_loc, right_loc))
    else:   # 양방향 모두 집이 아닌 경우
        return setAntenna(left_loc-1, right_loc+1)

# 4. 안테나 설치 위치 출력
aver_loc = (sum(house) // N)  # 최소 위치값
if isLocHouse(aver_loc):  # 집이 있으면
    print(aver_loc)
else:
    setAntenna(aver_loc-1, aver_loc+1)

