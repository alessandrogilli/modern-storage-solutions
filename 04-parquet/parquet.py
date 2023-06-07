import pyarrow.parquet as pq

# Load the Parquet file
file = pq.ParquetFile("trips.parquet")

# Retrieve the metadata of the Parquet file
file.metadata

# Retrieve the schema of the Parquet file
file.schema

# Read the Parquet file and convert it into a Pandas DataFrame
df = file.read().to_pandas()

# Save the DataFrame as a CSV file
df.to_csv("trips.csv")

# Save the DataFrame as a JSON file with specified options
df.to_json("trips.json", orient="records", lines=True)
