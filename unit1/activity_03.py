
price_hour = 300
min_hour = 40
bon = 1.5

hours = int(input("how many hours worked?"))
if (hours>40):
    hour_extra = hours - min_hour
    salary = (min_hour*price_hour) + (hour_extra*bon)
else:
    salary = hours*price_hour
print("payment", salary)