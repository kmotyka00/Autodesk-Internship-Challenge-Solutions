import random
import numpy as np
import matplotlib.pyplot as plt

MIN_RANGE = -100
MAX_RANGE = 100

def smallest_triangle(points_number: int):

    points = generate_points(points_number)

    min_area = np.inf
    for i in range(points_number):
        for j in range(i, points_number):
            for k in range(j, points_number):

                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]

                # Geometric formula based on trapeziums
                # area = np.abs((x1 * y2 + x2 * y3 + x3 * y1 - y1 * x2 - y2 * x3 - y3 * x1)) / 2.0
                area = abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))/2.0)
                
                if 0 < area < min_area:
                    min_area = area
                    min_triangle = (points[i], points[j], points[k])
    
    print(f"Smallest triangle: {min_triangle} with area {min_area}")
    visualize_triangle(min_triangle, points)
    return min_triangle

def generate_points(points_number: int):
    return [(random.uniform(MIN_RANGE, MAX_RANGE), random.uniform(MIN_RANGE, MAX_RANGE)) for i in range(points_number)]

def get_user_input():
    while True:
        try:
            return int(input("Provide the number of points: "))
        except ValueError:
            print("Enter integer!")

def visualize_triangle(min_triangle, points):
    x_points = [point[0] for point in points]
    y_points = [point[1] for point in points]
    plt.scatter(x_points, y_points, c='blue', label='all points')

    x_triangle = [point[0] for point in min_triangle]
    y_triangle = [point[1] for point in min_triangle]
    plt.scatter(x_triangle, y_triangle, c='red', label='smallest triangle')
    
    plt.legend()
    plt.show()

def main():
    n = get_user_input()
    smallest_triangle(n)

if __name__ == "__main__":
    main()