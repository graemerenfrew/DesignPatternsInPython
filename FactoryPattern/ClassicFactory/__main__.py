from factories import loader
''' this loader module is the one that does dynamic imports'''

for factory_name in 'chevy_factory','jeep_factory','ford_factory','tesla_factory':
    factory = loader.load_factory(factory_name)
    car = factory.create_autos()

    car.start()
    car.stop()