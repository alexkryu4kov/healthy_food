import glob
import json
import time
from dataclasses import dataclass
from itertools import combinations, product
from random import choice, sample

from model import Dish, PartOfTheDayEnum


def combs(lst, n):
    return (c for k in range(1, n+1) for c in combinations(lst, k))


def best_match_by_calories(lst, target, param='calories', n=3):
    return min(combs(lst, n), key=lambda c: (abs(target - sum([getattr(b, param) for b in c])), len(c)))


def generate_breakfast(list_of_dishes, target, param='calories'):
    porridge_list = [dish for dish in list_of_dishes if dish.kind == 'porridge']
    desserts_list = [dish for dish in list_of_dishes if dish.kind == 'desserts']
    beverage_list = [dish for dish in list_of_dishes if dish.kind == 'beverage']
    com = product(
        sample(porridge_list, len(porridge_list)//2),
        sample(desserts_list, len(desserts_list)//2),
        sample(beverage_list, len(beverage_list)//2),
    )
    return min(com, key=lambda c: (abs(target - sum([getattr(b, param) for b in c])), len(c)))


def generate_dinner(list_of_dishes, target, param='calories'):
    main_courses_list = [dish for dish in list_of_dishes if dish.kind == 'main_courses']
    salad_list = [dish for dish in list_of_dishes if dish.kind == 'salad']
    beverage_list = [dish for dish in list_of_dishes if dish.kind == 'beverage']
    com = product(
        sample(main_courses_list, len(main_courses_list)//2),
        sample(salad_list, len(salad_list)//2),
        sample(beverage_list, len(beverage_list)//2),
    )
    return min(com, key=lambda c: (abs(target - sum([getattr(b, param) for b in c])), len(c)))


def generate_supper(list_of_dishes, target, param='calories'):
    main_courses_list = [dish for dish in list_of_dishes if dish.kind == 'main_courses']
    fruits_list = [dish for dish in list_of_dishes if dish.kind == 'fruits']
    beverage_list = [dish for dish in list_of_dishes if dish.kind == 'beverage']
    com = product(
        sample(main_courses_list, len(main_courses_list)//2),
        sample(fruits_list, len(fruits_list)//2),
        sample(beverage_list, len(beverage_list)//2),
    )
    return min(com, key=lambda c: (abs(target - sum([getattr(b, param) for b in c])), len(c)))


def generate_lunch(list_of_dishes, target, param='calories'):
    salad_list = [dish for dish in list_of_dishes if dish.kind == 'salad']
    fruits_list = [dish for dish in list_of_dishes if dish.kind == 'fruits']
    desserts_list = [dish for dish in list_of_dishes if dish.kind == 'desserts']
    com = product(
        sample(salad_list, len(salad_list)//2),
        sample(fruits_list, len(fruits_list)//2),
        sample(desserts_list, len(desserts_list)//2),
    )
    return min(com, key=lambda c: (abs(target - sum([getattr(b, param) for b in c])), len(c)))


minerals = [
    'carbs',
    'fats',
    'proteins',
    'water',
    'fiber',
    'vitamin_a',
    'beta_carotene',
    'vitamin_b1',
    'vitamin_b2',
    'vitamin_b4',
    'vitamin_b5',
    'vitamin_b6',
    'vitamin_b9',
    'vitamin_b12',
    'vitamin_c',
    'vitamin_d',
    'vitamin_e',
    'vitamin_h',
    'vitamin_k',
    'vitamin_pp',
    'potassium',
    'calcium',
    'silicon',
    'magnesium',
    'sodium',
    'sulphur',
    'phosphorus',
    'chlorine',
    'ferrum',
    'iodine',
    'cobalt',
]


@dataclass
class PersonNorm:
    calories: float = 2547
    carbs: float = 331
    fats: float = 85
    proteins: float = 115
    water: float = 3770
    fiber: float = 20
    vitamin_a: float = 900
    beta_carotene: float = 5
    vitamin_b1: float = 1.5
    vitamin_b2: float = 1.8
    vitamin_b4: float = 500
    vitamin_b5: float = 5
    vitamin_b6: float = 2
    vitamin_b9: float = 400
    vitamin_b12: float = 3
    vitamin_c: float = 90
    vitamin_d: float = 10
    vitamin_e: float = 15
    vitamin_h: float = 50
    vitamin_k: float = 120
    vitamin_pp: float = 20
    potassium: float = 2500  # калий
    calcium: float = 1000  # кальций
    silicon: float = 30  # кремний
    magnesium: float = 400  # магний
    sodium: float = 1300  # натрий
    sulphur: float = 1000  # сера
    phosphorus: float = 800  # фосфор
    chlorine: float = 2300  # хлор
    ferrum: float = 10  # железо
    iodine: float = 150  # йод
    cobalt: float = 10  # кобальт


class DataLoader:

    def __init__(self, path: str):
        self._path = path

    def load_dishes(self, kind: str):
        list_of_dishes = []
        file_names = glob.glob(f'{self._path}/{kind}/*')
        for file in file_names:
            with open(file, 'r') as f:
                dish = json.loads(f.read())
                if kind in ('porridge'):
                    part_of_the_day = choice(
                        [
                            PartOfTheDayEnum.breakfast,
                        ],
                    )
                elif kind in ('salad'):
                    part_of_the_day = choice(
                        [
                            PartOfTheDayEnum.dinner,
                            PartOfTheDayEnum.lunch,
                            PartOfTheDayEnum.supper,
                        ],
                    )
                elif kind in ('bakery', 'drink', 'jams', 'beverage', 'desserts',  'blank', 'snack', 'fruits', 'vegetables', 'nuts'):
                    part_of_the_day = choice(
                        [
                            PartOfTheDayEnum.breakfast,
                            PartOfTheDayEnum.dinner,
                            PartOfTheDayEnum.lunch,
                            PartOfTheDayEnum.supper,
                        ],
                    )
                elif kind in ('garnish', 'main_courses', 'first_dishes', 'semi_processed', 'souces'):
                    part_of_the_day = choice(
                        [
                            PartOfTheDayEnum.dinner,
                            PartOfTheDayEnum.supper,
                        ],
                    )
                list_of_dishes.append(Dish(
                    name=dish['name'],
                    kind=kind,
                    calories=dish.get('Калорийность', 0),
                    carbs=dish.get('Углеводы', 0),
                    fats=dish.get('Жиры', 0),
                    proteins=dish.get('Белки', 0),
                    water=dish.get('Вода', 0),
                    fiber=dish.get('Пищевые волокна', 0),
                    vitamin_a=dish.get('Витамин А', 0),
                    beta_carotene=dish.get('бета Каротин', 0),
                    vitamin_b1=dish.get('Витамин В1', 0),
                    vitamin_b2=dish.get('Витамин B2', 0),
                    vitamin_b4=dish.get('Витамин B4', 0),
                    vitamin_b5=dish.get('Витамин B5', 0),
                    vitamin_b6=dish.get('Витамин B6', 0),
                    vitamin_b9=dish.get('Витамин B9', 0),
                    vitamin_b12=dish.get('Витамин B12', 0),
                    vitamin_c=dish.get('Витамин C', 0),
                    vitamin_d=dish.get('Витамин D', 0),
                    vitamin_e=dish.get('Витамин E', 0),
                    vitamin_h=dish.get('Витамин H', 0),
                    vitamin_k=dish.get('Витамин K', 0),
                    vitamin_pp=dish.get('Витамин PP', 0),
                    potassium=dish.get('Калий', 0),
                    calcium=dish.get('Кальций', 0),
                    silicon=dish.get('Кремний', 0),
                    magnesium=dish.get('Магний', 0),
                    sodium=dish.get('Натрий', 0),
                    sulphur=dish.get('Сера', 0),
                    phosphorus=dish.get('Фосфор', 0),
                    chlorine=dish.get('Хлор', 0),
                    ferrum=dish.get('Железо', 0),
                    iodine=dish.get('Йод', 0),
                    cobalt=dish.get('Кобальт', 0),
                    part_of_the_day=part_of_the_day,
                ))
        return list_of_dishes


def check_dish(dish):
    amount = 0
    for field in dish.__dataclass_fields__:
        if field not in ('name', 'kind', 'part_of_the_day'):
            if getattr(dish, field) > 0:
                amount += 1
    return amount > 10


class SimpleAlgorithm:

    def __init__(self, dishes):
        self._calories_norm = PersonNorm()
        self._breakfast_dishes = [dish for dish in dishes if dish.part_of_the_day == PartOfTheDayEnum.breakfast and check_dish(dish)]
        self._dinner_dishes = [dish for dish in dishes if dish.part_of_the_day == PartOfTheDayEnum.dinner and check_dish(dish)]
        self._lunch_dishes = [dish for dish in dishes if dish.part_of_the_day == PartOfTheDayEnum.lunch and check_dish(dish)]
        self._supper_dishes = [dish for dish in dishes if dish.part_of_the_day == PartOfTheDayEnum.supper and check_dish(dish)]

    def get_dishes(self, param='calories'):
        sum_of_calories = self._calories_norm.calories
        print(f'\nВаше меню на {sum_of_calories} калорий')
        breakfast_calories = int(sum_of_calories * 0.2)
        dinner_calories = int(sum_of_calories * 0.3)
        lunch_calories = int(sum_of_calories * 0.25/3)
        supper_calories = int(sum_of_calories * 0.25)
        
        breakfast_dishes = []
        for mineral in minerals:
            breakfast_dishes.extend(algo.get_breakfast(getattr(self._calories_norm, mineral), mineral))
        breakfast_list_of_dishes = generate_breakfast(breakfast_dishes, breakfast_calories, param)

        print(f'\nВаш завтрак на {breakfast_calories} калорий\n')
        for dish in breakfast_list_of_dishes:
            print(f'{dish.name}: {dish.calories} кКал')

        first_lunch_dishes = []
        for mineral in minerals:
            first_lunch_dishes.extend(algo.get_lunch(getattr(self._calories_norm, mineral), mineral))
        first_lunch_list_of_dishes = generate_lunch(first_lunch_dishes, lunch_calories, param)

        print(f'\nВаш первый перекус на {lunch_calories} калорий\n')
        for dish in first_lunch_list_of_dishes:
            print(f'{dish.name}: {dish.calories} кКал')
        
        dinner_dishes = []
        for mineral in minerals:
            dinner_dishes.extend(algo.get_dinner(getattr(self._calories_norm, mineral), mineral))
        dinner_list_of_dishes = generate_dinner(dinner_dishes, dinner_calories, param)

        print(f'\nВаш обед на {dinner_calories} калорий\n')
        for dish in dinner_list_of_dishes:
            print(f'{dish.name}: {dish.calories} кКал')
        
        second_lunch_dishes = []
        for mineral in minerals:
            second_lunch_dishes.extend(algo.get_lunch(getattr(self._calories_norm, mineral), mineral))
        second_lunch_list_of_dishes = generate_lunch(second_lunch_dishes, lunch_calories, param)

        print(f'\nВаш второй перекус на {lunch_calories} калорий\n')
        for dish in second_lunch_list_of_dishes:
            print(f'{dish.name}: {dish.calories} кКал')
        
        supper_dishes = []
        for mineral in minerals:
            supper_dishes.extend(algo.get_supper(getattr(self._calories_norm, mineral), mineral))
        supper_list_of_dishes = generate_supper(supper_dishes, supper_calories, param)

        print(f'\nВаш ужин на {supper_calories} калорий\n')
        for dish in supper_list_of_dishes:
            print(f'{dish.name}: {dish.calories} кКал')
            
        third_lunch_dishes = []
        for mineral in minerals:
            third_lunch_dishes.extend(algo.get_lunch(getattr(self._calories_norm, mineral), mineral))
        third_lunch_list_of_dishes = generate_lunch(third_lunch_dishes, lunch_calories, param)

        print(f'\nВаш вечерний перекус на {lunch_calories} калорий\n')
        for dish in third_lunch_list_of_dishes:
            print(f'{dish.name}: {dish.calories} кКал')

        all_dishes = [
            *breakfast_list_of_dishes,
            *first_lunch_list_of_dishes,
            *dinner_list_of_dishes,
            *second_lunch_list_of_dishes,
            *supper_list_of_dishes,
            *third_lunch_list_of_dishes,
        ]

        sum_of_calories = sum(dish.calories for dish in all_dishes)
        print(f'\nCalories: {sum_of_calories} {(sum_of_calories/self._calories_norm.calories)*100} % от нормы')
        for mineral in minerals:
            sum_of_mineral = sum(getattr(dish, mineral)for dish in all_dishes)
            print(f'{mineral}: {sum_of_mineral} {sum_of_mineral/getattr(self._calories_norm, mineral)*100} % от нормы')

    def get_breakfast(self, sum_of_param: float, param: str):
        breakfast_sum_of_param = sum_of_param * 0.2
        breakfast_list_of_dishes = generate_breakfast(self._breakfast_dishes, breakfast_sum_of_param, param)
        # print(breakfast_list_of_dishes)
        return breakfast_list_of_dishes

    def get_dinner(self, sum_of_param: float, param: str):
        dinner_sum_of_param = sum_of_param * 0.3
        dinner_list_of_dishes = generate_dinner(self._dinner_dishes, dinner_sum_of_param, param)
        # print(dinner_list_of_dishes)
        return dinner_list_of_dishes
    
    def get_lunch(self, sum_of_param: float, param: str):
        lunch_sum_of_param = sum_of_param * 0.25/3
        lunch_list_of_dishes = generate_lunch(self._lunch_dishes, lunch_sum_of_param, param)
        # print(lunch_list_of_dishes)
        return lunch_list_of_dishes
    
    def get_supper(self, sum_of_param: float, param: str):
        supper_sum_of_param = sum_of_param * 0.25
        supper_list_of_dishes = generate_supper(self._supper_dishes, supper_sum_of_param, param)
        # print(supper_list_of_dishes)
        return supper_list_of_dishes


if __name__ == '__main__':
    loader = DataLoader('data')
    full_list_of_dishes = []
    full_list_of_dishes.extend(loader.load_dishes('bakery'))
    full_list_of_dishes.extend(loader.load_dishes('beverage'))
    full_list_of_dishes.extend(loader.load_dishes('blank'))
    full_list_of_dishes.extend(loader.load_dishes('desserts'))
    full_list_of_dishes.extend(loader.load_dishes('drink'))
    full_list_of_dishes.extend(loader.load_dishes('first_dishes'))
    full_list_of_dishes.extend(loader.load_dishes('fruits'))
    full_list_of_dishes.extend(loader.load_dishes('garnish'))
    full_list_of_dishes.extend(loader.load_dishes('jams'))
    full_list_of_dishes.extend(loader.load_dishes('main_courses'))
    full_list_of_dishes.extend(loader.load_dishes('nuts'))
    full_list_of_dishes.extend(loader.load_dishes('porridge'))
    full_list_of_dishes.extend(loader.load_dishes('salad'))
    full_list_of_dishes.extend(loader.load_dishes('semi_processed'))
    full_list_of_dishes.extend(loader.load_dishes('snack'))
    full_list_of_dishes.extend(loader.load_dishes('souces'))
    full_list_of_dishes.extend(loader.load_dishes('vegetables'))
    algo = SimpleAlgorithm(full_list_of_dishes)
    algo.get_dishes()
