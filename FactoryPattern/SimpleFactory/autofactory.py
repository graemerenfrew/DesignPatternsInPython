from inspect import getmembers, isclass, isabstract
import autos
''' these are imported from the introspection module'''
''' the autos package import will also import the other classes in the __init__ in the auto package'''


class AutoFactory(object):
    ''' this dictionary stores the model and a REFERENCE To the class definition of that model'''
    autos = {} #key value pair of model and the class

    def __init__(self):
        ''' this builds the dictionary'''
        self.load_autos()

    def load_autos(self):
        ''' find the concrete classes that were imported into the autos package in the autos.__init__'''
        classes = getmembers(autos,
                             lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            '''Look for subclasses of the abstract auto base classes to the dictionary'''
            if isclass(_type) and issubclass(_type, autos.AbsAuto):
                self.autos.update([[name, _type]])

    def create_instance(self, carname):
        ''' look for the carname in the autos dictionary
            If it finds one it will return it, else it will create and instance of the nullcar
        '''
        if carname in self.autos:
            return self.autos[carname]()
        else:
            return autos.NullCar(carname)