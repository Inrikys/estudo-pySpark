from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.appName('Curso de pySpark').getOrCreate()

df = spark.read.parquet('./../DATASETS/IMC.parquet', header=True)

(
    df
    # arredondar para quantidade de casas decimais determinada
    .withColumn('round', f.round(f.col('peso'), 1))
    # arredonda pra cima, sem numero decimal
    .withColumn('ceil', f.ceil(f.col('peso')))
    # arredonda para baixo
    .withColumn('floor', f.floor(f.col('peso')))
    .withColumn('altura_negativa', -f.col('peso'))
    # numero absoluto
    .withColumn('abs', f.abs(f.col('altura_negativa')))
    # potencia
    .withColumn('pow', f.pow(f.col('peso'), 2))
    #raiz quadrada
    .withColumn('sqrt', f.sqrt(f.col('pow')))
    .show()
)

(
    df
    .withColumn('imc', f.round(f.pow(f.col('peso'), 2)/ f.col('altura'), 1))
    .show()
)