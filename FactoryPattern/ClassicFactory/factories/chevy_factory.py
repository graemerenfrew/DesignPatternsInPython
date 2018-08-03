from .abs_factory import AbsFactory
from autos.chevyvolt import chevyvolt

class ChevyFactory(AbsFactory):

    ''' This is not a true part of the factory pattern, it's just one way we could implement it'''
    def create_autos(self):
        self.chevy = chevy = chevyvolt()
        chevy.name = 'Chevy Volt'
        return chevy