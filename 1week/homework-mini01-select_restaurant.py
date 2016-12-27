import random

type_list = ["한식", "중식", "일식"]      # 음식 종류 리스트

# 음식의 종류를 랜덤으로 되돌려주는 메소드
def select_type():
    return type_list[random.randint(0, len(type_list) - 1)]

print("음식 종류 : {}".format(select_type()))
