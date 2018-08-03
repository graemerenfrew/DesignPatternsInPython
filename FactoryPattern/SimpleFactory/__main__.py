from autofactory import AutoFactory
''' import an instance of the autofactory'''

factory = AutoFactory()

''' loop through each one'''
for carname in 'chevyvolt','fordfocus','jeepsahara','Tesla':
    car = factory.create_instance(carname)
    car.start()
    car.stop()