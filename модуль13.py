# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
a = int(input('Введите количество билетов '))
num = 0
for i in range(1, a+1):
    vozrast = int(input('Введите возраст посетителя '))
    if vozrast < 18:
        num = num + 0
    elif 18 <= vozrast < 25:
        num = num + 990
    else:
        num = num + 1390
if a >= 3:
    num = num * 0.9
print('Сумма к оплате = ', num, 'руб.')
