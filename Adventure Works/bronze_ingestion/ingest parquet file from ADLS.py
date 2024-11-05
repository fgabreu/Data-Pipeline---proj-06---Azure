# Databricks notebook source
display(dbutils.fs.ls('mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load'))

# COMMAND ----------

from pyspark.sql.functions import col, current_timestamp

# COMMAND ----------

spark.read.format('parquet').load('mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_SalesOrderHeader.parquet')


df = df.withColumn('bronze_ingestion_timestamp', current_timestamp())


df.write.mode('overwrite').option('overwriteSchema','True').format('delta').saveAsTable('adventure_works_bronze.Sales_SalesOrderHeader')

# COMMAND ----------



# COMMAND ----------

from pyspark.sql.functions import col, current_timestamp
#Trabalhando na ingestao de várias tabelas

def ingest_bronze_and_save(file_path, table_name, database_name):
    print(f'Lendo arquivo: {file_path}')
    #le o arquivo
    df = spark.read.format('parquet').load(file_path)
    #Transforma
    df = df.withColumn('bronze_ingestion_timestamp', current_timestamp())
    #Salvar
    df.write.mode('overwrite').option('overwriteSchema','True').format('delta').saveAsTable(f"{database_name}.{table_name}")
    print(f"Salvo com sucesso a tabela: {database_name}.{table_name}")

# COMMAND ----------

file_path = 'mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_SalesOrderHeader.parquet'
database_name = 'adventure_works_bronze'
table_name = 'Sales_SalesOrderHeader'
input_format = 'parquet'

ingest_bronze_and_save(file_path, table_name, database_name)

# COMMAND ----------



# COMMAND ----------


