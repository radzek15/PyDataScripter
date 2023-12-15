import re
from typing import Union

import pandas as pd


class EntryValidator:
    @staticmethod
    def validate_email(df: pd.DataFrame) -> pd.DataFrame:
        pattern = r"^[^@]+@[^@]+\.[a-zA-Z0-9]{1,4}$"
        return df[df["email"].str.contains(pattern, na=False)]

    # For excluding rows from df when there is null value in specified column, so not only for phone like in the task
    # Works perfectly fine for entries with null phone, just specify 'telephone_number' as 2nd arg
    @staticmethod
    def exclude_null(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
        return df[df[column_name].notnull()]

    @staticmethod
    def standardize_phone_number(df: pd.DataFrame) -> pd.DataFrame:
        df["telephone_number"] = df["telephone_number"].apply(lambda x: re.sub(r"\s", "", x)[-9:])
        return df

    @staticmethod
    def remove_duplicates(
        df: pd.DataFrame, column_names: Union[str, list[str]], sort_by: str = "created_at", keep: str = "last"
    ) -> pd.DataFrame:
        return df.sort_values(by=sort_by).drop_duplicates(subset=[column_names], keep=keep)
