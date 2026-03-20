from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.appName('Curso de pySpark').getOrCreate()

df = spark.read.parquet('./../DATASETS/LOGINS.parquet').select('data_de_nascimento', 'data_cadastro')

(
    df
    .withColumn('add_months', f.add_months(df.data_cadastro, 1))  # Deslocar meses
    .withColumn('add_months_negativo', f.add_months(df.data_cadastro, -12))
    .withColumn('current_date', f.current_date())
    .withColumn('current_timestamp', f.current_timestamp())
    .withColumn('date_add', f.date_add(df.data_cadastro, 15))
    .withColumn('date_add_negativo', f.date_add(df.data_cadastro, -15))
    .withColumn('date_sub', f.date_sub(df.data_cadastro, 15))  # mesma coisa da date_add com valor negativo
    .withColumn('date_format', f.date_format(df.data_de_nascimento, "dd/MM/y"))
    .withColumn('datediff', f.datediff(f.current_date(), df.data_de_nascimento))
    .withColumn('dayofmonth', f.dayofmonth(df.data_de_nascimento))
    .withColumn('dayofweek', f.dayofweek(df.data_de_nascimento))
    .withColumn('weekofyear', f.weekofyear(df.data_de_nascimento))
    .withColumn('year', f.year(df.data_de_nascimento))
    .withColumn('month', f.year(df.data_de_nascimento))
    .withColumn('last_day', f.last_day(df.data_de_nascimento))  # ultimo dia do mês de determinada data
    .withColumn('months_between', f.months_between(f.current_date(), df.data_de_nascimento))
    .withColumn('next_day', f.next_day(df.data_de_nascimento, 'Mon')) # Qual a segunda feira seguinte dessa data?
    .withColumn('make_date', f.make_date(f.lit(2020), f.lit(8), f.lit(1)))
    .withColumn('to_date', f.to_date(f.lit("2020-08-01")))

).show()
