import pyspark
from pyspark.sql import SparkSession
from typing import Optional, Dict, List
import os
from config.database_config import get_database_config

class SparkConnection:
    def __init__(self,
                 app_name : str,
                 master_url: str = "spark://spark-master:7077",
                 executor_core: Optional[int] = 2,
                 executor_memory: Optional[str] = "4g",
                 num_executors: Optional[int] = 2,
                 driver_memory: Optional[str] = "4g",
                 jars_packages: Optional[List[str]] = None,
                 history_log_dir:  Optional[List[str]] = None,
                 enable_delta: bool = False,
                 minio_config: Optional[dict] = None,
                 log_level: str = "WARN", ):
        self.app_name = app_name
        self.master_url = master_url
        self.executor_core = executor_core
        self.executor_memory = executor_memory
        self.driver_memory = driver_memory
        self.num_executors = num_executors
        self.jars = jars_packages
        self.history_log_dir = history_log_dir,
        self.enable_delta = enable_delta,
        self.minio_config = minio_config,
        self.log_level = log_level

        self.spark = self.create_spark_session()

    def create_spark_session(self):
        builder = SparkSession.builder.appName(self.app_name).master(self.master_url)
        
        if self.executor_core:
            builder.config("spark.executor.cores", self.executor_core)
        if self.executor_memory:
            builder.config("spark.executor.memory", self.executor_memory)
        if self.driver_memory:
            builder.config("spark.executor.")
        if self.num_executors:
            builder.config("spark.executor.instances", self.num_executors)
        
        if self.jars:
            abs_jars_path = []
            for jar in self.jars:
                jar_path = os.path.abspath(jar)
                abs_jars_path.append(jar_path)
            jar_paths = ",".join(abs_jars_path)
            builder.config("spark.jars", jar_paths)

        if self.enable_delta:
            builder.config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
            builder.config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")

        if self.minio_config:
            builder.config("spark.hadoop.fs.s3a.endpoint", self.minio_config["endpoint"])
            builder.config("spark.hadoop.fs.s3a.access.key", self.minio_config["access_key"])
            builder.config("spark.hadoop.fs.s3a.secret.key", self.minio_config["secret_key"])
            builder.config("spark.haddop.fs.s3a.path.style.access", "true")
            builder.config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")

        spark = builder.getOrCreate()
        spark.sparkContext.setLogLevel(self.log_level)
        print(f"SparkSession {self.app_name} create successfully")
        return spark
    
    def stop(self):
        if self.spark:
            self.spark.stop()
        print("SparkSession stop")

class SparkWrite:
    def __init__(self, spark: SparkSession):
        self.spark = spark

    def write_data_mysql(self, df: DataFrame, tabel_name, jdbc_url, user, password, mode="append"):
        df.write.format("jdbc") \
            .option("url", jdbc_url) \
            .option("driver", "com.msql.cj.jdbc.Driver") \
            .option("dbtable", tabel_name) \
            .option("user", user) \
            .option("password", password) \
            .mode(mode) \
            .save()
        
    def write_data_minio(self, df: DataFrame, delta_path):
        df.write \
            .format("delta") \
            .mode("overwrite") \
            .save(delta_path)
    
class SparkRead:
    def __init__(self, spark: SparkSession):
        self.spark = spark
    
    def read_data_mysql(self, table_name, jdbc_url, user = "mysqluser", password = "mysqlpass"):
        df_read = self.spark.read.format("jdbc") \
            .option("url", jdbc_url) \
            .option("dbtable", table_name) \
            .option("user", user) \
            .option("password", password) \
            .option("driver", "comd.mysql.cj.jdbc.Driver") \
            .load()
        return df_read
    
    def read_data_csv(self, path, schema = None):
        reader = self.spark.read \
            .option("header", True) \
            .option("mode", "PERMESSTIVE") \
            .option("inferSchema", True)
        
        if schema:
            df = reader.schema(schema).csv(path)
        else:
            df = reader.csv(path)
        return df
    
    def read_data_minio(self, path):
        df = self.spark.read.format("delta").load(path)
        return df
    

    if __name__ == '__main__':
        jars = [
            "./jars/mysql-connector-j-9.2.0.jar"
        ]
        spark_connect = SparkConnection(
            app_name = "EcommerceLakehouse",
            jars = jars,
            log_level="INFO"
        )
        spark = spark_connect.spark




    