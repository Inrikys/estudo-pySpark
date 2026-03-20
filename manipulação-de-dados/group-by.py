from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.appName('Curso de pySpark').getOrCreate()

df = spark.read.parquet('./../DATASETS/LOGINS.parquet')

df.groupby("cor_favorita").count().show()
df.groupby("estado","cor_favorita").count().show()
df.groupby("estado","cor_favorita").count().groupby("estado").sum("count").show()
df.groupby("estado","cor_favorita").count().groupby("estado").min("count").show()
df.groupby("estado","cor_favorita").count().groupby("estado").max("count").show()
df.groupby(f.year("data_de_nascimento")).count().show()