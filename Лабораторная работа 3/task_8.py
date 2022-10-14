money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = 0

while money_capital > 0:
    if month == 0:
        money_capital = money_capital - spend
        month += 1
    else:
        spend = spend + (spend * increase)
        money_capital = money_capital + salary - spend
        if money_capital > 0:
            month += 1

print(month)
