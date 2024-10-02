from db import connect_to_database, query_user_data


def test_db():
    result = connect_to_database()
    assert result == True
