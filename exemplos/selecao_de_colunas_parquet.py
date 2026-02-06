from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pyspark.sql.functions as f
spark = SparkSession.builder.appName('Curso de pySpark').getOrCreate()

df = spark.read.parquet('./../DATASETS/LOGINS.parquet', header=True)

# Varios exemplos de selecionar colunas
df.select('email', 'senha').show()
df.select(df.cpf, df.data_de_nascimento).show()
df.select(df['estado'], df['ipv4']).show()
df.select(col('data_cadastro')).show()
df.select(f.col('data_cadastro')).show()

df.select("*").show()
#seleciona todas, menos as especificadas
df.drop('email', 'estado').show()