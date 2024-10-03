import numpy as np
import open3d as o3d
import pcd_bin_io

# File paths
original_bin_file = "/Users/tokeraabjerg/Dropbox/Skole/Universitet/5. Semester/MP5 Projekt/PointCloud_Scan_0.bin"
transformed_bin_file = "/Users/tokeraabjerg/Dropbox/Skole/Universitet/5. Semester/MP5 Projekt/TransformedPointCloud.bin"

# Downsample parameters
voxel_size = 0.05  # Adjust this value to control the level of downsampling

# Function to load and create point cloud from a .bin file
def load_point_cloud(bin_file):
    # Load the point cloud data using bin_read
    point_data = pcd_bin_io.read(bin_file)
    
    # Create an Open3D PointCloud object with the XYZ coordinates
    pcd = o3d.geometry.PointCloud()
    pcd.points = o3d.utility.Vector3dVector(point_data[:, :3])  # Use only X, Y, Z for point cloud
    return pcd

# Load original and transformed point clouds
original_pcd = load_point_cloud(original_bin_file)
transformed_pcd = load_point_cloud(transformed_bin_file)

# Downsample both point clouds for efficient visualization
original_pcd_downsampled = original_pcd.voxel_down_sample(voxel_size=voxel_size)
transformed_pcd_downsampled = transformed_pcd.voxel_down_sample(voxel_size=voxel_size)

# Assign colors to distinguish the point clouds
original_pcd_downsampled.paint_uniform_color([1, 0, 0])  # Red color for the original point cloud
transformed_pcd_downsampled.paint_uniform_color([0, 1, 0])  # Green color for the transformed point cloud

# Display both point clouds together in the same viewer
o3d.visualization.draw_geometries([original_pcd_downsampled, transformed_pcd_downsampled],
                                  window_name="Original and Transformed Point Clouds",
                                  point_show_normal=False)
