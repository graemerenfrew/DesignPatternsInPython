from .abs_auto import AbsAuto

class chevyvolt(AbsAuto):
    def start(self):
        print('Chevy Volt running with power')

    def stop(self):
        print('Chevy Volt stopping')