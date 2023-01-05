import json

# Load the JSON data into a Python object
with open('character.json', 'r') as f:
  character = json.load(f)

def use_spell(spell_name, spell_level):
  # Find the spell in the character's spell list
  spell = None
  for s in character['hechizos']:
    if s['nombre'] == spell_name:
      spell = s
      break

  # Return None if the spell was not found
  if spell is None:
    return None

  # If the requested spell level is higher than the spell's actual level, print a message and return None
  if spell_level > spell['level']:
    print('Overpowered!')
    return None

  # Get the maximum and remaining number of spells for the given level
  spell_level_max = character['spell_slots'][f'spell_level_{spell_level}_max']
  spell_level_remaining = character['spell_slots'][f'spell_level_{spell_level}']

  # Return None if there are no remaining spells
  if spell_level_remaining == 0:
    return None

  # Decrement the number of remaining spells by 1
  spell_level_remaining -= 1

  # Update the number of remaining spells in the JSON data
  character['spell_slots'][f'spell_level_{spell_level}'] = spell_level_remaining

  # If the requested spell level is the same as the spell's actual level, print the spell's details
  if spell_level == spell['level']:
    print(f'Hit: {spell["damage"]["hit"]}')
    print(f'Saving throw: {spell["damage"]["saving_throw"]}')
    print(f'Damage dice: {spell["damage"]["damage_dice"]}')
    print(f'Damage type: {spell["damage"]["damage_type"]}')

  # Return the spell object
  return spell