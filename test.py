import random
import time

arsAr = {'Атака': 'Стрела Тьмы (+10), Отравленная стрела (+15), Тройная стрела (*3)', 'Защита': 'Уклонение кувырком, Ответный выстрел'}
arsSw = {'Атака': 'Меч Света (+15), Усиление Света (+20), Двойная битва (*2)', 'Защита': 'Скользящая броня, Ответный удар'}


class Archer(object):

    def __init__(self):
        self.health = 100
        self.attst = 20 #Параметр для обнуления значения параметра Атаки после боевого столкновения
        self.attack = False
        self.defend = False

    def ttha(self):
        return print('Маг-Лучник, характеристики:\nЗдоровье: {}'.format(self.health))

    def ars(self):
        print('\nСписок доступных команд Лучника.')
        for key, value in arsAr.items():
            print(key, ':', value)

    def ver(self):
        a = random.randint(0,1)
        if a == 0:
            self.attack = False
            return self.attack
        else:
            self.attack += 20
            return self.attack

    def push(self, P1, P2, command):
        if 'Стрела Тьмы' in command or 'Стрела тьмы' in command or 'стрела Тьмы' in command or 'стрела тьмы' in command:
            self.attack = self.attack.__add__(10)
            return print ('\nСтрела Тьмы увеличила силу атаки до {} единиц.'.format(self.attack)), self.attack
        elif 'Отравленная стрела' in command or 'отравленная Стрела' in command or 'отравленная стрела' in command:
            self.attack = self.attack.__add__(15)
            return print ('\nОтравленная стрела увеличила силу атаки до {} единиц.'.format(self.attack)), self.attack
        elif 'Тройная стрела' in command or 'тройная Стрела' in command or 'тройная стрела' in command:
            self.attack = self.attack.__mul__(3)
            return print ('\nТройная стрела увеличила силу атаки до {} единиц.'.format(self.attack)), self.attack
        else:
            a = GameLogic()
            return print('\nНекорректная команда. Игровой ход сбрасывается.'), a.run(P1, P2)

    def back(self, P1, P2, command):
        if 'Уклонение кувырком' in command:
            return Archer.defense1(self)
        elif 'Ответный выстрел' in command:
            return Archer.defense2(self)
        else:
            a = GameLogic()
            return print('\nНекорректная команда. Игровой ход сбрасывается.'), a.run(P1, P2)

    def defense1(self):
        a = random.randint(1, 5)
        if a == 1 or a == 2 or a == 3:
            self.defend = True
            return print('\nКувырок увёл Вас с линии атаки.'), self.defend
        else:
            self.defend = False
            return print('\nКувырок Вас не спас.'), self.defend

    def defense2(self):
        a = random.randint(1, 2)
        if a == 1:
            self.defend = True
            return print('\nОтветный выстрел отбил удар.'), self.defend
        else:
            self.defend = False
            return print('\nОтветный выстрел не остановил удар.'), self.defend




class Sword(object):

    def __init__(self):
        self.health = 110
        self.attst = 25 #Параметр для обнуления значения параметра Атаки после боевого столкновения
        self.attack = False
        self.defend = False

    def tths(self):
        return print('Маг-Мечник, характеристики:\nЗдоровье: {}'.format(self.health))

    def ars(self):
        print('\nСписок доступных команд Мечника.')
        for key, value in arsSw.items():
           print(key, ':', value)

    def ver(self):
        a = random.randint(0,1)
        if a == 0:
            self.attack = False
            return self.attack
        else:
            self.attack += 25
            return self.attack

    def push(self, P1, P2, command):
        if 'Меч Света' in command or 'Меч света' in command or 'меч Света' in command or 'меч света' in command:
            self.attack = self.attack.__add__(15)
            return print('\nМеч Света увеличил силу атаки до {} единиц.'.format(self.attack)), self.attack
        elif 'Усиление Света' in command or 'Усиление света' in command or 'усиление Света' in command or 'усиление cвета' in command:
            self.attack = self.attack.__add__(20)
            return print('\nУсиление Света увеличило силу атаки до {} единиц.'.format(self.attack)), self.attack
        elif 'Двойная битва' in command or 'двойная Битва' in command or 'двойная битва' in command:
            self.attack = self.attack.__mul__(2)
            return print('\nДвойная битва увеличила силу атаки до {} единиц.'.format(self.attack)), self.attack
        else:
            a = GameLogic()
            return print('\nНекорректная команда. Игровой ход сбрасывается.'), a.run(P1, P2)

    def back(self, P1, P2, command):
        if 'Скользящая броня' in command:
            return Sword.defense1(self)
        elif 'Ответный удар' in command:
            return Sword.defense2(self)
        else:
            a = GameLogic()
            return print('\nНекорректная команда. Игровой ход сбрасывается.'), a.run(P1, P2)

    def defense1(self):
        a = random.randint(1, 6)
        if a == 1 or a == 2 or a == 3:
            self.defend = True
            return print('\nСкользящая броня сбила направленную атаку.'), self.defend
        else:
            self.defend = False
            return print('\nСкользящая броня не спасла Вас.'), self.defend

    def defense2(self):
        a = random.randint(1, 3)
        if a == 1 or a == 2:
            self.defend = True
            return print('\nОтветный удар остановил угрозу.'), self.defend
        else:
            self.defend = False
            return print('\nОтветный удар не помог.'), self.defend


class GameLogic(object):

    def run(self, P1, P2):
        t = random.randint(0, 1)
        if t == 0:
            return print('\nПервым ходит Игрок номер один.'), self.run1(P1, P2)
        else:
            return print('\nПервым ходит Игрок номер два.'), self.run2(P1, P2)

    def run1(self, P1, P2):
        P1.ars()
        P2.ars()
        x = input('\nИгрок 1 начинает Атаку: ')
        y = input('Игрок 2 обозначает Защиту: ')
        P1.ver()
        if P1.attack == False:
            return print ('\nИгрок 1 не смог провести атаку - его заклинание не сработало. Ход переходит к Игроку 2.'), self.run2 (P1, P2)
        else:
            P1.push(P1, P2, x)
            P2.back(P1, P2, y)
            if P2.defend is True:
                print('\nВ результате столкновения Игрок 2 не получил повреждений. Осталось {} хп.'.format(P2.health))
                P2.defend = False
                P1.attack = 0
                return self.run2(P1, P2)
            else:
                P2.health = P2.health.__sub__(P1.attack)
                if P2.health <= 0:
                    print('\nИгрок 1 победил, поздравляю!\nКонец игры!')
                    exit()
                else:
                    P1.attack = False
                    return print('\nУ Игрока 2 осталось {} хп'.format(P2.health)), self.run2(P1, P2)

    def run2(self, P1, P2):
        P1.ars()
        P2.ars()
        x = input('\nИгрок 2 начинает Атаку: ')
        y = input('Игрок 1 обозначает Защиту: ')
        P2.ver()
        if P2.attack == False:
            return print ('\nИгрок 2 не смог провести атаку - его заклинание не сработало. Ход переходит к Игроку 1.'), self.run1 (P1, P2)
        else:
            P2.push(P1, P2, x)
            P1.back(P1, P2, y)
            if P1.defend is True:
                print('\nВ результате столкновения Игрок 1 не получил повреждений. Осталось {} хп.'.format(P1.health))
                P1.attack = 0
                P2.defend = False
                return self.run1(P1, P2)
            else:
                P1.health = P1.health.__sub__(P2.attack)
                if P1.health <= 0:
                    print('\nИгрок 2 победил, поздравляю!\nКонец игры!')
                    exit()
                else:
                    P2.attack = False
                    return print('\nУ Игрока 1 осталось {} хп'.format(P1.health)), self.run1(P1, P2)



'''
Персонаж супер-пользователя, обладает всего одной ультимейт атакой, но большим количеством брони. Активируется по секретному коду. 
class Wizard(object):

    def __init__(self):
        self.health = 'Знач'
        self.attack = 'Знач'
        self.defend = 'Знач'
'''


def start():
    print(
        'Добро пожаловать на альфа-тест моей PvP игры. В данной игре Вы можете выбрать Мага за которого будете играть: Мага-Лучника или Мага-Мечника. \nВ дальнейшем, Вы получите список команд, доступных к выполнению, а так же освоите основные механики игры.')
    time.sleep(2)
    return menu()


def menu():
    print ('\nОбновление 21.01.2020: \n1. В игру добавлен рандомизатор атак персонажа. Теперь, после назначения атако-защитных действий, система будет проверять, удачно ли назначена атака. Если да - ход продолжится. Если нет - ход перейдёт к другому игроку. \n2. Нивелирована требовательность регистра при вводе команд персонажей: можно писать как с заглавных, так и с строчных букв.\n')
    time.sleep(3)
    print('В игре участвуют два игрока, ходящие по очереди. \nДоговоритесь между собой, кто будет первым, а кто - вторым. \nПо выбранной очередности выберите себе персонажа: Лучник или Мечник (можно одинаковых)\n')
    P1 = input('Персонаж первого Игрока: ')
    P2 = input('Персонаж второго Игрока: ')
    if 'Лучник' in P1 or 'лучник' in P1:
        P1 = Archer()
        print(P1.ttha())
    elif 'Мечник' in P1 or 'мечник' in P1:
        P1 = Sword()
        print(P1.tths())
    else:
        return print('Такого персонажа не существует, повторите ввод обоих персонажей. '), menu()
    if 'Лучник' in P2 or 'лучник' in P2:
        P2 = Archer()
        print(P2.ttha())
    elif 'Мечник' in P2 or 'мечник' in P2:
        P2 = Sword()
        print(P2.tths())
    else:
        return print('Такого персонажа не существует, повторите ввод обоих персонажей. '), menu()
    time.sleep(3)
    print('\nМеханика игры подразумевает поочерёдные вводы Атаки-Защиты, начиная с рандомного игрока. \nВ результате введённых команд будут происходить вычисления, поэтому очередность должна сохраняться. \nКонечная цель игры - довести счётчик жизней оппонента до нуля.')
    time.sleep(5)
    a = GameLogic()
    return a.run(P1, P2)


start()