import matplotlib.pyplot as plt
import random
import sweepline


def generate_random_segments():
    n = int(input("Enter amount of segments to be generated(more than 50 is not recommended) => "))
    min_coord, max_coord = map(float, input("Enter bounds to be used for generation for example -5 5\n").split())
    segments = []
    for _ in range(n):
        x1 = random.uniform(min_coord, max_coord)
        y1 = random.uniform(min_coord, max_coord)
        x2 = random.uniform(min_coord, max_coord)
        y2 = random.uniform(min_coord, max_coord)
        segment = ((x1, y1), (x2, y2))
        segments.append(segment)
    return segments


def input_segments():
    segments = []
    n = int(input("Enter amount of segments to be tested => "))
    print("Enter segment (two pairs of x and y per line).")
    for _ in range(n):
        x1, y1, x2, y2 = map(float, input().split())
        segments.append([[x1, y1], [x2, y2]])
    return segments


def plot_segments_and_intersections(segments, intersections):
    # Extract x and y coordinates from line segments
    x_coords = [[segment[0][0], segment[1][0]] for segment in segments]
    y_coords = [[segment[0][1], segment[1][1]] for segment in segments]

    # Plot line segments
    for x, y in zip(x_coords, y_coords):
        plt.plot(x, y, 'b')

    # Plot intersection points
    intersection_x = [intersection[0] for intersection in intersections]
    intersection_y = [intersection[1] for intersection in intersections]
    plt.plot(intersection_x, intersection_y, 'ro')

    # Add labels and title
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Line Segments and Intersection Points')

    # Display the plot
    plt.show()


segments = None
if int(input("Enter 0 if you want to enter segments yourself or 1 for random => ")) == 0:
    segments = input_segments()
else:
    segments = generate_random_segments()

intersections = sweepline.isect_segments(segments)
plot_segments_and_intersections(segments, intersections)
