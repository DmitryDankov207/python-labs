import re


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


def get_var_name(var):
        for k, v in globals().items():
            if v is var:
                return k    


def get_class_name(obj):
    return '_%s' % str(type(obj)).split('.')[-1][:-2]


def get_attr_names(obj):
    obj_name = get_class_name(obj)
    try:
        obj_attrs = {re.sub(obj_name, '', k):v for k, v in obj.__dict__.items()}
    except AttributeError:
        raise Exception('Invalid attribute!')
    obj_attrs = {k: v for k, v in obj_attrs.items() if not k.startswith('__')}
    return obj_attrs


def parse_obj(obj, json=''):
    v_type = type(obj)
    if obj is None:
        json += r'"null"'
    elif v_type is str:
        json += r'"%s"' % obj
    elif v_type in {list, dict}:
        json += str(obj).replace('\'', r'"')
    elif str(obj).isnumeric():
        json += str(obj)
    elif v_type is bool:
        json = json + r'"true"' if obj else json + r'"false"'
    else:
        json += to_json(obj)
    return json


def parse_list(list_):
    json = '['
    for val in list_:
        json += parse_obj(val) + ', '
    return json[:-2] + ']'


def to_json(obj):
    if type(obj) is list:
        return parse_list(obj)

    obj_attrs = get_attr_names(obj)
    json = '{'
    for key, val in obj_attrs.items():
        json += r'"%s": ' % key
        json = parse_obj(val, json)
        if key != list(obj_attrs)[-1]:
            json += ', '
        else:
            json += '}'
    return json


if __name__ == '__main__':
    obj = Jsn()
    res = to_json(obj)
    print(res)
