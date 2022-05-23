
#is a class for characters
class Character:
    #class variables
    name = ""
    race = ""
    class_archtype = ""
    level = 0
    #class method for introducing characeters
    def introduction(self):
        intro = "My name is %s, I am a %s %s at level %s." % (self.name, self.race, self.class_archtype, self.level)
        return intro

#new character
player1 = Character()
player2 = Character()

#defining each new player
player1.name = "Jace"
player1.race = "Human"
player1.class_archtype = "Tank"
player1.level = 5

player2.name = "Grok"
player2.race = "Ork"
player2.class_archtype = "DPS"
player2.level = 3

#printing induction method from class
print(player1.introduction())
print(player2.introduction())