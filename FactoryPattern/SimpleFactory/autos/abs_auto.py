import abc

class AbsAuto(metaclass=abc.ABCMeta):
    ''' this methods must be implemented bby the concreate classes'''
    @abc.abstractmethod
    def start(self):
        pass

    @abc.abstractmethod
    def stop(self):
        pass