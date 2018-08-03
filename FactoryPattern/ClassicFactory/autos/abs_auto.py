import abc

class AbsAuto(metaclass=abc.ABCMeta):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    ''' this methods must be implemented bby the concreate classes'''
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass