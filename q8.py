import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
import numpy as np

# Limits: angle between 10 and 75 degrees
#         mass less than 6 digits

def generate_figure(angle, mass):
  # Define constants
  BAR_WIDTH = 0.15
  LINE_WIDTH = 1
  CIRCLE_RADIUS = 1
  ARC_RADIUS = 1.5
  HATCH_OFFSET = 0.4
  
  angle_label = angle

  if (angle < 15):
    angle = 15
  elif (angle > 70):
    angle = 70

  # Set up the figure and axis
  fig, ax = plt.subplots(figsize=(10, 5))
  ax.set_aspect('equal')
  # ax.set_xlim(-10, 2)
  # ax.set_ylim(-1, 5)
  ax.axis('off')

  # Draw right wall
  ax.plot([0, 0], [0, 4], color='black', linewidth=LINE_WIDTH)
  ax.add_patch(Rectangle((0, 0), BAR_WIDTH, 4, facecolor='none', edgecolor='black', linewidth=0, hatch='////', alpha=0.7, zorder=1))

  # Draw ground
  GROUND_DISPLACEMENT = 1
  ax.plot([-GROUND_DISPLACEMENT, 0], [0, 0], color='black', linewidth=LINE_WIDTH)
  ax.plot([-4, -GROUND_DISPLACEMENT], [0, 0], color='black', linewidth=LINE_WIDTH, linestyle='--')
  
  # Draw inclined surface
  SURFACE_LENGTH = 3
  surface_length_x = SURFACE_LENGTH*np.cos(np.radians(angle))
  surface_length_y = SURFACE_LENGTH*np.sin(np.radians(angle))
  HATCH_LENGTH = SURFACE_LENGTH-0.7/surface_length_y
  ax.plot([-GROUND_DISPLACEMENT-surface_length_x, -GROUND_DISPLACEMENT], [surface_length_y, 0], color='black', linewidth=LINE_WIDTH)
  ax.add_patch(Rectangle((-GROUND_DISPLACEMENT-surface_length_x, surface_length_y), BAR_WIDTH, HATCH_LENGTH, facecolor='none', edgecolor='black', linewidth=0, hatch=r'////', angle=-angle-90, rotation_point='xy', alpha=0.7, zorder=1))
  
  # Draw angle
  # ANGLE_TEXT_OFFSET_Y = ARC_RADIUS*np.sin(np.radians(angle/2-10))
  # ANGLE_TEXT_OFFSET_X = -GROUND_DISPLACEMENT-ARC_RADIUS*np.cos(np.radians(angle/2-10))
  ANGLE_TEXT_OFFSET_Y = 0.5*SURFACE_LENGTH*np.sin(np.radians(angle/4))-0.6*HATCH_OFFSET*np.sin(np.radians(angle))
  ANGLE_TEXT_OFFSET_X = -GROUND_DISPLACEMENT-0.65*SURFACE_LENGTH*np.cos(np.radians(angle))
  ax.add_patch(Arc((-GROUND_DISPLACEMENT, 0), ARC_RADIUS, ARC_RADIUS, angle=180-angle, theta1=0, theta2=angle, color='black', linewidth=LINE_WIDTH, zorder=2))
  ax.text(ANGLE_TEXT_OFFSET_X, ANGLE_TEXT_OFFSET_Y, f'{angle_label}°', fontsize=18, ha='right', va='bottom', fontfamily='times new roman')

  # Draw circle
  CIRCLE_OFFSET_Y = CIRCLE_RADIUS/np.cos(np.radians(angle))
  CIRCLE_OFFSET_X = -CIRCLE_RADIUS
  ax.add_patch(Circle((CIRCLE_OFFSET_X, CIRCLE_OFFSET_Y), CIRCLE_RADIUS, facecolor='none', edgecolor='black', linewidth=LINE_WIDTH, zorder=2))
  ax.add_patch(Circle((CIRCLE_OFFSET_X, CIRCLE_OFFSET_Y), 0.05, facecolor='black', edgecolor='black', linewidth=LINE_WIDTH, zorder=2))
  
  # Draw labels
  # Circle mass
  ax.text(-CIRCLE_RADIUS, CIRCLE_OFFSET_Y+CIRCLE_RADIUS/4, f'm={mass}kg', fontsize=14, weight='bold', ha='center', va='bottom', fontfamily='times new roman', math_fontfamily='cm')
  # label A
  A_OFFSET_X = CIRCLE_OFFSET_X-CIRCLE_RADIUS*np.sin(np.radians(angle))*0.8
  A_OFFSET_Y = CIRCLE_OFFSET_Y-CIRCLE_RADIUS*np.cos(np.radians(angle))*0.8
  ax.text(A_OFFSET_X, A_OFFSET_Y, 'A', fontsize=18, weight='bold', ha='center', va='center', fontfamily='times new roman')
  # label B
  B_OFFSET_X = BAR_WIDTH+0.1
  B_OFFSET_Y = CIRCLE_OFFSET_Y
  ax.text(B_OFFSET_X, B_OFFSET_Y, 'B', fontsize=18, weight='bold', ha='left', va='center', fontfamily='times new roman')  
  # 90 degree angle
  ax.plot([-BAR_WIDTH, -BAR_WIDTH], [0, BAR_WIDTH], color='black', linewidth=LINE_WIDTH)
  ax.plot([-BAR_WIDTH, 0], [BAR_WIDTH, BAR_WIDTH], color='black', linewidth=LINE_WIDTH)
  # ax.add_patch(Rectangle((BOX_OFFSET_X, BOX_OFFSET_Y), BOX_SIZE, BOX_SIZE, facecolor='none', edgecolor='black', linewidth=LINE_WIDTH, zorder=2))

  return fig, ax

if __name__ == "__main__":
  fig, ax = generate_figure(70, 10)
  plt.savefig("q8.png", dpi=300, bbox_inches='tight')
  plt.show()