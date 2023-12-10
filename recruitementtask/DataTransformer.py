import json
import re
import xml.etree.ElementTree as et

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

    @staticmethod
    def transform_xml_to_json(path: str) -> pd.DataFrame:
        parsed_xml = et.parse(path)
        root = parsed_xml.getroot()
        user_data = []
        for user in root.findall("user"):
            user_dict = {
                "firstname": user.find("firstname").text,
                "telephone_number": user.find("telephone_number").text,
                "email": user.find("email").text,
                "password": user.find("password").text,
                "role": user.find("role").text,
                "created_at": user.find("created_at").text,
                "children": [
                    {"name": child.find("name").text, "age": int(child.find("age").text)}
                    for child in user.find("children")
                ],
            }
            user_data.append(user_dict)
        return pd.DataFrame(user_data)
