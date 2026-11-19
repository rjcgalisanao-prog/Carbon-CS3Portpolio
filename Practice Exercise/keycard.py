
class Lab:
    def __init__(self, room_number, technician):
        self.room_number = room_number
        self.technician = technician

    def assign_lab(self):
        print(f"{self.technician.name} has been assigned to lab {self.room_number}.")

    def get_in_lab(self):
        print(f"Access granted to lab {self.room_number}.")


class Technician:
    def __init__(self, name):
        self.name = name

    def get_keycard(self):
        print(f"Keycard has been given to {self.name}.")


technician = Technician("Mijo De la Cruz")
lab = Lab("302", technician)

technician.get_keycard()
lab.assign_lab()
lab.get_in_lab()

