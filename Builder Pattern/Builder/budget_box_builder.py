from abs_builder import AbsBuilder

''' Now inherits from AbsBuilder and implements the required methods'''

class BudgetBoxBuilder(AbsBuilder):

    def get_case(self):
        self._computer.case = 'Some cheap case'

    def build_mainboard(self):
        self._computer.mainboard = 'Donky'
        self._computer.cpu = 'Intel Due Core 1'
        self._computer.memory = 'Corsair MB2'

    def install_mainboard(self):
        pass

    def install_hard_drive(self):
        self._computer.hard_drive = 'Segate 500GB'

    def install_video_card(self):
        self._computer.video_card = 'onboard'