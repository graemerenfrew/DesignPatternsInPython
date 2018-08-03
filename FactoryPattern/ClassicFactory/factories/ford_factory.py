from .abs_factory import AbsFactory
from autos.fordfocus import fordfocus

class FordFactory(AbsFactory):

    ''' This is not a true part of the factory pattern, it's just one way we could implement it'''
    def create_autos(self):
        self.ford = ford = fordfocus()
        ford.name = 'Ford Focus'
        return ford