n = int(input())
li = []
for i in range(n):
	li.append(int(input()))
control_rcv = int(input())
res = "пройден"
control = 0



print(f"Получено чисел: {len(li)}\nринятое контрольное значение: {control_rcv}\nВычисленное контрольноне значение: {control}\nКонтроль {res}")