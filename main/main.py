import random, time, pygame


class player:
  def __init__(self):
    self.location = "SW Grasslands"
    self.inventory = []
    self.clothing = [] #name, health, armour (reduces damage), insulation (temperature)
    #=======
    self.health = 100
    self.hunger = 100
    self.thirst = 100
    self.temperature = 50
    
    self.status_effects = [] #various symptoms and illnesses and ailments
    self.wounds = [] #details the wounding you have to different

class location:
  """this is the thing that will track each location's items, landmarks, name, animal and plant species, zombie population temperature, description, map position etc"""
  pass

class beast:
  """this will track the type of animal, and the health, blood, stamina, anger, etc.only tracks animals that are near the player"""
  def __init__(self, type):
    self.type = type


def turn():
  os.system('cls')
  #print player info and describe location and surroundings.
  #prompt the player for their action
  #parse the action. The effect on the player, inventory, structures and environment. And the amount of time it takes, and how noisy it is.
  #resolve the action
  #Check to see if an animal encounter occurs, note that some actions like searching for animals explicitly cause this
  
