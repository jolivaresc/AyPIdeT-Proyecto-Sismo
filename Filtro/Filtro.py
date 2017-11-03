
# coding: utf-8

# # Filtro de tweets
# 
# * De la BD que contiene los tweets de septiembre 2017, se buscan sólo los que se encuentran entre las fechas del 19 al 26, de los tweets obtenidos se filtran por palabras clave para crear una nueva BD con tweets relevantes ocurridos dentro del periodo de interés y se guardan en un archivo los IDs de los tweets obtenidos. (INCOMPLETO)
#     
#     **NOTA:** En la BD sólo hay tweets del día 19 y 20 de septiembre.
# 
# 
# * La nueva BD sirve para obtener las relaciones paradigmáticas de las palabras clave para hacer más completa la lista y poder extraer más resultados que pudieron haber sido omitidos una primera pasada del filtro. (FALTA)
# 
# 

# # Dependencies

# In[1]:

#!/usr/bin/env python


from pymongo import MongoClient
from nltk.tokenize import TweetTokenizer 


# # Conexión a MongoDB

# In[2]:

try:
    client = MongoClient()
    print("Connected to MongoDB\n")
except pymongo.errors.ConnectionFailure as e:
    print("Could not connect to MongoDB",e)


# # Seleccionar BD y colección
# BD de todo septiembre.

# In[3]:

db = client.sept2017_db
tweets = db.sept2017_collection


# # Nueva BD 
# Se crea una nueva BD con tweets dentro del periodo del 19 al 26 de septiembre.
# 

# In[4]:

db_new = client.sept19_26_db
tweets_new = db_new.sept19_26_collection


# # Consultar BD
# Buscar tweets dentro de un rango de fechas en BD.

# In[5]:

fecha = ["Tue Sep 19 00:00:00 +0000 2017","Wed Sep 20 14:59:58 +0000 2017"]
query = {
            'created_at' :
            {
                "$gte":"Wed Sep 20 14:59:58 +0000 2017"
            }
        }


# # Lista para filtro de palabras clave y tokenización de tweets
# * `filtro`: Lista para buscar palabras clave dentro del tweet
# * `ids`: set para guardar los tweets por id que contengan palabras clave para después hacer consulta a la BD por medio de su ID
# * `tknzr`: Tokenizador de tweets

# In[6]:

filtro = ["sismo", "albergue", "acopio", "víveres", "viveres", "alerta", "sísmica",
          "sismica", "ayuda", "#Verificado19S","19s","derrumbe","colecta","#fuerzamexico",
          "#fuerzaméxico"]

IDs = set()

tknzr = TweetTokenizer(preserve_case=False,       # Convertir a minúsculas
                       reduce_len=True,           # Reducir caracteres repetidos
                       strip_handles=False)       # Mostrar @usuarios


# # Se obtienen tweets relevantes

# In[9]:

for i in tweets.find({
                        "created_at":
                        {
                            "$gte":"Tue Sep 19 00:00:00 +0000 2017"
                        }
                    }):
    if "retweeted_status" in i:           # Si es retweet...
        tmp = tknzr.tokenize(i["retweeted_status"]['text'])
        for key in filtro:               # Para buscar palabras clave dentro del tweet
            if key in tmp:
                #print(i["created_at"])
                #IDs.add(i["_id"])
                try:                     # Insertar tweet con palabras clave en nueva BD
                    insertar = tweets_new.insert_one(i)
                except Exception as e:
                    #print("Error:",e)
                    pass

    else:                                # Si no es retweet...
        tmp = tknzr.tokenize(i['text'])
        for key in filtro:
            if key in tmp:
                #print(i["created_at"])
                #IDs.add(i["_id"])
                try:
                    insertar = tweets_new.insert_one(i)
                except Exception as e:
                    #print("Error:",e)
                    pass


# # Escribir IDs en archivo

# In[ ]:

if True:
    IDs_file = open('IDs.dat', 'w')
    for item in IDs:
        IDs_file.write(str(item)+"\n")
    IDs_file.close()


# 
