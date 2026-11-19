class HealthPotion:
    def use(self):
        print("You regain 50 HP!")

class ManaPotion:
    def use(self):
        print("You restore 30 MP!")

class SpeedPotion:
    def use(self):
        print("Your speed increases for 10 seconds!")

def apply_item(item):
    item.use()

item = [HealthPotion(), ManaPotion(), SpeedPotion()]
for potion in item:
    apply_item(potion)

