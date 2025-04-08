from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = (
    SparkSession.builder.appName("ClinicalDataLakehouseETL")
    .config("spark.sql.catalog.local", "org.apache.iceberg.spark.SparkCatalog")
    .config("spark.sql.catalog.local.type", "hadoop")
    .config("spark.sql.catalog.local.warehouse", "./warehouse")
    .getOrCreate()
)

# Load the dataset
df = spark.read.option("header", "true").csv("data/clinical_trials_sample.csv")

# Data transformation logic
df_transformed = df.select(
    col("NCT").alias("study_id"),
    col("Brief Title").alias("study_title"),
    col("Lead Sponsor").alias("lead_sponsor"),
    col("Start Date").cast("date").alias("start_date"),
    col("Conditions").alias("conditions"),
    col("Treatments").alias("treatments"),
    col("Enrollment Count").cast("integer").alias("enrollment_count"),
)

# Write to Iceberg
df_transformed.writeTo("local.db.clinical_trials").append()
