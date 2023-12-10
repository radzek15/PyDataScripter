import pandas as pd
import pytest

from recruitementtask.EntryValidator import EntryValidator


@pytest.fixture
def sample_dataframe():
    data = {
        "email": [
            "test@test.com",
            "test@test.com",
            "test1@test.com",
            "test",
            "test@@.com",
            "@a.com",
            None,
            "test@.com",
            "a@abc.commmm",
        ],
        "telephone_number": [
            "+48123456789",
            "00222222222",
            "(48) 111111111",
            "333 333 333",
            "123456789",
            "199299399",
            None,
            "123654785",
            "+48111111111",
        ],
        "created_at": [
            "2023-01-02 00:48:12",
            "2023-01-02 00:50:12",
            "2023-02-02 00:48:12",
            "2023-04-02 00:48:12",
            "2023-01-10 00:48:12",
            "2022-01-02 00:48:12",
            "2023-01-22 00:48:12",
            "2023-12-02 00:48:12",
            "2021-01-02 00:48:12",
        ],
    }
    return pd.DataFrame(data)


@pytest.mark.EntryValidator
def test_validate_email(sample_dataframe):
    result = EntryValidator.validate_email(sample_dataframe[["email"]])
    expected = pd.DataFrame({"email": ["test@test.com", "test@test.com", "test1@test.com"]})
    assert result.equals(expected)


@pytest.mark.EntryValidator
def test_exclude_null(sample_dataframe):
    result = EntryValidator.exclude_null(sample_dataframe[["email"]], "email")
    expected = pd.DataFrame(
        {
            "email": [
                "test@test.com",
                "test@test.com",
                "test1@test.com",
                "test",
                "test@@.com",
                "@a.com",
                "test@.com",
                "a@abc.commmm",
            ]
        }
    )
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))


@pytest.mark.EntryValidator
def test_standardize_phone_number(sample_dataframe):
    result = EntryValidator.standardize_phone_number(
        EntryValidator.exclude_null(sample_dataframe[["telephone_number"]], "telephone_number")
    )
    expected = pd.DataFrame(
        {
            "telephone_number": [
                "123456789",
                "222222222",
                "111111111",
                "333333333",
                "123456789",
                "199299399",
                "123654785",
                "111111111",
            ]
        }
    )
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))


@pytest.mark.EntryValidator
def test_remove_duplicates(sample_dataframe):
    result = EntryValidator.remove_duplicates(EntryValidator.validate_email(sample_dataframe), "email")
    expected = pd.DataFrame(
        {
            "email": ["test@test.com", "test1@test.com"],
            "telephone_number": ["00222222222", "(48) 111111111"],
            "created_at": ["2023-01-02 00:50:12", "2023-02-02 00:48:12"],
        }
    )
    pd.testing.assert_frame_equal(result.reset_index(drop=True), expected.reset_index(drop=True))
