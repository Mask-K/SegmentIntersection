import matplotlib.pyplot as plt
import sweepline

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

segments = [[[0, 0], [0, 6]], [[0, 5], [5, 5]], [[5, 5], [5, 0]], [[2, 2], [7, 7]],
            [[1, 4], [4, 1]], [[2, 6], [5, 2]], [[2, 5], [2, 0]]]
intersections = sweepline.isect_segments(segments)
print(intersections)

plot_segments_and_intersections(segments, intersections)
