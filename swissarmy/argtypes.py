import os.path
from argparse import ArgumentTypeError, ArgumentError
import dateutil.parser


def valid_dir(arg):
    if os.path.isdir(arg):
        return arg
    raise ArgumentTypeError(f"{arg!r} is not a valid directory")


def valid_file(arg):
    if os.path.isfile(arg):
        return arg
    raise ArgumentTypeError(f"{arg!r} is not a valid file")


def valid_connection(string):
    from sqlalchemy import create_engine
    from sqlalchemy.exc import DBAPIError

    try:
        eng = create_engine(string)
        con = eng.connect()
    except (ArgumentError, DBAPIError) as e:
        raise ArgumentTypeError(e)
    con.close()
    return string


def isodatetime_type(sValue):
    try:
        dt = dateutil.parser.isoparse(sValue)
    except Exception as e:
        raise ArgumentTypeError(e)
    return dt
