from datetime import datetime
startTime = datetime.now()

import numpy as np
import open3d as o3d
import pcd_bin_io

point_data = pcd_bin_io.read("/Users/tokeraabjerg/Dropbox/Skole/Universitet/5. Semester/MP5 Projekt/TransformedPointCloud.bin")

print("Bin read")
print(datetime.now() - startTime)

# Create an Open3D PointCloud object
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(point_data[:, :3])


# Visualize the point cloud
o3d.visualization.draw_geometries([pcd], window_name="Point Cloud Visualization")

# Optional: Save the point cloud to a file (e.g., PLY format)
# output_file = "/Users/tokeraabjerg/Downloads/PointCloudData.ply"
# o3d.io.write_point_cloud(output_file, pcd)
