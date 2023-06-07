from pyspark.sql import SparkSession


# Create a SparkSession
spark = SparkSession.builder \
    .appName("Schema Evolution") \
    .config("spark.jars.packages", "io.delta:delta-core_2.12:2.4.0") \
    .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension") \
    .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog") \
    .getOrCreate()

df1 = spark.createDataFrame([("bob", 47), ("li", 23), ("leonard", 51)]).toDF(
    "first_name", "age"
)

df2 = spark.createDataFrame([("frank", 68, "usa"), ("jordana", 26, "brasil")]).toDF(
    "first_name", "age", "country"
)

df1.show()
df2.show()

df1.write.format("delta").mode("overwrite").save("/tmp/fun_people")

# This line will trigger an error
# df2.write.format("delta").mode("append").save("/tmp/fun_people")

# We must specify the option for the schema merge
df2.write.option("mergeSchema", "true").format("delta").mode("append").save("/tmp/fun_people")

spark.read.format("delta").load("/tmp/fun_people").show()

# Stop the SparkSession
spark.stop()