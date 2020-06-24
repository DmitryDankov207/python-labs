def cached(func):
    res_dict = {}

    def fill_dict(*args, **kwargs):
        res_dict['cached'] = func(*args, **kwargs)
        res_dict['args'] = args
        res_dict['kwargs'] = kwargs

    def wrapper(*args, **kwargs):
        try:
            if res_dict['cached'] \
                    and res_dict['args'] == args \
                    and res_dict['kwargs'] == kwargs:
                pass
            else:
                fill_dict(*args, **kwargs)
        except KeyError:
            fill_dict(*args, **kwargs)
        return res_dict['cached']

    return wrapper



@cached
def mul(a, b):
    return a * b


@cached
def get_sum(a, b, c):
    return a + b + c


if __name__ == '__main__':
    print(mul(10, 6))
    print(get_sum(10, 6, c=15))
    print(mul(10, 6))
    print(get_sum(10, 6, c=15))
