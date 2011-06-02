from datetime import date as Date, time as Time, datetime as Timestamp
from time import localtime

from MySQLdb.compat import string_literal
from MySQLdb.connection import connect
from MySQLdb.exceptions import (Warning, Error, InterfaceError, DatabaseError,
    OperationalError, IntegrityError, InternalError, ProgrammingError,
    NotSupportedError)
from MySQLdb.types import BINARY, DATETIME, NUMBER, ROWID, STRING


apilevel = "2.0"
paramstyle = "pyformat"
# Multiple threads can use the module, but not the connections.
threadsafety = 1


def Binary(x):
    return str(x)

def DateFromTicks(ticks):
    return Date(*localtime(ticks)[:3])

def TimeFromTicks(ticks):
    return Time(*localtime(ticks)[3:6])

def TimestampFromTicks(ticks):
    return Timestamp(*localtime(ticks)[:6])