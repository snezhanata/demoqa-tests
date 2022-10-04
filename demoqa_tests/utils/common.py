from typing import Iterable, Any


def flatten(nested_iterable: Iterable[Iterable[Any]]):
    return [item for nested in nested_iterable for item in nested]
    # return tuple(item for nested in nested_iterable for item in nested)


'''
data
>>> [('Student Name', 'Nyan Cat'), ('Student Email', 'nyan.cat@gmail.com'), ('Gender', 'Female'), ('Mobile', '0123401234'), ('Date of Birth', '30 August,2000'), ('Subjects', 'History, Maths'), ('Hobbies', 'Sports, Music'), ('Picture', 'pic.jpg'), ('Address', 'https://www.youtube.com/watch?v=QH2-TGUlwu4'), ('State and City', 'Uttar Pradesh Agra')]
[item for pair in data for item in pair] # для каждой пары в дате, для каждого айтема в паре, вернем айтем
>>> ['Student Name', 'Nyan Cat', 'Student Email', 'nyan.cat@gmail.com', 'Gender', 'Female', 'Mobile', '0123401234', 'Date of Birth', '30 August,2000', 'Subjects', 'History, Maths', 'Hobbies', 'Sports, Music', 'Picture', 'pic.jpg', 'Address', 'https://www.youtube.com/watch?v=QH2-TGUlwu4', 'State and City', 'Uttar Pradesh Agra']
'''
