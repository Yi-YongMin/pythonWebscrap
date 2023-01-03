# name="nico"
# print(name.endswith("o")) endswith 같은 것을 method라고 부른다.
days_of_week=["MON","TUE","WED","THUR","FRI"]
print(days_of_week.count("WED"))
print(days_of_week[3]) # start from 0.
#여기까지가 list. tuple도 비슷하나 불변성을 가진다는 점이 list 와의 차이이다. 둘다 인덱스로 접근할 때는 []쓴다.
days=("MON","TUE","WED","THUR","FRI") # this is tuple.
print(days.count("WED"))
