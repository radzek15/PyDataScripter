import json
import re

import pandas as pd


class DataTransformer:
    @staticmethod
    def transform_children_csv(df: pd.DataFrame) -> pd.DataFrame:
        pattern = r"(\w+) \((\d+)\)"
        matches = df["children"].apply(lambda x: re.findall(pattern, str(x)))
        children = matches.apply(lambda x: [{"name": i[0], "age": int(i[1])} for i in x])
        df["children"] = children
        return df

    @staticmethod
    def json_serializer(df: pd.DataFrame) -> pd.DataFrame:
        df["children"] = df["children"].apply(json.dumps)
        return df
