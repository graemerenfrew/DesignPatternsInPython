from importlib import import_module
from inspect import getmembers, isabstract, isclass
from .abs_factory import AbsFactory

''' This module uses dynamic imports.  We give it a factory name, and it tries to import it from the factories package
    This means we don't import a load of factories that we don't end up needing
    As the init in the factories package is now empty, we can add new factories just by adding a class to the factories package folder
'''
def load_factory(factory_name):
    try:
        factory_module = import_module('.' + factory_name, 'factories')
    except ImportError:
        factory_module = import_module('.null_factory', 'factories')

    classes = getmembers(factory_module,
                         lambda m: isclass(m) and not isabstract(m))

    for name, _class in classes:
        if issubclass(_class, AbsFactory):
            return _class()