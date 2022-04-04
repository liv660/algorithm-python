# p.359 기출문제 23 - 국영수
import sys

# 1. 입력
N = int(sys.stdin.readline())
students = []
for i in range(N):
    input_data = sys.stdin.readline().split()
    students.append((input_data[0],int(input_data[1]), int(input_data[2]), int(input_data[3])))

# 2. (4 - 3 - 2 - 1) 순서로 정렬
sorted_students = sorted(   # 국어 내림차순
                    sorted( # 영어 오름차순
                        sorted( # 수학 내림차순
                            sorted(students, key=lambda s:s[0]) # 이름 오름차순
                        , key=lambda s:s[3], reverse=True)
                    , key=lambda s:s[2]), key=lambda s:s[1], reverse=True)

# 3. 출력
S = ""
for i in sorted_students:
    S += (i[0] + "\n")
print(S)
