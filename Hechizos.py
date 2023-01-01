spells = {
  "Fireball": Spell("Fireball", "Fire", 5, 50),
  "Lightning Bolt": Spell("Lightning Bolt", "Thunder", 4, 40),
  "Frostbite": Spell("Frostbite", "Ice", 3, 30)
}
class Spell:
  def __init__(self, name, magic_type, level, damage):
    self.name = name
    self.magic_type = magic_type
    self.level = level
    self.damage = damage

class MagicSystem:
  def __init__(self, max_uses_per_level):
    self.max_uses_per_level = max_uses_per_level
    self.uses_left = max_uses_per_level.copy()

  def use(self, level):
    if self.uses_left[level] > 0:
      self.uses_left[level] -= 1
      return True
    else:
      return False

  def set_uses(self, level, uses):
    self.uses_left[level] = uses

magic_system = MagicSystem({1: 2, 2: 3, 3: 4, 4: 5, 5: 6})


#Canviar el nombre de usos dels hechizos per level
magic_system.set_uses(fireball.level, 1)

if magic_system.use(fireball.level):
  # Lanzar hechizo fireball
  print(f"El hechizo {fireball.name} ha sido lanzado con éxito!")
if magic_system.use(fireball.level):
  print("No tienes más usos de magia de este nivel!")



print(spells["Fireball"].damage)
print(spells["Lightning Bolt"].damage)
print(spells["Frostbite"].damage)


def __init__(self, nombre, tipo, nivel):
        # Verificar que el nivel del hechizo esté dentro de los límites permitidos
        if nivel not in self.LIMITE_HECHIZOS:
            raise ValueError(f"Nivel de hechizo inválido: {nivel}")
        
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
    
    def definir_dano(self):
        # Calcular el daño en función del nivel del hechizo
        self.dano = 10 * self.nivel
        
        print(f"Hechizo usado: {self.nombre} (nivel {self.nivel}, daño {self.dano})")