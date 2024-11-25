import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.patches import Polygon
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
from sympy import symbols, Eq, solve
import numpy as np
import math

# Limits: angle between 10 and 75 degrees
#         mass less than 6 digits

def generate_figure(angle_A, angle_B):
  # Define constants
  BAR_WIDTH = 0.15
  AB_DIST = 6
  LINE_WIDTH = 1
  CIRCLE_RADIUS = 0.05
  ARC_RADIUS = 1.5

  # Set up the figure and axis
  fig, ax = plt.subplots(figsize=(10, 5))
  ax.set_aspect('equal')
  ax.set_xlim(-1, AB_DIST+1)
  ax.set_ylim(-5, 1)
  ax.axis('off')
  
  # Draw bar
  ax.plot([-0.25, AB_DIST+0.25], [0, 0], color='black', linewidth=LINE_WIDTH)
  ax.add_patch(Rectangle((-0.25, 0), AB_DIST+0.5, BAR_WIDTH, facecolor='none', edgecolor='black', linewidth=0, hatch='////'))
  
  # Draw point A
  ax.add_patch(Circle((0, 0), CIRCLE_RADIUS, color='black', zorder=2))
  ax.text(0, -0.1, 'A', fontsize=18, ha='right', va='top', fontfamily='times new roman', weight='bold')

  # Draw point B
  ax.add_patch(Circle((AB_DIST, 0), CIRCLE_RADIUS, color='black', zorder=2))
  ax.text(AB_DIST, -0.1, 'B', fontsize=18, ha='left', va='top', fontfamily='times new roman', weight='bold')

  return fig, ax

if __name__ == "__main__":
  fig, ax = generate_figure(30, 10)
  plt.savefig("q9.png", dpi=300, bbox_inches='tight')
  plt.show()