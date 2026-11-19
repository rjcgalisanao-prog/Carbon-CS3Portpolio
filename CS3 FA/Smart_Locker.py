class SmartLocker:

    def __init__(self, locker_number, owner, status):
        self.locker_number = locker_number;
        self.miggy = owner;
        self.stats = status;

    def assign_locker(self):
        self.miggy = Owner

    def release_locker(self):
        print(f"{self.miggy} has been removed\n")
        self.stats = "Available"
        self.miggy = "None"
        

    def display_info(self):
        
        print(f"Locker ID: {self.locker_number}")
        print(f"Owner: {self.miggy}")    
        print(f"Status: {self.stats}\n")


Locker1 = SmartLocker(101, "Jamie", "Occupied")
Locker2 = SmartLocker(102, "Taylor", "Occupied" )

Locker = [Locker1, Locker2]

for x in Locker:
    print(f"Name: {x.miggy} Locker ID: {x.locker_number} Status: {x.stats}\n")

Locker1.display_info()

Locker2.display_info()

Locker1.release_locker()

Locker1.display_info()

Locker2.display_info()