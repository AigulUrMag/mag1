n = int(input("Введите число: "))
s = 0
while (n != 0):
    s = s + n % 10
    n = n // 10
    print(s,n)
print("Сумма цифр числа равна: ", s)