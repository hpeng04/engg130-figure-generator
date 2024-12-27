import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc, Circle, Polygon, PathPatch
import matplotlib.path as mpath
import numpy as np
import math

# Limits: 

def generate_figure(force_A, force_B, force_C, force_D, 
                    ydist_AB, ydist_B, xdist_C, xdist_CD):

    # Define constants
  LINE_WIDTH = 1
  TRIANGLE_HEIGHT = 0.5
  TRIANGLE_WIDTH = 0.5
  ARROW_HEAD_LENGTH = 0.2
  ARROW_HEAD_WIDTH = 0.2
  ARROW_LENGTH = 1.8
  ANGLE_DIAMETER = 2.7
  ARROW_WIDTH = LINE_WIDTH*2.5
  EXTENSION = 3

  # Set distance constraints
  ydist_AB_label = ydist_AB
  ydist_B_label = ydist_B
  xdist_C_label = xdist_C
  xdist_CD_label = xdist_CD

  # Code not implemented for calculating resultant force
  # ccw = True
  # pos = True
  # total_moment = force_A*(ydist_AB+ydist_B) - force_B*ydist_B - force_C*xdist_C + force_D*(xdist_C+xdist_CD)
  


  MIN_DIST_RATIO = 0.2
  MAX_DIST_RATIO = 0.8

  TOT_DIST = 5

  total_x_dist = xdist_C + xdist_CD
  total_y_dist = ydist_AB + ydist_B

  if (ydist_AB/total_y_dist < MIN_DIST_RATIO):
    ydist_AB = MIN_DIST_RATIO*total_y_dist
  elif (ydist_AB/total_y_dist > MAX_DIST_RATIO):
    ydist_AB = MAX_DIST_RATIO*total_y_dist
  if (ydist_B/total_y_dist < MIN_DIST_RATIO):
    ydist_B = MIN_DIST_RATIO*total_y_dist
  elif (ydist_B/total_y_dist > MAX_DIST_RATIO):
    ydist_B = MAX_DIST_RATIO*total_y_dist
  
  if (xdist_C/total_x_dist < MIN_DIST_RATIO):
    xdist_C = MIN_DIST_RATIO*total_x_dist
  elif (xdist_C/total_x_dist > MAX_DIST_RATIO):
    xdist_C = MAX_DIST_RATIO*total_x_dist
  if (xdist_CD/total_x_dist < MIN_DIST_RATIO):
    xdist_CD = MIN_DIST_RATIO*total_x_dist
  elif (xdist_CD/total_x_dist > MAX_DIST_RATIO):
    xdist_CD = MAX_DIST_RATIO*total_x_dist

  ydist_AB = TOT_DIST*ydist_AB/total_y_dist
  ydist_B = TOT_DIST*ydist_B/total_y_dist

  xdist_C = TOT_DIST*xdist_C/total_x_dist
  xdist_CD = TOT_DIST*xdist_CD/total_x_dist

  total_y_dist = TOT_DIST
  total_x_dist = TOT_DIST

  # Set up the figure and axis
  fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 12))
  ax1.set_aspect('equal')
  ax1.axis('off')
  ax1.set_xlim(-7, total_x_dist+1+EXTENSION)
  ax1.set_ylim(-5, total_y_dist+1+EXTENSION)
  ax2.set_aspect('equal')
  ax2.axis('off')
  ax2.set_xlim(-1, total_x_dist+7+EXTENSION)
  ax2.set_ylim(-5, total_y_dist+1+EXTENSION)

  # Draw the frames

  ax1.plot([0, 0], [0, total_y_dist+EXTENSION], color='black', linewidth=LINE_WIDTH, zorder=10)
  ax1.arrow(0, total_y_dist+EXTENSION, 0, 0.001, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH, zorder=10)
  ax1.text(0, total_y_dist+EXTENSION+0.05+ARROW_HEAD_LENGTH, r'$\it{y}$', fontsize=18, ha='center', va='bottom', math_fontfamily='cm')
  ax1.plot([0, total_x_dist+EXTENSION], [0, 0], color='black', linewidth=LINE_WIDTH, zorder=10)
  ax1.arrow(total_x_dist+EXTENSION, 0, 0.001, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH, zorder=10)
  ax1.text(total_x_dist+EXTENSION+0.05+ARROW_HEAD_LENGTH, 0, r'$\it{x}$', fontsize=18, ha='left', va='center', math_fontfamily='cm')
  ax1.text(-0.1, -0.1, r'$\it{O}$', fontsize=18, ha='right', va='top', math_fontfamily='cm')
  ax1.add_patch(Circle((xdist_C+xdist_CD, 0), 0.07, edgecolor='none', facecolor='black', linewidth=LINE_WIDTH, zorder=10))
  ax1.text(xdist_C+xdist_CD-0.15, -0.3, r'$\it{A}$', fontsize=18, ha='center', va='top', math_fontfamily='cm')

  ax2.plot([0, 0], [0, total_y_dist+EXTENSION], color='black', linewidth=LINE_WIDTH, zorder=10)
  ax2.arrow(0, total_y_dist+EXTENSION, 0, 0.001, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH, zorder=10)
  ax2.text(0, total_y_dist+EXTENSION+0.05+ARROW_HEAD_LENGTH, r'$\it{y}$', fontsize=18, ha='center', va='bottom', math_fontfamily='cm')
  ax2.plot([0, total_x_dist+EXTENSION], [0, 0], color='black', linewidth=LINE_WIDTH, zorder=10)
  ax2.arrow(total_x_dist+EXTENSION, 0, 0.001, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH, zorder=10)
  ax2.text(total_x_dist+EXTENSION+0.05+ARROW_HEAD_LENGTH, 0, r'$\it{x}$', fontsize=18, ha='left', va='center', math_fontfamily='cm')
  ax2.text(-0.1, -0.1, r'$\it{O}$', fontsize=18, ha='right', va='top', math_fontfamily='cm')
  ax2.add_patch(Circle((xdist_C+xdist_CD, 0), 0.07, edgecolor='none', facecolor='black', linewidth=LINE_WIDTH, zorder=10))
  ax2.text(xdist_C+xdist_CD-0.15, -0.3, r'$\it{A}$', fontsize=18, ha='center', va='top', math_fontfamily='cm')

  # Plot forces in ax1
  # Force A
  ax1.arrow(ARROW_LENGTH+ARROW_HEAD_LENGTH+ARROW_HEAD_WIDTH, ydist_AB+ydist_B, -ARROW_LENGTH, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=ARROW_WIDTH, zorder=10)
  ax1.text(ARROW_LENGTH+ARROW_HEAD_LENGTH+ARROW_HEAD_WIDTH-1, ydist_AB+ydist_B+0.1, f'{force_A}N', fontsize=18, ha='left', va='bottom', math_fontfamily='cm', fontfamily='times new roman')
  # Force B  
  ax1.arrow(-(ARROW_LENGTH+ARROW_HEAD_LENGTH+ARROW_HEAD_WIDTH), ydist_B, ARROW_LENGTH, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=ARROW_WIDTH, zorder=10)
  ax1.text(-(ARROW_LENGTH+ARROW_HEAD_LENGTH+ARROW_HEAD_WIDTH-1), ydist_B+0.1, f'{force_B}N', fontsize=18, ha='right', va='bottom', math_fontfamily='cm', fontfamily='times new roman')
  # Force C
  ax1.arrow(xdist_C, ARROW_LENGTH+ARROW_HEAD_LENGTH+ARROW_HEAD_WIDTH, 0, -ARROW_LENGTH, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=ARROW_WIDTH, zorder=10)
  ax1.text(xdist_C, ARROW_LENGTH+ARROW_HEAD_LENGTH+ARROW_HEAD_WIDTH, f'{force_C}N', fontsize=18, ha='center', va='bottom', math_fontfamily='cm', fontfamily='times new roman')
  # Force D (force on point A)
  ax1.arrow(xdist_CD+xdist_C, 0, 0, ARROW_LENGTH, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=ARROW_WIDTH, zorder=10)
  ax1.text(xdist_CD+xdist_C, ARROW_LENGTH+ARROW_HEAD_LENGTH+ARROW_HEAD_WIDTH, f'{force_D}N', fontsize=18, ha='left', va='bottom', math_fontfamily='cm', fontfamily='times new roman')

  # Plot distances in ax1
  Y_MARKER_OFFSET = 4.5
  X_MARKER_OFFSET = 3
  ax1.plot([-Y_MARKER_OFFSET-0.5, -Y_MARKER_OFFSET+0.5], [0, 0], color='black', linewidth=LINE_WIDTH, zorder=10)
  ax1.arrow(-Y_MARKER_OFFSET, 0, 0, ydist_B-ARROW_HEAD_LENGTH, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH/2, zorder=10)
  ax1.arrow(-Y_MARKER_OFFSET, ydist_B, 0, -(ydist_B-ARROW_HEAD_LENGTH), head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH/2, zorder=10)
  ax1.text(-Y_MARKER_OFFSET-0.5, ydist_B/2, f'{ydist_B_label}m', fontsize=16, ha='right', va='center', math_fontfamily='cm', fontfamily='times new roman')
  ax1.plot([-Y_MARKER_OFFSET-0.5, -Y_MARKER_OFFSET+0.5], [ydist_B, ydist_B], color='black', linewidth=LINE_WIDTH, zorder=10)
  ax1.arrow(-Y_MARKER_OFFSET, ydist_B, 0, ydist_AB-ARROW_HEAD_LENGTH, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH/2, zorder=10)
  ax1.arrow(-Y_MARKER_OFFSET, ydist_B+ydist_AB, 0, -(ydist_AB-ARROW_HEAD_LENGTH), head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH/2, zorder=10)
  ax1.text(-Y_MARKER_OFFSET-0.5, ydist_B+ydist_AB/2, f'{ydist_AB_label}m', fontsize=16, ha='right', va='center', math_fontfamily='cm', fontfamily='times new roman')
  ax1.plot([-Y_MARKER_OFFSET-0.5, -Y_MARKER_OFFSET+0.5], [ydist_B+ydist_AB, ydist_B+ydist_AB], color='black', linewidth=LINE_WIDTH, zorder=10)

  ax1.plot([0,0], [-X_MARKER_OFFSET-0.5, -X_MARKER_OFFSET+0.5], color='black', linewidth=LINE_WIDTH, zorder=10)
  ax1.arrow(0, -X_MARKER_OFFSET, xdist_C-ARROW_HEAD_LENGTH, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH/2, zorder=10)
  ax1.arrow(xdist_C, -X_MARKER_OFFSET, -(xdist_C-ARROW_HEAD_LENGTH), 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH/2, zorder=10)
  ax1.text(xdist_C/2, -X_MARKER_OFFSET-0.5, f'{xdist_C_label}m', fontsize=16, ha='center', va='top', math_fontfamily='cm', fontfamily='times new roman')
  ax1.plot([xdist_C, xdist_C], [-X_MARKER_OFFSET-0.5, -X_MARKER_OFFSET+0.5], color='black', linewidth=LINE_WIDTH, zorder=10)
  ax1.arrow(xdist_C, -X_MARKER_OFFSET, xdist_CD-ARROW_HEAD_LENGTH, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH/2, zorder=10)
  ax1.arrow(xdist_C+xdist_CD, -X_MARKER_OFFSET, -(xdist_CD-ARROW_HEAD_LENGTH), 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH/2, zorder=10)
  ax1.text(xdist_C+xdist_CD/2, -X_MARKER_OFFSET-0.5, f'{xdist_CD_label}m', fontsize=16, ha='center', va='top', math_fontfamily='cm', fontfamily='times new roman')
  ax1.plot([xdist_C+xdist_CD, xdist_C+xdist_CD], [-X_MARKER_OFFSET-0.5, -X_MARKER_OFFSET+0.5], color='black', linewidth=LINE_WIDTH, zorder=10)
  
  # Plot distances in ax2
  d = 2
  ax2.plot([0,0], [-X_MARKER_OFFSET-0.5, -X_MARKER_OFFSET+0.5], color='black', linewidth=LINE_WIDTH, zorder=10)
  ax2.arrow(0, -X_MARKER_OFFSET, xdist_C+xdist_CD-ARROW_HEAD_LENGTH, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH/2, zorder=10)
  ax2.arrow(xdist_C+xdist_CD, -X_MARKER_OFFSET, -(xdist_C+xdist_CD-ARROW_HEAD_LENGTH), 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH/2, zorder=10)
  ax2.text((xdist_C+xdist_CD)/2, -X_MARKER_OFFSET-0.5, f'{xdist_C_label+xdist_CD_label}m', fontsize=16, ha='center', va='top', math_fontfamily='cm', fontfamily='times new roman')
  ax2.plot([xdist_C+xdist_CD, xdist_C+xdist_CD], [-X_MARKER_OFFSET-0.5, -X_MARKER_OFFSET+0.5], color='black', linewidth=LINE_WIDTH, zorder=10)
  ax2.arrow(xdist_C+xdist_CD, -X_MARKER_OFFSET, d-ARROW_HEAD_LENGTH, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH/2, zorder=10)
  ax2.arrow(xdist_C+xdist_CD+d, -X_MARKER_OFFSET, -d+ARROW_HEAD_LENGTH, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH/2, zorder=10)
  ax2.text(xdist_C+xdist_CD+d/2, -X_MARKER_OFFSET-0.5, 'd', fontsize=16, ha='center', va='top', math_fontfamily='cm', fontfamily='times new roman')
  ax2.plot([xdist_C+xdist_CD+d, xdist_C+xdist_CD+d], [-X_MARKER_OFFSET-0.5, -X_MARKER_OFFSET+0.5], color='black', linewidth=LINE_WIDTH, zorder=10)

  # Plot resultant force in ax2 at point d
  ax2.arrow(d+xdist_CD+xdist_C, 0, 0.8, ARROW_LENGTH-0.1, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=ARROW_WIDTH, zorder=10)
  ax2.text(d+xdist_CD+xdist_C+0.8, ARROW_LENGTH+0.1, r'$\it{F_R}$', fontsize=18, ha='left', va='bottom', math_fontfamily='cm', fontfamily='times new roman')

  
  return fig


if __name__ == "__main__":
  fig = generate_figure(10, 10, 5, 10, 1, 1, 3, 2)
  plt.savefig("q19.png", dpi=300, bbox_inches='tight')
  plt.show()