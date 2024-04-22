# Databricks notebook source
# MAGIC %run ./utils

# COMMAND ----------

# DBTITLE 1,Read Datasets as Dataframe
employee_read_path = 'dbfs:/FileStore/assignments/questoin1/resources/Employee_Q1.csv'
department_read_path = 'dbfs:/FileStore/assignments/questoin1/resources/Department_Q1.csv'
country_read_path = 'dbfs:/FileStore/assignments/questoin1/resources/Country_Q1.csv'

# COMMAND ----------

employee_df = read_csv(employee_read_path)
department_df = read_csv(department_read_path)
country_df = read_csv(country_read_path)

# COMMAND ----------

# DBTITLE 1,Write to Location
employee_write_path = 'dbfs:/FileStore/assignments/source_to_bronze/employee'
department_write_path = 'dbfs:/FileStore/assignments/source_to_bronze/department'
country_write_path = 'dbfs:/FileStore/assignments/source_to_bronze/country'

# COMMAND ----------

write_csv(employee_df, employee_write_path)
write_csv(department_df, department_write_path)
write_csv(country_df, country_write_path)
