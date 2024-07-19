def get_season(month):
    if month == 1 or month == 2 or month == 12:
        print('зима')
    elif month == 3 or month == 4 or month == 5:
        print('весна')
    elif month == 6 or month == 7 or month == 8:
        print('лето')
    else:
        print('осень')
month = int(input('Введите число от 1 до 12\n'))
get_season(month)