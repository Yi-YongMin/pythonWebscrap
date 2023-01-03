# name="nico"
# print(name.endswith("o")) endswith 같은 것을 method라고 부른다. 점 붙이고 쓰는 함수
days_of_week=["MON","TUE","WED","THUR","FRI"]
print(days_of_week.count("WED"))
print(days_of_week[3]) # start from 0.
#여기까지가 list. tuple도 비슷하나 불변성을 가진다는 점이 list 와의 차이이다. 둘다 인덱스로 접근할 때는 []쓴다.
days=("MON","TUE","WED","THUR","FRI") # this is tuple.
print(days.count("WED"))
player = { #dictionary 구조를 만들 때에는 등호로 속성을 표시하지 않고 :를 쓴다. key:value
    "name":"nico",
    'age': 12,
    'alive':True,
    'favorite':["soccer","baseball"]
}
print(player)
print(player.get('favorite'))# 아래와 동치이다.
print(player['favorite'])
player.pop('age') #key & value 제거
print(player)
player['lv']=1
print(player)
player['favorite'].append("basketball")#player안에있는 키의 이름이 'favorite'이다. 키가 갖는 value가 리스트이고 그 리스트가 가지는 built_in함수 append 활용가능.
print(player)