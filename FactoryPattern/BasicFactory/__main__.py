from chevyvolt import chevyvolt
from fordfocus import fordfocus
from jeepsahara import jeepsahara
from nullcar import NullCar

def getcar(carname):
    if carname == 'Chevy':
        return chevyvolt()
    elif carname == 'Ford':
        return fordfocus()
    elif carname == 'Jeep':
        return jeepsahara()
    else:
        return NullCar(carname)

for carname in 'Chevy','Ford','Jeep','Tesla':
    car = getcar(carname)
    car.start()
    car.stop()