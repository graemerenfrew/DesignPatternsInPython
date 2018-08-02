from abs_builder import AbsBuilder

''' Now inherits from AbsBuilder and implements the required methods'''

class MyComputerBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case = 'Some case'

    def build_mainboard(self):
        self._computer.mainboard = 'MSI'
        self._computer.cpu = 'Intel Due Core 2'
        self._computer.memory = 'Corsair MB4'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'Segate 2TB'

    def install_video_card(self):
        self._computer.video_card = 'GEFOXES'