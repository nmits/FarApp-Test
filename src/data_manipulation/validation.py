import regex as re


def isValidPhoneNumer(number):
    return re.match(r"\(?d{3}[)-.]\d{3}[-.]\d{4}", number)


def isValidEmail(email):
    return re.match(r"[\w\d]+@\w+\.\w{2,3}", email)