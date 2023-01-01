#has de posar el range un valor mes gran del que demanes

for i in range(1,5):
    for j in range(1,4):
        resultat= i*j
        if resultat < 5:
            print(resultat,"es menor que 5")
        elif 5 <= resultat < 10:
            print(resultat,"es entre 5 i 10")
        else:
            print(resultat,"es més gran que 10")








