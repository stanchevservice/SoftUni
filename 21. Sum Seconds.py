import math


time_first=int(input())
second_first=int(input())
third_first=int(input())


total_time=time_first+second_first+third_first

minutes=total_time/60
secund=total_time%60

minutes=math.floor(minutes)

if secund<10:
    print(f"{minutes}:0{secund}")
else:
    print(f"{minutes}:{secund}")