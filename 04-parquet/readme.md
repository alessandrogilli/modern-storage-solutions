# 04 - Apache Parquet

## Prerequisites
```bash
python3 -m venv parquet-env 

source parquet-env/bin/activate

pip install parquet-cli
```

## Download Data
```bash
curl -o trips.parquet https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet
```

## parquet-cli ops
```bash
parq trips.parquet

parq trips.parquet --schema

parq trips.parquet --head 10

parq trips.parquet --tail 10
```

## parquet.py

Imports the necessary module pyarrow.parquet for working with Parquet files.

Loads a Parquet file named "trips.parquet" using the pq.ParquetFile() function and assigns it to the file variable.

Retrieves the metadata of the Parquet file using file.metadata.

Retrieves the schema of the Parquet file using file.schema.

Reads the contents of the Parquet file and converts it into a Pandas DataFrame using file.read().to_pandas(). The resulting DataFrame is assigned to the variable df.

Saves the DataFrame df as a CSV file named "trips.csv" using the to_csv() method.

Saves the DataFrame df as a JSON file named "trips.json" using the to_json() method. The orient="records" parameter specifies the JSON format as a list of records, and the lines=True parameter writes each record on a separate line.

## Comparison between files
```bash
du -h trips.*
```
## Credits
Based on a [Mark Needham](https://gist.github.com/mneedham) [video](https://www.youtube.com/watch?v=KLFadWdomyI&list=PLw2SS5iImhETC2AL13rLdkNgdgRBWIcKj).