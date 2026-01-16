from src.spark.spark_config import SparkConnection, SparkRead, SparkWrite


if __name__ == '__main__':
    jars = [
        "./jars/mysql-connector-j-9.2.0.jar",
        "/opt/spark/jars/delta-spark_2.12-3.2.0.jar"
    ]

    jdbc_url = "jdbc:mysql//myusql:3306/ecommerce"

    spark_connect = SparkConnection(
        app_name = "EcommerceLakehouse",
        jars = jars,
        log_level="INFO"
    )

    spark = spark_connect.spark
    
    spark_read = SparkRead(spark)
    spark_write = SparkWrite(spark)

    # schema_config = get_schema


