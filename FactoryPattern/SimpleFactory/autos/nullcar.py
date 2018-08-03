from .abs_auto import AbsAuto

class NullCar(AbsAuto):
    ''' This a constructor, which the other concrete classes don't have
    this is so the user can pass an unsupported car make to the program, and this object
    will return something useful, rather than just breaking'''
    def __init__(self, carname):
        self._carname = carname

    def start(self):
        print('Unknown car "%s."' % self._carname)

    def stop(self):
        pass
