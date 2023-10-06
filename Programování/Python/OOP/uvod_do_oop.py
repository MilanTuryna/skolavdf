"""V pythonu vytvoř skript, ve kterém bude definována třída Rectangle, která bude mít dvě privátní vlatnosti - strany a, b, 
které musí být větší než 0. Součástí třídy budou gettery pro zjištění délky strany a a strany b. 
Pomocí setterů bude možné změnit hodnoty stran a, b. Metoda get_rect_content bude vracet obsah obdélníku, 
metoda get_rect_permimeter bude vracet obvod obdélníku. Magická metoda __str__ bude vracet text 
v podobě "Obdélník o stranách a = číslo a b = číslo má obsah S = číslo a obvod O = číslo"."""
class Rectangle:
    def __init__(self, a, b):
        self.errorMessages = []
        if a <= 0:
            self.__add_error_message("a", a, 1)
            a = 1
        if b <= 0:
            self.__add_error_message("b", b, 1)
            b = 1
        self.set_a(a)
        self.set_b(b)
    
    def __add_error_message(self, var, original_val, new_val):
       self.errorMessages.append(f"Strana {var} ({original_val}) musí být větší jak nula. Byla tedy změněna na {new_val}. ")

    def set_a(self, a):
        self.__a = a

    def set_b(self, b):
        self.__b = b  

    # Vrátí obsah obdelníku
    def get_rect_content(self):
        return self.__a*self.__b

    def get_rect_perimeter(self):
        return 2*(self.__a+self.__b)
    
    def __str__(self):
        result = ""
        for x in self.errorMessages:
            result += x
        result += f"Obdelník o stranách a = {self.__a} a b = {self.__b} má obsah S = {self.get_rect_content()} a obvod O = {self.get_rect_perimeter()}"
        return result

my_rectangle = Rectangle(14, 13)
print(my_rectangle)