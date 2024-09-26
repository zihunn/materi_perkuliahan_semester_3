import random

class Hero:
    def __init__(self, name, role, hp, ad, skill):
        self.name = name
        self.role = role
        self.hp = hp
        self.ad = ad
        self.skill = skill
    
    # Function Basic Attack
    def attack(self, enemy_hero):
        if random.random() < 0.1:
            print(f"{self.name} attack missed!")
        else:
            damage = self.ad
            # Pengecekan apakah ada kemungkinan serangan kritis (20%)
            if random.random() < 0.2:
                damage *= 2
                print(f"Critical Hit! {self.name} hits {enemy_hero.name} for double damage!")
            else:
                print(f"{self.name} menyerang {enemy_hero.name}!")
            
            enemy_hero.hp -= damage
            print(f"{enemy_hero.name} kehilangan {damage} HP, sisa HP: {enemy_hero.hp}")
    
    # Function Attack dengan Skill
    def use_skill(self, enemy_hero):
        # Pengecekan apakah ada kemungkinan miss skill (10%)
        if random.random() < 0.1:
            print(f"{self.name} skill {self.skill} missed!")
        else:
            skill_damage = self.ad * 1.5
            print(f"{self.name} menggunakan skill {self.skill} terhadap {enemy_hero.name}!")
            enemy_hero.hp -= skill_damage
            print(f"{enemy_hero.name} kehilangan {skill_damage} HP dari skill {self.skill}, sisa HP: {enemy_hero.hp}")
    
    # Function Show Statistik Hero
    def show_data(self):
        print(f"\nHero: {self.name}\nRole: {self.role}\nHP: {self.hp}\nAttack Damage: {self.ad}\nSkill: {self.skill}\n")
    
    # Function Hero Kalah
    def defeated(self):
        return self.hp <= 0

#  Function Battle
def battle(hero1, hero2):
    turn = 1
    while not hero1.defeated() and not hero2.defeated():
        print(f"\n--- Turn {turn} ---")
        print(f"{hero1.name} HP: {hero1.hp} | {hero2.name} HP: {hero2.hp}")
        print(f"{hero1.name} turn:")
        action = input(f"Apa yang ingin dilakukan {hero1.name}? (1: Attack, 2: Use Skill): ")
        
        if action == '1':
            hero1.attack(hero2)
        elif action == '2':
            hero1.use_skill(hero2)
        else:
            print("Pilihan tidak valid, serangan dilewatkan!")

        if hero2.defeated():
            print(f"\n{hero2.name} dikalahkan oleh {hero1.name}!")
            break
        
        print(f"\n{hero2.name} turn:")
        action = input(f"Apa yang ingin dilakukan {hero2.name}? (1: Attack, 2: Use Skill): ")
        
        if action == '1':
            hero2.attack(hero1)
        elif action == '2':
            hero2.use_skill(hero1)
        else:
            print("Pilihan tidak valid, serangan dilewatkan!")

        if hero1.defeated():
            print(f"\n{hero1.name} dikalahkan oleh {hero2.name}!")
            break
        
        turn += 1

layla = Hero(name="Layla", role="Marksman", hp=300, ad=80, skill="Destruction Rush")
tigreal = Hero(name="Tigreal", role="Tank", hp=500, ad=50, skill="Implosion")


layla.show_data()
tigreal.show_data()

battle(layla, tigreal)
