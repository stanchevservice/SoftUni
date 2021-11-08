import math

buget=float(input())
person=int(input())
price_dres=float(input())

total_price_dres=0

decor_price=buget*0.10

if  person>150:
    total_price_dres=(person*price_dres)
    total_price_dres=total_price_dres-(total_price_dres*0.1)
else:
    total_price_dres=(person*price_dres)

total_sum=buget-total_price_dres-decor_price


if total_sum<0:
    total_sum = math.fabs(total_sum)
    print("Not enough money!")
    print(f"Wingard needs {total_sum:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {total_sum:.2f} leva left.")
