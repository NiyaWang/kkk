import sys
from pprint import pprint


def introspection_info(obj):
    obj_type = type(obj).__name__
    obj_module = getattr(obj, '__module__', 'built-in')
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith('__')]
    methods = [attr for attr in dir(obj) if callable(getattr(obj, attr)) and not attr.startswith('__')]
    all_members = dir(obj)

    return {
        'type': obj_type,
        'module': obj_module,
        'attributes': attributes,
        'methods': methods,
        'all_members': all_members
    }



string_info = introspection_info('String')
print(string_info)
