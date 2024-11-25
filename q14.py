import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from matplotlib.patches import Arc
from matplotlib.patches import Polygon
from matplotlib.patches import Circle
from matplotlib.patches import Rectangle
import math

from mpl_toolkits.mplot3d import Axes3D
from matplotlib.patches import FancyArrowPatch
from mpl_toolkits.mplot3d import proj3d

def generate_figure(length_X, length_Y, length_Z, Fz, Fy):

  class Arrow3D(FancyArrowPatch):
    def __init__(self, xs, ys, zs, *args, **kwargs):
      super().__init__((0,0), (0,0), *args, **kwargs)
      self._verts3d = xs, ys, zs

    def do_3d_projection(self, renderer=None):
      xs3d, ys3d, zs3d = self._verts3d
      xs, ys, zs = proj3d.proj_transform(xs3d, ys3d, zs3d, self.axes.M)
      self.set_positions((xs[0],ys[0]),(xs[1],ys[1]))

      return np.min(zs)

  # Define constants
  LINE_WIDTH = 1
  label_X = length_X
  label_Y = length_Y
  label_Z = length_Z
  ARROW_HEAD_WIDTH = 0.3
  ARROW_HEAD_LENGTH = 0.4
  
  AXIS_EXTENSION = 0.5
  MARKER_SIZE = 0.15
  MARKER_OFFSET = 0.02

  # Set max ratio
  base_dim = length_X + 2*length_Y
  if (length_X/base_dim < 0.3):
    length_X = 0.3*base_dim
  elif (length_X/base_dim > 0.7):
    length_X = 0.7*base_dim
  if (length_Y/base_dim < 0.3):
    length_Y = 0.3*base_dim
  elif (length_Y/base_dim > 0.7):
    length_Y = 0.7*base_dim
  if (length_Z/base_dim < 0.3):
    length_Z = 0.3*base_dim
  elif (length_Z/base_dim > 0.7):
    length_Z = 0.7*base_dim
  
  base_dim = length_X + length_Y
  length_X = length_X/base_dim
  length_Y = length_Y/base_dim
  length_Z = length_X/label_X*length_Z
  base_dim = length_X + length_Y

  ARROW_LENGTH = 0.8*length_Y

  # Create figure and axis
  fig = plt.figure(figsize=(10, 10))
  ax = fig.add_subplot(111, projection="3d")

  # Set view
  ax.view_init(elev=35, azim=45)
  ax.set_xlim(length_X+0.5, -0.5)
  ax.set_ylim(length_Y+0.5, -0.5-length_Y)
  ax.axis('off')

  # Define box vertices
  vertices = {
    'O': [0, 0, 0],  # O (Symbolic)
    'A': [length_X, -length_Y, 0],  # A (x-axis)
    'B': [length_X, length_Y, 0],  # B
    'C': [0, length_Y, 0],  # C
    'D': [0, -length_Y, 0],  # D
    'O_top': [0, 0, length_Z],  # O_top (Symbolic)
    'A_top': [length_X, -length_Y, length_Z],  # A_top
    'B_top': [length_X, length_Y, length_Z],  # B_top
    'C_top': [0, length_Y, length_Z],  # C_top
    'D_top': [0, -length_Y, length_Z],  # D_top
    'X_axis_start': [-AXIS_EXTENSION, 0, 0],
    'X_axis_end': [length_X+AXIS_EXTENSION, 0, 0],
    'Y_axis_start': [0, -length_Y-AXIS_EXTENSION, 0],
    'Y_axis_end': [0, length_Y+0.5*AXIS_EXTENSION, 0],
    'Z_axis_start': [0, 0, length_Z+AXIS_EXTENSION],
    'Z_axis_end': [0, 0, 0]
  }

  axes = [
    [vertices['X_axis_start'], vertices['X_axis_end']],
    [vertices['Y_axis_start'], vertices['Y_axis_end']],
    [vertices['Z_axis_start'], vertices['Z_axis_end']]
  ]

  # Faces of the box
  faces = [
    # Bottom face
    [vertices['D'], vertices['A'], vertices['B'], vertices['C']],  # Bottom face
    [vertices['D_top'], vertices['A_top'], vertices['B_top'], vertices['C_top']],  # Top face
    [vertices['D'], vertices['A'], vertices['A_top'], vertices['D_top']],  # Front face
    [vertices['B'], vertices['C'], vertices['C_top'], vertices['B_top']],  # Back face
    [vertices['A'], vertices['B'], vertices['B_top'], vertices['A_top']],  # Right face
    [vertices['D'], vertices['C'], vertices['C_top'], vertices['D_top']],  # Left face
  ]

  edges = [
    [vertices['D'], vertices['A']],
    [vertices['A'], vertices['B']],
    [vertices['B'], vertices['C']],
    [vertices['C'], vertices['D']],
    [vertices['D_top'], vertices['A_top']],
    [vertices['A_top'], vertices['B_top']],
    [vertices['B_top'], vertices['C_top']],
    [vertices['C_top'], vertices['D_top']],
    [vertices['D'], vertices['D_top']],
    [vertices['A'], vertices['A_top']],
    [vertices['B'], vertices['B_top']],
    [vertices['C'], vertices['C_top']],
  ]

  behind_edges = [ # Dashed
    [vertices['B'], vertices['C']],
    [vertices['B'], vertices['B_top']],
    [vertices['A'], vertices['B']]
  ] 

  front_edges = [e for e in edges if e not in behind_edges]  # Solid

  # Plot the faces
  for face in faces:
    face_array = np.array(face)
    ax.add_collection3d(Poly3DCollection([face_array], color="lightgray", alpha=1, edgecolor='none', linewidths=0, zorder=7))
  
  for edge in front_edges:
    start, end = edge
    x_coords = start[0], end[0]
    y_coords = start[1], end[1]
    z_coords = start[2], end[2]
    ax.plot3D(x_coords, y_coords, z_coords, color="black", linewidth=LINE_WIDTH, zorder=8)

  for edge in behind_edges:
    start, end = edge
    x_coords = start[0], end[0]
    y_coords = start[1], end[1]
    z_coords = start[2], end[2]
    ax.plot3D(x_coords, y_coords, z_coords, color="black", linewidth=LINE_WIDTH, linestyle='--', zorder=8)

  # Plot X axis
  ax.text(vertices['X_axis_start'][0]-0.06, vertices['X_axis_start'][1]-0.03, vertices['X_axis_start'][2], r"$\it{x}$", color="black", fontsize=20, math_fontfamily='cm', ha='right', fontfamily='times new roman')
  ax.plot([vertices['X_axis_start'][0], vertices['X_axis_end'][0]], [vertices['X_axis_start'][1], vertices['X_axis_end'][1]], [vertices['X_axis_start'][2], vertices['X_axis_end'][2]], color="black", linewidth=LINE_WIDTH, zorder=4)
  ax.plot([vertices['X_axis_start'][0], vertices['X_axis_end'][0]], [vertices['X_axis_start'][1], vertices['X_axis_end'][1]], [vertices['X_axis_start'][2], vertices['X_axis_end'][2]], color="black", linewidth=LINE_WIDTH, zorder=10, linestyle='-.')

  # Plot Y axis
  ax.text(vertices['Y_axis_start'][0]-0.03, vertices['Y_axis_start'][1]-0.06, vertices['Y_axis_start'][2], r"$\it{y}$", color="black", fontsize=20, math_fontfamily='cm', ha='left', fontfamily='times new roman')
  ax.plot([vertices['Y_axis_start'][0], vertices['Y_axis_end'][0]], [vertices['Y_axis_start'][1], vertices['Y_axis_end'][1]], [vertices['Y_axis_start'][2], vertices['Y_axis_end'][2]], color="black", linewidth=LINE_WIDTH, zorder=10)

  # Plot Z axis
  ax.text(vertices['Z_axis_start'][0], vertices['Z_axis_start'][1], vertices['Z_axis_start'][2]+0.05, r"$\it{z}$", color="black", fontsize=20, math_fontfamily='cm', ha='center', fontfamily='times new roman')
  ax.plot([vertices['Z_axis_start'][0], vertices['Z_axis_end'][0]], [vertices['Z_axis_start'][1], vertices['Z_axis_end'][1]], [vertices['Z_axis_start'][2], vertices['Z_axis_end'][2]], color="black", linewidth=LINE_WIDTH, zorder=10)

  # Add force vector
  # Fz
  Fz_arrow = Arrow3D([vertices['A_top'][0], vertices['A_top'][0]], [vertices['A_top'][1], vertices['A_top'][1]], [vertices['A_top'][2]+ARROW_LENGTH, vertices['A_top'][2]], mutation_scale=15, lw=2, arrowstyle="-|>", color="black", zorder=9)
  ax.add_artist(Fz_arrow)
  ax.text(vertices['A_top'][0], vertices['A_top'][1], vertices['A_top'][2]+ARROW_LENGTH, f"{Fz} N", fontsize=18, color="black", fontfamily='times new roman', ha='center', va='bottom', zorder=10)
  # Fy
  Fy_arrow = Arrow3D([vertices['A_top'][0], vertices['A_top'][0]], [vertices['A_top'][1]-ARROW_LENGTH, vertices['A_top'][1]], [vertices['A_top'][2], vertices['A_top'][2]], mutation_scale=15, lw=2, arrowstyle="-|>", color="black", zorder=9)
  ax.add_artist(Fy_arrow)
  ax.text(vertices['A_top'][0], vertices['A_top'][1]-ARROW_LENGTH/2, vertices['A_top'][2], f"{Fy} N", fontsize=18, color="black", fontfamily='times new roman', ha='left', va='bottom', zorder=10)
  # Label O
  ax.text(vertices['O'][0]-0.04, vertices['O'][1]+0.13, vertices['O'][2], r"$\it{O}$", color="black", fontsize=18, ha='right', va='top', zorder=10, fontfamily='times new roman')

  # Distance separators
  # OD
  ax.plot([vertices['C'][0]-MARKER_SIZE-MARKER_OFFSET, -MARKER_OFFSET], [vertices['C'][1], vertices['C'][1]], [vertices['C'][2], vertices['C'][2]], color="black", linewidth=LINE_WIDTH, zorder=10)
  ax.plot([vertices['D'][0]-MARKER_SIZE-MARKER_OFFSET, -MARKER_OFFSET], [vertices['D'][1], vertices['D'][1]], [vertices['D'][2], vertices['D'][2]], color="black", linewidth=LINE_WIDTH, zorder=10)
  OD_arrow = Arrow3D([vertices['O'][0]-(MARKER_SIZE)/2-MARKER_OFFSET, vertices['D'][0]-(MARKER_SIZE)/2-MARKER_OFFSET], [vertices['O'][1], vertices['D'][1]], [vertices['O'][2], vertices['D'][2]], mutation_scale=15, lw=LINE_WIDTH, arrowstyle="-|>", color="black", zorder=9)
  ax.add_artist(OD_arrow)
  DO_arrow = Arrow3D([vertices['D'][0]-(MARKER_SIZE)/2-MARKER_OFFSET, vertices['O'][0]-(MARKER_SIZE)/2-MARKER_OFFSET], [vertices['D'][1], vertices['O'][1]], [vertices['D'][2], vertices['O'][2]], mutation_scale=15, lw=LINE_WIDTH, arrowstyle="-|>", color="black", zorder=9)
  ax.add_artist(DO_arrow)
  ax.text(vertices['O'][0]-(MARKER_SIZE+MARKER_OFFSET)-0.1, vertices['O'][1]-length_Y/2, vertices['O'][2], f"{label_Y} m", color="black", fontsize=18, ha='center', va='top', zorder=10, fontfamily='times new roman')
  # DA
  ax.plot([vertices['A'][0], vertices['A'][0]], [vertices['A'][1]-MARKER_SIZE-MARKER_OFFSET, vertices['A'][1]-MARKER_OFFSET], [vertices['A'][2], vertices['A'][2]], color="black", linewidth=LINE_WIDTH, zorder=10)
  DA_arrow = Arrow3D([vertices['D'][0], vertices['A'][0]], [vertices['D'][1]-(MARKER_SIZE)/2-MARKER_OFFSET, vertices['A'][1]-(MARKER_SIZE)/2-MARKER_OFFSET], [vertices['D'][2], vertices['A'][2]], mutation_scale=15, lw=LINE_WIDTH, arrowstyle="-|>", color="black", zorder=9)
  ax.add_artist(DA_arrow)
  AD_arrow = Arrow3D([vertices['A'][0], vertices['D'][0]], [vertices['A'][1]-(MARKER_SIZE)/2-MARKER_OFFSET, vertices['D'][1]-(MARKER_SIZE)/2-MARKER_OFFSET], [vertices['A'][2], vertices['D'][2]], mutation_scale=15, lw=LINE_WIDTH, arrowstyle="-|>", color="black", zorder=9)
  ax.add_artist(AD_arrow)
  ax.text(vertices['A'][0]-length_X/2, vertices['A'][1]-(MARKER_SIZE+MARKER_OFFSET), vertices['A'][2], f"{label_X} m", color="black", fontsize=18, ha='left', va='top', zorder=10, fontfamily='times new roman')

  # AA_top
  AA_top_arrow = Arrow3D([vertices['A'][0], vertices['A_top'][0]], [vertices['A'][1]-MARKER_SIZE/2-MARKER_OFFSET, vertices['A_top'][1]-MARKER_SIZE/2-MARKER_OFFSET], [vertices['A'][2], vertices['A_top'][2]], mutation_scale=15, lw=LINE_WIDTH, arrowstyle="-|>", color="black", zorder=9)
  ax.add_artist(AA_top_arrow)
  A_topA_arrow = Arrow3D([vertices['A_top'][0], vertices['A'][0]], [vertices['A_top'][1]-MARKER_SIZE/2-MARKER_OFFSET, vertices['A'][1]-MARKER_SIZE/2-MARKER_OFFSET], [vertices['A_top'][2], vertices['A'][2]], mutation_scale=15, lw=LINE_WIDTH, arrowstyle="-|>", color="black", zorder=9)
  ax.add_artist(A_topA_arrow)
  ax.text(vertices['A'][0], vertices['A'][1]-(MARKER_SIZE+MARKER_OFFSET), vertices['A'][2]+length_Z/2, f"{label_Z} m", color="black", fontsize=18, ha='left', va='center', zorder=10, fontfamily='times new roman')
  return fig, ax

if __name__ == "__main__":
  fig, ax = generate_figure(0.70, 0.65, 0.50, 100, 100)
  plt.savefig("q14.png", dpi=300, bbox_inches='tight')
  plt.show()
