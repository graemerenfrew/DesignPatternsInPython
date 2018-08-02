import abc
from computer import Computer

class AbsBuilder(object):
    __metaclass__ = abc.ABCMeta

    ''' Implement the get and new methods in the abstract base clase
        otherwise these would have had to been repeated in each of the concrete
        builder classes 
    '''
    def get_computer(self):
        return self._computer

    def new_computer(self):
        self._computer = Computer()

    '''each step of building a computer is represented here by abstract methods
        which each of the concrete builders must implement
    '''

    @abc.abstractmethod
    def build_mainboard(self):
        pass

    @abc.abstractmethod
    def get_case(self):
        pass

    @abc.abstractmethod
    def install_mainboard(self):
        pass


    @abc.abstractmethod
    def install_hard_drive(self):
        pass


    @abc.abstractmethod
    def install_video_card(self):
        pass
