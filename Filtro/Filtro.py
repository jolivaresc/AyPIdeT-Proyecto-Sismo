
# coding: utf-8

# # Dependencies

# In[2]:

#!/usr/bin/env python


#import json
from pymongo import MongoClient
from nltk.tokenize import TweetTokenizer #, word_tokenize
#from keras.preprocessing.text import text_to_word_sequence


# # Conexión a DB

# In[3]:

try:
	client = MongoClient()
	print("Connected to MongoDB\n")
except pymongo.errors.ConnectionFailure as e:
	print("Could not connect to MongoDB",e)


# # Seleccionar BD y colección

# In[4]:

db = client.sept2017_db
tweets = db.sept2017_collection


# # Lista para filtro y tokenización
# * `filtro`: Lista para buscar palabras clave dentro del tweet
# * `ids`: set para guardar los tweets por id que contengan palabras clave para después hacer consulta a la BD por medio de su ID
# * `tknzr`: Tokenizador de tweets

# In[5]:

filtro = ["sismo", "albergue", "acopio", "víveres", "viveres", "alerta", "sísmica",
          "sismica", "ayuda", "#Verificado19S","19s"]
ids = set()
tknzr = TweetTokenizer(preserve_case=False,       # Convertir a minúsculas
                       reduce_len=True,           # Reducir caracteres repetidos
                       strip_handles=False)       # Mostrar @usuarios


# In[5]:

for i in tweets.find():
    if "retweeted_status" in i:
        tmp = tknzr.tokenize(i["retweeted_status"]['text'])
        for key in filtro:
            if key in tmp:
                #print(i["_id"],tmp)
                ids.add(i["_id"])
    else:
        tmp = tknzr.tokenize(i['text'])
        for key in filtro:
            if key in tmp:
                #print(i["_id"],tmp)
                ids.add(i["_id"])


# # Escribir IDs en archivo

# In[6]:

ids_file = open('ids.dat', 'w')
for item in ids:
    ids_file.write(str(item)+"\n")
ids_file.close()


# In[ ]:

'''
db.sept2017_collection.find(ObjectId('59e55c2d0e0bab1d2663dff6')).
forEach(function(tweet){print(tweet.text)})
'''
