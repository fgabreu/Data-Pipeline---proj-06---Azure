# Databricks notebook source
dbutils.widgets.text('name', 'Felipe')
dbutils.widgets.texgt('idade', '35')

# COMMAND ----------

name = dbutils.widgets.get('name')
idade = dbutils.widgets.get('idade')

# COMMAND ----------

print(f"{name} tem {idade} anos")
