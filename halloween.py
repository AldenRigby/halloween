class Monster():
    def __init__(self, name, origin, fight=""):
        self.name = name
        self.origin = origin
        self.fight = fight

    def __str__(self):
        return f"{self.name} from {self.origin}"
    
    @staticmethod
    def attack(first, second):
        if len(first.fight) > len(second.fight):
            return first
        elif len(first.fight) < len(second.fight):
            return second
        else:
            return first
        
class Skeleton(Monster):
    def __init__(self, name, origin, fight):
        super().__init__(name, origin, fight)
    
    def __str__(self):
        return super().__str__()
        
class Ghost(Monster):
    def __init__(self, name, origin, fight):
        super().__init__(name, origin, fight)
    
    def __str__(self):
        return super().__str__()
        
class Spirit(Monster):
    def __init__(self, name, origin, fight):
        super().__init__(name, origin, fight)
    
    def __str__(self):
        return super().__str__()
        
class Zombie(Monster):
    def __init__(self, name, origin, fight):
        super().__init__(name, origin, fight)
    
    def __str__(self):
        return super().__str__()
    
spooky = Spirit("Jim", "Michigan", "grenade.")
scary = Zombie("Demon Slayer IV", "Colorado", "Holy scimitar, passed down through generations")
skeleton = Skeleton("Clare", "the gates of hell", "a rock")
    
print(Monster.attack(spooky, scary))
print(Monster.attack(scary, skeleton))
print(Monster.attack(spooky, skeleton))