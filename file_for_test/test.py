import pep8
import StringIO

code_to_be_checked = """
import random
import string


class SimplePasswordGenerator(object):

    list_of_chars = [string.letters, string.digits, string.punctuation]
    union_of_chars = list(set().union(*list_of_chars))

    def __init__(self, available_chars=union_of_chars, length=8):
        self.available_chars = available_chars
        self.length = length

    def __iter__(self):
        return self

    def next(self):  # use __next__ in Python 3.x
        password = ''.join([random.choice(self.available_chars) for i in range(self.length)])
        return password
"""

myfile = StringIO.StringIO(code_to_be_checked)
fchecker = pep8.Checker(lines=myfile.readlines(), show_source=True)
errors = fchecker.check_all()

print("PEP8 error count: {}".format(errors))