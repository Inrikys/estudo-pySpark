from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Curso de pySpark').getOrCreate()

df = spark.read.parquet('./../DATASETS/LOGINS.parquet', header=True)
# spark.conf.set('spark.sql.rpl.eagerEval.enabled', True) # -> configuração de exibição de dados ao executar df.show()

df.show()