import numpy as np
import time
import open3d as o3d
import pcd_bin_io

def random_downsampling(points, target_count):
    """Downsample the point cloud by randomly sampling points until the target count is reached."""
    if len(points) <= target_count:
        return points  # No need to downsample if we have fewer or equal points
    indices = np.random.choice(len(points), target_count, replace=False)
    return points[indices]

def intensity_based_downsampling(points, intensity_threshold, target_count):
    """Downsample based on intensity, keeping points above a threshold and reducing to target count."""
    filtered_points = points[points[:, 3] > intensity_threshold]
    if len(filtered_points) > target_count:
        indices = np.random.choice(len(filtered_points), target_count, replace=False)
        return filtered_points[indices]
    return filtered_points

def voxel_downsampling(points, voxel_size, target_count):
    """Downsample the point cloud using voxel grid filtering and reduce to target count."""
    pcd = o3d.geometry.PointCloud()
    
    if points.ndim == 2 and points.shape[1] == 4:
        pcd.points = o3d.utility.Vector3dVector(points[:, :3])  # Use x, y, z only

    # Voxel downsampling
    downsampled_pcd = pcd.voxel_down_sample(voxel_size=voxel_size)
    downsampled_points = np.asarray(downsampled_pcd.points)

    if len(downsampled_points) > target_count:
        indices = np.random.choice(len(downsampled_points), target_count, replace=False)
        return downsampled_points[indices]
    
    return downsampled_points

# Read the point cloud data from the binary file
points = pcd_bin_io.read("/Users/tokeraabjerg/Dropbox/Skole/Universitet/5. Semester/MP5 Projekt/TransformedPointCloud.bin")

# Set parameters
intensity_threshold = 0.5  # Example threshold for intensity
voxel_size = 0.01  # Example voxel size for downsampling
target_count = 1000000  # Desired number of points after downsampling

# Measure time for random downsampling
start_time_random = time.time()
downsampled_random = random_downsampling(points, target_count)
end_time_random = time.time()

# Measure time for intensity-based downsampling
start_time_intensity = time.time()
downsampled_intensity = intensity_based_downsampling(points, intensity_threshold, target_count)
end_time_intensity = time.time()

# Measure time for voxel downsampling
start_time_voxel = time.time()
downsampled_voxel = voxel_downsampling(points, voxel_size, target_count)
end_time_voxel = time.time()

# Print results
print("Original number of points:", len(points))
print("Number of points after random downsampling:", len(downsampled_random))
print("Time taken for random downsampling: {:.6f} seconds".format(end_time_random - start_time_random))
print("Number of points after intensity-based downsampling:", len(downsampled_intensity))
print("Time taken for intensity-based downsampling: {:.6f} seconds".format(end_time_intensity - start_time_intensity))
print("Number of points after voxel downsampling:", len(downsampled_voxel))
print("Time taken for voxel downsampling: {:.6f} seconds".format(end_time_voxel - start_time_voxel))
