class Date:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-': my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2019 >= year >= 0:
                    return f'Отлично'
                else:
                    return f'Неккоректно указан год'
            else:
                return f'Неккоректно указан месяц'
        else:
            return f'Неккоректно указан день'

    def __str__(self):
        return f'Сегодняшняя дата {Date.extract(self.day_month_year)}'


today = Date('8 - 9 - 2020')
print(today)
print(Date.valid(10, 20, 2042))
print(today.valid(8, 9, 2020))
print(Date.extract('12 - 12 - 2012'))
print(today.extract('11 - 11 - 2011'))
print(Date.valid(1, -2, 0))
