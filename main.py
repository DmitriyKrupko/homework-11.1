def MonthGenerator():
    list_month = [
        'Январь', 'Февраль', 'Март', 'Апрель', 
        'Июнь', 'Июль', 'Август', 'Сентябрь', 
        'Октябрь', 'Ноябрь', 'Декабрь']
    for month in list_month:
        yield month
months = MonthGenerator()
for month in months:
    print(month)
