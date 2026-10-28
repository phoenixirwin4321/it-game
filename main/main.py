import random, time, pygame


class Player:
  def __init__(self):
    self.location = "Southern grasslands"     #Capitals for first word and lower case for everything else
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
      self.type = "outdoors" #affects animal encounters, and also actions. Like outdoors you would say "forage" but indoors you would say "search room" or something.
      self.description = "You are standing in a large empty field, there is nothing else in existance, only the empty field with a small house in the middle."
      self.distant_description = "A large empty field, with no trees, plants or landmarks visible, except a small house"
      self.direction = {"north":"", "south":"", "east":"","west":"", "into house":"Small house 1"}
    case "Small house 1":
      self.fauna = []
      self.flora = []
      self.zombie_population = []
      self.weather = "temperate"
      self.type = "indoors"
      self.description = "You are standing in a small empty house"
      self.distant_description = "A small empty house standing in the field"
      self.direction = {"out":"Empty field"}

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
  global locations = {  #directions from locations can be North/West/South/East OR In/Out for different buildings.
    "Southern grasslands":Location("Southern grasslands"),
    "S":Location(),
    "":Location(),
    "":Location(),
    "":Location(),
    "":Location(),
  }
  
  
  
def turn():
  os.system('cls')
  #print player info and describe location and surroundings.
  #prompt the player for their action
  #parse the action. The effect on the player, inventory, structures and environment. And the amount of time it takes, and how noisy it is.
  #resolve the action
  #Check to see if an animal encounter occurs, note that some actions like searching for animals explicitly cause this
  
