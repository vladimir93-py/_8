class OrgTech:

    def __init__(self, name, price, quantity, number_of_lists, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.numb = number_of_lists
        self.my_store_full = []
        self.my_store = []
        self.my_org = {'Модель устройства': self.name, 'Цена за ед': self.price, 'Количество': self.quantity}

    def __str__(self):
        return f'{self.name} цена {self.price} количество {self.quantity}'

    def recep(self):

        try:
            org = input(f'Введите наименование - ')
            org_p = int(input(f'Введите цену за ед -'))
            org_q = int(input(f'Введите количество -'))
            unique = {'Модель устройства': org, 'Цена за ед': org_p, 'Количество': org_q}
            self.my_org.update(unique)
            self.my_store.append(self.my_org)
            print(f'Текущий список -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода - Q, продолжение - Enter')
        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)
            print(f'Весь склад -\n {self.my_store_full}')
            return f'Выход'
        else:
            return OrgTech.recep(self)

class MFU(OrgTech):
    def to_MFU(self):
        return f'to MFU {self.numb}'


class papper(OrgTech):
    def to_papper(self):
        return f'to papper {self.numb}'


class phone(OrgTech):
    def to_phone(self):
        return f'to phone {self.numb}'


org_1 = MFU('kyocera', 2000, 5, 10)
org_2 = papper('A4', 1200, 5, 10)
org_3 = phone('CISCO', 1500, 1, 15)
print(org_1.recep())
print(org_2.recep())
print(org_3.recep())
print(org_1.to_MFU())
print(org_3.to_phone()) #все работает, но мне кажется, что криво соединил 3 задания и можно юыло бы поинтересней придумать..й