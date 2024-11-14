import matplotlib.pyplot as plt
from matplotlib.patches import Arc
import numpy as np
import math

def generate_figure(length_OA, length_AB, length_BC, angle, force):
  # Define constants
  BAR_WIDTH = 0.5
  arrow_head_width = 0.3 #0.01*(length_OA+length_AB+1.6*length_BC)
  arrow_head_length = 0.3 #0.01*(length_OA+length_AB+1.6*length_BC)
  triangle_width = 1
  line_width = 1
  circle_radius = 0.1
  triangle_height = 1.2

  label_OA = length_OA
  label_AB = length_AB
  label_BC = length_BC

  # Set limits for the lengths
  total_length = length_OA + length_AB + length_BC

  if (length_OA/total_length < 0.2):
    length_OA = 0.2*total_length
  elif (length_OA/total_length > 0.8):
    length_OA = 0.8*total_length
  if (length_AB/total_length < 0.2):
    length_AB = 0.2*total_length
  elif (length_AB/total_length > 0.8):
    length_AB = 0.8*total_length
  if (length_BC/total_length < 0.2):
    length_BC = 0.2*total_length
  elif (length_BC/total_length > 0.8):
    length_BC = 0.8*total_length
  
  total_length = length_OA + length_AB + length_BC
  length_OA = 15*length_OA/total_length
  length_AB = 15*length_AB/total_length
  length_BC = 15*length_BC/total_length
  total_length = 15
  
  # Set up the figure and axis
  fig, ax = plt.subplots(figsize=(10, 5))
  ax.set_aspect('equal')
  ax.set_xlim(-1, length_OA+length_AB+1.5*length_BC+2)
  ax.set_ylim(-5-length_BC*math.tan(math.radians(angle)), 5)
  ax.axis('off')

  ### Support at left end ###
  ax.plot([0, 0], [-1, 1], color='black', linewidth=line_width)

  # hatch marks to left of support
  for (i, x) in enumerate(np.linspace(-1+0.3, 1-line_width/100, 6)):
    ax.plot([-0.3, 0-line_width/100], [x-0.3, x], color='black', linewidth=line_width)

  # (Optional) Highlight a vertical region from x=-0.3 to x=0 with light grey
  # ax.fill_between([-0.3, 0], 0, 3, color='lightgrey')

  ### Draw bar OA extending right of support ###
  ax.plot([0, length_OA], [BAR_WIDTH/2, BAR_WIDTH/2], color='black', linewidth=line_width)
  ax.plot([0, length_OA], [-BAR_WIDTH/2, -BAR_WIDTH/2], color='black', linewidth=line_width)
  # Highlight the pipe grey
  ax.fill([0, 0, length_OA, length_OA], [-BAR_WIDTH/2, BAR_WIDTH/2, BAR_WIDTH/2, -BAR_WIDTH/2], color='lightgrey')
  
  ### Draw bar AB extending right of OA ###
  # Calculate inner and outer edge lengths
  L_inner = length_AB + length_OA 
  L_outer = length_AB +  length_OA + math.tan(math.radians(angle/2)) * BAR_WIDTH
  ax.plot([length_OA, L_outer], [BAR_WIDTH/2, BAR_WIDTH/2], color='black', linewidth=line_width) # Outer edge
  ax.plot([length_OA, L_inner], [-BAR_WIDTH/2, -BAR_WIDTH/2], color='black', linewidth=line_width) # Inner edge
  # Highlight the pipe grey
  ax.fill([length_OA, length_OA, L_outer, L_inner], [-BAR_WIDTH/2, BAR_WIDTH/2, BAR_WIDTH/2, -BAR_WIDTH/2], color='lightgrey')

  ### Draw bar BC extending right of AB and down at angle ###
  # Calculate bar length
  bar_length_BC = length_BC / math.cos(math.radians(angle))
  total_bar_length = length_BC + length_AB + length_OA
  # Calculate x and y coordinates
  x1_in = L_inner
  x1_out = L_outer
  x2_in = total_bar_length - (math.sin(math.radians(angle)) * BAR_WIDTH/2)
  x2_out = total_bar_length + (math.sin(math.radians(angle)) * BAR_WIDTH/2)
  y1_in = -BAR_WIDTH/2
  y1_out = BAR_WIDTH/2
  y2_in = -BAR_WIDTH/2 * math.cos(math.radians(angle)) - bar_length_BC * math.sin(math.radians(angle))
  y2_out = BAR_WIDTH/2 * math.cos(math.radians(angle)) - bar_length_BC * math.sin(math.radians(angle))

  ### Angle annotation between AB and BC ###
  # Write Text
  if ((angle >= 30 and angle <= 65) or (length_BC/total_length) > 0.33):
    ax.annotate(f"{angle}\u00B0", xy=(x1_out + 0.5*length_BC, -BAR_WIDTH/2*length_BC*math.sin(math.radians(angle))), fontsize=18, color="black", fontfamily='times new roman')
  elif (angle > 65):
    ax.annotate(f"{angle}\u00B0", xy=(x1_out + 0.5*length_BC, y1_in-0.1*bar_length_BC*math.sin(math.radians(angle))), fontsize=18, color="black", fontfamily='times new roman')
  else:
    ax.annotate(f"{angle}\u00B0", xy=(x1_out + 0.3*length_BC, y1_out+0.3), fontsize=18, color="black", fontfamily='times new roman')
  # Draw dashed line extending from AB outer edge
  ax.plot([x1_out, x1_out + 0.7 * length_BC], [y1_out, y1_out], linestyle="--", color="black", linewidth=line_width)
  # Draw arc
  ax.add_patch(Arc((x1_out, y1_out), 0.7*length_BC, 0.7*length_BC, angle=0, theta1=-angle, theta2=0, color="black"))
 
  # Draw the bar
  ax.plot([x1_out, x2_out], [y1_out, y2_out], color='black', linewidth=line_width) # Outer edge
  ax.plot([x1_in, x2_in], [y1_in, y2_in], color='black', linewidth=line_width) # Inner edge
  ax.plot([x2_in, x2_out], [y2_in, y2_out], color='black', linewidth=line_width) # Bottom edge
  # Highlight the pipe grey
  ax.fill([x1_in, x1_out, x2_out, x2_in], [y1_in, y1_out, y2_out, y2_in], color='lightgrey')


  ### Force vector at the end of BC ###
  # Write Theta
  if ((angle >= 30 and angle <= 65) or (length_BC/total_length) > 0.33):
    ax.annotate("\u03B8", xy=(x2_in + 0.5*length_BC, y2_in + 0.2*bar_length_BC*math.sin(math.radians(angle))), fontsize=18, color="black", fontfamily='times new roman')
  elif (angle > 65):
    ax.annotate("\u03B8", xy=(x2_out + 0.6*length_BC, y2_in + 0.2*bar_length_BC*math.sin(math.radians(angle))), fontsize=18, color="black", fontfamily='times new roman')
  else:
    ax.annotate("\u03B8", xy=(x2_out + 0.5*bar_length_BC+0.3, y2_in + 0.2*bar_length_BC*math.sin(math.radians(angle))), fontsize=18, color="black", fontfamily='times new roman')
  # Draw dashed line extending from BC outer edge
  ax.plot([(x2_out+x2_in)/2, (x2_out+x2_in)/2 + 0.5*bar_length_BC], [(y2_out+y2_in)/2, (y2_out+y2_in)/2], linestyle="--", color="black", linewidth=line_width)
  # Draw arc
  ax.add_patch(Arc(((x2_out+x2_in)/2, (y2_out+y2_in)/2), 0.5*bar_length_BC, 0.5*bar_length_BC, angle=0, theta1=0, theta2=angle, color="black"))
  # Draw arrow at the end of the arc pointing in the direction of angle theta2
  ax.arrow((x2_out+x2_in)/2, (y2_out+y2_in)/2, 0.5*bar_length_BC*math.cos(math.radians(angle)), 0.5*bar_length_BC*math.sin(math.radians(angle)), head_width=arrow_head_width, head_length=arrow_head_length, color="black", linewidth=line_width)
  # Write Force at the end of arrow
  ax.text((x2_out+x2_in)/2 + 0.6*bar_length_BC*math.cos(math.radians(angle)), (y2_out+y2_in)/2 + 0.2 + 0.5*bar_length_BC*math.sin(math.radians(angle))+0.01*(length_OA+length_AB+1.6*length_BC), f"{force} N", fontsize=18, color="black", fontfamily='times new roman', ha='center')
  
  baseline = -((math.sin(math.radians(angle))*bar_length_BC)+BAR_WIDTH+0.6)
  ### Separator dashed line between OA and AB ###
  # Draw line
  ax.plot([length_OA, length_OA], [1.2*baseline, 2.2], linestyle="--", color="black", linewidth=line_width)
  # Write text
  ax.text(length_OA, 1.25*baseline-0.35, "a", fontsize=18, color="black", fontfamily='times new roman', weight='bold', ha='center')

  ### Distance measurements ###
  # Draw arrow for distance between OA
  ax.arrow(0, baseline+0.4, length_OA-arrow_head_length, 0, head_width=arrow_head_width, head_length=arrow_head_length, color="black", linewidth=line_width)
  ax.arrow(length_OA, baseline+0.4, -(length_OA-arrow_head_length), 0, head_width=arrow_head_width, head_length=arrow_head_length, color="black", linewidth=line_width)
  # Write distance text
  ax.text(length_OA/2, 1.1*baseline-0.01*(length_OA+length_AB+1.6*length_BC), f"{label_OA} m", fontsize=18, color="black", fontfamily='times new roman', ha='center')

  # Draw arrow for distance between AB
  ax.arrow(length_OA, baseline+0.4, length_AB-arrow_head_length, 0, head_width=arrow_head_width, head_length=arrow_head_length, color="black", linewidth=line_width)
  ax.arrow(length_OA+length_AB, baseline+0.4, -(length_AB-arrow_head_length), 0, head_width=arrow_head_width, head_length=arrow_head_length, color="black", linewidth=line_width)
  # Write distance text
  ax.text(length_OA+length_AB/2, 1.1*baseline-0.01*(length_OA+length_AB+1.6*length_BC), f"{label_AB} m", fontsize=18, color="black", fontfamily='times new roman', ha='center')

  # Draw arrow for distance between BC
  ax.arrow(length_OA+length_AB, baseline+0.4, length_BC-arrow_head_length, 0, head_width=arrow_head_width, head_length=arrow_head_length, color="black", linewidth=line_width)
  ax.arrow(length_OA+length_AB+length_BC, baseline+0.4, -(length_BC-arrow_head_length), 0, head_width=arrow_head_width, head_length=arrow_head_length, color="black", linewidth=line_width)
  # Write distance text
  ax.text(length_OA+length_AB+length_BC/2, 1.1*baseline-0.01*(length_OA+length_AB+1.6*length_BC), f"{label_BC} m", fontsize=18, color="black", fontfamily='times new roman', ha='center')

  # Draw tick marks for separating distances
  # offset = length_OA+length_AB+1.6*length_BC
  ax.plot([0,0], [baseline+0.2, baseline+0.6], color="black", linewidth=line_width)
  ax.plot([length_OA, length_OA], [baseline+0.2, baseline+0.6], color="black", linewidth=line_width)
  ax.plot([length_OA+length_AB, length_OA+length_AB], [baseline+0.2, baseline+0.6], color="black", linewidth=line_width)
  ax.plot([length_OA+length_AB+length_BC, length_OA+length_AB+length_BC], [baseline+0.2, baseline+0.6], color="black", linewidth=line_width)

  return fig, ax


if __name__ == "__main__":
  fig, ax = generate_figure(1, 100, 45, 30, 1500)
  plt.savefig("q4.png", dpi=300, bbox_inches='tight')
  plt.show()
