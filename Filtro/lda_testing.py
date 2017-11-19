from nltk.stem.porter import PorterStemmer
from nltk.tokenize import RegexpTokenizer

import gensim
from gensim import corpora, models
from stop_words import get_stop_words

tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('es')

# Create p_stemmer of class PorterStemmer
p_stemmer = PorterStemmer()
    
# create sample documents

tweets = ['@sweets_emotions en todos los centros de acopio muchas gracias por ayudar',
 '#fuerzaméxico 🇲 🇽 #rescateprimero 🙏 🏻',
 'jamás olvidaré todo lo que he visto hoy mi gente mi país si podemos salir adelante #fuerzamexico',
 'en chatapas estaremos ofreciendo comida gratis a voluntarios y afectados por el sismo si alguien desea ayudar los esperamos',
 '#fuerzaméxico #noshemoslevantadodepeores #sisepuede 🇲 🇽 en coyoacán',
 '22/09 20:20 #voluntarios entrada plaza galerías en bicis para ir de acopio en acopio para lo que se necesiten 10 a 10:30 pm #ayudacdmx',
 'enhorabuena la banda de heavy metal @slipknot donó medicamentos para los afectados del #sismo 👏 👏 #mexico',
 'todas las redes de #wifi de #telmex #infinitum son abiertas a la comunidad con la contraseña 803261 #ayuda #sismo #fuerzamexico #cdmx',
 'urge escalera de 5 metros en derrumbe de escocia y gabriel mancera si conocen a algún vecino que tenga una láncese para acá por fa',
 '#confirmado frida sofía la niña del #rébsamen habló con sus rescatistas y dice q habla con 5 compañeros más ojalá así sea 🙏 #fuerzaméxico',
 'su necesitas ayuda para encontrar personas comunicate al 55 3993 9549',
 'centro de acopio se encuentra en la explanada del @parquemexico @lacondesa_',
 'raza hay fugas de gas en áreas cercanas a centro de acopio #parquemexico #brigadistas usen tapabocas no fumen y apaguen celulares #rt',
 'sismo se sintió duro',
 'despliega @gobcdmx 50 mil elementos en labores de rescate y atención por sismo de 7.1 grados en la escala de richter',
 'aún hay trabajo que hacer #fuerzamexico #prayformexico',
 'por qué el gobierno de méxico no aceptó la ayuda del gobierno de suiza qué esconde eso qué protagonismos proteje #sismo',
 'hoy se suspenden actividades en el centro regional de cultura de toluca hasta nuevo aviso #fuerzamexico #mexicounido',
 'se necesitan herramientas víveres y medicamentos en la col roma #verificado19s',
 'lo que importa es la unión y ayudar a los que nos necesitan #ayudacdmx #fuerzamexico',
 'y así se lleva méxico en la piel 🇲 🇽 💔 #fuerzaméxico',
 '🔴 #actualización ⚡ total 324 fallecidos por #sismo 19/09 17 #cdmx 186 #morelos 73 #puebla 45 #edoméx 13 #guerrero 6 #oaxaca 1',
 'cuando le dan like o dan a poetuits se entorpece la ayuda dejen que pase un tiempo y ya rinden pleitesía o dan eco a influencers',
 '12 horas interminables hoy le doy asilo a mi familia mañana salimos en ayuda a otras familias 🙏 🏻 #fuerzaméxico',
 '#méxicoestádepie #mexicounido #ayudacdmx todos lo que puedan ayudar háganlo por mas poco que sea todo es buena ayuda en estos momentos 💔',
 '#mexicanosunidos #fuerzaméxico 🙏 ❤',
 'el gobernador alfredo del mazo confirma al menos dos muertes en el estado de méxico por sismo de magnitud 7.1',
 '#entérate informa condusef que suspende plazos y procedimientos tras sismo #abriendolaconversación',
 '\U0001f91d el actor @diegoluna_ continúa en el centro de acopio de lago de tanganica 67 en polanco \U0001f91d solicita tanques de ox',
 'ayúdenme a encontrarlo por favor #sismo',
 'bien lo decía un tuit que leí si tenían hambre se hubieran acercado a un centro de acopio pidiendo ayuda #tuiterosvendidos',
 'se nota la diferente reacción de la gente con la #alertasismica :(',
 '#sntesolidario alista secc 44 durango envió de víveres #ayudaciudadana por #temblor al magisterio y sociedad',
 'es tan conmovedor ver el apoyo que recibe méxico de otros países mil gracias #fuerzaméxico #méxicodepie',
 'aquí se necesitan víveres']

doc_a = "Brocolli is good to eat. My brother likes to eat good brocolli, but not my mother."
doc_b = "My mother spends a lot of time driving my brother around to baseball practice."
doc_c = "Some health experts suggest that driving may cause increased tension and blood pressure."
doc_d = "I often feel pressure to perform well at school, but my mother never seems to drive my brother to do better."
doc_e = "Health professionals say that brocolli is good for your health." 

# compile sample documents into a list
doc_set = [doc_a, doc_b, doc_c, doc_d, doc_e]

# list for tokenized documents in loop
texts = []

# loop through document list
for i in tweets:
	# clean and tokenize document string	
	raw = i.lower()
	tokens = tokenizer.tokenize(raw)
	# remove stop words from tokens
	stopped_tokens = [i for i in tokens if not i in en_stop]
	
	# stem tokens
	stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]
	
	# add tokens to list
	texts.append(stemmed_tokens)

# turn our tokenized documents into a id <-> term dictionary
dictionary = corpora.Dictionary(texts)
    
# convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=50, id2word = dictionary, passes=20)

print(ldamodel)

print(ldamodel.print_topics(num_topics=2, num_words=4))
