import random, time
#====================
  

class Player:
  def __init__(self):
    self.coordinates = (0, 0)
    self.inventory = []
    self.armour = [["T-shirt", 15, 0, 4],["Shorts", 10, 0, 2],["Underwear", 10, 0, 0.1]]  #{name, health, armour, insulation}
    #======
    self.HP = 100 #you die
    self.maximum_HP = 100 #this is your maximum HP, your HP is dynamic but wounds can lower the maximum.
    
    self.stamina = 100  #determines akshiooooons
    self.blood_lost = 0

    self.pain = 0 #affects dexterity penalty. Has a minimum and goes down to the minimum during combat
    self.minimum_pain = 0 #this is constant pain caused by wounds
    
    self.hunger = 100
    self.thirst = 100 #affects morale and hydration
    self.temperature = 50

    self.wounds = [] #[type, damage, pain, bleeding, germs]
    self.status_effects = [] #[type, amount]   This includes all of the symptoms, and status effects like nausea, fever, wet
    self.ailments = [] #type, amount    This includes all diseases, infections, etc.

    self.dexterity_penalty = 0 #makes actions take longer, less effective during combat, etc

def simulate(self, time_ticks):
  #1 time tick is equal to 10 minutes  720 time ticks in a day

  self.hunger -= 0.1
  self.thirst -= 0.1
  self.stamina += random.randint(5,10)
  self.HP += 0.5
  
  if self.pain > self.pain_minimum:
    self.pain -= 2

  if self.HP < 1:
    self.die()
  
  if self.hunger < 10:
    self.HP -= 1
  if self.thirst < 10:
    self.HP -= 1
  if self.temperature > 70:
    self.HP -= 1
  if self.temperature < 30:
    self.HP -= 1

  if self.temperature > 60:
    self.thirst -= 0.2
  if self.temperature < 40:
    self.hunger -= 0.1

  for status in status_effects:
    status_type = status[0]
    
    match status_type:
      case "poison":
        if status[1] >= 1:
          self.HP -= 1
          status[1] -= 1
        else:
          status_effects.remove("poison")
      case "x":
        if status[1]>=1:
          #affect shit
          status[1] -=1
        else:
          status_effects.remove("x")
      case "fever"
        #affect shit. Whether the status effect is valid is based on the check to see if anything is causing it.
      
        
        
  
def variable_cap(self):
  self.HP = min(max(self.HP, 0), 100)
  self.stamina = min(max(self.stamina, 0),100)
  self.maximum_HP = min(max(self.maximum_HP, 0), 100)
  self.Blood_lost = min(max(self.blood_lost, 0), 100)
  self.temperature = min(max(self.temperature, 0),100)
  self.thirst = min(max(self.thirst , 0),100)
  self.hunger = min(max(self.hunger, 0),100)
  
def die(self):
  pass
