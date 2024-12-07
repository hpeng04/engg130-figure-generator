import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.patches import Polygon
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
import numpy as np
import math

def generate_figure(length_BO, length_OC, height):
  # Define constants
  BAR_WIDTH = 0.7
  DIST_BC = 15
  FRAME_EXTENSION = 0.5
  MAX_FRAME_HEIGHT = 8
  SPRING_LENGTH = 3
  SPRING_AMP = 0.3
  WEIGHT_WIDTH = 2.5
  WEIGHT_HEIGHT = 2
  ARROW_HEAD_WIDTH = 0.25
  ARROW_HEAD_LENGTH = 0.25
  line_width = 2
  CIRCLE_RADIUS = 0.25


  label_BO = length_BO
  label_OC = length_OC
  label_height = height

  total_width = length_BO+length_OC
  height_ratio = height/total_width

  if (length_BO/total_width < 0.3):
    length_BO = 0.3*total_width
  elif (length_BO/total_width > 0.7):
    length_BO = 0.7*total_width
  if (length_OC/total_width < 0.3):
    length_OC = 0.3*total_width
  elif (length_OC/total_width > 0.7):
    length_OC = 0.7*total_width
  # if (height_ratio < 0.1):
  #   height_ratio = 0.005*total_width
  # elif (height_ratio > 0.8):
  #   height_ratio = 0.1*total_width

  height = height_ratio*DIST_BC

  if height > MAX_FRAME_HEIGHT:
    height = MAX_FRAME_HEIGHT
  elif height < 1.7:
    height = 1.7

  total_width = length_BO + length_OC
  length_BO = DIST_BC*length_BO/total_width
  length_OC = DIST_BC*length_OC/total_width
  total_width = DIST_BC

  # Set up the figure and axis
  fig, ax = plt.subplots(figsize=(10, 5))
  ax.set_aspect('equal')
  # ax.set_xlim(-FRAME_EXTENSION, DIST_BC+FRAME_EXTENSION)
  # ax.set_ylim(-height-5, 2)
  ax.axis('off')

  # Draw ceiling
  ax.add_patch(Rectangle((-FRAME_EXTENSION, 0), DIST_BC+2*FRAME_EXTENSION, BAR_WIDTH, facecolor='none', edgecolor='black', linewidth=0, hatch='/////', zorder=1))
  ax.plot([-FRAME_EXTENSION, DIST_BC+FRAME_EXTENSION], [0, 0], color='black', linewidth=line_width)

  # Draw spring
  def draw_spring(ax, start, end, amplitude):
    NUM_COILS = 7
    
    # Unpack start and end coordinates
    x1, y1 = start
    x2, y2 = end

    # Calculate the direction and distance
    angle = np.arctan2(y2 - y1, x2 - x1)

    x2 = np.sqrt((x2-x1)**2 + (y2-y1)**2) + x1


    # Create an array of x-coordinates
    x = np.linspace(x1, x2, num=2*NUM_COILS+1)

    

    # Create the y-offsets
    spring_offsets = np.zeros_like(x)
    spring_offsets[1::2] = -amplitude
    spring_offsets[2::2] = amplitude
    spring_offsets[-1] = 0

    # Rotate the spring points back to the line direction
    dx = x - x1
    dy = spring_offsets
    rotated_x = dx * np.cos(angle) - dy * np.sin(angle)
    rotated_y = dx * np.sin(angle) + dy * np.cos(angle)

    # Add the offsets to the start point
    spring_x = rotated_x + x1
    spring_y = rotated_y + y1

    ax.plot(spring_x, spring_y, color='black', linewidth=2)

    return ax
  
  # Draw connector ring
  ax.add_patch(Circle((length_BO, -height), CIRCLE_RADIUS, facecolor='none', linewidth=1, edgecolor='black'))

  # Draw BA rope + spring
  length_BA = np.sqrt(length_BO**2 + height**2)
  x1 = 0
  y1 = 0
  x2 = (length_BA/2-SPRING_LENGTH/2)*np.cos(np.arctan(height/length_BO))
  y2 = -(length_BA/2-SPRING_LENGTH/2)*np.sin(np.arctan(height/length_BO))
  ax.plot([x1, x2], [y1, y2], color='black', linewidth=line_width)
  x3 = x2 + SPRING_LENGTH*np.cos(np.arctan(height/length_BO))
  y3 = y2 - SPRING_LENGTH*np.sin(np.arctan(height/length_BO))
  draw_spring(ax, (x2,y2), (x3,y3), SPRING_AMP)
  x4 = length_BO - CIRCLE_RADIUS/2
  y4 = -height + CIRCLE_RADIUS/2
  TEXT_OFFSET_X = (x2+x3)/2-0.6
  TEXT_OFFSET_Y = (y2+y3)/2-0.6
  ax.text(TEXT_OFFSET_X, TEXT_OFFSET_Y, 'k', fontsize=18, ha='center', va='center', fontfamily='times new roman')
  ax.plot([x3, x4], [y3, y4], color='black', linewidth=line_width)

  # Draw AC rope + spring
  length_AC = np.sqrt(length_OC**2 + height**2)
  x1 = DIST_BC
  y1 = 0
  x2 = DIST_BC - ((length_AC/2)-SPRING_LENGTH/2)*np.cos(np.arctan(height/length_OC))
  y2 = -(length_AC/2-SPRING_LENGTH/2)*np.sin(np.arctan(height/length_OC))
  ax.plot([x1, x2], [y1, y2], color='black', linewidth=line_width)
  x3 = x2 - SPRING_LENGTH*np.cos(np.arctan(height/length_OC))
  y3 = y2 - SPRING_LENGTH*np.sin(np.arctan(height/length_OC))
  draw_spring(ax, (x2,y2), (x3,y3), SPRING_AMP)
  x4 = length_BO + CIRCLE_RADIUS/2
  y4 = -height + CIRCLE_RADIUS/2
  TEXT_OFFSET_X = (x2+x3)/2+0.6
  TEXT_OFFSET_Y = (y2+y3)/2-0.6
  ax.text(TEXT_OFFSET_X, TEXT_OFFSET_Y, 'k', fontsize=18, ha='center', va='center', fontfamily='times new roman')
  ax.plot([x3, x4], [y3, y4], color='black', linewidth=line_width)
  
  # Draw weight
  WEIGHT_OFFSET_Y = -height - 1.5
  ax.plot([length_BO, length_BO], [-height - CIRCLE_RADIUS/2, WEIGHT_OFFSET_Y], color='black', linewidth=line_width)
  ax.add_patch(Rectangle((length_BO - WEIGHT_WIDTH/2, WEIGHT_OFFSET_Y-WEIGHT_HEIGHT), WEIGHT_WIDTH, WEIGHT_HEIGHT, facecolor='lightgray', edgecolor='black', linewidth=1, zorder=1))
  ax.text(length_BO, WEIGHT_OFFSET_Y-WEIGHT_HEIGHT/2, 'w', fontsize=18, ha='center', va='center', fontfamily='times new roman')

  # Draw point labels
  ax.text(0, -0.5, 'B', fontsize=18, ha='center', va='top', fontfamily='times new roman')
  ax.text(DIST_BC, -0.5, 'C', fontsize=18, ha='center', va='top', fontfamily='times new roman')
  ax.text(length_BO-0.5, -height-0.2, 'A', fontsize=18, ha='right', va='center', fontfamily='times new roman')

  # Draw distance markers
  MARKER_OFFSET = 0.4
  # BO
  ax.plot([0, 0], [BAR_WIDTH+MARKER_OFFSET, 1+BAR_WIDTH+MARKER_OFFSET], color='black', linewidth=1)
  ax.plot([length_BO, length_BO], [BAR_WIDTH+MARKER_OFFSET, 1+BAR_WIDTH+MARKER_OFFSET], color='black', linewidth=1)
  ax.arrow(0, BAR_WIDTH+MARKER_OFFSET+1/2, length_BO-ARROW_HEAD_LENGTH, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, color='black')
  ax.arrow(length_BO, BAR_WIDTH+MARKER_OFFSET+1/2, -length_BO+ARROW_HEAD_LENGTH, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, color='black')
  ax.text(length_BO/2, BAR_WIDTH+MARKER_OFFSET+1/2, f'{label_BO} m', fontsize=18, ha='center', va='bottom', fontfamily='times new roman')

  # OC
  ax.plot([DIST_BC, DIST_BC], [BAR_WIDTH+MARKER_OFFSET, 1+BAR_WIDTH+MARKER_OFFSET], color='black', linewidth=1)
  ax.arrow(DIST_BC, BAR_WIDTH+MARKER_OFFSET+1/2, -length_OC+ARROW_HEAD_LENGTH, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, color='black')
  ax.arrow(length_BO, BAR_WIDTH+MARKER_OFFSET+1/2, length_OC-ARROW_HEAD_LENGTH, 0, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, color='black')
  ax.text(length_BO+(length_OC)/2, BAR_WIDTH+MARKER_OFFSET+1/2, f'{label_OC} m', fontsize=18, ha='center', va='bottom', fontfamily='times new roman')

  # Height
  ax.plot([DIST_BC + FRAME_EXTENSION + MARKER_OFFSET, DIST_BC + FRAME_EXTENSION + MARKER_OFFSET + 1], [0, 0], color='black', linewidth=1)
  ax.plot([DIST_BC + FRAME_EXTENSION + MARKER_OFFSET, DIST_BC + FRAME_EXTENSION + MARKER_OFFSET + 1], [-height, -height], color='black', linewidth=1)
  ax.arrow(DIST_BC + FRAME_EXTENSION + MARKER_OFFSET + 1/2, 0, 0, -height+ARROW_HEAD_LENGTH, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, color='black')
  ax.arrow(DIST_BC + FRAME_EXTENSION + MARKER_OFFSET + 1/2, -height, 0, height-ARROW_HEAD_LENGTH, head_width=ARROW_HEAD_WIDTH, head_length=ARROW_HEAD_LENGTH, color='black')
  ax.text(DIST_BC + FRAME_EXTENSION + MARKER_OFFSET + 0.7, -height/2, f'{label_height} m', fontsize=18, ha='left', va='center', fontfamily='times new roman')

  return fig, ax

if __name__ == "__main__":
  fig, ax = generate_figure(40, 40, 300)
  plt.savefig("q16.png", dpi=300, bbox_inches='tight')
  plt.show()