class Smartphone:
    def __init__(self, brand, model, storage, battery_life=100):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.battery_life = battery_life
        self.app = []

    def charge(self, amount):
        self.battery_life = min(100, self.battery_life + amount)
        return f"{self.model} charged {self.battery_life}%"
    def take_picture(self):
        return f"{self.model} takes quality pictures!"
    def install_app(self, app_name):
        self.app.append(app_name)
        return f"{app_name} installed on {self.model}. Current apps: {','.join(self.app)}"
    def _str_(self):
        return f"{self.brand} {self.model} | Storage: {self.storage}GB | Battery: {self.battery_life}%"
class GamingSmartphone(Smartphone):
    def __init__(self, brand, model, storage, cooling_system, battery_life=100):
        super().__init__(brand, model, storage, battery_life)
        self.cooling_system = cooling_system
    def launch_game(self, game_name):
        if(self.battery_life < 10):
            return f"Battery too low to play! {game_name}"
        self.battery_life -= 10
        return f"Launching {game_name} on {self.model}... Battery now at {self.battery_life}%"
    # Polymorphism: override take_picture
    def take_picture(self):
        return f"{self.model} takes a gaming picture with RGB filters!"

phone1 = Smartphone("Sumsang", "S4", 128)
phone2 = GamingSmartphone("ASUS", "IPhone 6", 256, "Liquid Cooling")

# print(phone1)
# print(phone1.install_app("Instagram"))
# print(phone1.take_picture())
# print(phone1.charge(15))

print("\n" + str(phone2))
print(phone2.install_app("PUBG Mobile"))
print(phone2.launch_game("PUBG Mobile"))
print(phone2.take_picture())