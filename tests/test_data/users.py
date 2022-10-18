import datetime
from dataclasses import dataclass
from enum import Enum
from typing import Tuple

from demoqa_tests import config


class Subject(Enum):
    History = 'History'
    Maths = 'Maths'
    Physics = 'Physics'


class Hobby(Enum):
    Sports = '1'
    Reading = '2'
    Music = '3'


class Gender(Enum):
    Male = 'Male'
    Female = 'Female'
    Other = 'Other'


@dataclass
class User:
    first_name: str
    gender: Gender
    last_name: str
    email: str
    mobile_number: str
    birth_date: datetime.date
    birth_day: str
    birth_month: str
    birth_year: str
    # date_of_birth: str = '08 August,2000' # noqa
    subjects: Tuple
    hobbies: Tuple
    picture_file: str
    current_address: str
    state: str
    city: str


student_1 = User(
    first_name='Nyan',
    gender=Gender.Female,
    last_name='Cat',
    email='nyan.cat@gmail.com',
    mobile_number='0123401234',
    birth_date=datetime.date(2000, 8, 30),
    birth_day='30',
    birth_month='August',
    birth_year='2000',
    subjects=(
        Subject.History,
        Subject.Maths,
    ),
    hobbies=(Hobby.Sports, Hobby.Music),
    picture_file='pic.jpg',
    current_address='https://www.youtube.com/watch?v=QH2-TGUlwu4',
    state='Uttar Pradesh',
    city='Agra',
)

student_2 = User(
    first_name='Eren',
    gender=Gender.Male,
    last_name='Yeager',
    email='eren.yeager@gmail.com',
    mobile_number='0123401234',
    birth_date=datetime.date(1993, 5, 19),
    birth_day='19',
    birth_month='May',
    birth_year='1993',
    subjects=(
        Subject.History,
        Subject.Maths,
    ),
    hobbies=(Hobby.Sports, Hobby.Music),
    picture_file='pic_2.png',
    current_address='Shiganshina',
    state='Uttar Pradesh',
    city='Agra',
)


def format_input_date(value: datetime.date):
    return value.strftime(config.datetime_input_format)


def format_view_date(value: datetime.date):
    return value.strftime(config.datetime_view_format)
