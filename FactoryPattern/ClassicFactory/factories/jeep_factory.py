from .abs_factory import AbsFactory
from autos.jeepsahara import jeepsahara

class JeepFactory(AbsFactory):

    ''' This is not a true part of the factory pattern, it's just one way we could implement it'''
    def create_autos(self):
        self.jeep = jeep = jeepsahara()
        jeep.name = 'Jeep Sahara'
        return jeep