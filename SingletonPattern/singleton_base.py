class Singleton(object):
    '''this base class keeps track of all instances in a dictionary'''
    _instances = {}     # dict([cls, instance])

    def __new__(cls, *args, **kwargs):
        ''' new is invoked each time a given class is instantiated, but BEFORE init'''
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]
