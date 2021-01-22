import array
import sys
from collections import Counter
import datetime
from itertools import islice, count

from jinja2._compat import ifilter

"""
>>> from collections import Counter
>>> z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
>>> Counter(z)
Counter({'blue': 3, 'red': 2, 'yellow': 1})
"""

# def test_wrap(func):
#     def func_wrapper(name):
#         return f"function name is: {func(name)}"
#     return func_wrapper


sample_array = array.array('s', ["George", "Ricardo", "Silva"])
print(sample_array.index(0))

# @test_wrap
# def test(name):
#     return "test..." + name
#
#
# def get_unique(l):
#     uniques = []
#
#     for i in l:
#         if l.count(i) == 1:
#             uniques.append(i)
#
#     return uniques

# print([i for i in ifilter(lambda x: x % 5, islice(count(5), 10))])

# def my_function():
#     print(my_function.what)
#
#

# my_function.what = "right?"
# my_function() # Prints "right?"
#
# a = 10
# print(sys.path)
# l = [1, 2, 3]
# try:
#     l[5]
# except IndexError:
#     print("error")
# finally:
#     print("final")
# def a():
#     return 10
#
# print(type(a))

# print(type(my_function))
# print(type(a))

# if __name__ == '__main__':
#     # print(test("George"))
#     # l = [n for n in range(0, 100) if n % 2 == 0]
#     print(get_unique([1, 2, 3, 4, 4, 6, 7, 3, 4, 5, 2, 7]))

"""
Generators is a callable object that acts as an iterable (Objects you can iterate in for cycles, etc..)
"""
