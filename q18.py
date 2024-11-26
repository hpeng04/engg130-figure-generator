import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc, Circle
import numpy as np
import math

# Limits: 

def generate_figure(A_width, B_width, force_angle, force_B):
  
  # Define constants
  LINE_WIDTH = 1
  ARC_DIAMETER = 1
  BAR_LENGTH = 4
  BAR_HEIGHT = 3
  ARROW_HEAD_LENGTH = 0.08
  ARROW_HEAD_WIDTH = 0.08
  ARROW_LENGTH = 1 - ARROW_HEAD_LENGTH
  ARROW_WIDTH = 0.1 * ARROW_HEAD_WIDTH
  ARROW_SPACING = 0.04
  BOX_SIZE = 0.15
  

  # Set up the figure and axis
  fig, ax = plt.subplots(figsize=(7, 7))
  ax.set_aspect('equal')
  # ax.set_xlim(-1, 6)
  # ax.set_ylim(-5, 1)
  ax.axis('off')

  A_width_label = f'{A_width}m'
  B_width_label = f'{B_width}m'
  force_angle_label = f'{force_angle}°'

  total_width = A_width + B_width

  if (A_width/total_width < 0.35):
    A_width = 0.35*total_width
  elif (A_width/total_width > 0.65):
    A_width = 0.65*total_width
  if (B_width/total_width < 0.35):
    B_width = 0.35*total_width
  elif (B_width/total_width > 0.65):
    B_width = 0.65*total_width
  
  total_width = A_width + B_width

  A_width = A_width/total_width
  B_width = B_width/total_width

  total_width = A_width + B_width

  if (force_angle < 30):
    force_angle = 30

  # Draw L beam outline
  ax.plot([0, 0], [0, -A_width], color='black', linewidth=LINE_WIDTH)
  ax.plot([0, BAR_LENGTH], [0, 0], color='black', linewidth=LINE_WIDTH)
  ax.plot([0, BAR_LENGTH-B_width], [-A_width, -A_width], color='black', linewidth=LINE_WIDTH)
  ax.plot([BAR_LENGTH, BAR_LENGTH], [0, -BAR_HEIGHT], color='black', linewidth=LINE_WIDTH)
  ax.plot([BAR_LENGTH-B_width, BAR_LENGTH-B_width], [-A_width, -BAR_HEIGHT], color='black', linewidth=LINE_WIDTH)
  ax.plot([BAR_LENGTH-B_width, BAR_LENGTH], [-BAR_HEIGHT, -BAR_HEIGHT], color='black', linewidth=LINE_WIDTH)

  # Fill L beam
  ax.add_patch(Rectangle((0, -A_width), BAR_LENGTH, A_width, facecolor='lightgray', edgecolor='none', linewidth=LINE_WIDTH))
  ax.add_patch(Rectangle((BAR_LENGTH-B_width, -BAR_HEIGHT), B_width, BAR_HEIGHT, facecolor='lightgray', edgecolor='none', linewidth=LINE_WIDTH))

  # Draw width labels at A
  ax.text(-0.6, -A_width/2, A_width_label, fontsize=14, ha='right', va='center', fontfamily='times new roman', math_fontfamily='dejavuserif')
  ax.arrow(-0.5, 0, 0, -A_width+ARROW_HEAD_LENGTH, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black')
  ax.arrow(-0.5, -A_width, 0, A_width-ARROW_HEAD_LENGTH, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black')
  
  # Draw width labels at B
  ax.arrow(BAR_LENGTH, -BAR_HEIGHT-0.8, -B_width+ARROW_HEAD_LENGTH, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black')
  ax.arrow(BAR_LENGTH-B_width, -BAR_HEIGHT-0.8, B_width-ARROW_HEAD_LENGTH, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black')
  ax.text(BAR_LENGTH-B_width/2, -BAR_HEIGHT-1, B_width_label, fontsize=14, ha='center', va='top', fontfamily='times new roman', math_fontfamily='dejavuserif')
  ax.plot([BAR_LENGTH-B_width, BAR_LENGTH-B_width], [-BAR_HEIGHT-0.9, -BAR_HEIGHT-0.05], color='black', linewidth=LINE_WIDTH)
  ax.plot([BAR_LENGTH, BAR_LENGTH], [-BAR_HEIGHT-0.9, -BAR_HEIGHT-0.05], color='black', linewidth=LINE_WIDTH)

  # Draw force couple at A
  ax.arrow(-ARROW_SPACING, 0, -ARROW_LENGTH, 0, width=ARROW_WIDTH, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black')
  ax.arrow(-ARROW_LENGTH-ARROW_HEAD_LENGTH-ARROW_SPACING, -A_width, ARROW_LENGTH, 0, width=ARROW_WIDTH, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black')
  ax.text(-ARROW_LENGTH, 0.07, r'$\it{F}$', fontsize=18, ha='left', va='bottom', fontfamily='times new roman', math_fontfamily='dejavuserif')
  ax.text(-ARROW_LENGTH, -A_width-0.07, r'$\it{F}$', fontsize=18, ha='left', va='top', fontfamily='times new roman', math_fontfamily='dejavuserif')

  # Draw 90 degree angle square at A
  ax.plot([-BOX_SIZE, 0], [-BOX_SIZE, -BOX_SIZE], color='black', linewidth=LINE_WIDTH)
  ax.plot([-BOX_SIZE, -BOX_SIZE], [-BOX_SIZE, 0], color='black', linewidth=LINE_WIDTH)

  # Draw force couple at B
  arrow_offset_x = (ARROW_LENGTH+ARROW_HEAD_LENGTH+ARROW_SPACING)*np.sin(np.radians(force_angle))
  arrow_offset_y = (ARROW_LENGTH+ARROW_HEAD_LENGTH+ARROW_SPACING)*np.cos(np.radians(force_angle))
  arrow_length_x = ARROW_LENGTH*np.sin(np.radians(force_angle))
  arrow_length_y = ARROW_LENGTH*np.cos(np.radians(force_angle))
    # Force couple vector arrows
  ax.arrow(BAR_LENGTH-B_width-arrow_offset_x, -BAR_HEIGHT-arrow_offset_y, arrow_length_x, arrow_length_y, width=ARROW_WIDTH, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black')
  ax.arrow(BAR_LENGTH+arrow_offset_x, -BAR_HEIGHT+arrow_offset_y, -arrow_length_x, -arrow_length_y, width=ARROW_WIDTH, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black')
    # Angle arcs
  ax.add_patch(Arc((BAR_LENGTH, -BAR_HEIGHT), ARC_DIAMETER, ARC_DIAMETER, angle=90-force_angle, theta1=0, theta2=force_angle, color='black'))
  ax.add_patch(Arc((BAR_LENGTH-B_width, -BAR_HEIGHT), ARC_DIAMETER, ARC_DIAMETER, angle=270-force_angle, theta1=0, theta2=force_angle, color='black'))
    # Force labels
  ax.text(BAR_LENGTH-B_width-arrow_offset_x, -BAR_HEIGHT-arrow_offset_y, f'{force_B} N', fontsize=18, ha='right', va='bottom', fontfamily='times new roman', math_fontfamily='dejavuserif')
  ax.text(BAR_LENGTH+arrow_offset_x, -BAR_HEIGHT+arrow_offset_y, f'{force_B} N', fontsize=18, ha='left', va='top', fontfamily='times new roman', math_fontfamily='dejavuserif')
    # Angle labels
  text_radius = ARC_DIAMETER*0.9
  text_offset_x = text_radius*np.sin(np.radians(force_angle/2))
  text_offset_y = text_radius*np.cos(np.radians(force_angle/2))

  ax.text(BAR_LENGTH-B_width-text_offset_x, -BAR_HEIGHT-text_offset_y, f'{force_angle_label}', fontsize=18, ha='center', va='center', fontfamily='times new roman')
  ax.text(BAR_LENGTH+text_offset_x, -BAR_HEIGHT+text_offset_y, f'{force_angle_label}', fontsize=18, ha='center', va='center', fontfamily='times new roman')
  return fig, ax

if __name__ == "__main__":
  fig, ax = generate_figure(0.25, 0.2, 20, 10)
  plt.savefig("q18.png", dpi=300, bbox_inches='tight')
  plt.show()