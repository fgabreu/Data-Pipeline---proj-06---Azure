# Databricks notebook source
# colunas = spark.table("adventure_works_prata.sales_salesorderheader").columns
# # 
# for i in colunas:
#     print(f", {i} AS {i}")

# COMMAND ----------

# MAGIC %sql 
# MAGIC
# MAGIC CREATE OR REPLACE TABLE adventure_works_prata.sales_salesorderheader AS
# MAGIC
# MAGIC SELECT 
# MAGIC  SalesOrderID AS Sales_Order_ID
# MAGIC , RevisionNumber AS Revision_Number
# MAGIC , OrderDate AS Order_Date
# MAGIC , DueDate AS Due_Date
# MAGIC , ShipDate AS Ship_Date
# MAGIC , Status AS Status
# MAGIC , OnlineOrderFlag AS Online_Order_Flag
# MAGIC , SalesOrderNumber AS Sales_Order_Number
# MAGIC , PurchaseOrderNumber AS Purchase_Order_Number
# MAGIC , AccountNumber AS Account_Number
# MAGIC , CustomerID AS Customer_ID
# MAGIC , SalesPersonID AS Sales_Person_ID
# MAGIC , TerritoryID AS Territory_ID
# MAGIC , BillToAddressID AS Bill_To_Address_ID
# MAGIC , ShipToAddressID AS Ship_To_Address_ID
# MAGIC , ShipMethodID AS Ship_Method_ID
# MAGIC , CreditCardID AS Credit_Card_ID
# MAGIC , CreditCardApprovalCode AS Credit_Card_Approval_Code
# MAGIC , CurrencyRateID AS Currency_Rate_ID
# MAGIC , SubTotal AS Sub_Total
# MAGIC , TaxAmt AS Tax_Amt
# MAGIC , Freight AS Freight
# MAGIC , TotalDue AS Total_Due
# MAGIC , Comment AS Comment
# MAGIC , rowguid AS rowguid
# MAGIC , ModifiedDate AS Modified_Date
# MAGIC , bronze_ingestion_timestamp AS bronze_ingestion_timestamp
# MAGIC
# MAGIC FROM adventure_works_bronze.sales_salesorderheader
# MAGIC
# MAGIC WHERE OrderDate > '2011-05-30T00:00:00.000+00:00'
