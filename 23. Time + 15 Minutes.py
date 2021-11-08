import math

hours=int(input())
minutes=int(input())

time_after_15min=0

hours_after_15min=0
minutes_after_15min=0

hours_after_15min=((hours*60)+minutes+15)/60

hours_after_15min=math.floor(hours_after_15min)
if hours_after_15min>23:
    hours_after_15min=0

minutes_after_15min=minutes+15
if minutes_after_15min>59:
    minutes_after_15min=minutes_after_15min-60

if minutes_after_15min<10:
    print(f"{hours_after_15min}:0{minutes_after_15min:}")
else:
    print(f"{hours_after_15min}:{minutes_after_15min:}")


