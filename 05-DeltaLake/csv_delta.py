from pyspark.sql import SparkSession

input = "../04-parquet/trips.csv"
output = "./trips.delta"

# Create a SparkSession
spark = SparkSession.builder \
    .appName("CSV to Delta") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

# Read the CSV file
df = spark.read.format("csv") \
    .option("header", "true") \
    .load(input)

# Write the DataFrame as a Delta table
df.write.format("delta").mode("overwrite").save(output)

# Stop the SparkSession
spark.stop()