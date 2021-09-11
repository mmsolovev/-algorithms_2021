"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""


from collections import namedtuple


COMPANY = namedtuple('COMPANY', 'name quarter_1 quarter_2 quarter_3 quarter_4')
count = int(input('Введите количество предприятий для расчета прибыли: '))
profit_dict = {}


def year_profit_func(some_str):
    str_list = some_str.split()
    year_profit = 0
    for i in str_list:
        year_profit += int(i)
    return year_profit


for j in range(count):
    company_name = input('Введите название предприятия: ')
    my_list = (input('через пробел введите прибыль данного предприятия\nза каждый квартал(Всего 4 квартала): ')).split()
    company = COMPANY(
        name=company_name,
        quarter_1=int(my_list[0]),
        quarter_2=int(my_list[1]),
        quarter_3=int(my_list[2]),
        quarter_4=int(my_list[3])
    )
    profit_dict[company.name] = company.quarter_1 + company.quarter_2 + company.quarter_3 + company.quarter_4

avr = sum(profit_dict.values())/count
print(f'Средняя годовая прибыль всех предприятий: {avr}')

more_list = []
less_list = []

for n in profit_dict:
    if profit_dict[n] > avr:
        more_list.append(n)
    else:
        less_list.append(n)

print(f'Предприятия, с прибылью выше среднего значения: {more_list}')
print(f'Предприятия, с прибылью ниже среднего значения: {less_list}')
