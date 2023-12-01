import re

class RegexPattern:
    def __init__(self, pattern=""):
        self.set_pattern(pattern)

    def set_pattern(self, pattern):
        try:
            self.pattern = re.compile(pattern)
        except re.error:
            print("Invalid regular expression pattern.")
            self.pattern = None

    def is_valid(self, string):
        if self.pattern is not None:
            return self.pattern.fullmatch(string) is not None
        return False

    # TODO, add additional methods can be added for more functionality such as find_all, replace, etc.


# regex = RegexPattern()
# regex.set_pattern(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
# print(regex.is_valid("example@email.com"))
# print(regex.is_valid("not-an-email"))       
