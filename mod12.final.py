money = int(input('Money: '))
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
per_cent_list = list(per_cent.values())
deposit = []
deposit.append(round(money * (round(per_cent_list[0] / 100, 8))))
deposit.append(round(money * (round(per_cent_list[1] / 100, 8))))
deposit.append(round(money * (round(per_cent_list[2] / 100, 8))))
deposit.append(round(money * (round(per_cent_list[3] / 100, 8))))
print('Максимальная сумма, которую Вы можете заработать - ', max(deposit))
