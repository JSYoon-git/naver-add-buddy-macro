from datetime import datetime, timedelta


min_ = "5분 전"
hour = "4시간 전"
day = "2022. 5. 28."

#############################
b = ['a', 'a', 'b', 'b', 'c', 'd','e']

b_count = {} # 각 원소의 등장 횟수를 카운팅할 딕셔너리

for i in b:
    try: # 이미 등장한 값의 경우
        b_count[i] += 1
    except: # 처음 등장한 값의 경우
        b_count[i] = 1

print(b_count) # {'a': 2, 'b': 2, 'c': 1, 'd': 1}

new_b = []
new_d = []

for k, v in b_count.items():
    if v >= 2: # n회 이상 등장한 원소로도 변경 가능
        new_b.append(k)
    else:
        new_d.append(k)
print(new_d)
print(new_b) # ['a', 'b']
############################

if "분" in day:
    diff = 1
elif "시간" in day:
    diff = 1
else:
    day_list = day.split(".")
    time1 = datetime(int(day_list[0]), int(day_list[1]), int(day_list[2]))
    time2 = datetime.now()
    diff =(time2 - time1).days
    print(diff)
    
if datetime.now() <= datetime(2022, 6, 1, 10, 10, 0):
    print(True)
else:
    print(False)