from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Curso de pySpark').getOrCreate()

df = spark.read.csv('./../DATASETS/LOGINS.txt', header=True)
# spark.conf.set('spark.sql.rpl.eagerEval.enabled', True) # -> configuração de exibição de dados ao executar df.show()

df.show()

# tipagem das colunas
df.printSchema()