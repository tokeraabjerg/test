from datetime import datetime
import numpy as np
import open3d as o3d
import pcd_bin_io

# Start timer to measure execution time
startTime = datetime.now()

# Path to original and transformed .bin files
bin_file = "/Users/tokeraabjerg/Dropbox/Skole/Universitet/5. Semester/MP5 Projekt/PointCloud_Scan_0.bin"
save_file = "/Users/tokeraabjerg/Dropbox/Skole/Universitet/5. Semester/MP5 Projekt/TransformedPointCloud.bin"

# Read the original .bin point cloud data
point_data = pcd_bin_io.read(bin_file, transpose=True)  # Read in column-major format
print("Original point cloud loaded")
print(datetime.now() - startTime)

# Create an Open3D PointCloud object from the loaded data
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(point_data[:, :3])  # Only use X, Y, Z for the point cloud

# Transformation: Apply a small translation and rotation

# Create a translation vector (e.g., move the point cloud by [0.01, 0.02, 0.03])
translation = np.array([0.01, 0.02, 0.03])

# Define a small rotation around the Z-axis (e.g., 5 degrees)
angle_rad = np.deg2rad(5)
rotation_matrix = np.array([
    [np.cos(angle_rad), -np.sin(angle_rad), 0],
    [np.sin(angle_rad), np.cos(angle_rad),  0],
    [0,                0,                 1]
])

# Apply the transformation to the point cloud
# 1. Rotate the points
rotated_points = np.dot(np.asarray(pcd.points), rotation_matrix.T)

# 2. Translate the points
transformed_points = rotated_points + translation

# Combine transformed points (X, Y, Z) with the original intensity (I) column
intensity_column = point_data[:, 3].reshape(-1, 1)  # Extract the intensity column
transformed_data = np.hstack((transformed_points, intensity_column))  # Combine X, Y, Z with intensity I

# Save the transformed point cloud back to a .bin file using bin_read.save()
pcd_bin_io.save(save_file, transformed_data, transpose=True)  # Save in column-major order

# Verify that reading the saved file produces identical data to the transformed data
point_cloud_data_saved = pcd_bin_io.read(save_file, transpose=True)
if np.array_equal(transformed_data, point_cloud_data_saved):
    print("Verification successful: The saved data is identical to the transformed data.")
else:
    print("Verification failed: The saved data differs from the transformed data.")

print("Transformed point cloud saved to", save_file)
print("Execution Time:", datetime.now() - startTime)

# Optional: Visualize the transformed point cloud
pcd_transformed = o3d.geometry.PointCloud()
pcd_transformed.points = o3d.utility.Vector3dVector(transformed_data[:, :3])  # Use transformed points
o3d.visualization.draw_geometries([pcd_transformed], window_name="Transformed Point Cloud Visualization")
