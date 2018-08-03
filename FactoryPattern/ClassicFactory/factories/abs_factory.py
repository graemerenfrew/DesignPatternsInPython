import abc
''' This new factory base class - and each factory must implement this'''

class AbsFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_autos(self):
        pass