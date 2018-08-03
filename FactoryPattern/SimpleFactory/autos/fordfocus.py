from .abs_auto import AbsAuto

class fordfocus(AbsAuto):
    def start(self):
        print('Ford focus running with power')

    def stop(self):
        print('Ford focus stopping')