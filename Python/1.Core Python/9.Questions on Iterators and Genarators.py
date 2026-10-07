# ----Questions on Iterators
#
#
# 1,Write a custom iterator that prints numbers from 1 to N.

# class Numbers:
#     def __init__(self, n):
#         self.n = n
#         self.current = 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current <= self.n:
#             value = self.current
#             self.current += 1
#             return value
#         else:
#             raise StopIteration
#
#
# obj = Numbers(5)
#
# for number in obj:
#     print(number)



# 2. Create an iterator that returns only even numbers from a given list.

# class EvenNumbers:
#     def __init__(self, numbers):
#         self.numbers = numbers
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.index < len(self.numbers):
#
#             value = self.numbers[self.index]
#             self.index += 1
#
#             if value % 2 == 0:
#                 return value
#
#         raise StopIteration
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]
#
# obj = EvenNumbers(numbers)
#
# for number in obj:
#     print(number)


3.Iterator that iterates over a string character by character in reverse order

class ReverseString:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            value = self.text[self.index]
            self.index -= 1
            return value

        raise StopIteration


text = "PYTHON"

obj = ReverseString(text)

for char in obj:
    print(char)



3.Iterator that iterates over a string character by character in reverse order

class ReverseString:
    def __init__(self, text):
        self.text = text
        self.index = len(text) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            value = self.text[self.index]
            self.index -= 1
            return value

        raise StopIteration


text = "PYTHON"

obj = ReverseString(text)

for char in obj:
    print(char)



