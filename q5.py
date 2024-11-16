import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.patches import Polygon
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
import numpy as np
import math

def generate_figure(length_OA, length_AB, length_BC, force_AB, force_BC, force_BC_angle):
  # Define constants
  BAR_WIDTH = 0.5
  arrow_head_width = 0.3 
  arrow_head_length = 0.4 
  triangle_width = 1
  line_width = 1
  circle_radius = 0.1
  triangle_height = 1.2

  label_OA = length_OA
  label_AB = length_AB
  label_BC = length_BC

  # Set limits for the lengths
  total_length = length_OA + length_AB + length_BC

  total_width = length_OA + length_BC

  if (length_OA/total_width < 0.15):
    length_OA = 0.15*total_width
  elif (length_OA/total_width > 0.85):
    length_OA = 0.85*total_width
  if (length_AB/total_width < 0.10):
    length_AB = 1
  elif (length_AB/total_width > 0.7):
    length_AB = 0.7*total_width
  if (length_BC/total_width < 0.15):
    length_BC = 0.15*total_width
  elif (length_BC/total_width > 0.85):
    length_BC = 0.85*total_width
  
  total_width = length_OA + length_BC
  length_OA = 15*length_OA/total_width
  length_AB = 15*length_AB/total_width
  length_BC = 15*length_BC/total_width
  total_width = 15
  baseline = -2

  # Set up the figure and axis
  fig, ax = plt.subplots(figsize=(10, 5))
  ax.set_aspect('equal')
  ax.set_xlim(-4, 18)
  ax.set_ylim(-3, length_AB + 3)
  ax.axis('off')

  ### Support at left end ###
  ax.plot([0, 0], [baseline, 2], color='black', linewidth=line_width)
  for (i, x) in enumerate(np.linspace(baseline+0.3, 2-line_width/100, 8)):
    ax.plot([-0.5, 0-line_width/100], [x-0.3, x], color='black', linewidth=line_width)
  
  # Draw bar OA
  ax.plot([0, length_OA-BAR_WIDTH/2], [BAR_WIDTH/2, BAR_WIDTH/2], color='black', linewidth=line_width)
  ax.plot([0, length_OA+BAR_WIDTH/2], [-BAR_WIDTH/2, -BAR_WIDTH/2], color='black', linewidth=line_width)
  ax.fill([0, 0, length_OA-BAR_WIDTH/2, length_OA+BAR_WIDTH/2], [-BAR_WIDTH/2, BAR_WIDTH/2, BAR_WIDTH/2, -BAR_WIDTH/2], color='lightgrey')

  # Draw bar AB
  ax.plot([length_OA-BAR_WIDTH/2, length_OA-BAR_WIDTH/2], [BAR_WIDTH/2, length_AB+BAR_WIDTH/2], color='black', linewidth=line_width)
  ax.plot([length_OA+BAR_WIDTH/2, length_OA+BAR_WIDTH/2], [-BAR_WIDTH/2, length_AB-BAR_WIDTH/2], color='black', linewidth=line_width)
  ax.fill([length_OA-BAR_WIDTH/2, length_OA+BAR_WIDTH/2, length_OA+BAR_WIDTH/2, length_OA-BAR_WIDTH/2], [BAR_WIDTH/2, -BAR_WIDTH/2, length_AB-BAR_WIDTH/2, length_AB+BAR_WIDTH/2], color='lightgrey')

  # Draw bar BC
  ax.plot([length_OA-BAR_WIDTH/2, length_OA+BAR_WIDTH/2+length_BC], [length_AB+BAR_WIDTH/2, length_AB+BAR_WIDTH/2], color='black', linewidth=line_width)
  ax.plot([length_OA+BAR_WIDTH/2, length_OA+BAR_WIDTH/2+length_BC], [length_AB-BAR_WIDTH/2, length_AB-BAR_WIDTH/2], color='black', linewidth=line_width)
  ax.fill([length_OA-BAR_WIDTH/2, length_OA+BAR_WIDTH/2, length_OA+BAR_WIDTH/2+length_BC, length_OA+BAR_WIDTH/2+length_BC], [length_AB+BAR_WIDTH/2, length_AB-BAR_WIDTH/2, length_AB-BAR_WIDTH/2, length_AB+BAR_WIDTH/2], color='lightgrey')
  ax.plot([length_OA+BAR_WIDTH/2+length_BC, length_OA+BAR_WIDTH/2+length_BC], [length_AB+BAR_WIDTH/2, length_AB-BAR_WIDTH/2], color='black', linewidth=line_width)
  ax.add_patch(Circle((total_width, length_AB), 0.1, facecolor='black', linewidth=0))

  # Draw points and forces
  ax.text(1.3, 0.6, 'A', fontsize=24, ha='right', fontfamily='times new roman', weight='bold')
  # Force on bar AB
  ax.arrow(length_OA, length_AB+1.5+arrow_head_length+BAR_WIDTH/2+0.1, 0, -1.5, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.text(length_OA+arrow_head_width/2, length_AB+1.5/2+arrow_head_length+BAR_WIDTH/2, f"{force_AB} N", fontsize=18, color='black', ha='left', va='bottom', math_fontfamily='dejavuserif', fontfamily='times new roman')
  # Force on tip of bar BC
  arrow_length = 1.7
  arrow_xlen = -arrow_length*math.sin(math.radians(force_BC_angle))
  arrow_ylen = arrow_length*math.cos(math.radians(force_BC_angle))
  ax.arrow(length_OA+length_BC+(arrow_head_length)*math.sin(math.radians(force_BC_angle))-arrow_xlen+0.1+BAR_WIDTH/2, length_AB-(arrow_head_length)*math.cos(math.radians(force_BC_angle))-arrow_ylen, arrow_xlen, arrow_ylen, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.add_patch(Arc((length_OA+length_BC+BAR_WIDTH/2, length_AB), 2, 2, angle=270, theta1=-10, theta2=force_BC_angle, color='black'))
  ax.text(length_OA+length_BC+(arrow_head_length)*math.sin(math.radians(force_BC_angle))+0.5+BAR_WIDTH/2, length_AB-(arrow_head_length)*math.cos(math.radians(force_BC_angle))-0.2*arrow_ylen, f"{force_BC} N", fontsize=18, color='black', ha='left', va='bottom', math_fontfamily='dejavuserif', fontfamily='times new roman')
  ax.text(length_OA+length_BC+0.5-arrow_xlen/2, length_AB-(arrow_head_length)*math.cos(math.radians(force_BC_angle))-arrow_ylen-1.5, f"{force_BC_angle}\u00B0", fontsize=18, color='black', ha='center', va='bottom', fontfamily='times new roman')

  # Draw distance markers
  # Width
  ax.plot([length_OA, length_OA], [baseline, 1.5*arrow_head_width+baseline], color='black', linewidth=line_width)
  ax.plot([length_OA+length_BC, length_OA+length_BC], [baseline, length_AB-BAR_WIDTH/2-0.1], color='black', linewidth=line_width, linestyle="--")

  ax.arrow(0, (1.5*arrow_head_width)/2+baseline, length_OA-arrow_head_length, 0, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.arrow(length_OA, (1.5*arrow_head_width)/2+baseline, -(length_OA-arrow_head_length), 0, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.text(length_OA/2, -(3*arrow_head_width)+baseline, f"{label_OA} m", fontsize=18, color='black', ha='center', va='bottom', fontfamily='times new roman')

  ax.arrow(length_OA, (1.5*arrow_head_width)/2+baseline, length_BC-arrow_head_length, 0, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.arrow(total_width, (1.5*arrow_head_width)/2+baseline, -(length_BC-arrow_head_length), 0, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.text(length_OA+length_BC/2, -(3*arrow_head_width)+baseline, f"{label_BC} m", fontsize=18, color='black', ha='center', va='bottom', fontfamily='times new roman')
  
  #Height
  ax.plot([-2, 1.5], [0, 0], color='black', linewidth=line_width, linestyle="--")
  ax.plot([-2, total_width], [length_AB, length_AB], color='black', linewidth=line_width, linestyle="--")
  ax.arrow(-2, 0, 0, length_AB-arrow_head_length, head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.arrow(-2, length_AB, 0, -(length_AB-arrow_head_length), head_width=arrow_head_width, head_length=arrow_head_length, color='black')
  ax.text(-2.2, length_AB/2, f"{label_AB} m", fontsize=18, color='black', ha='right', va='center', fontfamily='times new roman')

  return fig ,ax


if __name__ == "__main__":
  fig, ax = generate_figure(1,1,1,800,400,60)
  plt.savefig("q5.png", dpi=300, bbox_inches='tight')
  plt.show()