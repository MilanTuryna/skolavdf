class Polygon:
    '''
    Třída polygon definuje obecný polygon o n hranách.
    '''
    
    amount_of_objects = 0
    
    def __init__(self, amount = 0, name = "unknown"):
        Polygon.amount_of_objects += 1
        self.__amount_of_sides = amount
        self.__polygon_name = name

    def __del__(self):
        Polygon.amount_of_objects -= 1

    def get_num_of_sides(self):
        return self.__amount_of_sides

    def get_name(self):
        return self.__polygon_name
    
    def __set_num_of_sides(self, amount):
        self.__amount_of_sides = amount

    def __set_name(self, name):
        self.__polygon_name = name
        
    def set_polygon(self, amount, name):
        self.__set_num_of_sides(amount)
        self.__set_name(name)

    def __str__(self):
        return f"Ahoj, já jsem {self.__polygon_name} a počet mých hran je {self.__amount_of_sides}."
        
    
my_triangle = Polygon(3, "trojúhelník")
print(my_triangle)

my_octagon = Polygon(8, "osmiúhelník")
print(my_octagon)

my_polygon = Polygon(5, "pětiúhelník")
print(my_polygon)

my_polygon.set_polygon(6, "šestiúhelník")

print(my_polygon)
print(my_polygon.get_num_of_sides())
print(my_polygon.get_name())
print(type(my_polygon))