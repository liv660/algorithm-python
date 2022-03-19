# p.311 기출문제 01 - 모험가 길드

n = int(input())
# print("전체 모험가: ", n)

data = list(map(int, input().split()))
# print("모험가 공포도: ", data)

data.sort(reverse = True)
# print("내림차순 정렬: ", data)

index = 0;
result = 0;

while index < n:
  if (data[index] <= n):
    index += data[index]
    result += 1;
  else:
    break

print("그룹: ", result)