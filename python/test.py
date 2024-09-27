import open3d as o3d
import numpy as np

# Load the point cloud from a .ply file
pcd = o3d.io.read_point_cloud("airplane.ply")

# Convert point cloud to a numpy array
points = np.asarray(pcd.points)

o3d.visualization.draw_geometries([pcd])


# Print the number of points and the first 5 points
print(f"Total number of points: {points.shape[0]}")
print("First 5 points:")
print(points[:10])