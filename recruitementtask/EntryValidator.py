import re


class EntryValidator:
    @staticmethod
    def validate_email(email):
        pattern = r"^[^@]+@[^@]+\.[a-zA-Z0-9]{1,4}$"
        return True if re.match(pattern, email) else False
