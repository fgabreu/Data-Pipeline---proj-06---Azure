# Databricks notebook source
#Criação do dicionário com todas as tabelas e o atributo 'ativo'

database_tables = {
    "Sales_SalesOrderHeader": {
        "ativo": True,
        "notebook_path": "caminho/para/notebook_Sales_SalesOrderHeader"
    },
    "Sales_SalesOrderDetail": {"ativo": True},
    "Production_Product": {"ativo": True},
    "Production_ProductSubcategory": {"ativo": True},
    "Production_ProductModel": {"ativo": True},
    "Production_ProductDescription": {"ativo": True},
    "Sales_Customer": {"ativo": True},
    "Sales_SpecialOffer": {"ativo": True},
    "Sales_Currency": {"ativo": True},
    "Sales_SalesTerritory": {"ativo": True},
    "Sales_SalesReason": {"ativo": True},
    "Person_Address": {"ativo": True},
    "Person_Person": {"ativo": True},
    "Person_EmailAddress": {"ativo": True},
    "Person_PersonPhone": {"ativo": True},
    "Person_StateProvince": {"ativo": True},
    "Person_CountryRegion": {"ativo": True}
}

# COMMAND ----------

for table in database_tables:
    path = database_tables[table]['notebook_path']
    if database_tables[table]['ativo']:
        print(f'Executando tabela: {table}')
