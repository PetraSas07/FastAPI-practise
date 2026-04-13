class Fizzbuzz:
    def __init__(self, n):
        self.string_list = []
        self.size = n
        self.index = 0

    def fizz(self):
        self.string_list.append("fizz")

    def buzz(self):
        self.string_list.append("buzz")

    def fizzbuzz(self):
        self.string_list.append("fizzbuzz")

    def number(self):
        self.string_list.append(str(self.index + 1))