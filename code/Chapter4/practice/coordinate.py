import math

points = [(1, 8), (3, 4), (-2, 5), (12.5, 2)]

distances = []
for point in points:
    distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
    distances.append(distance)

print(points[distances.index(min(distances))])