nuber = int(input())

bonus_points = 0

if nuber <= 100:
    bonus_points = 5
elif nuber > 1000:
    bonus_points = nuber * 0.1
else:
    bonus_points = nuber * 0.2

if nuber % 10 == 5:
    bonus_points = bonus_points + 2
if nuber % 2 == 0:
    bonus_points = bonus_points + 1

print(bonus_points)
print(bonus_points+nuber)