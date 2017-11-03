# CÓDIGO DE PRUEBA
# coding: utf-8

# # Dependencies

# In[2]:

#!/usr/bin/env python

from pymongo import MongoClient

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
my_db = "sept2017_db"
my_collection = "sept2017_collection"

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
                #"$gt":"Tue Sep 19 00:00:01 +0000 2017",
                "$gt":"Tue Sep 19 00:00:05 +0000 2017",
                #"$lt":"Mon Oct 16 23:59:59 +0000 2017"
                "$lt":"Tue Sep 26 23:56:09 +0000 2017"
            }
        }

for tw in tweets.find(query):
    print(tw["text"],tw["created_at"])

client.close()
