from dataclasses import dataclass
from enum import Enum, auto
from typing import Optional


class PartOfTheDayEnum(Enum):
    breakfast = auto()
    dinner = auto()
    lunch = auto()
    supper = auto()


@dataclass
class Dish:
    name: str
    kind: str
    calories: float
    carbs: Optional[float] = None
    fats: Optional[float] = None
    proteins: Optional[float] = None
    water: Optional[float] = None
    fiber: Optional[float] = None
    vitamin_a: Optional[float] = None
    beta_carotene: Optional[float] = None
    vitamin_b1: Optional[float] = None
    vitamin_b2: Optional[float] = None
    vitamin_b4: Optional[float] = None
    vitamin_b5: Optional[float] = None
    vitamin_b6: Optional[float] = None
    vitamin_b9: Optional[float] = None
    vitamin_b12: Optional[float] = None
    vitamin_c: Optional[float] = None
    vitamin_d: Optional[float] = None
    vitamin_e: Optional[float] = None
    vitamin_h: Optional[float] = None
    vitamin_k: Optional[float] = None
    vitamin_pp: Optional[float] = None
    potassium: Optional[float] = None  # калий
    calcium: Optional[float] = None  # кальций
    silicon: Optional[float] = None  # кремний
    magnesium: Optional[float] = None  # магний
    sodium: Optional[float] = None  # натрий
    sulphur: Optional[float] = None  # сера
    phosphorus: Optional[float] = None  # фосфор
    chlorine: Optional[float] = None  # хлор
    ferrum: Optional[float] = None  # железо
    iodine: Optional[float] = None  # йод
    cobalt: Optional[float] = None  # кобальт
    part_of_the_day: Optional[PartOfTheDayEnum] = None
