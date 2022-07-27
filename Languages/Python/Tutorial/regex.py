import re
"""
\d   Matches any decimal digit, this is equivalent
     to the set class [0-9].
\D   Matches any non-digit character.
\s   Matches any whitespace character.
\S   Matches any non-whitespace character
\w   Matches any alphanumeric character, this is
     equivalent to the class [a-zA-Z0-9_].
\W   Matches any non-alphanumeric character

https://www.geeksforgeeks.org/regular-expression-python-examples-set-1/
"""

string = """Hello 2myae Number is 123456789 and my friend's number is 987654321"""
pattern = "\W"
match = re.findall(pattern,string)
print(match)
print(len(match))

pattern = re.compile(r'ae')
match = pattern.findall(string)
print(match)
