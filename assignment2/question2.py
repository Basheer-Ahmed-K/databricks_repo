# Databricks notebook source
# MAGIC %run ./schema

# COMMAND ----------

pip install requests

# COMMAND ----------

import requests
import json
from pyspark.sql.types import *
from pyspark.sql.functions import explode, split, current_date

# COMMAND ----------

response_data = requests.get('https://reqres.in/api/users?page=2')
json_data = response_data.json()

# COMMAND ----------

df = spark.createDataFrame([json_df], custom_schema)

# COMMAND ----------

df = df.drop('page', 'per_page', 'total', 'total_pages', 'support')

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df = df.withColumn('data', explode('data'))

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df = df.withColumn("id", df.data.id).withColumn('email', df.data.email).withColumn('first_name', df.data.first_name).withColumn('last_name', df.data.last_name).withColumn('aatar', df.data.avatar).drop(df.data)

# COMMAND ----------

derived_site_address_df = df.withColumn("site_address",split(df["email"],"@")[1])

# COMMAND ----------

loaded_date = derived_site_address_df.withColumn('load_date', current_date())

# COMMAND ----------

loaded_date.write.format('delta').mode('overwrite').save('dbfs:/FileStore/assignments/question2/site_info/person_info')

# COMMAND ----------

testing_df = spark.read.format('delta').load('dbfs:/FileStore/assignments/question2/site_info/person_info')
