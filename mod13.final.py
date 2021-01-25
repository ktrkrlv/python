N = int(input("Введите количество участников конференции: "))
z = list(range(1, N+1))
L = [int(input("Введите возраст участника {}: ".format(z[i]))) for i in range(N)]
count = 0
print()
for a in range(N):
    if L[a] < 18:
        print("Стоимость билета для участника {}: 0 р.".format(z[a]))
        count += 0
    elif 18 <= L[a] < 25:
        print("Стоимость билета для участника {}: 990 р.".format(z[a]))
        count += 990
    elif L[a] >= 25:
        print("Стоимость билета для участника {}: 1390 р.".format(z[a]))
        count += 1390
print()
if N >= 3:
    count = float(count) * 0.9
    print("Общая стоимость билетов: ", count)
else:
    print("Общая стоимость билетов: ", count)
