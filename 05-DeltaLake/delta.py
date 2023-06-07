from delta import *
from pyspark.sql import SparkSession


spark = SparkSession.builder \
    .appName("quickstart") \
    .master("local[*]") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()


# data = spark.range(5, 10)
# data.write.format("delta").mode("overwrite").save("/tmp/delta-table")

# df = spark.read.format("delta") \
#   .option("versionAsOf", 0) \
#   .load("/tmp/delta-table")

# df.show()

# df.printSchema()

# history_df = spark.sql("DESCRIBE HISTORY delta.`/tmp/delta-table`")
# history_df.show(truncate=False)

spark.stop()