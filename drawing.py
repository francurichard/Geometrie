import matplotlib.pyplot as plt


class Drawing:

    def __init__(self, points):
        self.points = points

    def __draw_polygon(self):
        points_x, points_y = [], []
        for point in self.points['coordinates']:
            points_x.append(point[0])
            points_y.append(point[1])
        points_x.append(points_x[0])
        points_y.append(points_y[0])
        plt.plot(points_x, points_y)

    def __draw_convexity(self):
        convex_principal_points_x, convex_principal_points_y = [], []
        convex_non_principal_points_x, convex_non_principal_points_y = [], []
        concave_principal_points_x, concave_principal_points_y = [], []
        concave_non_principal_points_x, concave_non_principal_points_y = [], []

        for index in range(len(self.points['coordinates'])):
            if self.points['convexity'][index]:
                if self.points['principality'][index]:
                    convex_principal_points_x.append(self.points['coordinates'][index][0])
                    convex_principal_points_y.append(self.points['coordinates'][index][1])
                else:
                    convex_non_principal_points_x.append(self.points['coordinates'][index][0])
                    convex_non_principal_points_y.append(self.points['coordinates'][index][1])

            else:
                if self.points['principality'][index]:
                    concave_principal_points_x.append(self.points['coordinates'][index][0])
                    concave_principal_points_y.append(self.points['coordinates'][index][1])
                else:
                    concave_non_principal_points_x.append(self.points['coordinates'][index][0])
                    concave_non_principal_points_y.append(self.points['coordinates'][index][1])

        plt.plot(convex_principal_points_x, convex_principal_points_y, 'ro', label="Convex Principal")
        plt.plot(convex_non_principal_points_x, convex_non_principal_points_y, 'bo', label="Convex Neprincipal")
        plt.plot(concave_principal_points_x, concave_principal_points_y, 'go', label="Concav Principal")
        plt.plot(concave_non_principal_points_x, concave_non_principal_points_y, 'yo', label="Concav Neprincipal")

    def draw(self):
        self.__draw_polygon()
        self.__draw_convexity()
        plt.legend(loc="upper left")
        plt.show()
