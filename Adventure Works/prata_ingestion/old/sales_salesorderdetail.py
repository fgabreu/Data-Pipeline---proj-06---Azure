# Databricks notebook source
# colunas = spark.table("adventure_works_prata.sales_salesorderheader").columns
# # 
# for i in colunas:
#     print(f", {i} AS {i}")

# COMMAND ----------

# MAGIC %sql 
# MAGIC
# MAGIC CREATE OR REPLACE TABLE adventure_works_prata.sales_salesorderdetail AS
# MAGIC
# MAGIC SELECT 
# MAGIC  SalesOrderID AS Sales_Order_ID
# MAGIC , SalesOrderDetailID AS Sales_Order_Detail_ID
# MAGIC , CarrierTrackingNumber AS Carrier_Tracking_Number
# MAGIC , OrderQty AS Order_Qty
# MAGIC , ProductID AS Product_ID
# MAGIC , SpecialOfferID AS Special_Offer_ID
# MAGIC , UnitPrice AS Unit_Price
# MAGIC , UnitPriceDiscount AS Unit_Price_Discount
# MAGIC , LineTotal AS Line_Total
# MAGIC , rowguid AS rowguid
# MAGIC , ModifiedDate AS Modified_Date
# MAGIC , bronze_ingestion_timestamp AS bronze_ingestion_timestamp
# MAGIC FROM adventure_works_bronze.sales_salesorderdetail
# MAGIC
# MAGIC
# MAGIC WHERE ModifiedDate > '2011-05-30T00:00:00.000+00:00'
