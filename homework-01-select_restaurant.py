import random

# 맛집 고르기
menu = input("메뉴를 선택해주세요.( * 숫자 입력)\n1.한식\n2.중식\n3.일식\n")
KOREAN_FOOD = 1                               # 한식
CHINESE_FOOD = 2                              # 중식
JAPANESE_FOOD = 3                             # 일식
korean_dish = ["핵겹살", "핵장국", "핵떡갈비"]      # 한식 리스트
chinese_dish = ["핵짜장면", "핵짬뽕", "핵탕수육"]   # 중식 리스트
japanese_dish = ["핵초밥", "핵텐동", "핵카츠"]     # 일식 리스트

print("===== 추천 맛집 =====")

# 선택한 메뉴에 따라 다른 값을 출력하는 메소드
def select_random_menu(select_menu_num):
    try:
        if type(int(select_menu_num)) is str:
            raise ValueError
        else:
            if select_menu_num is KOREAN_FOOD:
                return random.choice(korean_dish)
            elif select_menu_num is CHINESE_FOOD:
                return random.choice(chinese_dish)
            else:
                return random.choice(japanese_dish)
    except ValueError:
        return "숫자로만 입력해주세요."

print(select_random_menu(menu))
