
import json

# Load the JSON file
with open("character.json", "r") as f:
    data = json.load(f)

# Extract the hit, saving_throw, and damage_dice fields from the first spell in the list

hit = data["hechizos"][0]["damage"]["hit"]
saving_throw = data["hechizos"][0]["damage"]["saving_throw"]
damage_dice = data["hechizos"][0]["damage"]["damage_dice"]

# Print the extracted fields
print("Hit:", hit)
print("Saving throw:", saving_throw)
print("Damage dice:", damage_dice)




#per fer que es modifiqui del archiu json
import json

# Load the JSON file
with open("character.json", "r") as f:
    data = json.load(f)

# Get the maximum number of level 1 spells and the remaining number of uses
max_level_1_spells = data["spell_slots"]["spell_level_1_max"]
remaining_level_1_uses = data["spell_slots"]["spell_level_1"]

# Function to use a level 1 spell
def use_level_1_spell():
    global remaining_level_1_uses
    if remaining_level_1_uses > 0:
        # Use a level 1 spell
        remaining_level_1_uses -= 1
        print("Used a level 1 spell. Remaining level 1 spells:", remaining_level_1_uses)
        # Update the "spell_level_1" field in the JSON file
        data["spell_slots"]["spell_level_1"] = remaining_level_1_uses
        with open("character.json", "w") as f:
            json.dump(data, f)
    else:
        # Cannot use a level 1 spell
        print("No remaining level 1 spells")