import datetime


class Singleton(type):  #note this is not inheriting from Objects
    _instances = {}

    ''' instead of new methods'''
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]