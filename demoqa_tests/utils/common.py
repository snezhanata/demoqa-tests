from typing import Iterable, Any


def flatten(nested_iterable: Iterable[Iterable[Any]]):
    return [item for nested in nested_iterable for item in nested]
    # return tuple(item for nested in nested_iterable for item in nested)