class Avenger:
    def __init__(self, name, age, gender, super_power, weapon, leader=False):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon
        self.leader = leader

    def get_info(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Gender:", self.gender)
        print("Super Power:", self.super_power)
        print("Weapon:", self.weapon)

    def is_leader(self):
        if self.leader:
            print(self.name, "is the leader of the Avengers")
        else:
            print(self.name, "is not the leader of the Avengers")


super_heroes = [
    Avenger("Captain America", 101, "Male", "Super Strength", "Shield", leader=True),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 49, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 38, "Male", "Fighting Skills", "Bow and Arrows")
]

for hero in super_heroes:
    hero.get_info()
    hero.is_leader()
    print()
