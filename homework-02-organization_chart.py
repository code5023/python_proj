# 회사 조직도
class Person:
    name = "default"        # 이름
    age = 0                 # 나이
    gender = "default"      # 성별: man | woman

class CoWorker(Person):
    position = "대리"    # 직급

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

print("===== 직원의 신상정보를 입력해주세요 =====")

worker_name = input("이름을 입력해주세요 : ")
worker_age = input("나이를 입력해주세요 : ")
worker_gender = input("성별을 입력해주세요 : ")
worker_position = input("직급을 입력해주세요 : ")

coWorker = CoWorker(worker_name, worker_age, worker_gender)
position = coWorker.position

# 직급을 출력하는 메소드
def return_position():
    if worker_position is "":
        return position
    else:
        return worker_position

# 프로필을 출력
print("===== 직원 정보 =====")
print("이름 : {}\n나이 : {}\n성별 : {}\n직급 : {}\n".format(coWorker.name, coWorker.age, coWorker.gender, return_position()))
