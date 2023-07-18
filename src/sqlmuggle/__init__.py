import sqlite3
import typing as t
from contextlib import contextmanager
from dataclasses import dataclass


class Transaction:
    pass


@dataclass(frozen=True)
class Column:
    name: str
    type_: t.Any
    primary_key: bool = False


@dataclass(frozen=True)
class Table:
    name: str
    columns: t.Sequence[Column]


class Integer:
    pass


@dataclass(frozen=True)
class String:
    length: int


class Database(t.Protocol):
    def transaction(self) -> t.ContextManager[Transaction]:
        ...


class Introspet(t.Protocol):
    def tables(self) -> t.Sequence[Table]:
        ...


class IntrospectImplementation:
    def __init__(self, transaction: Transaction):
        self.transaction = transaction

    def tables(self) -> t.Sequence[Table]:
        return []


class SqliteDatabase(Database):
    def __init__(self, connection_string: str):
        self.connection = sqlite3.connect(connection_string)

    @contextmanager
    def transaction(self) -> t.Iterator[Transaction]:
        yield Transaction()

    @property
    def introspect(self):
        with self.transaction() as t:
            return IntrospectImplementation(t)


def database(connection_string: str) -> Database:
    return SqliteDatabase(connection_string)


def migrate(transaction: Transaction, tables: t.Sequence[Table]):
    pass
