import pytest

import sqlmuggle as sql


@pytest.fixture
def tmp_sqlite(tmp_path) -> sql.Database:
    db_path = tmp_path / "test.db"
    connection_string = f"{db_path}"
    db = sql.database(connection_string)
    yield db


@pytest.fixture(params=["tmp_sqlite"])
def tmp_db(request):
    return request.getfixturevalue(request.param)


def test_will_migrate_up(tmp_db):
    table = sql.Table(
        "users",
        [
            sql.Column("id", sql.Integer, primary_key=True),
            sql.Column("name", sql.String(50)),
        ],
    )

    with tmp_db.transaction() as t:
        sql.migrate(t, [table])

    # assert tmp_db.introspect.tables() == [table]
