import h5py

# Path to your HDF5 file
file_path = 'data/ex3/ex3_eval_ntraj_data.hdf'


with h5py.File(file_path, 'r+') as f:
    metadata_group = f['metadata']
    
    # Read the current string value
    n_traj_str = metadata_group.attrs['n_traj']
    
    # Convert to integer
    n_traj_int = int(n_traj_str)
    
    # Delete the old attribute
    del metadata_group.attrs['n_traj']
    
    # Create a new attribute with integer type
    metadata_group.attrs.create('n_traj', n_traj_int, dtype='i')

print("Attribute 'n_traj' successfully converted to integer.")

