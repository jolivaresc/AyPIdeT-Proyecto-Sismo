# CÓDIGO DE PRUEBA
# coding: utf-8

# # Dependencies

# In[2]:

#!/usr/bin/env python

from pymongo import MongoClient
from datetime import datetime as dt

# # Conexión a DB

# In[3]:

try:
	client = MongoClient()
	print("Connected to MongoDB\n")
except pymongo.errors.ConnectionFailure as e:
	print("Could not connect to MongoDB",e)


# # Seleccionar BD y colección

# In[4]:

# Tomar tweets de BD completa
my_db = "fechasdb"
my_collection = "fechascoll"

db = client[my_db]
tweets = db[my_collection]

# Nueva BD con tweets de 19 al 26 de septiembre
'''
db_new = client.sept19_26_db
tweets_new = db_new.sept19_26_collection

'''
# Buscar tweets dentro del rango de fechas en BD
query = {
            'created_at':
            {
                "$gte":"Mon Oct 16 2017 11:55:58 GMT-0500 (CDT)",
                "$lte":"Mon Oct 16 2017 11:56:09 GMT-0500 (CDT)"
            }
        }

for tw in tweets.find(query):
    print(tw["text"],tw["created_at"])


# forEach(function(t){print(t.created_at)})
