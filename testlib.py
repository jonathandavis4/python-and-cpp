import ctypes


def hello_world():
    lib = ctypes.CDLL('./lib.so')
    lib.hello_world()

def add(a, b):
    lib = ctypes.CDLL('./lib.so')
    return lib.add(a, b)

def multiply_by_2(a):
    lib = ctypes.CDLL('./lib.so')
    double = lib.multiply_by_2(a)
    return double

def get_string():
    lib = ctypes.CDLL('./lib.so')
    lib.get_string.restype = ctypes.c_char_p
    s_bytes = lib.get_string()
    s_unicode = s_bytes.decode()
    return s_unicode

def get_obj_id():
    class MyClass(object):
        @property
        def _as_parameter_(self):
            my_id = id(self)
            return f'MyClass {my_id}'.encode()

    lib = ctypes.CDLL('./lib.so')
    obj = MyClass()
    lib.get_obj_id.restype = ctypes.c_char_p
    obj_id_string = lib.get_obj_id(obj).decode()
    return obj_id_string
