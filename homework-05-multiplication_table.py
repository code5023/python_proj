print("===== 구구단 =====")
input_num = input("몇 단을 계산하시겠습니까?\n")
print("===== 계산 결과 =====")
def calc(num):
    try:
        if type(int(num)) is str:
            raise ValueError
        elif int(num) is 0:
            raise ZeroDivisionError
        else:
            for i in range(1, 10):
                print("{} * {} = {}".format(num, i, int(num) * i))
    except ValueError:
        print("숫자만 입력할 수 있습니다.")
    except ZeroDivisionError:
        print("0이 아닌 다른 수를 입력해주세요.")

calc(input_num)
