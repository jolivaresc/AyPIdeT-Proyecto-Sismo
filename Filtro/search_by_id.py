#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pymongo import MongoClient
from bson.objectid import ObjectId
from nltk.tokenize import TweetTokenizer


try:
	client = MongoClient()
	print("Connected to MongoDB\n")
except pymongo.errors.ConnectionFailure as e:
	print("Could not connect to MongoDB",e)

db = client.sept2017_db
tweets = db.sept2017_collection

tknzr = TweetTokenizer(preserve_case=False,       # Convertir a minúsculas
                       reduce_len=True,           # Reducir caracteres repetidos
                       strip_handles=False)       # Mostrar @usuarios


tweet = tknzr.tokenize(db.sept2017_collection.find_one({'_id': ObjectId('59e55c370e0bab1d26640d94') }).get('text'))

print(tweet)
