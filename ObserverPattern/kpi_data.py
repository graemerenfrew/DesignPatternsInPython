from collections import namedtuple
from itertools import starmap

data = (('new', 25), ('open', 66), ('closed',25)) #iterable tuples
nt = namedtuple('KPI', 'name value')
KPI_Data = starmap(nt, data)