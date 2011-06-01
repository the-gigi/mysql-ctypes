import contextlib

import py

from MySQLdb.cursors import DictCursor

from .base import BaseMySQLTests


class TestConnection(BaseMySQLTests):
    def test_custom_cursor_class(self, connection):
        with contextlib.closing(connection.cursor(DictCursor)) as cur:
            assert type(cur) is DictCursor

    def test_closed_rollback(self, connection):
        connection.close()
        with py.test.raises(connection.OperationalError):
            connection.rollback()