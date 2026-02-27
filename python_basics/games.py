#MWANGI ERICK
#23.02.2026
#program to show a game

class FighterCharacter:

    def __init__(self, role, health, damage, speed):
        self.character_role = role
        self.character_health = health
        self.character_damage = damage
        self.character_speed = speed

    def run(self, direction):
        print(f"Game log: {self.character_role} runs {direction} at speed {self.character_speed}")

    def report_status(self):
        print(f"\nCharacter Log:")
        print(f" Role: {self.character_role}")
        print(f" Health: {self.character_health}")
        print(f" Damage: {self.character_damage}")
        print(f" Speed: {self.character_speed}")
        print(" __ \n")

    def kick(self, opponent):
        damage = self.character_damage
        opponent.character_health -= damage
        print(f"Game Log: {self.character_role} deals {damage} damage to the {opponent.character_role}.")

    def tackle(self, opponent):
        damage = self.character_damage
        opponent.character_speed -= damage
        if opponent.character_speed < 0:
            opponent.character_speed = 0
        print(f"Game Log: {self.character_role} tackles {opponent.character_role}, reducing their speed by {damage}.")


# Create characters
ninja_character = FighterCharacter("Ninja", health=100, damage=40, speed=120)
warrior_character = FighterCharacter("Warrior", health=160, damage=80, speed=80)

# Test
ninja_character.report_status()
warrior_character.report_status()

ninja_character.run("Up")
ninja_character.kick(warrior_character)

ninja_character.report_status()
warrior_character.report_status()

warrior_character.tackle(ninja_character)
ninja_character.report_status()
