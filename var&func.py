#파이썬은 변수선언이 따로 없네? 원래 이랬나 C랑 다르다.
def f1():
    print("This is f1")
def f2(a=10):
    print("기본값은",a,"이다")
f1()
f2()
f2(15) # 함수에 디폴트값이 아닌 다른값 입력
def tax(money):
    return money*0.3
def pay_tax(tax):
    print("Thanks for paying",tax)
pay_tax(tax(100)) #리턴 함수를 또 다른 함수에 넣음으로써 간략화.
