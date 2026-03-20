from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.appName('Curso de pySpark').getOrCreate()

df = spark.read.parquet('./../DATASETS/LOGINS.parquet')
