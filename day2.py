def say_hello():
    print("안녕하세요! 파이싼의 세계에 오신 걸 환영합니다.")

say_hello()
say_hello()
say_hello()

print("-----------------------------------")

def greet(name):
    print(f"반갑습니다, {name}님!")

greet("윤성")
greet("지민")

print("-----------------------------------")

def add(a,b):
    return a + b

result = add(10, 20)
print(f"두 수의 합: {result} ")

print("-----------------------------------")

number = int(input("숫자를 입력하세요: "))
print(type(number))

for i in range(1,10):
    print(f"{number} *{i} = {number*i}")

print("-----------------------------------")
#x = int(input("숫자를 입력하세요: "))

def gugu():
    for y in range(1,10):
        print(f"{x}*{y} = {x*y}")

gugu(9)

        


    