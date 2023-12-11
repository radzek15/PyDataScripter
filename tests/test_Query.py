import pytest

from recruitementtask.Query import Query


@pytest.fixture
def sample_query():
    return Query("my_sqlite.db", "users_json")


@pytest.mark.Query
def test_check_credentials(sample_query):
    assert sample_query.check_credentials("ngreen@example.org", "n(9vNQ$jqO") == True
    assert sample_query.check_credentials("736121560", "n(9vNQ$jqO") == True
    assert sample_query.check_credentials("test@example.com", "test") == False


@pytest.mark.Query
def test_get_all_accounts(sample_query):
    assert sample_query.get_all_accounts() == 30


@pytest.mark.Query
def test_get_oldest_account(sample_query):
    assert (
        sample_query.get_oldest_account()
        == "name: Justin\nemail_address: opoole@example.org\ncreated_at: 2022-11-25 02:19:37"
    )


@pytest.mark.Query
def test_count_children_by_age(sample_query):
    result = sample_query.count_children_by_age()
    expected = [
        (1, 1),
        (2, 3),
        (3, 2),
        (4, 2),
        (5, 2),
        (6, 1),
        (7, 1),
        (8, 3),
        (9, 2),
        (10, 2),
        (11, 3),
        (12, 3),
        (13, 1),
        (14, 1),
        (15, 1),
        (16, 3),
        (17, 4),
        (18, 1),
    ]
    assert result == expected


@pytest.mark.Query
def test_get_children_by_user(sample_query):
    result = sample_query.get_children_by_user("736121560")
    expected = [{"name": "Michael", "age": 17}, {"name": "Angela", "age": 14}]
    assert result == expected


@pytest.mark.Query
def test_get_similar_children_by_age(sample_query):
    result = sample_query.get_similar_children_by_age("stewartpaige@example.org")
    expected = {"Joan , 232756993: Karen, 7; Danielle, 11; Dustin, 7", "Tanner , 604020303: Anna, 18; Mindy, 11"}
    assert result == expected
