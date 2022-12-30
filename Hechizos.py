class Hechizos:
    # Diccionario para llevar un conteo de los hechizos creados para cada nivel
    LIMITE_HECHIZOS = {
        1: 10,
        2: 5,
        3: 3
    }
    
    # Diccionario que almacena el número de veces que se ha utilizado cada nivel
    USO_HECHIZOS = {
        1: 0,
        2: 0,
        3: 0
    }
    
    def __init__(self, nombre, tipo, nivel):
        # Verificar si se ha alcanzado el límite de hechizos para el nivel especificado
        if Hechizos.USO_HECHIZOS[nivel] >= Hechizos.limite_hechizos[nivel]:
            raise ValueError(f"Se ha alcanzado el límite de hechizos para el nivel {nivel}")
        
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
        
        # Aumentar el conteo de hechizos creados para el nivel especificado
        Hechizos.USO_HECHIZOS[nivel] += 1
    
    def daño(self, nivel_extra=0):
        # Calcula el daño base del hechizo
        daño = self.nivel * 10
        
        # Añade el daño adicional por cada nivel extra
        for i in range(nivel_extra):
            daño += 15
        
        return daño
    
    def modificar_uso_hechizo(self, nivel, usos):
        # Modificar el número de usos del nivel especificado
        self.USO_HECHIZOS[nivel] = usos






class Hechizo:
    def __init__(self, nombre, tipo, nivel):
        self.nombre = nombre
        self.tipo = tipo
        self.nivel = nivel
    
    def calcular_dano(self, valor_base, multiplicador):
        # Función que calcula el daño del hechizo en función de los parámetros recibidos
        self.dano = valor_base * multiplicador
    
    def usar(self):
        print(f"Hechizo usado: {self.nombre} (nivel {self.nivel}, daño {self.dano})")



hechizo = Hechizo("Bola de Fuego", "Fuego", 3)
hechizo.calcular_dano(50, 1.5)