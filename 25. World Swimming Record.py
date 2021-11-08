import math

record_seconds=float(input())
distance=float(input())
sonds_per_mether=float(input())

distance_time=math.floor(distance*sonds_per_mether)
insert_time=math.floor(distance/15)
insert_time_sec=math.floor(insert_time*12.5)
total_time=distance_time+insert_time_sec
total_time=math.floor(total_time)
record_time=total_time-record_seconds
record_time=math.floor(record_time)

if record_time>record_seconds:
    print(f"No, he failed! He was {record_time:.2f} seconds slower.")
else:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")