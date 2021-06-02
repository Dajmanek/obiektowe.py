import re

while string := input():
    print(bool(re.fullmatch(r'[0-9]*.?[0-9]{0,2}', string)))