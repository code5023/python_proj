total_lines = 10                    # 표현 할 전체 라인수
lines = int(total_lines / 2)        # 상단 하단을 구분하기 위한 중간 라인

print("===== 다이아몬드 =====")

# # 우측만 튀어나온 형태
# for i in range(1, total_lines):
#     if i <= lines:
#         zero = lines - i
#         one = i
#         print("1 " * one)
#     else:
#         zero = i - lines
#         one = total_lines - i
#         print("1 " * one)

# # 좌측만 튀어나온 형태
# for i in range(1, total_lines):
#     if i <= lines:
#         zero = lines - i
#         one = i
#         print(" " * zero + "1")
#     else:
#         zero = i - lines
#         one = total_lines - i
#         print(" " * zero + "1")

# 전체 다이아몬드 형태
for i in range(1, total_lines):
    if i <= lines:
        zero = lines - i
        one = (i * 2) - 1
        print("0" * zero + "1" * one + "0" * zero)
    else:
        zero = i - lines
        one = ((total_lines - i) * 2) - 1
        print("0" * zero + "1" * one + "0" * zero)
