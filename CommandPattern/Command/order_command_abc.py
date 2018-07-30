from abc import ABCMeta, abstractproperty

class AbsOrderCommand(metaclass=ABCMeta):
    @abstractproperty
    def name(self):
        pass

    @abstractproperty
    def description(self):
        pass