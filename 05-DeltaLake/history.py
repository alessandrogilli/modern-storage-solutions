from delta import *
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
import os

path = "/tmp/test-table"

spark = SparkSession.builder \
    .appName("history") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

print("--- Writing Data ---")

if not os.path.exists(path):

    df = spark.range(0, 3)
    print("Version 0 of the data:")
    df.show()
    df.repartition(1).write.format("delta").save(path)

    df = spark.range(8, 11)
    print("Version 1 of the data:")
    df.show()
    df.repartition(1).write.mode("append").format("delta").save(path)

    df = spark.createDataFrame([(55,), (66,), (77,)]).toDF("id")
    print("Version 2 of the data:")
    df.show()
    df.repartition(1).write.mode("overwrite").format("delta").save(path)

else:
    print(f'\n-- Data already present in {path}, skipping. --')

print("\n--- Reading Data ---\n")

print("Reading the current version of the data:")
spark.read.format("delta").load(path).show()

print("Reading data at version 0:")
spark.read.format("delta").option("versionAsOf", "0").load(path).show()

print("Reading data at version 1:")
spark.read.format("delta").option("versionAsOf", "1").load(path).show()

print("Reading data at version 2:")
spark.read.format("delta").option("versionAsOf", "2").load(path).show()


print("\n--- History Metadata of the Delta Table ---\n")


spark.sql(f"DESCRIBE HISTORY delta.`{path}`").show(truncate=False)


