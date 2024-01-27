import math

# antena_list = [
#     (6, 11, 4),
#     (8, 17, 3),
#     (19, 19, 2),
#     (19, 11, 4),
#     (15, 7, 6),
#     (12, 19, 4),
# ]
# start = (10, 19)
# end = (19, 14)


# # test 1
# start = (5, 17)
# end = (8, 11)
# antena_list = [
#     (5, 11, 2),
#     (5, 14, 2),
#     (5, 17, 2),
#     (8, 17, 2),
#     (11, 17, 2),
#     (8, 11, 2),
# ]

# test2
# start = (8, 11)
# end = (12, 3)


# antena_list = [
#     (5, 11, 2),
#     (5, 14, 2),
#     (5, 17, 2),
#     (8, 17, 2),
#     (11, 17, 2),
#     (8, 11, 2),
#     (5, 7, 2),
#     (5, 4, 2),
#     (8, 4, 2),
#     (11, 4, 2),
# ]


class Poligon:
    def __init__(self, antennas: list|set, start: tuple, end: tuple):
        self.antennas = antennas
        self.start_point = start
        self.end_point = end

    @staticmethod
    def check_the_neighboring_antenna(base_antena: tuple, neighboring_antenna: tuple) -> bool:
        """
        Checks whether the antennas have a common field

        Args:
            base_antena (tuple): (x,y) first antena
            neighboring_antenna (tuple): (x,y) second antena

        Returns:
            bool: whether the antennas share a common field
        """
        x_d = abs(base_antena[0] - neighboring_antenna[0])
        y_d = abs(base_antena[1] - neighboring_antenna[1])
        distance = math.sqrt(x_d ** 2 + y_d ** 2)
        r1 = base_antena[2]
        r2 = neighboring_antenna[2]
        if r1 + r2 >= distance:
            return True
        else:
            return False

    @staticmethod
    def check_point_in_cyrcle(point: tuple, cyrcle: tuple) -> bool:
        """
        Checks whether a point is in a circle

        Args:
            point (tuple): (x,y) point
            cyrcle (tuple): (x,y,r) cyrcle

        Returns:
            bool: whether the point is in a circle
        """
        distance = (point[0] - cyrcle[0]) ** 2 + (point[1] - cyrcle[1]) ** 2
        return distance <= cyrcle[2] ** 2

    def where_is_antenna(self, point:tuple, antennas: list|set) -> tuple:
        """
        Checks the range of the antenna where the point is located

        Args:
            point (tuple): (x,y) point
            antennas (list | set): ((x1,y1,r1)...(xn,yn,rn)) of cyrcle (antennas)

        Returns:
            tuple: (x,y,r) cyrcle/antena
        """
        for antenna in antennas:
            if self.check_point_in_cyrcle(point, antenna):
                return antenna
        return None

    def find_neighbor_antenna(self, base_antenna: tuple, antennas: list|set) -> set:
        """
        Searches for all neighboring antennas that have a common range.

        Args:
            base_antenna (tuple): (x,y,r) cyrcle/antena
            antennas (list | set): ((x1,y1,r1)...(xn,yn,rn)) of cyrcle (antennas)

        Returns:
            set: ((x1,y1,r1)...(xn,yn,rn)) of cyrcle (antennas)
        """
        neighbors = set()
        for antenna in antennas:
            if self.check_the_neighboring_antenna(base_antenna, antenna):
                neighbors.add(antenna)
        return neighbors

    def check_area(self) -> str:
        """
        Checks whether the flight is safe.

        Returns:
            str: bezpieczny przelot nie jest możliwy / bezpieczny przelot jest możliwy
        """
        start_antenna = self.where_is_antenna(self.start_point, self.antennas)
        end_antenna = self.where_is_antenna(self.end_point, self.antennas)

        if (not start_antenna) or (not end_antenna):
            return "bezpieczny przelot nie jest możliwy"

        range = {start_antenna}
        find_neighbor = {start_antenna}
        neighbors = set()
        antennas_to_check = set(self.antennas)
        antennas_to_check.remove(start_antenna)

        while find_neighbor:
            neighbors.clear()
            for antenna in find_neighbor:
                neighbors.update(self.find_neighbor_antenna(antenna, antennas_to_check))
                range = range | neighbors
            for antenna in neighbors:
                antennas_to_check.remove(antenna)

            find_neighbor.clear()
            find_neighbor.update(neighbors)

            if end_antenna in range:
                return "bezpieczny przelot jest możliwy"

        return "bezpieczny przelot nie jest możliwy"

#  for testing
# poligon = Poligon(antena_list, start, end)
# print(poligon.check_area())



num_antennas = int(input("Podaj liczbę nadajników: "))


antena_list = []
for i in range(num_antennas):
    x, y, m = map(int, input("Podaj współrzędne i moc nadajnika (x y m): ").split())
    antena_list.append((x, y, m))


start_x, start_y = map(int, input("Podaj współrzędne punktu początkowego (x y): ").split())
start = (start_x, start_y)


end_x, end_y = map(int, input("Podaj współrzędne punktu końcowego (x y): ").split())
end = (end_x, end_y)

poligon = Poligon(antena_list, start, end)
print(poligon.check_area())
