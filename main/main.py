import random, time, pygame


class Player:
  def __init__(self):
    self.location = "SW grasslands"     #Capitals for first word and lower case for everything else
    self.inventory = []
    self.clothing = [] #name, health, armour (reduces damage), insulation (temperature)
    #=======
    self.health = 100
    self.hunger = 100
    self.thirst = 100
    self.temperature = 50

    self.pain = 0
    self.dexterity_penalty = 0
    
    self.status_effects = [] #various symptoms and illnesses and ailments
    self.wounds = [] #details the wounding you have to different
  def update_stats(time):
    #1 time point = 10 minutes.
    #set pain and dexterity penalty and temperature to a fixed value and update accordingly.
    #the first step is to check the weather and set the temperature accordingly
    #then check status effects and resolve each of their effects, like if fever[1] is in the status_effects list add 10 to temperature.
    #then degrade all of the basic status effects
    #then update the wounds, which includes healing pain etc.
    
class Location(self, name):
  """this is the thing that will track each location's items, landmarks, name, animal and plant species, zombie population temperature, description, map position etc"""
  self.name = name
  self.items = []
  self.landmarks = []
  match self.name:
    case "Empty field":
      self.fauna = [["rabbit", 3]]  #[name, population relative]
      self.flora = []
      self.zombie_population = 0
      self.weather = "temperate"
      self.description = "You are standing in a large empty field, there is nothing else in existance, only the empty field."
      self.distant_description = "A large empty field, with no trees, plants or landmarks visible"
      self.direction = {"north":"", "south":"", "east":"","west":"",}

class Beast:
  """this will track the type of animal, and the health, blood, stamina, anger, etc.only tracks animals that are near the player"""
  def __init__(self, type):
    self.type = type
    match self.type:
      case "basic zombie":
       pass

def game_setup():
  os.system('cls')
  global player = Player()
  global L_SW_grasslands = Location("SW grasslands")
  global L_SE_grasslands = Location("SE grasslands")
  
  
  
def turn():
  os.system('cls')
  #print player info and describe location and surroundings.
  #prompt the player for their action
  #parse the action. The effect on the player, inventory, structures and environment. And the amount of time it takes, and how noisy it is.
  #resolve the action
  #Check to see if an animal encounter occurs, note that some actions like searching for animals explicitly cause this
  
