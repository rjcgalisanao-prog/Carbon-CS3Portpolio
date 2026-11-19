class PhysicsInstrument:
    def __init__(self, name, measurement):
        self.name = name
        self.__measurement = measurement

    def get_measurement(self):
        return self.__measurement

    def display_reading(self):
        print(f"{self.name} reading: {self.get_measurement()}")

    def calculate_values(self):
        pass

    def display_info(self):
        print(f"Instrument: {self.name}, Measurement: {self.get_measurement()}")

class Thermometer(PhysicsInstrument):
    def __init__(self, name, measurement):
        super().__init__(name, measurement)

    def display_reading(self):
        print(f"{self.name} reading: {self.get_measurement()} °C")

    def calculate_values(self):
        if self.get_measurement() < 20:
            return " Cool Temperature"
        elif self.get_measurement() >= 20 and self.get_measurement() < 30:
            return "Normal Temperature"
        else:
            return "Hot Temperature"

    def display_info(self):
        print(f"Instrument: {self.name}, Measurement: {self.get_measurement()} °C, Temperature Status: {self.calculate_values()}")

class Speedometer(PhysicsInstrument):
    def __init__(self, name, measurement, time):
        super().__init__(name, measurement)
        self.time = time

    def display_reading(self):
        print(f"{self.name} reading: {self.get_measurement()} km in {self.time} hours")

    def calculate_values(self):
        if self.time <= 0:
            return "Time must be greater than zero to calculate speed."
        elif self.time > 0:
            return self.get_measurement() / self.time

    def display_info(self):
        print(f"Instrument: {self.name}, Measurement: {self.get_measurement()} km, Time: {self.time} hours, Speed: {self.calculate_values()} km/h")

class Forcemeter(PhysicsInstrument):
    def __init__(self, name, measurement, acceleration):
        super().__init__(name, measurement)
        self.acceleration = acceleration

    def display_reading(self):
        print(f"{self.name} reading: {self.get_measurement()} kg with an acceleration of {self.acceleration} m/s²")

    def calculate_values(self):
        force = self.get_measurement() * self.acceleration
        return force

    def display_info(self):
        print(f"Instrument: {self.name}, Measurement: {self.get_measurement()} kg, Acceleration: {self.acceleration} m/s², Force: {self.calculate_values()} N")

def values():
    for instrument in instruments:
        instrument.display_info()

a = int(input("Enter the temperature in Celsius: "))
b = int(input("Enter the distance in km: "))
b2 = int(input("Enter the time in hours: "))
c2 = int(input("Enter the acceleration in m/s²: "))
c = int(input("Enter the mass in kilograms: "))

temp = Thermometer("Thermometer", a)
speed = Speedometer("Speedometer", b, b2)
force = Forcemeter("Forcemeter", c, c2)

instruments = [temp, speed, force]

values()