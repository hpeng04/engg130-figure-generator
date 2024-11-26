import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
import numpy as np

# Limits: angle between 10 and 70 degrees

def generate_figure(angle_A, angle_B):
  # Define constants
  BAR_WIDTH = 0.4
  BAR_EXTENSION = 1
  AB_DIST = 15
  LINE_WIDTH = 1
  CIRCLE_RADIUS = 0.15
  ARC_DIAMETER = 4
  TEXT_RADIUS = ARC_DIAMETER*0.9

  angle_A_label = f'{angle_A}°'
  angle_B_label = f'{angle_B}°'

  # if (angle_A) < 20:
  #   angle_A = 20
  # if (angle_B < 20):
  #   angle_B = 20

  # Set up the figure and axis
  fig, ax = plt.subplots(figsize=(10, 5))
  ax.set_aspect('equal')
  # ax.set_xlim(-1, AB_DIST+1)
  # ax.set_ylim(-17, 1)
  ax.axis('off')
  
  # Draw bar
  ax.plot([-BAR_EXTENSION, AB_DIST+BAR_EXTENSION], [0, 0], color='black', linewidth=LINE_WIDTH)
  ax.add_patch(Rectangle((-BAR_EXTENSION, 0), AB_DIST+2*BAR_EXTENSION, BAR_WIDTH, facecolor='none', edgecolor='black', linewidth=0, hatch='////'))
  
  # Draw point A
  ax.add_patch(Circle((0, 0), CIRCLE_RADIUS, color='black', zorder=2))
  ax.text(0, -0.2, 'A', fontsize=18, ha='right', va='top', fontfamily='times new roman', weight='bold')

  # Draw point B
  ax.add_patch(Circle((AB_DIST, 0), CIRCLE_RADIUS, color='black', zorder=2))
  ax.text(AB_DIST, -0.2, 'B', fontsize=18, ha='left', va='top', fontfamily='times new roman', weight='bold')

  # Draw point C
  angle_C = 180 - angle_A - angle_B
  C_OFFSET_X = ((np.sin(np.radians(angle_B)) * AB_DIST) / np.sin(np.radians(angle_C))) * np.cos(np.radians(angle_A))
  C_OFFSET_Y = -np.tan(np.radians(angle_A)) * C_OFFSET_X
  ax.add_patch(Circle((C_OFFSET_X, C_OFFSET_Y), CIRCLE_RADIUS, color='black', zorder=2))
  ax.text(C_OFFSET_X+0.2, C_OFFSET_Y-0.2, 'C', fontsize=18, ha='left', va='top', fontfamily='times new roman', weight='bold')
  
  # Draw lines AC and BC
  ax.plot([0, C_OFFSET_X], [0, C_OFFSET_Y], color='black', linewidth=LINE_WIDTH)
  ax.plot([AB_DIST, C_OFFSET_X], [0, C_OFFSET_Y], color='black', linewidth=LINE_WIDTH)
  
  # Draw angle A
  ax.add_patch(Arc((0, 0), ARC_DIAMETER, ARC_DIAMETER, angle=-angle_A, theta1=0, theta2=angle_A, color='black', linewidth=LINE_WIDTH))
  # Draw angle B
  ax.add_patch(Arc((AB_DIST, 0), ARC_DIAMETER, ARC_DIAMETER, angle=angle_B, theta1=180-angle_B, theta2=180, color='black', linewidth=LINE_WIDTH))
  
  # Annotate angles
  if (angle_B < 20 or angle_A < 20):
    ax.text(AB_DIST-ARC_DIAMETER/2, BAR_WIDTH+0.1, angle_B_label, fontsize=18, ha='center', va='bottom', fontfamily='times new roman', math_fontfamily='cm')
    ax.text(ARC_DIAMETER/2, BAR_WIDTH+0.1, angle_A_label, fontsize=18, ha='center', va='bottom', fontfamily='times new roman', math_fontfamily='cm')
  if (angle_B >= 20 and angle_A >= 20):
    ax.text(AB_DIST-TEXT_RADIUS*np.cos(np.radians(angle_B/2)), -TEXT_RADIUS*np.sin(np.radians(angle_B/2)), angle_B_label, fontsize=18, ha='center', va='center', fontfamily='times new roman', math_fontfamily='cm')
    ax.text(TEXT_RADIUS*np.cos(np.radians(angle_A/2)), -TEXT_RADIUS*np.sin(np.radians(angle_A/2)), angle_A_label, fontsize=18, ha='center', va='center', fontfamily='times new roman', math_fontfamily='cm')

  # Draw force vector P
  Px = -1
  Py = -2
  ax.arrow(C_OFFSET_X, C_OFFSET_Y, -1, -2, head_width=0.2, head_length=0.2, fc='black', ec='black')
  ax.text(C_OFFSET_X-0.8, C_OFFSET_Y-2, r'$\vec{P}$', fontsize=18, ha='left', va='top', fontfamily='times new roman', weight='bold', math_fontfamily='stix')

  # Draw angle alpha
  alpha = np.degrees(np.arctan(Py/Px))
  ax.plot([C_OFFSET_X-2.5, C_OFFSET_X], [C_OFFSET_Y, C_OFFSET_Y], color='black', linewidth=LINE_WIDTH, linestyle='--')
  ax.add_patch(Arc((C_OFFSET_X, C_OFFSET_Y), ARC_DIAMETER/2, ARC_DIAMETER/2, angle=180, theta1=0, theta2=alpha, color='black', linewidth=LINE_WIDTH))
  ax.text(C_OFFSET_X+Px, C_OFFSET_Y-0.5, r'$\alpha$', fontsize=18, ha='right', va='top', fontfamily='times new roman', weight='bold', math_fontfamily='stix')

  return fig, ax

if __name__ == "__main__":
  fig, ax = generate_figure(20, 20)
  plt.savefig("q9.png", dpi=300, bbox_inches='tight')
  plt.show()