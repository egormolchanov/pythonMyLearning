import random
from collections import Counter
print([n*n for n in range(0, 11) if n % 2 != 0])
print([n*n if n*n == 9 else '55' for n in range(0, 11) if n % 2 != 0])
print([(x, y) for x in range(0, 9) for y in range(0, 18, 2) if x + y == 0])


class StrConverter:

    @staticmethod
    def to_str(bytes_or_str):
        if isinstance(bytes_or_str, bytes):
            value = bytes_or_str.decode('utf-8')
        else:
            value = bytes_or_str
        return value

    @staticmethod
    def to_bytes(bytes_or_str):
        if isinstance(bytes_or_str, str):
            return bytes_or_str.encode('utf-8')
        return bytes_or_str


# test = StrConverter()

List1 = [4, 87, 4, 73, 16, 34]
List2 = [73, 12, 34, 4, 8, 99, 73]

# Написать код, который бы вывел (в уникальном виде) цифры, которые есть в обоих списках
# Вывод:
# 4, 34, 73

list3 = [n for n in List1 for y in List2 if n != y]

print(set(list3))

print(list(filter(lambda u: list3.count(u) > 2, list3)))

print(StrConverter.to_str('A'))
print(StrConverter.to_str('\x41'))
print(StrConverter.to_bytes('A'))
print(StrConverter.to_bytes('\x41'))


class Animal:
    def die(self):
        print('bye-bye')
        self.health = 0


class Carnivour:
    def hunt(self):
        print('eating')
        self.satiety = 100


class Dog(Animal, Carnivour):
    def bark(self):
        print('woof-woof')


class Road():
    def __init__(self, length) -> None:
        self.length = length

    def __str__(self) -> str:
        return f'self.length {self.length}'

    def __len__(self):
        return self.length

    def __del__(self):
        print('destroyed')


# ---------------------------------------------------------------
board = [' ' for _ in range(0, 9)]


def print_state(state):
    for i, c in enumerate(state):
        if (i + 1) % 3 == 0:
            print(f'{c}')
        else:
            print(f'{c}|', end='')


print_state(board)
winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                        (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]


def get_winner(state, combinations):
    for (x, y, z) in combinations:
        if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == '0'):
            return state[x]
    return ''


def play_game(board):
    current_sing = 'X'
    while(get_winner(board, winning_combinations) == ''):
        index = int(input(f'Where do you want to draw {current_sing}?'))
        board[index] = current_sing

        print_state(board)

        winner_sing = get_winner(board, winning_combinations)
        if winner_sing != '':
            print(f'We have a winner: {winner_sing}')

        current_sing = 'X' if current_sing == '0' else '0'


# play_game(board)
# for i, c in enumerate(range(0, 8)):
#     print(i, c)
# import requests

# res = requests.get('https')
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
print('#######')

alphabet = ('a', 'e', 'i', 'o', 'u', 'y')


def count_vowels(param):
    count = 0
    for n in alphabet:
        count += param.count(n)
    return count


def count_vowels(param):
    return len([n for n in param if n in alphabet])


def count_vowels(param):
    return len(list(filter(lambda n: n in alphabet, param)))


def count_vowels(param):
    return sum([1 for n in param.lower() if n in alphabet])


# print(count_vowels('abcd'))
# print(count_vowels('abcdef'))
# print(count_vowels('bdc'))
# print(count_vowels('aaaiel'))


def is_full_house(arr):
    list1 = list(set([arr.count(n) for n in arr]))
    return 2 in list1 and 3 in list1


def is_full_house(arr):
    list1 = Counter(arr).values()
    return 2 in list1 and 3 in list1


# print(is_full_house(['A', 'A', 'A', 'K', 'K']))
# print(is_full_house(['3', 'J', 'J', '3', '3']))
# print(is_full_house(['10', 'J', '10', '10', '10']))
# print(is_full_house(['10', 'J', '10', '3', '2']))

def check_sequence(arr):
    if (arr == sorted(arr, reverse=True)):
        return -1
    elif arr == sorted(arr):
        return 1 if len(set(arr)) == len(arr) else 0
    return 0


# print(check_sequence([1, 2, 3]))
# print(check_sequence([3, 2, 1]))
# print(check_sequence([1, 1, 2]))
# print(check_sequence([1, 2, 1]))
# print(check_sequence([2, 2, 3]))
# print(check_sequence([1, 2, 2]))
# _____________________________________________________
file = open('WordsStockRus.txt', 'r', encoding="utf-8").readlines()
word = file[random.randrange(0, len(file))]

print(word)


class GameGallows():

    def __init__(self, attempts=3):
        '''Constructor'''
        self.__attempts = attempts
        self.word = ''

    @property
    def attempts(self):
        return self.__attempts


inst = GameGallows()
