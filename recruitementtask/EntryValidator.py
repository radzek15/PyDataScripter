class EntryValidator:
    @staticmethod
    def validate_email(df):
        pattern = r"^[^@]+@[^@]+\.[a-zA-Z0-9]{1,4}$"
        mask = df["email"].str.match(pattern)
        filtered_df = df.loc[mask]
        return filtered_df

    @staticmethod
    def exclude_null(df, column_name):
        return df[df[column_name].notnull()]
