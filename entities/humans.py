from __future__ import annotations
from utils.roll import roll_dice
from debugging import debug, Debugger

class Human:
  def __init__(self, name, weapon, player=False):
    self.name = name

    self.strength = roll_dice(10)
    self.defense = roll_dice(10)
    self.health = 100
    self.weapon = weapon
    self.player = player
    self.conscious = True
    self.is_defending = False

  def attack(self, target: Human):
        if self.conscious and target.conscious:
            attack_roll = roll_dice(20) + self.weapon.attack
            defense_roll = roll_dice(20)
            if Debugger.debugging:
                print("DEBUG: Attack was {attack} Defense was {defense}".format(attack = attack_roll, defense = defense_roll))
            if defense_roll + target.defense >= attack_roll + self.strength:
                print("{attacker}'s attack missed!".format(attacker=self.name))
            elif target.is_defending:
                block_chance = roll_dice(100) + target.defense
                if block_chance >= 90:
                    print("{defender} blocked the attack!".format(defender=target.name))
                else:
                    damage_roll = roll_dice(10) + self.weapon.damage - target.defense
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
                damage_roll = roll_dice(10) + self.weapon.damage
                knockout_roll = roll_dice(100)
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
