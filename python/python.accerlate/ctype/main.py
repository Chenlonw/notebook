import ctypes

class People(ctypes.Structure):
    _fields_ = [("name", ctypes.c_char * 20), ("age", ctypes.c_int)]

if __name__ == "__main__":
    lib = ctypes.cdll.LoadLibrary("./libtest.so")
    lib.people_init.restype = ctypes.POINTER(People)
    p = lib.people_init(ctypes.c_int32(24))

    print "%s: %d" %(p.contents.name, p.contents.age)
