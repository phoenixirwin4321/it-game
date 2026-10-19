import random, time
#====================


class Player:
  def __init__(self):
    self.coordinates = (0, 0)
    self.inventory = []
    self.armour = [{"T-shirt", 15, 0, 4},{"Shorts", 10, 0, 2},{"Underwear", 10, 0, 0.1}]  #{name, health, armour, insulation}
    #======
    self.HP = 100 #you die
    self.stamina = 100  #determines actions
    self.Blood_lost = 100

    self.morale = 50 #affects your appetite and immune system
    self.pain = 0 #affects morale
    
    self.hunger = 100
    self.appetite = 50 #affects how fast your hunger goes down
    self.weight = 50

    self.stomach = 0 #transfers into intestines
    self.intestines = 0 #transfers into weight
    
    self.thirst = 100 #affects morale and hydration
    self.hydration = 100 #gives you headaches, damage

    self.temperature = 50 #affected by the weather and infections

    self.wounds = [] #{type, damage, pain, bleeding, germs}
    
    self.status_effects = [] #{type, amount}   This includes all of the symptoms, and afflictions like heatstroke etc
    self.ailments = [] #type, amount    This includes all diseases, infections, etc.

    self.dexterity_penalty = 0 #makes actions take longer, less effective during combat, etc

def simulate(time_ticks):
  pass #1 time tick is equal to 10 minutes  720 time ticks in a day
