import random

# 가위바위보 게임
weapons_list = {
    1 : "가위",
    2 : "바위",
    3 : "보"
}
score = 0                                    # 점수

print("===== 가위/바위/보 게임 시작 =====")
user_name = input("사용자의 이름을 입력해주세요.")
print("반갑습니다. {}님".format(user_name))

# 유저가 선택한 값을 알려주는 메소드
def print_selected_weapons(select_weapons):
    try:
        select_weapons / 1
        return weapons_list[select_weapons]
    except:
        return "잘못된 번호"

# 컴퓨터가 선택한 값을 알려주는 메소드
def computer_selected_weapons():
    return weapons_list[random.randint(1,3)]

# 이겼을경우 점수를 더하는 메소드
def add_score():
    global score
    score = score + 1

# 승패를 구분하는 메소드
def contend_for_victory(user_weapon, com_weapon):
    win = "승리하였습니다."
    defeat = "패배하였습니다."
    print("===== 결과 =====")
    if user_weapon is com_weapon:
        print("비겼습니다.")
    elif user_weapon is weapons_list[1]:
        if com_weapon is weapons_list[2]:
            print(defeat)
        if com_weapon is weapons_list[3]:
            add_score()
            print(win)
    elif user_weapon is weapons_list[2]:
        if com_weapon is weapons_list[1]:
            add_score()
            print(win)
        if com_weapon is weapons_list[3]:
            print(defeat)
    elif user_weapon is weapons_list[3]:
        if com_weapon is weapons_list[1]:
            print(defeat)
        if com_weapon is weapons_list[2]:
            add_score()
            print(win)

for i in range(0, 4):
    if i < 3:
        select_weapons = input("'1.{} / 2.{} / 3.{}' 중에 하나를 선택해주세요.\n".format(weapons_list[1], weapons_list[2], weapons_list[3]))
        computer_weapon = computer_selected_weapons()
        print("컴퓨터는 " + computer_weapon + "를 선택하였습니다.")
        print("{}님은 ".format(user_name) + print_selected_weapons(int(select_weapons)) + "를 선택하셨습니다.")
        contend_for_victory(print_selected_weapons(int(select_weapons)), computer_weapon)
    else:
        print("===== 최종 점수 =====")
        print(score)
