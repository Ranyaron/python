class Road:
    """Расчет массы асфальта для покрытия всего дорожного полотна."""

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_asphalt(self, mass=25, blade_thickness=5):
        mass_asphalt = round((self.__length * self.__width * mass * blade_thickness / 1000), 2)
        print(f'Масса асфальта шириной {self.__length} м. и длиной {self.__width} м. = {mass_asphalt} тонн.')


road = Road(20, 5000)
road.mass_asphalt()
