# 05 - Delta Lake

## Environment setup
Create a Python virtual environment:
```bash
python3 -m venv delta-env
```
Activate the virtual environment:
```
source delta-env/bin/activate 
```
Install the dependencies inside the environment:
```bash
pip install pyspark==3.4.0 delta-spark==2.4.0
```
Check if Spark starts properly:
```bash
pyspark --packages io.delta:delta-core_2.12:2.4.0 \
  --conf "spark.sql.extensions=io.delta.sql.DeltaSparkSessionExtension" \
  --conf "spark.sql.catalog.spark_catalog=org.apache.spark.sql.delta.catalog.DeltaCatalog"
```
## Examples

- Versioning of a Dataframe:

  ```bash
  python history.py
  ```

- CSV to Delta Table:

  ```bash
  python history.py
  ```

  comparison of the different dimensions:

  ```bash
  du -h ../04-parquet/trips.csv
  du -h ../04-parquet/trips.parquet
  du -h trips.delta
  ```

- Schema Evolution:
  ```bash
  python schema_evo.py
  ```

## Credits

https://delta.io