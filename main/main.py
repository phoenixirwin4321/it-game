import random, time, subprocess, os
#remember 1440 minutes per day so 144 turns per day. Also here is the Unicode dot point symbol: •

#------------------------------------------------
def cls():
  subprocess.run('cls' if os.name == "nt" else "clear", shell=True)
  
def chance(percent):
  return (random.random *100 <= percent)

def dice(x):
  return random.randint(1, x+1)

def between(x, minimum, maximum):
  return minimum <= x <= maximum
  
def cap(x, minimum, maximum):
  return min(max(x, minimum), maximum)

def debug_print(x):
  print(f"debug message //  {x}")
#------------------------------------------------

class Weather:
  def __init__(self):
    self.current_cloudiness = "clear"
    self.air_temperature = 0    #20 lower than celsius
    self.wind = 0 #lowers temperature, and also can make the player get windburn or something like that. 0/20 scale maybeeeeee
    self.precipitation = 0
    self.time = 36 #144 10 minute runs turns in a day. so 0 = 0:00   12:00 midday would be 72. 8:00am = 48. game starts at 6:00am so 36.
    self.cloudiness_modifiers = {
      "clear":5, #different cloudiness have different rain chance
      "cloudy":-5,
      "very cloudy":-9,
      "slightly cloudy":-2,
      "very sunny":9
    }
    self.time_rounded_temporary = round(self.time/14.4)
    self.time_temperature_modifiers = {1:-5,2:-2,3:1,4:3,5:5,6:4,7:2,8:0,9:-2,10:-3,}
  def update(self):
    #change all of the data, based on the location, time of day and random chance.
    self.current_cloudiness = random.choice(list(self.cloudiness_modifiers.keys()))
    self.air_temperature = dice(4)-2
    self.wind = dice(10) *locations[player.location].weather[1]
    self.precipitation = round(min(dice(100), dice(100)) *locations[player.location].weather[2])
    
  def calculate_air_temp(self):
    t_x = self.air_temperature
    t_x += self.cloudiness_modifiers[self.current_cloudiness] #weather modifier
    t_x -= self.wind//2
    t_x += locations[player.location].weather[0]
    return t_x
    
  def is_day(self):
    return 36 <= self.time <= 120
    
  def write_description(self):
    description = []
    description.append(f"Rain: {self.precipitation} >50 is raining")
    description.append(f"Temperature: {self.calculate_air_temp()+20}")
    description.append(f"wind: {self.wind}")
    description.append(f"weather: {self.current_cloudiness}")
    description.append(f"time: {self.time//6}")

    for item in description:
      print(f"• {item}")
    print()

class Player:
  def __init__(self):
    self.location = "Southern grasslands" 
    self.inventory = []
    self.clothing = [("T-shirt", 10, 0, 1, ("thorax", "abdomen")),
                     ("shorts", 5, 0, 1, ("pelvis")),
                     ("briefs", 4, 0, 0, ("pelvis"))]       #name, health, armour (reduces damage), insulation, body parts (that armour protects)
    #=======
    self.stamina = 100
    
    self.hunger = 100
    self.wakefulness = 100
    self.thirst = 100
    self.temperature = 50
    self.target_temperature = 50
    
    self.mood = 50 #affects general penalty and also immunity. Can cause status effects like ecstatic, depressed, etc. Also is dynamic but normaliser scales.

    self.dirt = 0 #some actions increase, washing decreases
    self.immunity = 100

    self.pain = 0
    self.dexterity_penalty = 0
    self.general_penalty = 0
    self.movement_penalty = 0
    
    self.status_effects = [] #various symptoms and illnesses and effects like wet, cold, shivering, zombie infection, food poisoning. As tuples with different meanings of the other sections of the tuple for each effect.
    self.limbs = dict(head = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0}, 
                      thorax = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},
                      abdomen = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},
                      pelvis = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},
                      left_leg = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},
                      right_leg = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},
                      right_arm = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},
                      left_arm = {"health":100, "skin":100, "bleeding":0, "germs":0, "pain":0},)   #health, skin integrity, bleeding, germs, pain (acts like minimum pain)
                      
    self.insulation = 2
    
  def update_stats(self, time):
    for i in range(time):
      self.determine_active_status_effects()
      self.set_static_stats()
      self.resolve_status_effects()
      self.resolve_wound_effects() #like germs, bleeding, damage to limbs
      self.change_dynamic_stats()
      self.cap_values()
      self.remove_destroyed_clothing()

  def set_static_stats(self):
    #temperature
    self.insulation = self.calculate_insulation()
    self.target_temperature = 50 + (self.insulation + weather.calculate_air_temp())
    #----------------------
    #then we have pain
    self.pain -= 1
    t_x = self.calculate_minimum_pain()
    if self.pain < t_x:
      self.pain = t_x
    #-----------------------

  def calculate_insulation(self):
    temporary = 0
    for item in self.clothing:
      temporary += item[3]
    return temporary
  def calculate_minimum_pain(self):
    x = 0
    for limb in self.limbs.keys():
      x += self.limbs[limb]["pain"]
    return x

  def determine_active_status_effects(self):
    pass
  def resolve_status_effects(self):
    pass
  def cap_values(self):
    pass
  def change_dynamic_stats(self):
    pass
  def resolve_wound_effects(self):
    pass
  def remove_destroyed_clothing(self):
    pass
  
  def write_conditions(self):
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
        self.flora = {3:("grass tuft"), 2:("shrub"), 1:("kaju root"), 0:()}   #name and population. 1-3, 3 is common, 2 is kinda rare, 1 is very rare and 0 might be 1 in 4000 games you might see it you know
        self.fauna = {3:("rabbit"), 2:("seagull"), 1:("grass snake"), 0:()}
        self.items_to_forage = {3:("twig", "stone"), 2:("stick", "dry leaves"), 1:("leaves"), 0:()} #this is things that can be found like rocks, sticks, etc.
        self.ground = ("dirt", "dry grass")
        self.zombie_population = 1 #!!!!!MEANS THAT THERE IS A 1% OF ENCOUNTERING A ZOMBIE EVERY 144 TURNS SO IN OTHER WORDS 0.01/144 CHANCE PER TURN!!!!!
        self.weather = (5, 1.5, 0.8)    #temperature add / wind multiplier / precipitation multiplier
        self.type = "outdoors"
        self.direction = dict(north=("Northern grasslands", 2))  #The second element is the amount of turns it takes to travel in that direction
        self.description = "You are standing in a sweeping grassy plain which extends all around you."
        self.distant_description = "a sweeping field"

      case "Northern grasslands":
        self.flora = {3:("grass tuft", "shrub"), 2:(), 1:("small tree", "berry bush"), 0:()}
        self.fauna = {3:("rabbit"),2:("grass snake"),1:(), 0:()}
        self.items_to_forage = {3:("twig", "stone"),2:("stick", "dry leaves"),1:("leaves", "wood", "large rock"), 0:()}
        self.ground = ("dirt", "dry grass")
        self.zombie_population = 3
        self.weather = (3, 1.2, 0.9)
        self.type = "outdoors"
        self.direction = dict(north=("Town", 3), northwest=("Western woods", 2), northeast=("Eastern forest", 2),south=("Southern grasslands", 2))
        self.description = "You are standing in a grassy meadow area"
        self.distant_description = "a grassy meadow"

      case "Western woods":
        self.flora = {3:("small tree", "small tree", "bush", "tree", "shrub"), 2:("grass tuft", "berry bush", "mushroom patch", "snakegrass"), 1:("apple tree"), 0:()}
        self.fauna = {
          3:("rabbit", "bird"),
          2:("deer", "wolf", "boar"),
          1:("bear"),
          0:(),
        }
        self.items_to_forage = {
          3:("twig", "twig", "stone", "stick", "dry leaves", "leaves"),
          2:("wood", "large rock"),
          1:(),
          0:(),
        }
        self.ground = ("dirt", "leaves", "dry leaves")
        self.zombie_population = 7
        self.weather = (2, 0.9, 1)
        self.type = "outdoors"
        self.direction = dict(
          north=(),
          south=(("Northern grasslands", 2)),
          west=(("Town", 2)),
        )
        self.description = "You are standing in a quiet woods, birds are chirping in the trees."
        self.distant_description = "a temperate buzzing forest"
      case "Eastern forest":
        pass
      case "Town":
        pass
        
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

def turn():
  cls()
  #print player info and describe location and surroundings, landmarks and any animals, weather, environment, time of day, etc.
  #prompt the player for their action
  #parse the action. The effect on the player, inventory, structures and environment. And the amount of time it takes, and how noisy it is. Animals nearby can be startled and attack or run away.
  #resolve the action and print the result of the action like "you eat the cheese and suddenly keel over, clutching your stomach, you don't feel very well (+5 food poisoning)"
  #Check to see if an animal encounter occurs, note that some actions like searching for animals explicitly cause this.

continue_temporary = input("Welcome to Zompocalypse, the educational catholic zombie apocalypse survival game! Type \"y\" to play, anything else will quit: ")
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
  "Underground bunker":Location("Underground bunker"), #mechanic where looking around can reveal entrances possibly?
  "Ocean":Location("Ocean")
}

