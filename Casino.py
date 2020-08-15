from Cartas import barajas
class Cartas:
    class pica:
        carta_pica= []
        for pica in barajas:
            if "Pica" in pica:
                carta_pica.append(pica)
maso= Cartas
print(maso.pica.carta_pica)

    



