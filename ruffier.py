''' Модуль для расчета результатов пробы Руфье.

Сумма измерений пульса в трех попытках (до нагрузки, сразу после и после короткого отдыха)
в идеале должна быть не более 200 ударов в минуту. 
Мы предлагаем детям измерять свой пульс на протяжении 15 секунд, 
и приводим результат к ударам в минуту умножением на 4:
    S = 4 * (P1 + P2 + P3)
Чем дальше этот результат от идеальных 200 ударов, тем хуже.
Традиционно таблицы даются для величины, делённой на 10. 

Индекс Руфье   
    IR = (S - 200) / 10
оценивается по таблице в соответствии с возрастом:
        7-8             9-10                11-12               13-14               15+ (только для подростков!)
отл.     < 6.5           < 5                 < 3.5               < 2                 < 0.5  
хор.    >= 6.5 и < 12   >= 5 и < 10.5       >= 3.5 и < 9        >= 2 и < 7.5        >= 0.5 и < 6
удовл.  >= 12 и < 17    >= 10.5 и < 15.5    >= 9 и < 14         >= 7.5 и < 12.5     >= 6 и < 11
слабый  >= 17 и < 21    >= 15.5 и < 19.5    >= 14 и < 18        >= 12.5 и < 16.5    >= 11 и < 15
неуд.   >= 21           >= 19.5             >= 18               >= 16.5             >= 15

для всех возрастов результат "неуд" отстоит от "слабого" на 4, 
тот от "удовлетворительного" на 5, а "хороший" от "уд" - на 5.5

поэтому напишем функцию ruffier_result(r_index, level), которая будет получать
рассчитанный индекс Руфье и уровень "неуд" для возраста тестируемого, и отдавать результат

'''

def test(age, pulse1, pulse2, pulse3):
    S = 4 * (pulse1 + pulse2 + pulse3)
    IR = (S - 200) / 10
    if age == 7 or age == 8:
        if IR < 6.5:
            return 'Отличная работоспособность!'
        elif IR >= 6.5 and IR < 12:
            return 'Хорошая работоспособность'
        elif IR >= 12 and IR < 17:
            return 'Удовлетворительная работоспособность'
        elif IR >= 17 and IR < 21:
            return 'Слабая работоспособность'
        else:
            return 'Неудовлетворительная работоспособность'
    elif age == 9 or age == 10:
        if IR < 5:
            return 'Отличная работоспособность!'
        elif IR >= 5 and IR < 10.5:
            return 'Хорошая работоспособность'
        elif IR >= 10.5 and IR < 15.5:
            return 'Удовлетворительная работоспособность'
        elif IR >= 15.5 and IR < 19.5:
            return 'Слабая работоспособность'
        else:
            return 'Неудовлетворительная работоспособность'
    elif age == 11 or age == 12:
        if IR < 3.5:
            return 'Отличная работоспособность!'
        elif IR >= 3.5 and IR < 9:
            return 'Хорошая работоспособность'
        elif IR >= 9 and IR < 14:
            return 'Удовлетворительная работоспособность'
        elif IR >= 14 and IR < 18:
            return 'Слабая работоспособность'
        else:
            return 'Неудовлетворительная работоспособность'
    elif age == 13 or age == 14:
        if IR < 2:
            return 'Отличная работоспособность!'
        elif IR >= 2 and IR < 7.5:
            return 'Хорошая работоспособность'
        elif IR >= 7.5 and IR < 12.5:
            return 'Удовлетворительная работоспособность'
        elif IR >= 12.5 and IR < 16.5:
            return 'Слабая работоспособность'
        else:
            return 'Неудовлетворительная работоспособность'
    elif age >= 15 and age < 18:
        if IR < 0.5:
            return 'Отличная работоспособность!'
        elif IR >= 0.5 and IR < 6:
            return 'Хорошая работоспособность'
        elif IR >= 6 and IR < 11:
            return 'Удовлетворительная работоспособность'
        elif IR >= 11 and IR < 15:
            return 'Слабая работоспособность'
        else:
            return 'Неудовлетворительная работоспособность'
        
# print(test(15, 15, 35, 25))