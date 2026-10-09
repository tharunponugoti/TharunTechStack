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


# 3.Iterator that iterates over a string character by character in reverse order
#
# class ReverseString:
#     def __init__(self, text):
#         self.text = text
#         self.index = len(text) - 1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index >= 0:
#             value = self.text[self.index]
#             self.index -= 1
#             return value
#
#         raise StopIteration
#
#
# text = "PYTHON"
#
# obj = ReverseString(text)
#
# for char in obj:
#     print(char)


# 4.Write an iterator that yields elements of a list with their index (don’t use
# enumerate).
#
#
# class ListWithIndex:
#     def __init__(self, items):
#         self.items = items
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.items):
#             result = (self.index, self.items[self.index])
#             self.index += 1
#             return result
#
#         raise StopIteration
#
#
# items = ["Python", "SQL", "Django"]
#
# obj = ListWithIndex(items)
#
# for item in obj:
#     print(item)



# 5. Write a generator that yields digits from an integer one by one.
#
# def digits(number):
#     for digit in str(number):
#         yield int(digit)
#
#
# number = 12345
#
# for digit in digits(number):
#     print(digit)
#

#
# 6. Create a generator that yields cumulative sum of numbers in a list. Example:
# [1,2,3] → 1, 3, 6

# def cumulative_sum(numbers):
#     total = 0
#
#     for number in numbers:
#         total += number
#         yield total
#
#
# numbers = [1, 2, 3]
#
# for value in cumulative_sum(numbers):
#     print(value)



# 7. Implement a generator that yields vowels from a string.
#
# def vowels(text):
#     for char in text:
#         if char.lower() in "aeiou":
#             yield char
#
#
# text = "Python Programming"
#
# for vowel in vowels(text):
#     print(vowel)



# 8.Create an iterator that yields words from a sentence one by one.
#
#
# class Words:
#     def __init__(self, sentence):
#         self.words = sentence.split()
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.words):
#             word = self.words[self.index]
#             self.index += 1
#             return word
#
#         raise StopIteration
#
#
# sentence = "Python is easy to learn"
#
# obj = Words(sentence)
#
# for word in obj:
#     print(word)


# 9. Write an iterator that returns characters at even indices of a string.
#
# class EvenIndexCharacters:
#     def __init__(self, text):
#         self.text = text
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.index < len(self.text):
#             value = self.text[self.index]
#             self.index += 2
#             return value
#
#         raise StopIteration
#
#
# text = "Python"
#
# obj = EvenIndexCharacters(text)
#
# for char in obj:
#     print(char)

#
# 10.Implement a generator that yields running maximum from a list Example:
# [3,1,4,2] → 3, 3, 4, 4
#
#
# def running_maximum(numbers):
#     maximum = numbers[0]
#
#     for number in numbers:
#         if number > maximum:
#             maximum = number
#
#         yield maximum
#
#
# numbers = [3, 1, 4, 2]
#
# for value in running_maximum(numbers):
#     print(value)