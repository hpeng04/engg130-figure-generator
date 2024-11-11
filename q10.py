import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.patches import Polygon
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
import numpy as np
import math

def generate_figure(length_OA, length_AB, length_BC):
  # Define constants
  BAR_WIDTH = 0.5
  arrow_head_width = 0.2 #0.01*(length_OA+length_AB+1.6*length_BC)
  arrow_head_length = 0.2 #0.01*(length_OA+length_AB+1.6*length_BC)
  triangle_width = 1
  line_width = 1
  circle_radius = 0.1
  triangle_height = 1.2

  label_OA = length_OA
  label_AB = length_AB
  label_BC = length_BC

  # Set limits for the lengths
  total_length = length_OA + length_AB + length_BC

  if (length_OA/total_length < 0.15):
    length_OA = 0.15*total_length
  elif (length_OA/total_length > 0.85):
    length_OA = 0.85*total_length
  if (length_AB/total_length < 0.15):
    length_AB = 0.15*total_length
  elif (length_AB/total_length > 0.85):
    length_AB = 0.85*total_length
  if (length_BC/total_length < 0.15):
    length_BC = 0.15*total_length
  elif (length_BC/total_length > 0.85):
    length_BC = 0.85*total_length
  
  total_length = length_OA + length_AB + length_BC
  length_OA = 15*length_OA/total_length
  length_AB = 15*length_AB/total_length
  length_BC = 15*length_BC/total_length
  total_length = 15

  # Set up the figure and axis
  fig, ax = plt.subplots(figsize=(10, 5))
  ax.set_aspect('equal')
  ax.set_xlim(-1, 16)
  ax.set_ylim(-5, 5)
  ax.axis('off')
  
  # Draw bar
  ax.add_patch(Rectangle((0, -BAR_WIDTH/2), total_length, BAR_WIDTH, facecolor='lightgrey', edgecolor='black', linewidth=line_width))
  # ax.plot([0,0], [-BAR_WIDTH/2, BAR_WIDTH/2], color='black', linewidth=line_width)
  # ax.plot([0, total_length], [BAR_WIDTH/2, BAR_WIDTH/2], color='black', linewidth=line_width)
  # ax.plot([0, total_length], [-BAR_WIDTH/2, -BAR_WIDTH/2], color='black', linewidth=line_width)
  # ax.plot([total_length, total_length], [-BAR_WIDTH/2, BAR_WIDTH/2], color='black', linewidth=line_width)
  # ax.fill([0, 0, total_length, total_length], [-BAR_WIDTH/2, BAR_WIDTH/2, BAR_WIDTH/2, -BAR_WIDTH/2], color='lightgrey')

  # Draw force distribution
  ax.plot([0, total_length], [BAR_WIDTH/2+1.5, BAR_WIDTH/2+1.5], color='black', linewidth=1.5)
  for (i, x) in enumerate(np.linspace(0, total_length, 6)):
    ax.arrow(x, BAR_WIDTH/2+1.5, 0, -1.5+arrow_head_length, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.text(total_length/2, BAR_WIDTH/2+1.8, "$\it{w}$ N/m", fontsize=18, color='black', ha='center', va='bottom', math_fontfamily='dejavuserif', fontfamily='times new roman')
  
  # Draw triangle supports
  # Left support
  ax.add_patch(Polygon([[length_OA, -BAR_WIDTH/2], [length_OA-triangle_width/2, -triangle_height-BAR_WIDTH/2], [length_OA+triangle_width/2, -triangle_height-BAR_WIDTH/2]], linewidth=line_width, edgecolor='black', facecolor='grey'))
  ax.add_patch(Circle((length_OA, -BAR_WIDTH/2), 0.1, facecolor='black', edgecolor='white', linewidth=1))
  for (i, x) in enumerate(np.linspace(length_OA-triangle_width/2+circle_radius, length_OA+triangle_width/2-circle_radius, 4)):
    ax.add_patch(Circle((x, -triangle_height-BAR_WIDTH/2-circle_radius), circle_radius, facecolor='white', edgecolor='black', linewidth=line_width))
  ax.add_patch(Rectangle((length_OA-triangle_width/2-2*circle_radius, -triangle_height-BAR_WIDTH-2*circle_radius), triangle_width+4*circle_radius, BAR_WIDTH/2, facecolor='white', edgecolor='black', linewidth=line_width, hatch='/////////')) 
  ax.text(length_OA-0.8*triangle_width, -BAR_WIDTH-0.25, "$\it{A}$", fontsize=18, color='black', ha='center', va='center', math_fontfamily='dejavuserif', fontfamily='times new roman')
  # Right support
  ax.add_patch(Polygon([[length_OA+length_AB, -BAR_WIDTH/2], [length_OA+length_AB-triangle_width/2, -triangle_height-BAR_WIDTH/2], [length_OA+length_AB+triangle_width/2, -triangle_height-BAR_WIDTH/2]], linewidth=line_width, edgecolor='black', facecolor='grey'))
  ax.add_patch(Circle((length_OA+length_AB, -BAR_WIDTH/2), 0.1, facecolor='black', edgecolor='white', linewidth=1))
  ax.add_patch(Rectangle((length_OA+length_AB-triangle_width/2-2*circle_radius, -triangle_height-BAR_WIDTH), triangle_width+4*circle_radius, BAR_WIDTH/2, facecolor='white', edgecolor='black', linewidth=line_width, hatch='/////////')) 
  ax.text(length_OA+length_AB+0.8*triangle_width, -BAR_WIDTH-0.25, "$\it{B}$", fontsize=18, color='black', ha='center', va='center', math_fontfamily='dejavuserif', fontfamily='times new roman')
  
  # Label distances
  ax.plot([0, 0], [-triangle_height-BAR_WIDTH-2*circle_radius-0.5, -BAR_WIDTH], color='black', linewidth=1.5)

  ax.arrow(0, -triangle_height-BAR_WIDTH-2*circle_radius-0.3, length_OA-arrow_head_length, 0, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.arrow(length_OA, -triangle_height-BAR_WIDTH-2*circle_radius-0.3, -(length_OA-arrow_head_length), 0, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.text(length_OA/2, -triangle_height-BAR_WIDTH-2*circle_radius-0.7, f"{label_OA} m", fontsize=18, color='black', ha='center', va='center', math_fontfamily='dejavuserif', fontfamily='times new roman')

  ax.plot([length_OA, length_OA], [-triangle_height-BAR_WIDTH-2*circle_radius-0.5, -triangle_height-BAR_WIDTH-2*circle_radius-0.1], color='black', linewidth=1.5)
  ax.arrow(length_OA, -triangle_height-BAR_WIDTH-2*circle_radius-0.3, length_AB-arrow_head_length, 0, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.arrow(length_OA+length_AB, -triangle_height-BAR_WIDTH-2*circle_radius-0.3, -(length_AB-arrow_head_length), 0, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.text(length_OA+length_AB/2, -triangle_height-BAR_WIDTH-2*circle_radius-0.7, f"{label_AB} m", fontsize=18, color='black', ha='center', va='center', math_fontfamily='dejavuserif', fontfamily='times new roman')

  ax.plot([length_OA+length_AB, length_OA+length_AB], [-triangle_height-BAR_WIDTH-2*circle_radius-0.5, -triangle_height-BAR_WIDTH-2*circle_radius-0.1], color='black', linewidth=1.5)
  ax.arrow(length_OA+length_AB, -triangle_height-BAR_WIDTH-2*circle_radius-0.3, length_BC-arrow_head_length, 0, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.arrow(length_OA+length_AB+length_BC, -triangle_height-BAR_WIDTH-2*circle_radius-0.3, -(length_BC-arrow_head_length), 0, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.text(length_OA+length_AB+length_BC/2, -triangle_height-BAR_WIDTH-2*circle_radius-0.7, f"{label_BC} m", fontsize=18, color='black', ha='center', va='center', math_fontfamily='dejavuserif', fontfamily='times new roman')

  ax.plot([total_length, total_length], [-triangle_height-BAR_WIDTH-2*circle_radius-0.5, -BAR_WIDTH], color='black', linewidth=1.5)
  return fig, ax

if __name__ == "__main__":
  fig, ax = generate_figure(50,35,0.5)
  plt.savefig("q4.png", dpi=300, bbox_inches='tight')
  plt.show()