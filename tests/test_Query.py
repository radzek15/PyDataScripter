import pytest

from database.Database import Database
from database.Query import Query


@pytest.fixture
def sample_query():
    db = Database("test-data/data/", "my_sqlite.db")
    db.create_database()
    db.import_data()
    return Query(db.db_name, "users")


@pytest.mark.Query
def test_check_credentials(sample_query):
    assert sample_query.check_credentials("ngreen@example.org", "n(9vNQ$jqO") == True
    assert sample_query.check_credentials("736121560", "n(9vNQ$jqO") == True
    assert sample_query.check_credentials("test@example.com", "test") == False


@pytest.mark.Query
def test_get_all_accounts(sample_query):
    assert sample_query.get_all_accounts() == 84


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
        (1, 10),
        (2, 10),
        (3, 7),
        (4, 7),
        (5, 4),
        (6, 5),
        (7, 5),
        (8, 9),
        (9, 5),
        (10, 4),
        (11, 10),
        (12, 9),
        (13, 7),
        (14, 4),
        (15, 5),
        (16, 5),
        (17, 10),
        (18, 5),
    ]
    assert result == expected


@pytest.mark.Query
def test_get_children_by_user(sample_query):
    result = sample_query.get_children_by_user("736121560")
    expected = [{"name": "Michael", "age": 17}, {"name": "Angela", "age": 14}]
    assert result == expected


@pytest.mark.Query
def test_get_similar_children_by_age(sample_query):
    result = sample_query.get_similar_children_by_age("stewartpaige@example.org", sample_query.table_name)
    expected = {
        "Amanda , 208579481: Marie, 17; George, 8; Susan, 11",
        "Angela , 216474381: Jose, 12; Scott, 2; Olivia, 16",
        "Brianna , 505400027: Sheila, 4; Laurie, 12",
        "Bryan , 242024650: Frank, 11",
        "Caroline , 617796987: Leonard, 11",
        "Don , 612660796: Michael, 12; Theresa, 6; Judith, 1",
        "Joan , 232756993: Karen, 7; Danielle, 11; Dustin, 7",
        "Logan , 716290783: Rachel, 12; Jennifer, 7; Jermaine, 18",
        "Madeline , 441935720: Jonathan, 1; Natalie, 11",
        "Russell , 817730653: Rebecca, 11; Christie, 17",
        "Sandy , 577969415: Dorothy, 12; Kristen, 2",
        "Shannon , 121975731: Steven, 12; Christine, 18; Rachel, 6",
        "Steven , 691250247: Jessica, 14; Megan, 11; Michael, 9",
        "Tanner , 604020303: Anna, 18; Mindy, 11",
        "Theresa , 513112467: Christopher, 11; Suzanne, 12; Joshua, 3",
        "Timothy , 279179128: Jamie, 12",
    }
    assert result == expected
