
from abc import ABCMeta
from observer_abc import AbsObserver

class AbsSubject(metaclass=ABCMeta):
    _observers = set()  #create a private set for storing the references to observers

    ''' We actually code an implementation here!  
        In python, ABCs can have implementations if it is standardised and simple enough..
    '''

    def attach(self, observer):
        if not isinstance(observer, AbsObserver):
            raise TypeError("This Observer object was not derived from AbsObserver")
        self._observers |= {observer} #append into the set

    def detach(self, observer):
        self._observers -= {observer} #remove from set

    '''
    Loop through the observers in the set, and update them.
    The optional parameter value is supplied, update is called with it
    '''
    def notify(self, value=None):
        for observer in self._observers:
            if value is None:
                observer.update()
            else:
                observer.update(value)

    def __enter__(self):
        return self

    @abstractmethod
    def __exit__(self, exc_type, exc_value, traceback):
        self._observers.clear()  #disconnect all the observers
