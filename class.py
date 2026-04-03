from symtable import Class


class Facade:
    pass


facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)

class Grade:
    minimum_passing = 65

class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."


class Circle:
    pi = 3.14

    def __init__(self, diameter):
        self.radius = diameter / 2
        print(f"New circle with diameter: {diameter}")

    def area(self, radius):
        return Circle.pi * radius ** 2

    def circumference(self):
        return 2 * Circle.pi * self.radius

    def __repr__(self):
        return f"Circle with radius {self.radius}"


medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(dir(5))


def this_function_is_an_object(param=None):
    return "This is a function object!"


print(dir(this_function_is_an_object))

print(medium_pizza)
print(teaching_table)
print(round_room)

print(f"Medium pizza circumference: {medium_pizza.circumference()}")
print(f"Teaching table circumference: {teaching_table.circumference()}")
print(f"Round room circumference: {round_room.circumference()}")