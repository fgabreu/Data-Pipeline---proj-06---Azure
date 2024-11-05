# Databricks notebook source
configs = {
    'HumanResources_Department': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/HumanResources/HumanResources_Department.parquet',
        'table_name': 'HumanResources_Department',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'HumanResources_Employee': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/HumanResources/HumanResources_Employee.parquet',
        'table_name': 'HumanResources_Employee',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'HumanResources_EmployeeDepartmentHistory': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/HumanResources/HumanResources_EmployeeDepartmentHistory.parquet',
        'table_name': 'HumanResources_EmployeeDepartmentHistory',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'HumanResources_EmployeePayHistory': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/HumanResources/HumanResources_EmployeePayHistory.parquet',
        'table_name': 'HumanResources_EmployeePayHistory',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'HumanResources_JobCandidate': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/HumanResources/HumanResources_JobCandidate.parquet',
        'table_name': 'HumanResources_JobCandidate',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'HumanResources_Shift': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/HumanResources/HumanResources_Shift.parquet',
        'table_name': 'HumanResources_Shift',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Person_Address': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Person/Person_Address.parquet',
        'table_name': 'Person_Address',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Person_AddressType': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Person/Person_AddressType.parquet',
        'table_name': 'Person_AddressType',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Person_BusinessEntity': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Person/Person_BusinessEntity.parquet',
        'table_name': 'Person_BusinessEntity',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Person_BusinessEntityAddress': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Person/Person_BusinessEntityAddress.parquet',
        'table_name': 'Person_BusinessEntityAddress',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Person_BusinessEntityContact': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Person/Person_BusinessEntityContact.parquet',
        'table_name': 'Person_BusinessEntityContact',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Person_ContactType': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Person/Person_ContactType.parquet',
        'table_name': 'Person_ContactType',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Person_CountryRegion': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Person/Person_CountryRegion.parquet',
        'table_name': 'Person_CountryRegion',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Person_EmailAddress': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Person/Person_EmailAddress.parquet',
        'table_name': 'Person_EmailAddress',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Person_Password': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Person/Person_Password.parquet',
        'table_name': 'Person_Password',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Person_Person': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Person/Person_Person.parquet',
        'table_name': 'Person_Person',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Person_PersonPhone': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Person/Person_PersonPhone.parquet',
        'table_name': 'Person_PersonPhone',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Person_PhoneNumberType': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Person/Person_PhoneNumberType.parquet',
        'table_name': 'Person_PhoneNumberType',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Person_StateProvince': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Person/Person_StateProvince.parquet',
        'table_name': 'Person_StateProvince',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_BillOfMaterials': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_BillOfMaterials.parquet',
        'table_name': 'Production_BillOfMaterials',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_Culture': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_Culture.parquet',
        'table_name': 'Production_Culture',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_Document': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_Document.parquet',
        'table_name': 'Production_Document',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_Illustration': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_Illustration.parquet',
        'table_name': 'Production_Illustration',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_Location': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_Location.parquet',
        'table_name': 'Production_Location',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_Product': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_Product.parquet',
        'table_name': 'Production_Product',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ProductCategory': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ProductCategory.parquet',
        'table_name': 'Production_ProductCategory',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ProductCostHistory': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ProductCostHistory.parquet',
        'table_name': 'Production_ProductCostHistory',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ProductDescription': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ProductDescription.parquet',
        'table_name': 'Production_ProductDescription',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ProductDocument': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ProductDocument.parquet',
        'table_name': 'Production_ProductDocument',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ProductInventory': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ProductInventory.parquet',
        'table_name': 'Production_ProductInventory',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ProductListPriceHistory': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ProductListPriceHistory.parquet',
        'table_name': 'Production_ProductListPriceHistory',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ProductModel': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ProductModel.parquet',
        'table_name': 'Production_ProductModel',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ProductModelIllustration': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ProductModelIllustration.parquet',
        'table_name': 'Production_ProductModelIllustration',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ProductModelProductDescriptionCulture': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ProductModelProductDescriptionCulture.parquet',
        'table_name': 'Production_ProductModelProductDescriptionCulture',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ProductPhoto': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ProductPhoto.parquet',
        'table_name': 'Production_ProductPhoto',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ProductProductPhoto': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ProductProductPhoto.parquet',
        'table_name': 'Production_ProductProductPhoto',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ProductReview': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ProductReview.parquet',
        'table_name': 'Production_ProductReview',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ProductSubcategory': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ProductSubcategory.parquet',
        'table_name': 'Production_ProductSubcategory',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_ScrapReason': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_ScrapReason.parquet',
        'table_name': 'Production_ScrapReason',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_TransactionHistory': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_TransactionHistory.parquet',
        'table_name': 'Production_TransactionHistory',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_TransactionHistoryArchive': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_TransactionHistoryArchive.parquet',
        'table_name': 'Production_TransactionHistoryArchive',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_UnitMeasure': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_UnitMeasure.parquet',
        'table_name': 'Production_UnitMeasure',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_WorkOrder': {
        'file_path': '/mnt/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_WorkOrder.parquet',
        'table_name': 'Production_WorkOrder',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Production_WorkOrderRouting': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Production/Production_WorkOrderRouting.parquet',
        'table_name': 'Production_WorkOrderRouting',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Purchasing_ProductVendor': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Purchasing/Purchasing_ProductVendor.parquet',
        'table_name': 'Purchasing_ProductVendor',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Purchasing_PurchaseOrderDetail': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Purchasing/Purchasing_PurchaseOrderDetail.parquet',
        'table_name': 'Purchasing_PurchaseOrderDetail',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Purchasing_PurchaseOrderHeader': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Purchasing/Purchasing_PurchaseOrderHeader.parquet',
        'table_name': 'Purchasing_PurchaseOrderHeader',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Purchasing_ShipMethod': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Purchasing/Purchasing_ShipMethod.parquet',
        'table_name': 'Purchasing_ShipMethod',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Purchasing_Vendor': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Purchasing/Purchasing_Vendor.parquet',
        'table_name': 'Purchasing_Vendor',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_CountryRegionCurrency': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_CountryRegionCurrency.parquet',
        'table_name': 'Sales_CountryRegionCurrency',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_CreditCard': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_CreditCard.parquet',
        'table_name': 'Sales_CreditCard',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_Currency': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_Currency.parquet',
        'table_name': 'Sales_Currency',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_CurrencyRate': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_CurrencyRate.parquet',
        'table_name': 'Sales_CurrencyRate',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_Customer': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_Customer.parquet',
        'table_name': 'Sales_Customer',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_PersonCreditCard': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_PersonCreditCard.parquet',
        'table_name': 'Sales_PersonCreditCard',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_SalesOrderDetail': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_SalesOrderDetail.parquet',
        'table_name': 'Sales_SalesOrderDetail',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_SalesOrderHeader': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_SalesOrderHeader.parquet',
        'table_name': 'Sales_SalesOrderHeader',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_SalesOrderHeaderSalesReason': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_SalesOrderHeaderSalesReason.parquet',
        'table_name': 'Sales_SalesOrderHeaderSalesReason',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_SalesPerson': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_SalesPerson.parquet',
        'table_name': 'Sales_SalesPerson',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_SalesPersonQuotaHistory': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_SalesPersonQuotaHistory.parquet',
        'table_name': 'Sales_SalesPersonQuotaHistory',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_SalesReason': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_SalesReason.parquet',
        'table_name': 'Sales_SalesReason',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_SalesTaxRate': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_SalesTaxRate.parquet',
        'table_name': 'Sales_SalesTaxRate',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_SalesTerritory': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_SalesTerritory.parquet',
        'table_name': 'Sales_SalesTerritory',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_SalesTerritoryHistory': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_SalesTerritoryHistory.parquet',
        'table_name': 'Sales_SalesTerritoryHistory',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_ShoppingCartItem': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_ShoppingCartItem.parquet',
        'table_name': 'Sales_ShoppingCartItem',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_SpecialOffer': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_SpecialOffer.parquet',
        'table_name': 'Sales_SpecialOffer',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_SpecialOfferProduct': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_SpecialOfferProduct.parquet',
        'table_name': 'Sales_SpecialOfferProduct',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'Sales_Store': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/Sales/Sales_Store.parquet',
        'table_name': 'Sales_Store',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'dbo_DatabaseLog': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/dbo/dbo_DatabaseLog.parquet',
        'table_name': 'dbo_DatabaseLog',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    },
    'dbo_ErrorLog': {
        'file_path': '/mnt/adlsadvwrksprd/landing-zone/AdventureWorksOLTP/Full_load/dbo/dbo_ErrorLog.parquet',
        'table_name': 'dbo_ErrorLog',
        'database_name': 'adventure_works_bronze',
        'input_format': 'parquet'
    }
}
