import os

import pandas as pd
import pytest

from database.DataTransformer import DataTransformer


@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    data = {"children": ["Alice (5), Bob (8)", "Danielle (5), Justin (16)", "Josh (8)"]}
    return pd.DataFrame(data)


@pytest.mark.DataTransformer
def test_transform_children_csv(sample_dataframe: pd.DataFrame):
    result = DataTransformer.transform_children_csv(sample_dataframe)
    expected = pd.DataFrame(
        {
            "children": [
                [{"name": "Alice", "age": 5}, {"name": "Bob", "age": 8}],
                [{"name": "Danielle", "age": 5}, {"name": "Justin", "age": 16}],
                [{"name": "Josh", "age": 8}],
            ]
        }
    )
    pd.testing.assert_frame_equal(result, expected)


@pytest.mark.DataTransformer
def test_json_serializer(sample_dataframe: pd.DataFrame):
    result = DataTransformer.json_serializer(DataTransformer.transform_children_csv(sample_dataframe))
    assert result["children"].apply(lambda x: isinstance(x, str)).all()


@pytest.mark.DataTransformer
def test_transform_xml_to_json() -> None:
    # Create a sample XML file for testing
    xml_content = """
    <users>
        <user>
            <firstname>Alice</firstname>
            <telephone_number>1234567890</telephone_number>
            <email>alice@example.com</email>
            <password>pass123</password>
            <role>user</role>
            <created_at>2023-01-01</created_at>
            <children>
                <child>
                    <name>Alice</name>
                    <age>5</age>
                </child>
                <child>
                    <name>Bob</name>
                    <age>8</age>
                </child>
            </children>
        </user>
    </users>
    """
    with open("test.xml", "w+") as file:
        file.write(xml_content)
    result = DataTransformer.transform_xml_to_json("test.xml")
    expected = pd.DataFrame(
        {
            "firstname": ["Alice"],
            "telephone_number": ["1234567890"],
            "email": ["alice@example.com"],
            "password": ["pass123"],
            "role": ["user"],
            "created_at": ["2023-01-01"],
            "children": [[{"name": "Alice", "age": 5}, {"name": "Bob", "age": 8}]],
        }
    )
    pd.testing.assert_frame_equal(result, expected)
    os.remove("test.xml")
