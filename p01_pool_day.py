import math  # Импортиране на библиотеката math за закръгляне

# Входни данни
people_count = int(input())  # Брой на хората
entry_fee = float(input())  # Такса вход
sunbed_price = float(input())  # Цена за един шезлонг
umbrella_price = float(input())  # Цена за един чадър

# Изчисления
# Обща сума за входната такса
total_entry_fee = people_count * entry_fee

# 75% от хората искат шезлонг
sunbed_count = math.ceil(people_count * 0.75)
total_sunbed_price = sunbed_count * sunbed_price

# Един чадър стига за двама, така че намерете броя на необходимите чадъри
umbrella_count = math.ceil(people_count / 2)
total_umbrella_price = umbrella_count * umbrella_price

# Обща сума
total_cost = total_entry_fee + total_sunbed_price + total_umbrella_price

# Изход
print(f"{total_cost:.2f} lv.")