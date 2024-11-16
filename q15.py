import matplotlib.pyplot as plt
from matplotlib.patches import Arc
from matplotlib.patches import Polygon
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
import numpy as np
import math



def generate_figure(length_AC, length_CB, height_AD, force_B, moment_C):

  def doublearrow(ax, x, y, dx, dy, head_width=0.3, head_length=0.3):
    angle = math.degrees(math.atan2(dy, dx))
    ax.arrow(x, y, dx-math.cos(math.radians(angle))*head_length, dy-math.sin(math.radians(angle))*head_length, head_width=head_width, head_length=head_length, color='black')
    ax.arrow(x+dx, y+dy, -dx+math.cos(math.radians(angle))*head_length, -dy+math.sin(math.radians(angle))*head_length, head_width=head_width, head_length=head_length, color='black')
    return ax
  
  def circarrow(ax, diameter, x, y, angle, theta1, theta2, head_width=0.3, head_length=0.3):
    ax.add_patch(Arc((x, y), diameter, diameter, angle=angle, theta1=theta1, theta2=theta2, color='black', linewidth=2))
    arrowX = diameter/2*np.cos(np.radians(angle))
    arrowY = diameter/2*np.sin(np.radians(angle))
    arrowdX = 0.000001*diameter/2*np.sin(np.radians(angle))
    arrowdY = -0.000001*diameter/2*np.cos(np.radians(angle))
    ax.arrow(x+arrowX, y+arrowY, arrowdX, arrowdY, head_width=head_width, head_length=head_length, color='black')
    return ax
  
  # Define constants
  BAR_WIDTH = 0.5
  arrow_head_width = 0.3 
  arrow_head_length = 0.4 
  triangle_width = 1
  line_width = 1
  circle_radius = BAR_WIDTH/2+0.05
  triangle_height = 1

  label_AC = length_AC
  label_CB = length_CB
  label_AD = height_AD

  total_width = length_AC + length_CB

  if (length_AC/total_width < 0.15):
    length_AC = 0.15*total_width
  elif (length_AC/total_width > 0.85):
    length_AC = 0.85*total_width
  if (height_AD/total_width < 0.10):
    height_AD = 1
  elif (height_AD/total_width > 0.7):
    height_AD = 0.7*total_width
  if (length_CB/total_width < 0.15):
    length_CB = 0.15*total_width
  elif (length_CB/total_width > 0.85):
    length_CB = 0.85*total_width
  
  total_width = length_AC + length_CB
  length_AC = 15*length_AC/total_width
  height_AD = 15*height_AD/total_width
  length_CB = 15*length_CB/total_width
  total_width = 15

  # Set up the figure and axis
  fig, ax = plt.subplots(figsize=(10, 5))
  ax.set_aspect('equal')
  ax.set_xlim(-5, 18)
  ax.set_ylim(-3-height_AD, 5)
  ax.axis('off')

  # Bar AB (includes AC and CB)
  ax.add_patch(Rectangle((0, -BAR_WIDTH/2), total_width, BAR_WIDTH, facecolor='lightgrey', edgecolor='black', linewidth=line_width))

  # Bar DC
  angle = math.degrees(math.atan(height_AD/length_AC))
  length_DC = math.sqrt(length_AC**2 + height_AD**2)
  ax.add_patch(Rectangle((0, -height_AD), length_DC, BAR_WIDTH*0.7, facecolor='black', edgecolor='black', linewidth=line_width, angle=angle))

  # Support at left end
  height_offset = height_AD - 0.7*BAR_WIDTH*math.sin(math.radians(angle))
  ax.add_patch(Polygon([[-triangle_height, triangle_width/2], [0,0], [-triangle_height, -triangle_width/2]], closed=True, facecolor='grey', edgecolor='black', linewidth=line_width))
  ax.add_patch(Rectangle([-triangle_height-0.3, -triangle_width/2-0.3], 0.3, triangle_width+0.6, facecolor='white', edgecolor='black', linewidth=line_width, hatch='////////'))
  ax.add_patch(Polygon([[-triangle_height, triangle_width/2-height_offset], [0,-height_offset], [-triangle_height, -triangle_width/2-height_offset]], closed=True, facecolor='grey', edgecolor='black', linewidth=line_width))
  ax.add_patch(Rectangle([-triangle_height-0.3, -triangle_width/2-0.3-height_offset], 0.3, triangle_width+0.6, facecolor='white', edgecolor='black', linewidth=line_width, hatch='////////'))

  # Joints
  ax.add_patch(Circle((length_AC-0.7*BAR_WIDTH*math.sin(math.radians(angle)), 0), circle_radius, facecolor='white', edgecolor='black', linewidth=line_width))
  ax.add_patch(Circle((0, -height_AD+0.7*BAR_WIDTH*math.sin(math.radians(angle))), circle_radius, facecolor='white', edgecolor='black', linewidth=line_width))

  # Forces
  ax.arrow(total_width, BAR_WIDTH/2+1.5+arrow_head_length+0.1, 0, -1.5, head_width=arrow_head_width, head_length=arrow_head_length, width=0.05, color='black')
  ax.text(total_width+arrow_head_width, BAR_WIDTH/2+1.8, f'{force_B} kN', fontsize=18, ha='left', va='center', color='black', fontfamily='times new roman')
  circarrow(ax, 3, total_width, -BAR_WIDTH/2, 240, 0, 200, head_width=arrow_head_width, head_length=arrow_head_length)
  ax.text(total_width, -BAR_WIDTH/2-3/2-1, f'{moment_C} kN$\u22C5$m', fontsize=18, ha='center', va='center', color='black', fontfamily='times new roman')
  
  # Labels
  ax.text(0.2, BAR_WIDTH/2+0.5, 'A', fontsize=22, ha='center', va='center', color='black', fontfamily='times new roman', weight='bold')
  ax.text(length_AC, BAR_WIDTH/2+0.5, 'C', fontsize=22, ha='center', va='center', color='black', fontfamily='times new roman', weight='bold')
  ax.text(total_width, -BAR_WIDTH/2-0.8, 'B', fontsize=22, ha='center', va='center', color='black', fontfamily='times new roman', weight='bold')

  # Distance markers
  AC_offset = length_AC-0.7*BAR_WIDTH*math.sin(math.radians(angle))
  vert_offset = arrow_head_length+0.2
  ax.plot([0, 0], [2+vert_offset, 3+vert_offset], color='black', linewidth=line_width)
  doublearrow(ax, 0, 2.5+vert_offset, AC_offset, 0, head_width=arrow_head_width, head_length=arrow_head_length)
  ax.text(AC_offset/2, 3+vert_offset, f'{label_AC} m', fontsize=18, ha='center', va='bottom', color='black', fontfamily='times new roman')
  ax.plot([AC_offset, AC_offset], [2+vert_offset, 3+vert_offset], color='black', linewidth=line_width)
  doublearrow(ax, AC_offset, 2.5+vert_offset, total_width-AC_offset, 0, head_width=arrow_head_width, head_length=arrow_head_length)
  ax.text(AC_offset+(total_width-AC_offset)/2, 3+vert_offset, f'{label_CB} m', fontsize=18, ha='center', va='bottom', color='black', fontfamily='times new roman')
  ax.plot([total_width, total_width], [2+vert_offset, 3+vert_offset], color='black', linewidth=line_width)

  ax.plot([-triangle_height-1, -triangle_height-2], [0, 0], color='black', linewidth=line_width)
  doublearrow(ax, -triangle_height-1.5, 0, 0, -height_AD, head_width=arrow_head_width, head_length=arrow_head_length)
  ax.text(-triangle_height-2, -height_AD/2, f'{label_AD} m', fontsize=18, ha='right', va='center', color='black', fontfamily='times new roman')
  ax.plot([-triangle_height-1, -triangle_height-2], [-height_AD, -height_AD], color='black', linewidth=line_width)
  
  

  return fig, ax

if __name__ == "__main__":
  fig, ax = generate_figure(1,1,1,800,400)
  plt.savefig("q15.png", dpi=300, bbox_inches='tight')
  plt.show()
