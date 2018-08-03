from .abs_auto import AbsAuto

class fordfocus(AbsAuto):
    def start(self):
        print('%s running with power' % self.name)

    def stop(self):
        print('%s stopping' % self.name)