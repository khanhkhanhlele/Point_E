from PIL import Image
import torch
import matplotlib.pyplot as plt
from tqdm.auto import tqdm

from PIL import Image
from tqdm.auto import tqdm
import plotly.graph_objects as go

# from point_e.models.download import load_checkpoint
# from point_e.models.configs import MODEL_CONFIGS, model_from_config
# from point_e.util.pc_to_mesh import marching_cubes_mesh
# from point_e.util.plotting import plot_point_cloud
from point_e.util.point_cloud import PointCloud

# Plot the point cloud as a sanity check.
pc = PointCloud.load('point_e\\examples\\example_data\\pc_corgi.npz')
pc = pc.get_neighbors_cloud(1, 100)
fig_plotly = go.Figure(
  data=[
    go.Scatter3d(
      x=pc.coords[:,0], y=pc.coords[:,1], z=pc.coords[:,2], 
      mode='markers',
      marker=dict(
        size=2,
        color=['rgb({},{},{})'.format(r,g,b) for r,g,b in zip(pc.channels["R"], pc.channels["G"], pc.channels["B"])],
      )
    )
  ],
  layout=dict(
    scene=dict(
      xaxis=dict(visible=False),
      yaxis=dict(visible=False),
      zaxis=dict(visible=False)
    )
  ),
)
fig_plotly.show(renderer="vscode")