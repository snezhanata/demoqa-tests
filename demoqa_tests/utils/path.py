import os.path
from pathlib import Path
from selene import Element
from selene.core.wait import Command

from tests import resources


def to_resource(relative_path):
    return str(Path(resources.__file__).parent.joinpath(relative_path).absolute())
