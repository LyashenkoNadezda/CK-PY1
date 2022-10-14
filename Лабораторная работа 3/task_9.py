salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

need_money = 0  # количество денег, чтобы прожить 10 месяцев

for i in range(1, months + 1):
    if i == 1:
        need_money += spend - salary
    else:
        spend = spend + (spend * increase)
        need_money = need_money + spend - salary

print(round(need_money))
