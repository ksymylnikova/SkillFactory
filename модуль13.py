# В начале у пользователя запрашивается количество билетов, которые он хочет приобрести на мероприятие.
# Далее для каждого билета запрашивается возраст посетителя, в соответствии со значением которого выбирается стоимость:
# Если посетителю конференции менее 18 лет, то он проходит на конференцию бесплатно.
# От 18 до 25 лет — 990 руб.
# От 25 лет — полная стоимость 1390 руб.
# В результате программы выводится сумма к оплате.
# При этом, если человек регистрирует больше трёх человек на конференцию, то дополнительно получает 10% скидку на полную стоимость заказа.
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
