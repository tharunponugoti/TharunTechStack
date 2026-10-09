What are Dunder Methods in Python?

Dunder means Double Underscore.
Dunder methods are special methods in Python whose names begin and end with two underscores (__).

__init__()
__str__()
__len__()
__add__()
__eq__()


a = 10
b = 20

print(a + b)


Python internally uses the integer type  addition behavior, associated with __add__().

Similarly, when you  create an object, Python can call __init__() to initialize  it.

Why do we use dunder methods?

Create an object
print an object
Add, subtract, or compare objects.
Find an object length.
ccess items using indexing.
Iterate over objects.
Use operators such as in, ==, and +.
Use an object like a function.


__init__()

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s1 = Student("Rahul", 20)

print(s1.name)
print(s1.age)


__str__() and __repr__()
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Student name: {self.name}"

    def __repr__(self):
        return f"Student({self.name!r}, {self.age})"

s1 = Student("Rahul", 20)

print(s1)
print(repr(s1))

Dunder method	Operator or operation
__add__(self, other)	+
__sub__(self, other)	-
__mul__(self, other)	*
__matmul__(self, other)	@
__truediv__(self, other)	/
__floordiv__(self, other)	//
__mod__(self, other)	%
__divmod__(self, other)	divmod()
__pow__(self, other)	**
__lshift__(self, other)	<<
__rshift__(self, other)	>>
__and__(self, other)	&
__xor__(self, other)	^
__or__(self, other)	\|



custom addition __add__()

class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

a = Number(10)
b = Number(20)

print(a + b)
