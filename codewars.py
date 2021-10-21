# def to_camel_case(text: str) -> str:
#     try:
#         if text == '':
#             raise ZeroDivisionError

#         arrText = [text if idx == 0 else text.title() for idx, text in enumerate(
#             text.replace('-', '@').replace('_', '@').split('@'))]

#         return ''.join(arrText)

#     except ZeroDivisionError:
#         return text


# ------------------------------------
# def to_camel_case(s):
#     return s[0] + s.title().translate(None, "-_")[1:] if s else s

# -------------------------------------------------------


# import re


# lambda x: x.group(1).upper()

# def textLamda(x):
#     print(x.group(1))
#     return x.group(1).upper()


# def to_camel_case(text):
#     return re.sub('[_-](.)', textLamda, text)

# ------------------------------------------------------------
# def to_camel_case(text):
#     return reduce(lambda p, n: p + n[0].upper() + n[1:], re.split('[-_]', text))


# print(to_camel_case(""))
# print(to_camel_case("the-stealth-warrior"))
# print(to_camel_case("The_Stealth_Warrior"))
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# # return ['Senior' if (x, y) >= (55, 8) else 'Open' for (x, y) in data] not raight

# def open_or_senior(data):
#     return ['Senior' if x >= 55 and y >= 8 else 'Open' for (x, y) in data]


# def openOrSenior(data):
#     return map(lambda d: 'Senior' if d[0] >= 55 and d[1] > 7 else 'Open', data)


# print(open_or_senior([(45, 12), (55, 21), (19, -2), (104, 20)]))
# print(open_or_senior([(16, 23), (73, 1), (56, 20), (1, -1)]))
# print(open_or_senior(
#     [[18, 20], [45, 2], [61, 12], [37, 6], [21, 21], [78, 9]]))
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

# def xo(s):
#     return s.lower().count('o') == s.lower().count('x')


# print(xo('ooxx'))
# print(xo('xooxx'))
# print(xo('ooxXm'))
# print(xo('zpzpzpp'))
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def unique_in_order(iterable):
#     newArr = []
#     for idx, val in enumerate(iterable):
#         try:
#             if len(iterable) - 1 == idx or val != iterable[idx + 1]:
#                 newArr.append(val)

#         except IndexError:
#             break

#     return newArr
# -----------------------------------------------------------------------

# def unique_in_order(iterable):
#     return [n for idx, n in enumerate(iterable) if len(iterable) - 1 == idx or n != iterable[idx + 1]]
# -----------------------------------------------------------------------

# def unique_in_order(iterable):
#     print(iterable[0:])
#     print(iterable)
#     return None
# -----------------------------------------------------------------------
# from itertools import groupby


# def unique_in_order(iterable):                     best!!!!!!!
#     print(tuple(groupby(iterable))[1][0])
#     print(list(groupby(iterable))[0][0])
#     return [k for (k, _) in groupby(iterable)]


# print(unique_in_order('AAAABBBCCDAABBB'))
# print(unique_in_order('ABBCcAD'))
# print(unique_in_order([1, 2, 2, 3, 3]))
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def find_outlier(integers):

#     findIndex = None
#     newIntegers = [n % 2 for n in integers]

#     if newIntegers.count(0) > newIntegers.count(1):
#         findIndex = newIntegers.index(1)
#     else:
#         findIndex = newIntegers.index(0)

#     return integers[findIndex]
# -----------------------------------------------------------------------


# def find_outlier(integers):
#     parity = [n % 2 for n in integers]
#     return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]


# print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
# print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def high_and_low(numbers):
#     splitArr = numbers.split(' ')

#     return f'{max(splitArr, key=lambda i: int(i))} {min(splitArr, key=lambda i: int(i))}'


# def high_and_low(numbers):  # z.
#     nn = [int(s) for s in numbers.split(" ")]
#     return "%i %i" % (max(nn), min(nn))

# def high_and_low(numbers):
#     n = list(map(int, numbers.split(' ')))
#     return str(max(n)) + ' ' + str(min(n))

# def high_and_low(numbers):
#     return " ".join(x(numbers.split(), key=int) for x in (max, min))


# print(high_and_low("1 2 3 4 5"))
# print(high_and_low("1 2 -3 4 5"))
# print(high_and_low("1 9 3 4 -5"))

# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def valid_parentheses(string):

#     filterList = [n for n in string if n == '(' or n == ')']
#     if not len(filterList):
#         return True

#     try:
#         print(eval(''.join(filterList)))
#     except SyntaxError:
#         return False
#     except TypeError:
#         return True

#     return True


# def valid_parentheses(string):
#     string = "".join(ch for ch in string if ch in "()")
#     while "()" in string: string = string.replace("()", "")
#     return not string

# import re

# def valid_parentheses(s):
#     try:
#         re.compile(s)
#     except:
#         return False
#     return True


# print(valid_parentheses(''))
# print(valid_parentheses('    '))
# print(valid_parentheses('()'))
# print(valid_parentheses(")(()))"))
# print(valid_parentheses("("))
# print(valid_parentheses("(())((()())())"))
# print(valid_parentheses("  ("))
# print(valid_parentheses(")test"))
# print(valid_parentheses("hi())("))
# print(valid_parentheses("hi(hi)()"))
# # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# def two_sum(numbers, target):

#     firstIndex = 0
#     lastindex = 1

#     while True:
#         if lastindex == len(numbers):
#             lastindex = firstIndex
#             firstIndex += 1

#         if numbers[firstIndex] + numbers[lastindex] == target:
#             return (firstIndex, lastindex)
#         else:
#             lastindex += 1


# print(two_sum([1, 2, 3], 4))
# print(two_sum([1234, 5678, 9012], 14690))
# print(two_sum([2, 2, 3], 4))
# @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# from itertools import zip_longest

# def solution(s):
#     i_ = iter(s)
#     return [x + y for (x, y) in zip_longest(i_, i_, fillvalue='_')]
# -------------------------------------------
# import re

# def solution(s):
#     return re.findall(".{2}", s + "_")
# -------------------------------------------
# import re

# def solution(s):
#     return re.findall('..', s + '_')
# ========================================================================
# from itertools import zip_longest

# def solution(s):
#     return [''.join(a) for a in zip_longest(s[::2], s[1::2], fillvalue='_')]
# -----------------------------------------------------------------------
# def solution(s):
#     return list(map(''.join, zip(*[iter(s + '_')] * 2)))


# print(solution('abc'))
# print(solution('abcdef'))
# print(solution("asdfads"))
# print(solution(""))
# print(solution("x"))
