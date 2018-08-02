class Director(object):


    ''' The client will pass in the builder it wants to use, and this director will go
    and do all the steps in the correct order, using what ever builder it is sent'''
    def __init__(self):
        self._builder = builder

    def build_computer(self):
        self._builder.new_computer()
        self._builder.get_case()
        self._builder.build_mainboard()
        self._builder.install_mainboard()
        self._builder.install_hard_drive()
        self._builder.install_video_card()

    ''' This is to retrieve the finished computer from the builder'''
    def get_computer(self):
        return self._builder.get_computer()