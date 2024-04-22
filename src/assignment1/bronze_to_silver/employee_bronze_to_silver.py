# Databricks notebook source
from pyspark.sql.types import StructType, StructField, StringType, IntegerType

# COMMAND ----------

# MAGIC %run /Users/ba184279@gmail.com/assignment/assignment1/source_to_bronze/utils

# COMMAND ----------

# DBTITLE 1,Employee Schema
# EmployeeID	EmployeeName	Department	Country	Salary	Age
employee_custom_schema = StructType([
    StructField('EmployeeID', IntegerType(), True),
    StructField('EmployeeName', StringType(), True),
    StructField('Department', StringType(), True),
    StructField('Country', StringType(), True),
    StructField('Salary', IntegerType(), True),
    StructField('Age', IntegerType(), True)
])

# COMMAND ----------

# DBTITLE 1,Country Schema
# CountryCode	CountryName
country_custom_schema = StructType([
    StructField('CountryCode', StringType(), True),
    StructField('CountryName', StringType(), True)
])

# COMMAND ----------

# DBTITLE 1,Department Schema
# DepartmentID	DepartmentName
department_custom_schema = StructType([
    StructField('DepartmentID', StringType(), True),
    StructField('DepartmentName', StringType(), True)
])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Creating Dataframe using Custom Schema

# COMMAND ----------

employee_csv_path = '''dbfs:/FileStore/assignments/source_to_bronze/employee/part-00000-tid-4147078833494815971-b342c1bd-1fa5-4381-b0a9-cf13656d4014-35-1-c000.csv'''
country_csv_path = '''dbfs:/FileStore/assignments/source_to_bronze/country/part-00000-tid-2209771695011875465-8c5e33ab-7eab-477f-9ccf-e9d30663a02d-37-1-c000.csv'''
department_csv_path = '''dbfs:/FileStore/assignments/source_to_bronze/department/part-00000-tid-5778909917105095575-026680bc-bb7a-4dcb-9968-a77d1a6bc66a-36-1-c000.csv'''

# COMMAND ----------

employee_df = read_with_custom_schema(employee_csv_path,employee_custom_schema)
country_df = read_with_custom_schema_format(country_csv_path, country_custom_schema)
department_df = read_with_custom_schema(department_csv_path, department_custom_schema)

# COMMAND ----------

employee_snake_case_df = camel_to_snake_case(employee_df)

# COMMAND ----------

department_snake_case_df = camel_to_snake_case(department_df)

# COMMAND ----------

country_snake_case_df = camel_to_snake_case(country_df)

# COMMAND ----------

# DBTITLE 1,Adding load_date in df
employee_with_date_df = add_current_date(employee_snake_case_df)

# COMMAND ----------

department_with_date_df = add_current_date(department_snake_case_df)

# COMMAND ----------

country_with_date_df = add_current_date(country_snake_case_df)

# COMMAND ----------

# DBTITLE 1,creating employee_info database
spark.sql('create database employee_info')
spark.sql('use employee_info')

# COMMAND ----------

employee_df.write.option('path', 'dbfs:/FileStore/assignments/questoin1/silver/employee_info/dim_employee').saveAsTable('dim_employee')
