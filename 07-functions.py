# 함수 functions
# 입력값 parameters, 반환값 return

def hello_friends(name):
    print("hello, {}".format(name))

name1 = "bae3am"
name2 = "hj"
name3 = "tom"
name4 = "jin"
name5 = "bae3am"
name6 = "hj"
name7 = "tom"
name8 = "jin"
# print("hi, {}".format(name1))
# print("hi, {}".format(name2))
# print("hi, {}".format(name3))
# print("hi, {}".format(name4))
# print("hi, {}".format(name5))
# print("hi, {}".format(name6))
# print("hi, {}".format(name7))
# print("hi, {}".format(name8))

hello_friends(name1)
hello_friends(name2)
hello_friends(name3)
hello_friends(name4)
hello_friends(name5)
hello_friends(name6)
hello_friends(name7)
hello_friends(name8)

# 1) 입력값 o, 반환값 o
def sum(a, b):
    return a + b
# 2) 입력값 o, 반환값 x
def hello_friends(name):
    print("hello, {}".format(name))
# 3) 입력값 x, 반환값 o
def return_1():
    return 1
# 4) 입력값 x, 반환값 x
def hello_world():
    print("hello world")

num_1 = return_1()
print(num_1)
