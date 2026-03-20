from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('Curso de pySpark').getOrCreate()

df = spark.read.parquet('./../DATASETS/LOGINS.parquet', header=True)
# spark.conf.set('spark.sql.rpl.eagerEval.enabled', True) # -> configuração de exibição de dados ao executar df.show()

print("df.show()")
df.show()

print("df.printSchema()")
# tipagem das colunas # vantagem de usar parquet, ele mantem tipagem e facilita o uso das libs de cada tipo
df.printSchema()

print("df.count()")
#quantidade de linhas
print(df.count())

print("df.describe()")
#resumo de quantidade de valores por coluna, média, desvio padrão, menor valor e maior valor
print(df.describe())

print("df.columns")
# nomes das colunas
print(df.columns)

print("dtypes")
print(df.dtypes)