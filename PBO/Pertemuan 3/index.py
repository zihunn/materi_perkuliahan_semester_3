class Hero:
    def __init__(self, name, role, hp, ad, skill):
        self.name = name
        self.role = role
        self.hp = hp
        self.ad = ad
        self.skill = skill
    
    def show_stats(self):
        print(f"Status {self.name}:")
        print(f"Role: {self.role}")
        print(f"HP: {self.hp}")
        print(f"AD: {self.ad}")
        print(f"Skill: {self.skill}")
        print("-" * 30)
    
    def attack(self, enemy_hero):
        print(f"{self.name} menyerang {enemy_hero.name}!")
        enemy_hero.hp -= self.ad
        print(f"{enemy_hero.name} kehilangan {self.ad} HP.")
    
    def use_skill(self, enemy_hero, skill_damage):
        print(f"{self.name} menggunakan skill: {self.skill}!")
        enemy_hero.hp -= skill_damage
        print(f"{enemy_hero.name} kehilangan {skill_damage} HP.")

layla = Hero(name = "Layla", role = "Marksman", hp = 250, ad = 50, skill =  "Destruction Rush")
tigreal = Hero(name = "Tigreal", role = "Tank", hp = 450, ad = 40, skill = "Sacred Hammer")

layla.show_stats()
tigreal.show_stats()

layla.attack(tigreal)
tigreal.use_skill(layla, 100)

layla.show_stats()
tigreal.show_stats()
