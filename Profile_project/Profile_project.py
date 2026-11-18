from utils import roll_int
from debugging import Debugger

Debugger.debugging = True

weapon_rack = [Longsword, Mace, Dagger, Greatsword]

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
        if npc.health <= 0:

            print("You have won! Congratulations! The crowd roars and chants your name over and over.")
            npc.conscious = False

    while npc_turn == True and player_turn == False:
        action_choice = roll_int(1,100)
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
