import os.path
from pathlib import Path
from selene import Element
from selene.core.wait import Command

from tests import resources


def abs_path_from_project_root(pic):
    path = os.path.abspath(f'{pic}')
    return path


def to_resource(relative_path):
    return str(Path(resources.__file__).parent.joinpath(relative_path).absolute())


def path_to_resource(pic):
    path = os.path.abspath(f'{pic}')
    return path


def upload_resource(path:str) -> Command[Element]:
    def fn(element: Element):
        element().send_keys(to_resource(path))
    return Command(f'upload file from resources: {path}', fn)


