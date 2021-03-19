# swissarmy/__init__.py
__version__ = "0.1.1"
from typing import Any, Union, MutableSequence, overload

from math import (
    log,
    trunc,
)

from .EmptyNoneFormatter import EmptyNoneFormatter

NotStringSequence = Union[MutableSequence, tuple]

fmtEmpty = EmptyNoneFormatter()


def flatten(container):
    """flatten an arbitrarily nested list or tuple"""
    for i in container:
        if isinstance(i, list) or isinstance(i, tuple):
            for j in flatten(i):
                yield j
        else:
            yield i


def safe_cast(type, value, safe=None):
    """try and cast the value to the type

    return safe value if any exceptions occur
    """
    try:
        return type(value)
    except Exception:
        return safe


def sigfig(val, sigs=3):
    """Round val to `sigs` significant figures

    :param val: Value to round to the `sigs` number of the significant figures
    :type val: float
    :param sigs: number of significant figures defaults to 3
    :type sigs: int
    :return: float `val` rounded to significant figures

    """
    nExp = sigs - (1 + trunc(log(abs(float(val)), 10)))
    return round(float(val) * (10.0 ** nExp)) / (10.0 ** nExp)


def iter_or_none(val):
    """Return val if iterable else None"""
    try:
        if any(True for _ in val):
            return val
        return None
    except Exception:
        return None


def iter_or_list(val):
    """Return val if iterable else None"""
    try:
        if any(True for _ in val):
            return val
        return []
    except Exception:
        return [
            val,
        ]


@overload
def get_last_attr(elm: Any, attrs: NotStringSequence, default: Any) -> Any:
    ...


def get_last_attr(elm: Any, attrs: NotStringSequence, *args: Any) -> Any:
    """
    Recurse through sequence of strings to return the last element

    :param elm: element to return the attribute on
    :type elm: Any
    :param attrs: a list/tuple like object that contains strings for the
      attribute path
    :type attrs: Union[MutableSequence, tuple]
    :param \*args: only one (1) optional argument to return a value instead of
      raising an exception
    :type \*args: Any
    :return: attribute value

    """

    if len(args) > 1:
        raise TypeError(
            f"get_last_attr() takes 1 optional argument but {len(args)} were given"
        )
    try:
        if len(attrs) > 1:
            return get_last_attr(getattr(elm, attrs[0]), attrs[1:], *args)
        else:
            return getattr(elm, attrs[0])
    except AttributeError as e:
        if len(args) == 1:
            return args[0]
        raise AttributeError(e)
