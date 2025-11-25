"""
This file is used to test my math. It takes 3 circles' centers and radii as input and then returns the point of intersection that is common to the 3 circles. 
In the context of earthquakes, the point of intersection of the 3 circles is the epicenter of the earthquake recorded by the stations.
"""

import numpy as np
import matplotlib.pyplot as plt

def circle_intersection(c1, r1, c2, r2):
    """This function is going to find the intersection of 3 circles."""
    x1, y1 = c1
    x2, y2 = c2
    d = np.hypot(x2 - x1, y2 - y1)

    if d > r1 + r2 or d < abs(r1 - r2):
        return None  # No intersection

    a = (r1**2 - r2**2 + d**2) / (2 * d)
    h = np.sqrt(max(r1**2 - a**2, 0))

    xm = x1 + a * (x2 - x1) / d
    ym = y1 + a * (y2 - y1) / d

    xs1 = xm + h * (y2 - y1) / d
    ys1 = ym - h * (x2 - x1) / d
    xs2 = xm - h * (y2 - y1) / d
    ys2 = ym + h * (x2 - x1) / d

    return (xs1, ys1), (xs2, ys2)

def find_common_intersection(c1, r1, c2, r2, c3, r3):
    """Finds the intersection point common to the three circles that are given."""
    points = circle_intersection(c1, r1, c2, r2)
    if not points:
        return None

    for p in points:
        if np.isclose(np.hypot(p[0] - c3[0], p[1] - c3[1]), r3, atol=1e-6):
            return (round(p[0], 6), round(p[1], 6))  # Rounding to avoid floating-point errors

    return None

def plot_circles(c1, r1, c2, r2, c3, r3, intersection):
    """This function plots the three circles and as well as their intersection point, that is, the point common to all three circles."""
    fig, ax = plt.subplots()
    
    circles = [
        (c1, r1, 'r'),
        (c2, r2, 'g'),
        (c3, r3, 'b')
    ]
    
    for center, radius, color in circles:
        circle = plt.Circle(center, radius, color=color, fill=False, linestyle='dashed', linewidth=2)
        ax.add_patch(circle)
        ax.plot(*center, marker='o', color=color, markersize=5)

    if intersection:
        ax.plot(*intersection, marker='o', color='black', markersize=8, label='Intersection')

    ax.set_xlim(min(c1[0], c2[0], c3[0]) - max(r1, r2, r3), max(c1[0], c2[0], c3[0]) + max(r1, r2, r3))
    ax.set_ylim(min(c1[1], c2[1], c3[1]) - max(r1, r2, r3), max(c1[1], c2[1], c3[1]) + max(r1, r2, r3))

    ax.set_aspect('equal', adjustable='datalim')
    ax.legend()
    plt.grid()
    plt.show()

# Example usage:
c1, r1 = (4, 0), 2
c2, r2 = (2, 4), 4
c3, r3 = (-6, 0), 8

intersection = find_common_intersection(c1, r1, c2, r2, c3, r3)

if intersection:
    print(f"Intersection point: {intersection}")
else:
    print("Point of intersection common to the three circles cannot be found.")

plot_circles(c1, r1, c2, r2, c3, r3, intersection)
