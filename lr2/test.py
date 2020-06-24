from datetime import datetime

from cached.cached import cached

from singleton.singleton import Singleton

from vector.vector import Vector

from simple_json.simple_json import to_json

import json


def test_singleton_single_attr():
    class A(metaclass=Singleton):
        def __init__(self, p):
            setattr(self, 'p', p)

    a = A('val_1')
    b = A('val_2')

    assert b.p == 'val_1'


def test_singleton_plural_attr():
    class A(metaclass=Singleton):
        def __init__(self, p, k):
            setattr(self, 'p', p)
            setattr(self, 'k', k)

    a = A('val_1', 20)
    b = A('val_2', 40)

    assert (b.p == 'val_1' and b.k == 20)


def test_singleton_changed_attr():
    """

    :return: Этот тест должен быть не пройден, т.к.
    Синглетон данной реализации работает только с конструкторами.
    """
    class A(metaclass=Singleton):
        def __init__(self, p, k):
            setattr(self, 'p', p)
            setattr(self, 'k', k)

    a = A('val_1', 20)
    b = A('val_2', 40)
    b.k = 'val_2'

    assert (b.p == 'val_1' and b.k == 20)


def test_cached_single_attr():
    """

    :return: Если декоратор caсhed не работает,
    func возвращает удвоенный аргумент тестируемой функции.
    """
    flag = False
    @cached
    def func(attr):
        nonlocal flag
        if not flag:
            flag = True
            return attr
        else:
            return 2 * attr

    assert func(5) == func(5) and flag


def test_cached_plural_attr():
    flag = False
    @cached
    def func(*args, **kwargs):
        """

        :param args: позиционные аргументы
        :param kwargs: именованные аргументы
        :return: Если cached не работает, args = None, kwargs = None.
        """
        nonlocal flag
        if not flag:
            flag = True
            return args, kwargs
        else:
            return None, None

    args, kwargs = func(5)
    args, kwargs = func(5)

    assert flag and args == (5, ) and kwargs == {}


def test_cached_time():
    """

    :return: Сравнивает скорость
    выполнения при большом количестве аргументов.
    Тест не должен быть пройден.
    """
    @cached
    def func1(*args, **kwargs):
        return True

    def func2(*args, **kwargs):
        True

    time1 = datetime.now()
    func1((i for i in range(3000)))
    time1 = datetime.now() - time1

    time2 = datetime.now()
    func2((i for i in range(3000)))
    time2 = datetime.now() - time2

    assert time1 < time2


def test_vector_multiplication_diff_len():
    """

    :return: Векторы разной длины не должны умножаться.
    """
    v1 = Vector([3, 5, 6])
    v2 = Vector([1, 3, 5, 7])

    try:
        res = (v1 * v2)
    except:
        res = 'error'
    assert res != 'error'


def test_vector_multiplication_eq_len():
    v1 = Vector([3, 5, 6])
    v2 = Vector([1, 3, 5])

    try:
        res = (v1 * v2)
    except:
        res = 0

    assert res == 48


def test_parse_to_json():
    class A:
        def __init__(self):
            self.e = [4, 5, 6]
            self.f = {'7': 8, '9': 10}
            self.g = True
            self.l = None

    class Jsn:
        def __init__(self):
            self.a = 0
            self.b = 1
            self.c = '3'
            self.d = A()

    j = Jsn()
    res = '{"a": 0, "b": 1, "c": "3", "d": ' \
          '{"e": [4, 5, 6], "f": {"7": 8, "9": 10}, ' \
          '"g": "true", "l": "null"}}'

    assert to_json(j) == res


def test_parse_to_json_speed():
    """

    :return: Сравнивает скорость выполнения стандартной реализации
    преобразования в json и реализации в модуле simple_json.py.
    Тест не должен быть пройден.
    """
    arr = [val for val in range(1000)]
    time1 = datetime.now()
    res1 = to_json(arr)
    time1 = datetime.now() - time1

    time2 = datetime.now()
    res2 = json.dumps(arr)
    time2 = datetime.now() - time2

    assert time1 < time2 and res1 == res2
