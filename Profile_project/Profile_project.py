import random as r

#I'm lazy and don't want to type r.randinit every time I want to roll a number
def roll(num1, num2):
    roll = r.randint(num1, num2)
    return roll
debugging = False

class Human:
  def __init__(self, name, weapon, player=False):
    self.name = name
    #Randomize stats to make each fight truly unique. You might be a buff god made of iron, or a weak worm made of paper. Same goes for the NPC
    self.strength = roll(1, 10)
    self.defense = roll(1, 10)
    self.health = 100
    self.weapon = weapon
    self.player = player
    self.conscious = True
    self.is_defending = False
  def __repr__(self):
      return "A Human"
  
  #This took an absurd amount of my time, both in the original script and in this one
  def attack(self, target=None):
        if self.conscious and target.conscious:
            attack_roll = roll(1, 20) + self.weapon.attack
            defense_roll = roll(1, 20)
            if debugging:
                print("DEBUG: Attack was {attack} Defense was {defense}".format(attack = attack_roll, defense = defense_roll))
            if defense_roll + target.defense >= attack_roll + self.strength:
                print("{attacker}'s attack missed!".format(attacker=self.name))
            elif target.is_defending:
                block_chance = roll(1, 100) + target.defense
                if block_chance >= 90:
                    print("{defender} blocked the attack!".format(defender=target.name))
                else:
                    damage_roll = roll(1, 10) + self.weapon.damage - target.defense
                    if damage_roll < 0:
                        damage_roll = 0
                    print(
                        "{defender} partially deflected {attacker}'s attack! {defender} only takes {damage_roll} damage!".format(
                            defender=target.name, attacker=self.name, damage_roll=damage_roll
                        )
                    )
                    target.health -= damage_roll
                target.is_defending = False
            else:
                damage_roll = roll(1, 10) + self.weapon.damage
                #Go ahead and create a roll for the knockout check
                knockout_roll = roll(1, 100)
                #Check if you or the NPC has a mace, if so, here's the chance to crush their skull
                if self.weapon.make == "Mace" and knockout_roll >= 95:
                    target.conscious = False
                    print(
                        "{attacker}'s Mace lands on {defender}'s head with a loud crunch! {defender} has been knocked out!".format(
                            attacker=self.name, defender=target.name
                        )
                    )
                else:
                    target.health -= damage_roll
                    print(
                        "{attacker}'s weapon lands a blow! {defender} takes {damage} damage!".format(
                            attacker=self.name, defender=target.name, damage=damage_roll
                        )
                    )
        elif not target.conscious:
            print("{target} is already unconscious!".format(target=target.name))

  def defend(self):
    if self.conscious and self.is_defending == False:
      self.is_defending = True
      print("{defender} prepares for an attack...".format(defender = self.name))
    
    elif self.conscious and self.is_defending:
      print("{defender} can't be any more prepared for an attack!".format(defender = self.name))

class Weapon:
    def __init__(self, make):
        self.make = make
        #kinda proud of this. I didn't do it alone, it was built on a suggestion by ChatGPT, but the values and use are mine
        self.stats = {
            "Longsword": {"damage": 5, "attack": 10},
            "Mace": {"damage": 3, "attack": 3},
            "Dagger": {"damage": 2, "attack": 15},
            "Greatsword": {"damage": 15, "attack": 5}
        }

        if self.make in self.stats:
            self.damage = self.stats[self.make]["damage"]
            self.attack = self.stats[self.make]["attack"]
        else:
            self.damage = 0
            self.attack = 0

    def __repr__(self):
        return self.make

longsword = Weapon("Longsword")
mace = Weapon("Mace")
dagger = Weapon("Dagger")
greatsword = Weapon("Greatsword")
weapon_rack = [longsword, mace, dagger, greatsword]

#Nailed this one on the first try. I think I'm most proud of this function, out of this entire script, small, but it was a victory for me
def assign_name():
    first_names = ["Nicostratus", "Sostratus", "Patricius", "Leonius", "Beringarius", "Nerva", "Saul", "Demetrius", "Viggo", "Philandrus", "Philocrates", "Ladislaus", "Amatus", "Fidelis"]
    last_names = ["Procillus", "Cossus", "Clineas", "Blasio", "Laevinus", "Regillensis", "Pictor", "Libo", "Spinther", "Rutilus", "Mocilla", "Sacerdos", "Sisenna", "Crus", "Potitus"]
    name = first_names[roll(0, len(first_names) - 1)] + " " + last_names[roll(0, len(last_names) - 1)]
    return name

npc = Human(assign_name(), weapon = weapon_rack[roll(0, len(weapon_rack) - 1)])

#No matter how much I stripped it down, I couldn't help but put in a little bit of fanfare
print("""

You enter the arena to the roar of the crowd. A man in the emperor's box with a booming voice shouts, "Welcome, one and all, back to The Arena!"

The crowd roars again. After the din dies down, the announcer continues. "Today, we see battle between two fierce competitors! First, we have {npc} using a {weapon1}!"

Once more the arena erupts in cheers, some even chanting {npc}'s name.

"And second, we have...
""".format(npc = npc.name, weapon1 = npc.weapon))

player_name = input("Enter your name: ")

print("""

{player} using a...

""".format(player = player_name))

weapon = ""
while weapon == "":
    weapon_choice = input("Select a weapon from the following: DAGGER, GREATSWORD, LONGSWORD, MACE ")
    clean_weapon = weapon_choice.lower()
    if clean_weapon == "dagger":
        weapon = dagger
    elif clean_weapon == "greatsword" or clean_weapon == "great sword":
        weapon = greatsword
    elif clean_weapon == "longsword" or clean_weapon == "long sword":
        weapon = longsword
    elif clean_weapon == "mace":
        weapon = mace
    else:
        print("{choice} is not a valid choice".format(choice = weapon_choice))

print("""

{player_weapon}!" the crowd erupts into cheers again. Some chanting your name this time.

"Without further ado ladies and gentlemen, let the battle BEGIN!" he shouts, the crowd erupts in roars and your opponent rushes you!

""".format(player_weapon = weapon))
player = Human(player_name, weapon, True)

#Flags to make sure neither the user nor the NPC gets unlimited turns
player_turn = True
npc_turn = False

#Main game loop. If you or the NPC gets knocked out, game over
while player.conscious and npc.conscious:
    while player_turn == True and npc_turn == False:
        player_action = input("What do you want to do? ATTACK, DEFEND, or CHECK HEALTH? ").lower()
        if player_action == "attack":
            player.attack(npc)
            player_turn = False
            npc_turn = True
        elif player_action == "defend":
            player.defend()
            player_turn = False
            npc_turn = True
        elif player_action == "check health":
            print("You have {health} health left.".format(health = player.health))
            if debugging == True:
                print("DEBUG: Enemy Health is {health}".format(health = npc.health))
        elif player_action == "debug":
            print("Debugging enabled")
            debugging = True
        elif debugging == True and player_action == "stats":
            print("DEBUG: Player: Str: {strength} Def: {defense} \n DEBUG: NPC: Str: {npcstr} Def: {npcdef}".format(strength = player.strength, defense = player.defense, npcstr = npc.strength, npcdef = npc.defense))
        else:
            print("You can't do that!")
        #Admittedly this was annoying difficult. Hours upon hours figuring out why the loop wouldn't break appropriately or return the
        #right output. All because I declared this and the NPC unconscious condition at the top of the game loop
        if npc.health <= 0:

            print("You have won! Congratulations! The crowd roars and chants your name over and over.")
            npc.conscious = False

    #NPC Logic. Not smart enough to be called AI. Ensures you get a unique fight every game load.
    while npc_turn == True and player_turn == False:
        action_choice = roll(1,100)
        if debugging == True:
            print("DEBUG: Action Choice roll was {roll}".format(roll = action_choice))
        if action_choice >= 80:
            npc.defend()
            npc_turn = False
            player_turn = True
        else:
            npc.attack(player)
            npc_turn = False
            player_turn = True
        if player.health <= 0:
            print("You have been defeated. Game Over...")
            player.conscious = False




