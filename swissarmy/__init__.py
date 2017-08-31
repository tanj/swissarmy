#swissarmy/__init__.py

def flatten(container):
    """flatten an arbitrarily nested list or tuple"""
    for i in container:
        if isinstance(i, list) or isinstance(i, tuple):
            for j in flatten(i):
                yield j
        else:
            yield i
