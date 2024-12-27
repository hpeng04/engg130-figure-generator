import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Arc, Circle, Polygon, PathPatch
import matplotlib.path as mpath
import numpy as np
import math

# Limits: angles between 0 and 90 degrees exclusive

def generate_figure(angle_A, angle_B, force):
  
  # Define constants
  LINE_WIDTH = 1.5
  FRAME_WIDTH = 3
  TRIANGLE_HEIGHT = 0.5
  TRIANGLE_WIDTH = 0.5
  ARROW_HEAD_LENGTH = 0.08
  ARROW_HEAD_WIDTH = 0.08
  PULLEY_RADIUS = 0.6
  ARC_DIAMETER = PULLEY_RADIUS*2
  ARROW_LENGTH = 1 - ARROW_HEAD_LENGTH
  ARROW_WIDTH = 0.1 * ARROW_HEAD_WIDTH
  PULLEY_Y_OFFSET = 0.8
  ANGLE_DIAMETER = 2.7

  # Set angle constraints
  angle_A_label = angle_A
  angle_B_label = angle_B

  MIN_ANGLE = 20
  MAX_ANGLE = 70

  if angle_A < MIN_ANGLE:
    angle_A = MIN_ANGLE
  elif angle_A > MAX_ANGLE:
    angle_A = MAX_ANGLE
  if angle_B < MIN_ANGLE:
    angle_B = MIN_ANGLE
  elif angle_B > MAX_ANGLE:
    angle_B = MAX_ANGLE

  anchor_y_offset = 2.5
  if (angle_B > 40):
    anchor_y_offset = 2
  if (angle_B > 50):
    anchor_y_offset = 1.5
  if (angle_B > 60):
    anchor_y_offset = 1
  pulley_x_offset = np.tan(np.radians(angle_B))*(anchor_y_offset-PULLEY_Y_OFFSET+PULLEY_RADIUS*np.sin(np.radians(angle_B))) + PULLEY_RADIUS*np.cos(np.radians(angle_B)) + TRIANGLE_HEIGHT
  ROPE_COLOR = '#505050'


  # Set up the figure and axis
  fig, ax = plt.subplots(figsize=(7, 7))
  ax.set_aspect('equal')
  # ax.set_xlim(-1, 6)
  # ax.set_ylim(-5, 1)
  ax.axis('off')

  # Draw the frame
  ax.plot([0, -pulley_x_offset-2], [0,0], color='black', linewidth=FRAME_WIDTH, zorder=10)
  ax.plot([0,0], [0, -anchor_y_offset-1.0], color='black', linewidth=FRAME_WIDTH, zorder=10)

  # Draw directions
  ax.arrow(-pulley_x_offset-2, -anchor_y_offset-1.0, 0.5, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH, zorder=10)
  ax.text(-pulley_x_offset-2+ARROW_HEAD_WIDTH, -anchor_y_offset-1+0.5, r'$\it{y}$', fontsize=18, ha='left', va='center', math_fontfamily='cm')
  ax.arrow(-pulley_x_offset-2, -anchor_y_offset-1.0, 0, 0.5, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH, zorder=10)
  ax.text(-pulley_x_offset-2+0.5+ARROW_HEAD_LENGTH, -anchor_y_offset-1, r'$\it{x}$', fontsize=18, ha='left', va='center', math_fontfamily='cm')


  # Draw pulley
  BASE_WIDTH = 0.6
  TOP_WIDTH = 0.3
  SUPPORT_BOTTOM = -PULLEY_Y_OFFSET-0.15

  ax.add_patch(Circle((-pulley_x_offset, -PULLEY_Y_OFFSET), PULLEY_RADIUS, edgecolor='black', facecolor='lightgray', linewidth=LINE_WIDTH))
  ax.add_patch(Circle((-pulley_x_offset, -PULLEY_Y_OFFSET), PULLEY_RADIUS-0.08, edgecolor='black', facecolor='lightgray', linewidth=LINE_WIDTH))


  ax.plot([-pulley_x_offset+BASE_WIDTH/2, -pulley_x_offset+TOP_WIDTH/2], [0, SUPPORT_BOTTOM], color='black', linewidth=FRAME_WIDTH*0.6, zorder=10)
  ax.plot([-pulley_x_offset-BASE_WIDTH/2, -pulley_x_offset-TOP_WIDTH/2], [0, SUPPORT_BOTTOM], color='black', linewidth=FRAME_WIDTH*0.6, zorder=10)
  ax.plot([-pulley_x_offset+TOP_WIDTH/2, -pulley_x_offset-TOP_WIDTH/2], [SUPPORT_BOTTOM, SUPPORT_BOTTOM], color='black', linewidth=FRAME_WIDTH*0.6, zorder=10)
  ax.fill(
  [-pulley_x_offset-BASE_WIDTH/2, -pulley_x_offset+BASE_WIDTH/2, -pulley_x_offset+TOP_WIDTH/2, -pulley_x_offset-TOP_WIDTH/2], 
  [0, 0, SUPPORT_BOTTOM, SUPPORT_BOTTOM], 
  color='lightgray', zorder=9
  )
  ax.add_patch(Circle((-pulley_x_offset, -PULLEY_Y_OFFSET), 0.05, edgecolor='white', facecolor='black', linewidth=LINE_WIDTH*0.6, zorder=10))

  ax.text(-pulley_x_offset, -PULLEY_Y_OFFSET-0.3, r'$\it{A}$', fontsize=18, ha='right', va='center', math_fontfamily='cm')

  # Draw rope
  ROPE_EXTENSION = 1.2
  rope_arc_start_x = -np.tan(np.radians(angle_B))*(anchor_y_offset - PULLEY_Y_OFFSET + PULLEY_RADIUS*np.sin(np.radians(angle_B))) - TRIANGLE_HEIGHT
  rope_arc_start_y = -PULLEY_Y_OFFSET + PULLEY_RADIUS*np.sin(np.radians(angle_B))
  rope_arc_end_x = -pulley_x_offset - PULLEY_RADIUS*np.cos(np.radians(angle_A))
  rope_arc_end_y = -PULLEY_Y_OFFSET + PULLEY_RADIUS*np.sin(np.radians(angle_A))
  ax.plot([rope_arc_start_x, -TRIANGLE_HEIGHT], [rope_arc_start_y, -anchor_y_offset], color=ROPE_COLOR, linewidth=FRAME_WIDTH, zorder=5)
  ax.add_patch(Arc((-pulley_x_offset, -PULLEY_Y_OFFSET), ARC_DIAMETER, ARC_DIAMETER, angle=0, theta1=angle_B, theta2=180-angle_A, color=ROPE_COLOR, linewidth=FRAME_WIDTH, zorder=5))
  ax.plot([rope_arc_end_x, rope_arc_end_x-ROPE_EXTENSION*np.sin(np.radians(angle_A))], [rope_arc_end_y, rope_arc_end_y-ROPE_EXTENSION*np.cos(np.radians(angle_A))], color=ROPE_COLOR, linewidth=FRAME_WIDTH, zorder=5)

  # Draw force vector
  arrow_start_x = rope_arc_end_x - 1.05 * ROPE_EXTENSION * np.sin(np.radians(angle_A))
  arrow_start_y = rope_arc_end_y - 1.05 * ROPE_EXTENSION * np.cos(np.radians(angle_A))
  arrow_end_x = arrow_start_x - ARROW_LENGTH * np.sin(np.radians(angle_A))
  arrow_end_y = arrow_start_y - ARROW_LENGTH * np.cos(np.radians(angle_A))

  ax.arrow(arrow_start_x, arrow_start_y, arrow_end_x - arrow_start_x, arrow_end_y - arrow_start_y,
           head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, fc='black', ec='black', linewidth=LINE_WIDTH, zorder=6)
  ax.text(arrow_end_x, arrow_end_y-0.1, f'{force} N', fontsize=18, ha='right', va='top', color='black', fontfamily='times new roman', math_fontfamily='dejavuserif')

  # Draw angles
  y_distance = anchor_y_offset - PULLEY_Y_OFFSET + PULLEY_RADIUS*np.sin(np.radians(angle_B))
  x_distance = PULLEY_RADIUS*np.cos(np.radians(angle_B))
  text_x_offset_B = np.tan(np.radians(angle_B/2))*(1) - pulley_x_offset + PULLEY_RADIUS
  text_x_offset_A = -np.tan(np.radians(angle_A/2))*(1) - pulley_x_offset - PULLEY_RADIUS
  Path = mpath.Path
  ax.plot([rope_arc_start_x, rope_arc_start_x], [-PULLEY_Y_OFFSET-0.7, -PULLEY_Y_OFFSET-1.5], color='black', linewidth=LINE_WIDTH)
  ax.add_patch(Arc((rope_arc_start_x, rope_arc_start_y), ANGLE_DIAMETER, ANGLE_DIAMETER, angle=270, theta1=0, theta2=angle_B, color='black', linewidth=LINE_WIDTH))
  ax.text(text_x_offset_B, rope_arc_start_y-ANGLE_DIAMETER/2-0.1, f'{angle_B_label}\u00b0', fontsize=18, ha='center', va='top', fontfamily='times new roman', math_fontfamily='cm')

  ax.plot([rope_arc_end_x, rope_arc_end_x], [-PULLEY_Y_OFFSET-0.7, -PULLEY_Y_OFFSET-1.5], color='black', linewidth=LINE_WIDTH)
  ax.add_patch(Arc((rope_arc_end_x, rope_arc_end_y), ANGLE_DIAMETER, ANGLE_DIAMETER, angle=270-angle_A, theta1=0, theta2=angle_A, color='black', linewidth=LINE_WIDTH))
  ax.text(text_x_offset_A, rope_arc_end_y-ANGLE_DIAMETER/2-0.1, f'{angle_A_label}\u00b0', fontsize=18, ha='center', va='top', fontfamily='times new roman')

  # Draw right triangle support anchor
  ax.add_patch(Polygon([[0, -anchor_y_offset-TRIANGLE_WIDTH/2], [-TRIANGLE_HEIGHT, -anchor_y_offset], [0, -anchor_y_offset+TRIANGLE_WIDTH/2]], closed=True, edgecolor='black', facecolor='gray', linewidth=LINE_WIDTH))
  ax.add_patch(Circle((-TRIANGLE_HEIGHT, -anchor_y_offset), 0.05, edgecolor='white', facecolor='black', linewidth=LINE_WIDTH*0.6, zorder=7))



  return fig, ax


if __name__ == "__main__":
  fig, ax = generate_figure(25, 3, 500)
  plt.savefig("q22.png", dpi=300, bbox_inches='tight')
  plt.show()