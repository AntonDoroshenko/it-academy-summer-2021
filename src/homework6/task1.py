class Game_person:
    """Создайте  модель из жизни.

     Это может быть бронирование комнаты в отеле,
     покупка билета в транспортной компании, или простая РПГ. Создайте
     несколько объектов классов, которые описывают ситуацию.
     Объекты должны содержать как атрибуты так и методы класса для симуляции
     различных действий.

     В результате хотел реализовать небольшую игровую модель где имеются
     персонажи со своими особенностями.

     """
    def __init__(self, person_name, armor_strength, health_points):
        self.person_name = person_name
        self.armor_strength = armor_strength
        self.health_points = health_points

    def introduce_game_persons(self):
        print(f'Толпа приветствует {self.person_name}!')


class Good_character(Game_person):
    def __init__(self, person_name, armor_strength, health_points):
        super().__init__(person_name, armor_strength, health_points)

    def introduce_game_persons(self):
        print(f'Возрадуемся возвращению нашего легендарного героя!'
              f' Слава великому {self.person_name}!!!')
        print(f'Его основные атрибуты: очки прочности брони и очки здоровья '
              f'равны {self.armor_strength} и {self.health_points} '
              f'соответсвенно')


class Master(Game_person):
    def __init__(self, person_name, armor_strength, health_points):
        super().__init__(person_name, armor_strength, health_points)

    def introduce_game_persons(self):
        print(f'Против нашего героя будет биться {self.person_name}!!!')


class Weapon_Good_character(Good_character):
    def __init__(self, person_name, armor_strength, health_points, sword,
                 type_sword, sword_material):
        super().__init__(person_name, armor_strength, health_points)
        self.sword = sword
        self.type_sword = type_sword
        self.sword_material = sword_material

    def weapon_good_character(self):
        print(f'Наш герой {self.person_name} будет пользоваться мечом, который'
              f' наносит {self.sword} урона')
        print(f'При создании этого меча использовалась высококачественная '
              f'{self.sword_material},а его тип - {self.type_sword}, позволяет'
              f' стремительно наносить точные и тяжелые удары противнику!')


class Power_of_friendship(Good_character):
    def __init__(self, person_name, armor_strength, health_points, old_friend):
        super().__init__(person_name, armor_strength, health_points)
        self.old_friend = old_friend

    def mystery_of_the_battle(self):
        print(f'{self.person_name} встретил старого друга. Им оказался '
              f'{self.old_friend}, который сообщил что драться '
              f'{self.person_name} должен против своего наставника.')
        print(f'По этой причине {self.person_name} не вышел на бой.')


main_person_1 = Game_person('Короля Цинтры', 150, 350)
main_person_2 = Game_person('Королеву Цинтры', 70, 750)
main_person_1.introduce_game_persons()
main_person_2.introduce_game_persons()


gc = Good_character('Геральт', 150, 350)
gc.introduce_game_persons()


bg = Master('Весемир', 70, 750)
bg.introduce_game_persons()


wgc = Weapon_Good_character('Геральт', 150, 350, 100, 'одноручный',
                            'валерийская сталь')
wgc.weapon_good_character()

pof = Power_of_friendship('Геральт', 150, 350, 'Лютик')
pof.mystery_of_the_battle()
