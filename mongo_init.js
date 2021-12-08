mongosh "mongodb://root:password@mongodb_container:27017/planeador_eventos_api"
mongosh -u root -p password --authenticationDatabase admin
use planeador_eventos_api
db.createUser(
    { user: "root",
      pwd: "password",
      roles: [ { role: "readWrite", db: "planeador_eventos_api" } ]
    }
)

db.services.createIndex( { long_lat : "2dsphere" } )