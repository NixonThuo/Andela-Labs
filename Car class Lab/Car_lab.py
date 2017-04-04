class Car(object):
    def __init__(self, name='General', model='GM', car_type='saloon'):
        self.name = name
        self.model = model
        self.car_type = car_type
        self.speed = 0
        self.num_of_doors = self.car_doors()
        self.num_of_wheels = self.car_wheels()

    def car_doors(self):
        if self.name == 'Porshe' or self.name == 'Koenigsegg':
            return 2
        else:
            return 4

    def car_wheels(self):
        if self.car_type == 'trailer':
            return 8
        else:
            return 4

    def is_saloon(self):
        if self.car_type != 'saloon':
            return 'trailer'
        return True

    def drive(self, gear_number):
        if self.car_type == 'saloon':
            self.speed = int((1000 * gear_number) / 3)
        else:
            self.speed = int(gear_number * 11)
        return self
