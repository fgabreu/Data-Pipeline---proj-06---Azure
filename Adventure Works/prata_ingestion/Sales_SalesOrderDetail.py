# Databricks notebook source
import pyspark.sql.functions as F
from pyspark.sql import DataFrame

# COMMAND ----------

table = "Sales_SalesOrderDetail"
database = "adventure_works_bronze"
tabela_bronze = spark.read.table(f"{database}.{table}")

# COMMAND ----------

def logic_Sales_SalesOrderDetail(tabela:DataFrame) -> Dataframe:
    '''
    Transformação da tabela: Sales_SalesOrderHeader

    Parâmetros:
        tabela (DataFrame): DataFrame contendo os dados da tabela Sales_SalesOrderHeader

    Retorna:
        DataFrame: O DataFrame resultante após a transformação (no momento, é o mesmo que o input).
    '''
    #Aplicar a transformação desejada na tabela (atualmente, não há transformação)
    sdf = tabela

    sdf = sdf.withColumn('Prata_ingestion', F.current_timestamp())

    return sdf 


# COMMAND ----------

def logic_Sales_SalesOrderDetail(tabela:DataFrame) -> Dataframe:
    '''
    Transformação da tabela: Sales_SalesOrderHeader

    Parâmetros:
        tabela (DataFrame): DataFrame contendo os dados da tabela Sales_SalesOrderHeader

    Retorna:
        DataFrame: O DataFrame resultante após a transformação (no momento, é o mesmo que o input).
    '''
    #Aplicar a transformação desejada na tabela (atualmente, não há transformação)
    sdf = tabela

    sdf = sdf.withColumn('Prata_ingestion', F.current_timestamp())

    return sdf 

# COMMAND ----------

output = logic_Sales_SalesOrderDetail(tabela_bronze)

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

def criar_tabela_com_meu_nome(tabela_input):

    nova_tabela = tabela_input.withColumn("FELIPE")
