import os
import ray
import pandas as pd
from adlfs import AzureBlobFileSystem

# Initialize Ray
ray.init()

# Set up Azure Data Lake credentials
account_name = 'datalakeranga'
account_key = 'lngtIwbKM3M9hl8DoiPjWKajfKsqXQ21twcsTXPtVP+wkz8zW0KTNX/+Ek265JZo0QhxfLAfDFtf+AStC08eHA=='

# Create an AzureBlobFileSystem instance
fs = AzureBlobFileSystem(account_name=account_name, account_key=account_key)

# Read the CSV file using ray.data.read_csv
ds = ray.data.read_csv(
    "az://data/raw/YellowTaxis1.csv",
    filesystem=fs
)

print(ds.schema())

# Convert to pandas DataFrame
df = ds.to_pandas()

print(df.head())