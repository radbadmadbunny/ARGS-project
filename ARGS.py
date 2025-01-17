#Trying to make a very basic battler type of game.
#Notes for next time: Charge spell, character based dungeons, summon spell. Berserker and/or Paladin. Monk is a possibility also. Maybe beast tamer lol
#For-loop and variable based on how many players: Theoretically infinite also (Look low for more context)
#Charge and summon spell would be fun and possible however the mage already has so many attacks.
#It could be interesting if I added a passive ability to the rogue where if he doesn't use any offensive abilities for some turns it increases like damage and/or dexterity.
#Something else could work too I don't know man
#possibly rename basic spell magic missile, magic bolt, piercing bolt, magic strike, etc.
#I know mage has too much but what about meteor and/or magic weapon (gives strength for one turn or something)
#BREAKTHROUGH
#Hard code the code for extra players for now
#Make a function that uses a player as the variable thing.
#Make self.options

import random

def crit_hit(dext):
    random_number = random.randint(dext,20)
    if random_number == 20:
        print("Xx_Critical Hit_xX")
        return True
    else:
        return False



class Character:
    def __init__(self, poison, fire, health_potions, mana_potions, strength, health, fortitude, intellect, mana, wisdom, dexterity, blade_effect, alive, name, options):
        #Tracks poison
        self.poison = poison
        #Tracks fire
        self.fire = fire
        #Restores health
        self.health_potions = health_potions
        #Restores mana
        self.mana_potions = mana_potions
        #For melee attacks
        self.strength = strength
        #HP
        self.health = health
        #To prevent heals going over starting health
        self.fortitude = fortitude
        #Max Mana, same idea as fortitude
        self.intellect = intellect
        #Mainly for poison blade
        self.blade_effect = blade_effect
        #MP
        self.mana = mana
        #Magic damage
        self.wisdom = wisdom
        #Increases chance for critical hits
        self.dexterity = dexterity
        #Helps figure out who wins
        self.alive = alive
        #Literally just the player's inputted name
        self.name = name
        #For action options
        self.options = options

    def melee_attack(self, target_name):
        damage = self.strength * 1.5
        target = base_character
        if target_name == player1.name:
            target = player1
        elif target_name == player2.name:
            target = player2
        elif target_name == player3.name:
            target = player3
        elif target_name == player4.name:
            target = player4
        if crit_hit(self.dexterity):
            damage * 2
        if self.blade_effect == "poison":
            target.poison = 4
            self.blade_effect = "nothing"
            print(self.name, "poisons", target.name, "with their toxic dagger")
        target.health -= damage
        print(self.name, "attacks", target.name + ".\n" + str(target.name) + "takes", damage, "damage!")

    def health_potion(self, options):
        if self.health_potions > 0:
            before_health = self.health
            self.health += 15
            self.health_potions -= 1
            print(self.health_potions)
            self.maximum_checker()
            after_health = self.health
            health_healed = after_health - before_health
            if self.health_potions > 1:
                print("You healed", str(health_healed), "hit points.")
                print("You have", self.health_potions, "health potions left.")
            elif self.health_potions == 1:
                print("You healed", str(health_healed), "hit points.")
                print("You have", self.health_potions, "health potion left.")
            else:
                print("You healed", str(health_healed), "hit points.")
                print("You have no more health potions!")
                options.remove("Restore Health")
        else:
            print("You have no more health potions!")

    def mana_potion(self, options):
        if self.mana_potions > 0:
            before_mana = self.mana
            self.mana += 15
            self.mana_potions -= 1
            self.maximum_checker()
            after_mana = self.mana
            mana_restored = after_mana - before_mana
            if self.mana_potions > 1:
                print("You restored", str(mana_restored), "mana")
                print("You have", self.mana_potions, "mana potions left.")
            elif self.mana_potions == 1:
                print("You restored", str(mana_restored), "mana")
                print("You have", self.mana_potions, "mana potion left.")
            else:
                print("You restored", str(mana_restored), "mana")
                print("You have no more mana potions!")
                options.remove("Restore Mana")
        else:
            print("You have no more mana potions!\n")

    def options_maker(self):
        if isinstance(self, Rogue):
            self.options.append("Poison Blade")
        elif isinstance(self, Mage):
            self.options.append("Fireball")
            self.options.append("Erosion Ray")
            self.options.append("Magic Bolt")

    def alive_checker(self):
        if self.alive and self.health < 0:
            self.alive = False
            print(self.name, "has died!")
            player_name_list.remove(self.name)
            info_character.alive_people -= 1

    def turn_play(self):
        self.turn_start()
        acted = False
        while not acted:
            print(self.name, "it is your turn, what shall you do?")
            action = input("Your options are: \n" + str(self.options) + "\n")
            if action.lower() == "melee attack" or action.lower() == "melee":
                while True:
                    player_name_list.remove(self.name)
                    target_name = input("Who will be your target?\nOptions: " + str(player_name_list) + ".\n")
                    player_name_list.append(self.name)
                    if (target_name != player1.name) and (target_name != player2.name) and (target_name != player3.name) and (target_name != player4.name):
                        print("That is not a valid target.")
                    else:
                        self.melee_attack(target_name)
                        acted = True
                        break
            elif action.lower() == "restore mana" or action.lower() == "mana":
                self.mana_potion(self.options)
                acted = True
            elif action.lower() == "restore health" or action.lower() == "heal":
                self.health_potion(self.options)
            elif isinstance(self, Rogue):
                if action.lower() == "poison blade" or action.lower() == "poison":
                    self.poison_blade()
                    acted = True
            elif isinstance(self, Mage):
                if action.lower() == "fireball" or action.lower() == "fire":
                    while True:
                        player_name_list.remove(self.name)
                        target_name = input("Who will be your target?\nOptions: " + str(player_name_list) + ".\n")
                        player_name_list.append(self.name)
                        if (target_name != player1.name) and (target_name != player2.name) and (
                                target_name != player3.name) and (target_name != player4.name):
                            print("That is not a valid target.")
                        else:
                            self.magic_attack(player2, "fire")
                            acted = True
                            break
                elif action.lower() == "magic bolt" or action.lower() == "bolt":
                    while True:
                        player_name_list.remove(self.name)
                        target_name = input("Who will be your target?\nOptions: " + str(player_name_list) + ".\n")
                        player_name_list.append(self.name)
                        if (target_name != player1.name) and (target_name != player2.name) and (
                                target_name != player3.name) and (target_name != player4.name):
                            print("That is not a valid target.")
                        else:
                            self.magic_attack(player2, "bolt")
                            acted = True
                            break
                elif action.lower() == "erosion ray" or action.lower() == "erosion":
                    while True:
                        player_name_list.remove(self.name)
                        target_name = input("Who will be your target?\nOptions: " + str(player_name_list) + ".\n")
                        player_name_list.append(self.name)
                        if (target_name != player1.name) and (target_name != player2.name) and (
                                target_name != player3.name) and (target_name != player4.name):
                            print("That is not a valid target.")
                        else:
                            self.magic_attack(player2, "erosion")
                            acted = True
                            break
            if not acted:
                print("Please try again.")
            if acted:
                self.turn_end()


    def turn_end(self):
        if self.poison > 0:
            self.health -= 1.25
            self.poison -= 1
            print(self.name, "takes 1.25 damage from poison!")
        self.maximum_checker()

    def turn_start(self):
        if self.fire > 0:
            self.health -= 2
            self.fire -= 1
            print(self.name, "takes 2 damage from being on fire!")
        self.maximum_checker()

    def maximum_checker(self):
        if self.health >= self.fortitude:
            self.health = self.fortitude
        if self.mana >= self.intellect:
            self.mana = self.intellect
        if self.health < 0:
            self.health = 0
        if self.mana < 0:
            self.mana = 0

class Mage(Character):
    def magic_attack(self, target, spell_type):
        damage = 0
        if spell_type == "normal":
            if self.mana >= 3:
                damage = self.intellect * 1.2
                self.mana -= 3
                print(self.name, "shot a magic bolt at", str(target.name) + ".")
            else:
                print("That spell requires 3 mana and you have", str(self.mana) + ". You cannot afford that spell.")
        #Fire Ball
        elif spell_type == "fire":
            if self.mana >= 6:
                damage = self.intellect * 1.6
                target.fire = 2
                self.mana -= 6
                print(self.name, "shoots a fireball which sets ablaze", str(target.name) + ".")
            else:
                print("That spell requires 6 mana and you have", str(self.mana) + ". You cannot afford that spell.")
        #Lowers Max hp: Damage but cooler
        #used to be Acid Blast, now Erosion Ray
        elif spell_type == "erosion":
            if self.mana >= 7:
                target.fortitude -= 5
                target.maximum_checker()
                damage = self.intellect * 1.3
                self.mana -= 7
                print(self.name, "erodes away at", target.name + "'s health.")
            else:
                print("That spell requires 7 mana and you have", str(self.mana) + ". You cannot afford that spell.")
        if crit_hit(self.dexterity):
            damage *= 2
        target.health -= damage
        print(target.name, "takes", damage, "damage!")

class Rogue(Character):
    def poison_blade(self):
        #Makes next melee attack inflict poison
        self.blade_effect = "poison"
        print(self.name, "dips their blade in poison. Their dagger is now imbued with poison.")

class ExtraInfo:
    def __init__(self, alive_people):
        self.alive_people = alive_people


#def print_area():
base_character = Character(0,0,2,1,3,45,45,
                    20,20,3,3,"nothing",True, "nameless", "undefined")
rogue_class = Rogue(0,0,2,1,5,50,50,
                    20,20,2,5,"nothing",True, "nameless", "undefined")
mage_class = Mage(0,0,1,2,1,40,40,
                   20,20,5,1,"nothing",True, "nameless", "undefined")

#Melee users should have higher dext, less magic stats, strength based
#Magic users should have less health slightly more mana and such and not really any dext
#People reliant on other sources of damage should be weak in all stats
#All of this is so using the game mechanics of each character can be incentivised

#Actual stuff now?
#Consider making for-loop and variable based on how many players: Theoretically infinite also
#Optimize maybe make just one variable that gets reused

player_count = int(input("How many people will be playing this game? (Max. 4)\n"))

info_character = ExtraInfo(player_count)


player1 = base_character
player2 = base_character
player3 = base_character
player4 = base_character

for x in range (1, player_count + 1):
    if x == 1:
        while True:
            class_choice = input("Player 1, what class shall you be?(Rogue, Mage)\n")
            if class_choice.lower() == "rogue":
                player1 = rogue_class
                break
            elif class_choice.lower() == "mage":
                player1 = mage_class
                break
            else:
                print("Please try again.")
    elif x == 2:
        while True:
            class_choice = input("Player 2, what class shall you be?(Rogue, Mage)\n")
            if class_choice.lower() == "rogue":
                player2 = rogue_class
                break
            elif class_choice.lower() == "mage":
                player2 = mage_class
                break
            else:
                print("Please try again.")
    elif x == 3:
        while True:
            class_choice = input("Player 3, what class shall you be?(Rogue, Mage)\n")
            if class_choice.lower() == "rogue":
                player3 = rogue_class
                break
            elif class_choice.lower() == "mage":
                player3 = mage_class
                break
            else:
                print("Please try again.")
    elif x == 4:
        while True:
            class_choice = input("Player 4, what class shall you be?(Rogue, Mage)\n")
            if class_choice.lower() == "rogue":
                player4 = rogue_class
                break
            elif class_choice.lower() == "mage":
                player4 = mage_class
                break
            else:
                print("Please try again.")

player1.name = input("Player 1, what is your name?\n")
player2.name = input("Player 2, what is your name?\n")
player_name_list = [str(player1.name), str(player2.name)]
if player_count >= 3:
    player3.name = input("Player 3, what is your name?\n")
    player_name_list.append(player3.name)
if player_count >= 4:
    player4.name = input("Player 4, what is your name?\n")
    player_name_list.append(player4.name)


player1.options = ["Melee Attack", "Restore Mana", "Restore Health"]
player2.options = ["Melee Attack", "Restore Mana", "Restore Health"]
if player_count > 2:
    player3.options = ["Melee Attack", "Restore Mana", "Restore Health"]
if player_count > 3:
    player4.options = ["Melee Attack", "Restore Mana", "Restore Health"]

player1.options_maker()
player2.options_maker()
if player_count > 2:
    player3.options_maker()
if player_count > 3:
    player4.options_maker()


def health_print():
    if player_count == 2:
        print(player1.name, player1.health, ":", player2.name, player2.health)
    elif player_count == 3:
        print(player1.name, player1.health, ":", player2.name, player2.health, ":", player3.name, player3.health)
    elif player_count == 4:
        print(player1.name, player1.health, ":", player2.name, player2.health, ":", player3.name, player3.health, ":", player4.name, player4.health)

def alive_check():
    player1.alive_checker()
    player2.alive_checker()
    if player_count > 2:
        player3.alive_checker()
    if player_count > 3:
        player4.alive_checker()

turn_count = 0
for x in range(0,10):
    print("\n")
health_print()

while info_character.alive_people > 1:
    if player1.alive:
        player1.turn_play()
        alive_check()
        turn_count += 1
        health_print()
    if player1.alive:
        player2.turn_play()
        turn_count += 1
        health_print()
    if player_count > 2:
        if player1.alive:
            player3.turn_play()
            health_print()
            turn_count += 1
    if player_count > 3:
        if player1.alive:
            player4.turn_play()
            health_print()
            turn_count += 1

if player1.alive:
    print(player1.name, "wins!!!")
elif player2.alive:
    print(player2.name, "wins!!!")
elif player_count > 2:
    if player3.alive:
        print(player3.name, "wins!!!")
elif player_count > 3:
    if player4.alive:
        print(player4.name, "wins!!!")
else:
    print("It was a tie.")
print("The game lasted", turn_count, "turns!")