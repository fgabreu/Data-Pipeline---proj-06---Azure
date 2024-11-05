# Databricks notebook source
# MAGIC %md
# MAGIC ##Database Camada Bronze

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE DATABASE IF NOT EXISTS adventure_works_bronze
# MAGIC LOCATION '/mnt/adlsadvwrksprd/bronze/adventure_works_bronze'

# COMMAND ----------

# MAGIC %md
# MAGIC ##Database Camada Prata

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE DATABASE IF NOT EXISTS adventure_works_prata
# MAGIC LOCATION '/mnt/adlsadvwrksprd/prata/adventure_works_prata'
