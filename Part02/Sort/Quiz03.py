# p.180 실전문제 03 - 성적이 낮은 순서대로 학생 출력하기

# 1. 입력
N = int(input())

data = []
for i in range(N):
    data.append((input().split()))
# print(data)

# 2. 계수 정렬
cntData =["" for _ in range(101)]
for i in data:
    # print("인덱스:", i[1], "\t\t값:", i[0])
    cntData.insert(int(i[1]), i[0])

# 3. 출력
S = ""
for i in cntData:
    if i != "":
        S += (i + " ")
print(S)
