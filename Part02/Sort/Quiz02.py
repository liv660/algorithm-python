# p.178 실전문제 02 - 위에서 아래로

# 1. 입력
N = int(input())

data = []
for i in range(N):
    data.append(int(input()))

# 2. 라이브러리를 통한 내림차순 정렬
data.sort(reverse=True)


# 3. 출력
S = ""
for i in data:
    S += (str(i) + " ")
print(S)

