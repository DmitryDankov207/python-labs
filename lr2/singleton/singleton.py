class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = \
                super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


def __demonstrate():
    class A(metaclass=Singleton):
        def __init__(self, val):
            setattr(self, "a", val)

    a = A(5)
    print(a.a)
    b = A(6)
    print(b.a)


if __name__ == '__main__':
    __demonstrate()
