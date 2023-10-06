# Definuj třídu Linearf, která bude řešit výpočet lineární rovnice v tvaru ax+b = 0
# Vstupní parametry: a, b
# Příklad:
# a= 10
# b = 10
# 10x + 10 = 0 
# 10x = -10 /10
# x = -1 

class LinearF():
    def __init__(self, a, b):
        if(a == 0): 
            raise Exception("a != 0, jelikož nulou se dělit nedá")
        self.a = a
        self.b = b

    def vypocitej(self):
        return 0-self.b/self.a
    
    def __str__(self):
        return "X se rovná " + str(rovnice.vypocitej())

rovnice = LinearF(5,-15)
print(rovnice)