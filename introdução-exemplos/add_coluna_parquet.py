from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.appName('Curso de pySpark').getOrCreate()

df = spark.read.parquet('./../DATASETS/LOGINS.parquet', header=True)

# Criar coluna com valor default para todas as linhas
(
    df
    .withColumn('pais', f.lit('Brasil'))
    # Copia a coluna estado e cria a sigla_estado com os mesmos valores
    .withColumn('sigla_estado', f.col('estado'))
    .withColumn('num', f.lit(5))
    .show()
)

(
    df
    # quando estado == ac, cria coluna nome_estados com valor Acre
    .withColumn('nome_estados', f.when(f.col('estado') == 'AC', 'Acre')
                .when(f.col('estado') == 'AL', 'Alagoas')
                .when(f.col('estado') == 'AP', 'Amapá')
                .when(f.col('estado') == 'GO', 'Goiás'))
    .withColumn('flag_rose', f.when(f.col('cor_favorita') == 'Rosa', 1))
    .show()
)
