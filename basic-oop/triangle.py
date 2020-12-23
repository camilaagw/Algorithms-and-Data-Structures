
class Triangle:

    number_of_sides = 3

    def __init__(self, angle1, angle2, angle3):
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    def check_angles(self):
        return self.angle1 + self.angle2 + self.angle3 == 180


class Equilateral(Triangle):

    def __init__(self):
        super().__init__(60, 60, 60)


if __name__ == "__main__":
    my_triangle = Triangle(90, 30, 60)

    print(f' Number of sides: {my_triangle.number_of_sides}')
    print(f' Angles check: {my_triangle.check_angles()}')

