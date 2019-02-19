import re

def validate_pw_long(password:str):
    complex_enough = True
    if not re.match("^.{8,}", password):
        complex_enough = False
    return complex_enough

def validate_pw_complexity(password:str):
    complex_enough = True
    if not re.match("^.{8,}", password):
        complex_enough = False
    if not re.match("[a-z]", password):
        complex_enough = False
    if not re.match("[A-Z]", password):
        complex_enough = False
    if not re.match("[0-9]", password):
        complex_enough = False
    if not re.match("[^0-9 A-Z a-z\s]", password):
        complex_enough = False
    if re.match("\s", password):
        complex_enough = False

    return complex_enough