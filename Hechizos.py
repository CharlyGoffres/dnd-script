#Menu de hechizos para ver los hechizos que tengo por nivel
import json

# Carga el archivo JSON en un diccionario
with open("variables.json", "r") as f:
    variables = json.load(f)

# Obtiene la lista de hechizos
spells = variables["hechizos"]

# Agrupa los hechizos según su nivel
spells_by_level = {}
for spell in spells:
    level = spell["level"]
    if level not in spells_by_level:
        spells_by_level[level] = []
    spells_by_level[level].append(spell)

# Imprime un menú con las secciones correspondientes a cada nivel de hechizo
print("Selecciona un hechizo:")
print()
for level, level_spells in spells_by_level.items():
    print(f"Nivel {level}:")
    for i, spell in enumerate(level_spells):
        print(f"  {i+1}. {spell['nombre']}")
print()


