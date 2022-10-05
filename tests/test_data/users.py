from dataclasses import dataclass, field
from enum import Enum
from typing import List, Tuple, Literal

# def sample_email_(domain='gmail'):
#     return f'nyan.cat@{domain}.com'
# sample_email_()

sample_email = lambda domain='gmail': f'nyan.cat@{domain}.com'


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


'''
OR 
Gender = Literal['Male', 'Female', 'Other']
'''


@dataclass
class User:
    name: str
    gender: Gender
    last_name: str = 'Cat'
    email: str = sample_email()
    mobile_number: str = '0123401234'
    birth_day: str = '30'
    birth_month: str = 'August'
    birth_year: str = '2000'
    '''
    date_of_birth: str = '08 August,2000'
    '''
    subjects: Tuple[Subject] = (
        Subject.History,
        Subject.Maths,
    )
    hobbies: Tuple[Hobby] = (Hobby.Sports, Hobby.Music)
    picture_file: str = 'pic.jpg'
    current_address: str = 'https://www.youtube.com/watch?v=QH2-TGUlwu4'
    state: str = 'Uttar Pradesh'
    city: str = 'Agra'


user = User(name='Nyan', gender=Gender.Female)
'''
OR (for Literal case)
cat = User(name='Nyan', gender='Female')
'''