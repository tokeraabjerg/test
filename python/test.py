import numpy as np
import open3d as o3d

# Path to your .bin file
bin_file = "/Users/tokeraabjerg/Downloads/PointCloud_Scan_0.bin"

# Load the .bin file assuming 'double' precision (float64) for (X, Y, Z, I)
point_data = np.fromfile(bin_file, dtype=np.float64).reshape(-1, 4)

# Filter out rows that contain only zeros
# This removes any points where all values are zero
filtered_data = point_data[np.any(point_data != 0, axis=1)]

# Extract X, Y, Z columns (omit intensity)
xyz = filtered_data[:, :3]

subset_xyz = xyz[:10]  # Change this number as needed

# Create an Open3D point cloud object
pcd = o3d.geometry.PointCloud()

# Assign points to the point cloud
pcd.points = o3d.utility.Vector3dVector(xyz)

# Visualize the point cloud
o3d.visualization.draw_geometries([pcd])

# Print the number of points and the first 10 points after filtering
print(f"Total number of points after filtering: {xyz.shape[0]}")
print("First 10 points after filtering:")
print(xyz[1000:2000])