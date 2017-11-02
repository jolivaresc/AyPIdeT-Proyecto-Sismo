#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId
from nltk.tokenize import TweetTokenizer
from datetime import datetime as dt


try:
	client = MongoClient()
	print("Connected to MongoDB\n")
except pymongo.errors.ConnectionFailure as e:
	print("Could not connect to MongoDB",e)

db = client.sept2017_db
tweets = db.sept2017_collection

fecha1 = "Tue Sep 19 00:00:01 +0000 2017"
fecha_inicio = dt.strptime(fecha1,'%a %b %d %H:%M:%S +0000 %Y')
print(fecha_inicio)

fecha2 = "Tue Sep 26 23:59:59 +0000 2017"
fecha_fin = dt.strptime(fecha2,'%a %b %d %H:%M:%S +0000 %Y')
print(fecha_fin)

tknzr = TweetTokenizer(preserve_case=False,       # Convertir a minúsculas
                       reduce_len=True,           # Reducir caracteres repetidos
                       strip_handles=False)       # Mostrar @usuarios


id_tweet = tknzr.tokenize(tweets.find_one({'_id': ObjectId('59e55c370e0bab1d26640d94') }).get('text'))
#fecha_tweet = tknzr.tokenize(tweets.find_one({"created_at": {"$gte":dt(2017,9,19),"$lt":dt(2017,9,26)}}).get('text'))

print(id_tweet)
