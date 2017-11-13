/*
* Código para cambiar el formato de fecha de los tweets para poder realizar
* comparaciones entre fechas
*/


conn = new Mongo();                           // Conexión a MongoDB

db = conn.getDB("sept2017_db");               // Usar BD de septiembre



/*
cursor = db.sept2017_collection.find();
while (cursor.hasNext()) {
  printjson(cursor.next().created_at)
}*/

// Cambio de formato a las fechas de creación de los tweets.
db.sept2017_collection.find()
  .forEach(function(t){
    t.created_at = new Date(t.created_at)     // Casting
    db.sept2017_collection.save(t)
});

print("Filtrando por fechas...")

new_db = conn.getDB("sept19_26_db");          // Nueva BD para tweets del 19 al 26 sept.


db.sept2017_collection.find(
  {             // Query
    "created_at":
    {           // rango de fechas
      $gte:new Date("Tue Sep 19 2017 00:00:00 GMT-0500 (CDT)"),
      $lte:new Date("Tue Sep 26 2017 23:59:59 GMT-0500 (CDT)")
    }
  }).forEach(function(t){
                // Insertar tweets dentro del rango en nueva BD
    new_db.sept19_26_collection.insert(t);
  })
