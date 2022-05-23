class Character:
    name = ""
    race = ""
    class_archtype = ""
    level = 0

    def introduction(self):
        intro = "My name is %s, I am a %s %s at level %s." % (self.name, self.race, self.class_archtype, self.level)
        return intro


player1 = Character()
player2 = Character()

player1.name = "Jace"
player1.race = "Human"
player1.class_archtype = "Tank"
player1.level = 5

player2.name = "Grok"
player2.race = "Ork"
player2.class_archtype = "DPS"
player2.level = 3

print(player1.introduction())
print(player2.introduction())