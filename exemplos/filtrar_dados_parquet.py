from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pyspark.sql.functions as f

spark = SparkSession.builder.appName('Curso de pySpark').getOrCreate()

df = spark.read.parquet('./../DATASETS/LOGINS.parquet', header=True)

df.filter(df.estado == 'MG').show()

df.filter((df.estado == 'MG') & (df.cor_favorita == 'Azul')).show()

# concatenar filtros
df.filter(df.estado == 'MG').filter(df.cor_favorita == 'Azul').show()

df.filter((df.cor_favorita == 'Ciano') | (df.estado == 'GO')).show()

# lógica OU na mesma coluna
df.filter(df.cor_favorita.isin('Ciano', 'Azul')).show()

# lógica OU e E -> where e filter fazem a mesma coisa
df.where(df.cor_favorita.isin('Ciano', 'Azul')).where(df.estado == 'GO').show()

# boa prática é concatenar funções
(
    df
    .filter(f.col('estado') == 'MG')
    .filter(f.col('cor_favorita') == 'Azul')
    .filter(f.col('profissao') == 'Tenente')
    .show()
)
