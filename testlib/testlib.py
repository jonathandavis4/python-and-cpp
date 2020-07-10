from ctypes import CDLL, c_char_p


so_file = 'C++/testlib.so'


def hello_world():
    lib = CDLL(so_file)
    lib.hello_world()

def add(a, b):
    lib = CDLL(so_file)
    return lib.add(a, b)

def multiply_by_2(a):
    lib = CDLL(so_file)
    double = lib.multiply_by_2(a)
    return double

def get_string():
    lib = CDLL(so_file)
    lib.get_string.restype = c_char_p
    s_bytes = lib.get_string()
    s_unicode = s_bytes.decode()
    return s_unicode

def get_obj_id():
    class MyClass(object):
        @property
        def _as_parameter_(self):
            my_id = id(self)
            return f'MyClass {my_id}'.encode()

    lib = CDLL(so_file)
    obj = MyClass()
    lib.get_obj_id.restype = c_char_p
    obj_id_string = lib.get_obj_id(obj).decode()
    return obj_id_string
