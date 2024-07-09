import random

# Soldier


class Soldier:
    def __init__(self, health, strength):
        self.health = health
        self.strength = strength
    
    def attack(self):
        return self.strength

    def receiveDamage(self, damage):
        self.health -= damage
        
        
    

# Viking

class Viking(Soldier):
    def __init__(self, name, health, strength):   
        super().__init__(health, strength)        #invoca la clase Soldier , y lo inicializa con health y strenght
        self.name = name 

    def battleCry(self):
        return "Odin Owns You All!"
        

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"{self.name} has received {damage} points of damage"  #los test contienen string en ingles, se cambia para pasar tests
        else:
            return f"{self.name} has died in act of combat"

# Saxon

class Saxon(Soldier):
    
    def __init__(self, health, strength):
        super().__init__(health, strength)

    def receiveDamage(self, damage):
        self.health -= damage
        if self.health > 0:
            return f"A Saxon has received {damage} points of damage"
        else:
            return "A Saxon has died in combat"

# Davicente

class War():
    def __init__(self):
        self.vikingArmy = []
        self.saxonArmy = []

    def addViking(self, viking):
        self.vikingArmy.append(viking)
    
    def addSaxon(self, saxon):
        self.saxonArmy.append(saxon)
    
    def vikingAttack(self):
        import random
        random_saxon = random.choice(self.saxonArmy)  #el metodo random.choice de la biblioteca random, elige un elemento al azar de cualquier lista o secuencia
        random_viking = random.choice(self.vikingArmy)
        result = random_saxon.receiveDamage(random_viking.strength)
        if random_saxon.health <= 0:
            self.saxonArmy.remove(random_saxon)
        return result
    
    def saxonAttack(self):
        import random
        random_viking = random.choice(self.vikingArmy)
        random_saxon = random.choice(self.saxonArmy)
        result = random_viking.receiveDamage(random_saxon.strength)
        if random_viking.health <= 0:
            self.vikingArmy.remove(random_viking)
        return result

    def showStatus(self):
        if len(self.saxonArmy) == 0:
            return "Vikings have won the war of the century!"
        elif len(self.vikingArmy) == 0:
            return "Saxons have fought for their lives and survive another day..."
        else:
            return "Vikings and Saxons are still in the thick of battle."
    

# #yop
# class War2:

#     def __init__(self):
#         # your code here

#     def addViking(self, Viking):
#         # your code here
    
#     def addSaxon(self, Saxon):
#         # your code here
    
#     def vikingAttack(self):
#         # your code here

#     def saxonAttack(self):
#         # your code here

#     def showStatus(self):
#         # your code here

#     pass


