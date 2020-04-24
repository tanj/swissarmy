# swissarmy/__init__.py
from math import (
    log,
    trunc,
)

from .EmptyNoneFormatter import EmptyNoneFormatter

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
    """Round val to <sigs> significant figures

       return float
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
