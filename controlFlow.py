#python standard library 를 자주 봐라 https://docs.python.org/3/library/
# a=10
# if a>10:
#     print("a is greater than 10")
# elif a== 10:
#     print("a is 10")
# else :
#     print("a")#C랑 거의 유사하다. 위에서 먼저 조건을 충족하면 아래까지 읽지않음.
# # age=input("How much?")
# # print("it is",age)
# age=int(input("How old r u?")) #int로 애워싸면서 age에게 숫자를 대입
# if age>=18:
#     print("U can")
# else :
#     print("U can't")
# True and True==True
# True and False==False
# False and True==False
# False and False==False #이거 디논 게이트 1*1 1*0 0*1 0*0 게이트(or)도 디논때 배운대로

from random import randint,random  #random 모듈에서 randint 라는 함수를 쓰겠다는 선언
achoice=int(input("Choose number"))
bchoice= randint(1,100)
playing=True
while playing:
    if achoice==bchoice:
        print("SAME")
        playing=False
    elif achoice > bchoice:
        print("당신이 선택한 숫자가 더 높음.")
        achoice = int(input("Choose number"))
    else :
        print("당신이 선택한 숫자가 더 낮음.")
        achoice = int(input("Choose number"))






