from pyspark.sql import SparkSession
import pyspark.sql.functions as f

spark = SparkSession.builder.appName('Curso de pySpark').getOrCreate()

df = (
    spark
    .read
    .parquet('./../DATASETS/LOGINS.parquet', header=True)
    .select('email', 'senha', 'estado', 'cor_favorita', 'profissao')
)

(
    df
    .withColumn('usuario', f.split(df.email, '@').getItem(0))
    .withColumn('provedor', f.split(df.email, '@').getItem(1))
    # usar coluna criada anteriormente para gerar dados, "." é um caractere usado pelo python, então para utilizar ele como string é necessário a barra invertida
    .withColumn('nome_provedor', f.split(f.col('provedor'), '\.').getItem(0))
    .show(20, False)
)

(
    df
    .withColumn('concatenado', f.concat(f.col('profissao'), f.col('cor_favorita')))
    # concatenar com valor fixo
    .withColumn("contatenado_2", f.concat(f.col('estado'), f.lit(' - Brasil')))
    .withColumn('lower', f.lower(f.col('profissao')))
    .withColumn('upper', f.upper(f.col('cor_favorita')))
    .withColumn('initcap', f.initcap(f.col('lower')))
    .withColumn('substring', f.substring(f.col('cor_favorita'), 1, 3))
    .withColumn('format_string', f.format_string('Olá %s, sua cor favorita é %s', f.col('email'), f.col('cor_favorita')))
    # a partir de qual caractere começa a substring escrita
    .withColumn("instr", f.instr(f.col('email'), '@gmail'))
    .withColumn("length", f.length(f.col('profissao')))
    .withColumn("repeat", f.repeat(f.col('estado'), 5))
    .withColumn("concatenado_espaco_branco", f.concat(f.lit('        '), f.col('estado'), f.lit('          ')))
    .withColumn("trim", f.trim(f.col('concatenado_espaco_branco')))
    .withColumn("lpad", f.lpad(f.col('cor_favorita'), 10, '0'))
    .withColumn("rpad", f.rpad(f.col('cor_favorita'), 10, '0'))
    .show(20, False)
)
