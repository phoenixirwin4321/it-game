import random, time, subprocess, os

class Weather:
  def __init__(self):
    self.current_cloudiness = "clear"
    self.air_temperature = 0    #20 lower than normal
    self.windiness = 0 #lowers temperature, and also can make the player get windbite or shit.
    self.precipitation = 0
    self.time = 36 #144 10 minute runs turns in a day. so 0 = 0:00   12:00 midday would be 72. 8:00am = 48. game starts at 6:00am so 36.
    self.cloudiness_modifiers = {
      "clear":0, #different cloudiness have different rain chance
      "cloudy":-3,
      "extremely cloudy":-10,
      "slightly cloudy":10,
    }
    self.time_rounded_temporary = round(self.time/14.4)
    self.time_temperature_modifiers = {1:-5,2:-2,3:1,4:3,5:5,6:4,7:2,8:0,9:-2,10:-3,}
  def write_description():
    pass

class Player:
  def __init__(self):
    self.location = "Southern grasslands" 
    self.inventory = []
    self.clothing = [("T-shirt", 10, 0, 1), ("shorts", 5, 0, 1), ("briefs", 4, 0, 0)] #name, health, armour (reduces damage), insulation (temperature). Clothing can be taken off and used for cloth, etc.
    #=======
    self.stamina = 100
    self.hunger = 100
    self.wakefulness = 100 #starts to cause dexterity penalty when low.
    self.thirst = 100
    self.temperature = 50

    self.dirt = 0 #some actions increase, washing decreases
    self.immunity = 100

    self.pain = 0
    self.dexterity_penalty = 0
    
    self.status_effects = [] #various symptoms and illnesses and effects like wet, cold, shivering, zombie infection, food poisoning. As tuples with different meanings of the other sections of the tuple for each effect.
    self.limbs = dict(head = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0}, 
                      thorax = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},
                      abdomen = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},
                      pelvis = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},
                      left_leg = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},
                      right_leg = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},
                      right_arm = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},
                      left_arm = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},)   #health, skin integrity, bleeding, germs, pain (acts like minimum pain)
                      
    
  def update_stats(self, time):
    for i in range(time):
      pass

  def write_conditions(self):
    pass
  def write_info(self):
    pass
    
class Location:
  """this is the thing that will track each location's items, landmarks, name, animal and plant species, zombie population temperature, description, map position etc"""
  def __init__(self, name):
    self.name = name
    self.items = [] #items dropped on the floor ; like sticks, rocks, tools list of objects? (track possible interactions and also damage done, rotten? etc)
    self.landmarks = [] #things like campfires, tents, trees, bushes, boulders, furniture etc list of objects?? (class will track possible interactions)
    self.beasts = [] #these are all of the animals and beasts. List of objects
    match self.name:
      case "Southern grasslands":
        self.flora = [("grass tuft", 3), ("shrub",2), ("berry bush",1)]   #name and population. 1-3, 3 is common, 2 is kinda rare, 1 is very rare
        self.fauna = [("rabbit", 3), ("partridge", 2)]
        self.items_to_forage = [("twig",3), ("rock", 2), ("dry leaves",2), ("stick",1)] #this is things that can be found like rocks, sticks, etc.
        self.ground = ["dry leaves", "dirt", "dry grass"]
        self.landmarks = []
        self.zombie_population = 1 #very tiny
        self.weather = (5, "dry") #temperature addon, and how often it rains. either "dry" "average" or "wet"
        self.type = "outdoors"
        self.direction = dict(north="Northern grasslands")
        self.description = "You are standing in an expansive sweeping grasslands, the tufts of dry grass blow in the wind."
        self.distant_description = "a sweeping field of grass blowing in the wind"
        
  def write_description(self):
    pass
        

class Beast:
  """this will track the type of animal, and the health, blood, stamina, anger, etc.only tracks animals that are near the player"""
  def __init__(self, type):
    self.type = type
    match self.type:
      case "basic zombie":
       pass

class item:
  def __init__(self, type):
    self.type = type
    
class landmark:
  def __init__(self, type):
    self.type = type


def items_in(location):
  return list(locations[player.location].items)
def cls():
  subprocess.run('cls' if os.name == "nt" else "clear", shell=True)
def chance(percent):
  return (random.random *100 <= percent)

def turn():
  cls()
  #print player info and describe location and surroundings, landmarks and any animals, weather, environment, time of day, etc.
  #prompt the player for their action
  #parse the action. The effect on the player, inventory, structures and environment. And the amount of time it takes, and how noisy it is. Animals nearby can be startled and attack or run away.
  #resolve the action and print the result of the action like "you eat the cheese and suddenly keel over, clutching your stomach, you don't feel very well (+5 food poisoning)"
  #Check to see if an animal encounter occurs, note that some actions like searching for animals explicitly cause this.

continue_temporary = input("Welcome to Zompocalypse, the educational catholic zombie apocalypse survival game! Type \"y\" to play, anything else will quit")
if (not continue_temporary.lower() == "y") or (__name__ != "__main__"):
  quit()
#===========otherwise start the game!!!!!!!!!!!!
cls()
player = Player()
weather = Weather()
locations = {  #directions from locations can be North/West/South/East OR In/Out for different buildings.
  "Southern grasslands":Location("Southern grasslands"),
  "Northern grasslands":Location("Northern grasslands"),
  "Spooky woods":Location("Spooky woods"),
  "Eastern forest":Location("Northern forest"),
  "Western woods":Location("Southern woods"),
  "Northern bushlands":Location("Western bushlands"),
  "Lake bank":Location("Lake bank"),
  "Island":Location("Island"),
  "Town":Location("Town"),
  "Mountain edge":Location("Mountain edge"),
  "Snowy peaks":Location("Snowy peaks"),
  "Abandoned hut":Location("Abandoned hut"),
  "Witch's hut":Location("Witch's hut"),
  "Townhouse 1":Location("Townhouse 1"),
  "Townhouse 2":Location("Townhouse 2"),
  "Clinic":Location("Clinic"),
  "Supermarket":Location("Supermarket"),
  "Church":Location("Church"),
  "Cheese shop":Location("Cheese shop"),
  "Mountain cave":Location("Mountain cave"),
  "Underground bunker":Location("Underground bunker") #mechanic where looking around can reveal entrances possibly?
}
