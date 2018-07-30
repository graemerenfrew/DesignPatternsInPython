from observer import AbsObserver

class CurrentKPIs(AbsObserver):
    open_tickets = -1
    closed_tickets = -1
    new_tickets = -1

    def __init__(self, kpis):  # <-- takes a reference to the Subject in the constructor, so the observer know what it is observing
        self._kpis = kpis
        kpis.attach(self)  # <-- this observer is now attached to the kpis subject

    def update(self):
        '''
        This method uses the refernce to the kpi subject to get a reference to the subject's properties
        :return:
        '''
        self.open_tickets = self._kpis.open_tickets
        self.closed_tickets = self._kpis.closed_tickets
        self.new_tickets = self._kpis.new_tickets
        self.display()

    def display(self):
        print('Current Open tickets: {}'.format(self.open_tickets))
        print('Current Closed tickets: {}'.format(self.closed_tickets))
        print('Current New tickets: {}'.format(self.new_tickets))