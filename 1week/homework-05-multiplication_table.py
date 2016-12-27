print("===== 구구단 =====")

def calc():
    try:
        input_num = int(input("몇 단을 계산하시겠습니까?\n"))

        if type(input_num) is str:
            raise ValueError
        elif input_num < 2 or input_num > 9:
            print("2 ~ 9 사이의 숫자를 입력해주세요.")
            calc()
        else:
            print("===== 계산 결과 =====")
            for i in range(1, 10):
                print("{} * {} = {}".format(input_num, i, input_num * i))
    except ValueError:
        print("숫자만 입력할 수 있습니다.")
        calc()

calc()
