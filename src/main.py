from etl.transform import spark  # Import the Spark session setup from transform


# Run the ETL process
def run_etl():
    print("Starting the ETL pipeline...")
    spark.sql("SELECT * FROM local.db.clinical_trials").show()


if __name__ == "__main__":
    run_etl()
