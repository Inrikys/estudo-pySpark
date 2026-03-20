from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.appName('Curso de pySpark').getOrCreate()

df = spark.read.parquet('./../DATASETS/LOGINS.parquet')
df.orderBy(f.desc('email')).show()
df.orderBy(f.asc('email')).show()
df.orderBy('estado', 'data_cadastro', f.desc('cor_favorita')).show()