import inspect

def introspection_info(obj):
    obj_info = {}
    obj_methods = []
    obj_attributes = []
    obj_info["type"] = type(obj).__name__
    try:
        obj_info["module"] = obj.__module__
    except:
        obj_info['module'] = 'n/a'
    try:
        for attr_name in obj.__dict__:
            obj_attributes.append(attr_name)
    except:
        obj_attributes.append('n/a')
    obj_info['attributes'] = obj_attributes
    for meth_name in dir(obj):
        meth = getattr(obj, meth_name)
        if inspect.ismethod(meth) or inspect.ismethodwrapper(meth) or inspect.isbuiltin(meth):
            obj_methods.append(meth_name)
    obj_info['methods'] = obj_methods
    return obj_info


class MyClass:
    def __init__(self):
        self.attribute_1 = 100
        self.attribute_2 = 'text'

    def func_1(self):
        pass

obj_class = MyClass()
print(introspection_info(obj_class))

# for attr_name in obj_class.__dict__:
#     print(attr_name)

print(obj_class.__dict__)

num = [1,2]
print(introspection_info(num))

# from pprint import pprint
# pprint(dir(obj_class))