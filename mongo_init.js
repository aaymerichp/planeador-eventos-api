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

db.users.deleteMany({})
db.providers.deleteMany({})
db.services.deleteMany({})
db.products.deleteMany({})
db.events.deleteMany({})
db.payments.deleteMany({})

db.users.insertOne(
    {
        "email": "nologin@gmail.com",
        "image": "https://cdn.business2community.com/wp-content/uploads/2017/08/blank-profile-picture-973460_640.png",
        "is_active": true,
        "name": "Planeador Proveedor",
        "phone": "88888888",
        "type": "PROVIDER",
        "uuid": "a11d39d6-bdbd-4f08-92cd-0dce38ddbd27"
    }
);

db.providers.insertOne(
    {
        "company_name": "string",
        "subscription": "PREMIUM",
        "user": "a11d39d6-bdbd-4f08-92cd-0dce38ddbd27",
        "uuid": "d011b895-0766-444a-9fa3-06075775b67d"
    }
);

db.services.insertMany(
[
    {
		"uuid": "41363596-b24b-409d-88b0-4ae12a628d21",
        "provider": "d011b895-0766-444a-9fa3-06075775b67d",
        "name": "Fotos Fantasia",
        "description": "Paquetes para todo tipo de evento.",
        "type": "Fotografía",
        "image": "https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Ffoto.jpeg?alt=media&token=d6a87371-1f97-414f-928d-e30520ff940c",
        "provincia": "Alajuela",
        "canton": "",
        "is_active": true,
        "long_lat": {
            "type": "Point",
            "coordinates": [10.058082883459361, -84.08186609499008]
        }
    },
	{
		"uuid": "8a00627e-9c25-43cd-b1b9-81839d5f9d21",
        "provider": "d011b895-0766-444a-9fa3-06075775b67d",
        "name": "Decoraciónes Cascante",
        "description": "Ofrecemos servicios con diseños de moda.",
        "type": "Decoración",
        "image": "https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fdeco.jpeg?alt=media&token=70f05ba7-8695-469d-be66-001f705fd62b",
        "provincia": "San José",
        "canton": "",
        "is_active": true,
        "long_lat": {
            "type": "Point",
            "coordinates": [10.058082883459361, -84.08186609499008]
        }
    },
	{
		"uuid": "39ead6de-98ac-4519-84b2-2943bad07086",
        "provider": "d011b895-0766-444a-9fa3-06075775b67d",
        "name": "Sweet-Life",
        "description": "Deliciosos postres.",
        "type": "Pastelería",
        "image": "https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fpasteleria.jpeg?alt=media&token=9327b4f2-154b-4a09-9ee1-0a1a951b99fa",
        "provincia": "Cartago",
        "canton": "Montes de oca",
        "is_active": true,
        "long_lat": {
            "type": "Point",
            "coordinates": [10.058082883459361, -84.08186609499008]
        }
    },
	{
		"uuid": "e820e561-2225-426b-ac66-be4b8a254470",
        "provider": "d011b895-0766-444a-9fa3-06075775b67d",
        "name": "Catering Deluxe",
        "description": "Comidas para eventos de toda hora.",
        "type": "Alimentos y bebidas",
        "image": "https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fcomidas.jpeg?alt=media&token=83409e87-47a2-4a42-ba4e-5731a2cb0b35",
        "provincia": "Alajuela",
        "canton": "Montes de oca",
        "is_active": true,
        "long_lat": {
            "type": "Point",
            "coordinates": [10.058082883459361, -84.08186609499008]
        }
    },
	{
		"uuid": "fc513f4c-eef8-4863-8ee7-e73d044f287b",
        "provider": "d011b895-0766-444a-9fa3-06075775b67d",
        "name": "Banda: Maria y sus amigos",
        "description": "Musica en vivo",
        "type": "Música",
        "image": "https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fmusica.jpeg?alt=media&token=cacca59e-93e0-4ca7-88b5-81495cc157d9",
        "provincia": "Alajuela",
        "canton": "Montes de oca",
        "is_active": true,
        "long_lat": {
            "type": "Point",
            "coordinates": [10.058082883459361, -84.08186609499008]
        }
    },
	{
		"uuid": "e48f265f-85aa-4b7d-a62c-c79b6201f53c",
        "provider": "d011b895-0766-444a-9fa3-06075775b67d",
        "name": "Pereira y asociados",
        "description": "Ofrecemos servicios legales.",
        "type": "Servicios legales",
        "image": "https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Flegales.jpeg?alt=media&token=042b6764-f2eb-492c-bbee-e650f9fc0f1f",
        "provincia": "Alajuela",
        "canton": "Montes de oca",
        "is_active": true,
        "long_lat": {
            "type": "Point",
            "coordinates": [10.058082883459361, -84.08186609499008]
        }
    },
	{
		"uuid": "1ae4376b-55cd-49d7-bed8-9260305151a2",
        "provider": "d011b895-0766-444a-9fa3-06075775b67d",
        "name": "Luz es vida",
        "description": "Le damos vida a su evento con nuestros servicios.",
        "type": "Luces y escenografía",
        "image": "https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fluces.jpeg?alt=media&token=e95140ac-dffe-4a95-8275-6e8c0805abc7",
        "provincia": "Alajuela",
        "canton": "Montes de oca",
        "is_active": true,
        "long_lat": {
            "type": "Point",
            "coordinates": [10.058082883459361, -84.08186609499008]
        }
    },
	{
		"uuid": "7b83aa1b-4b47-4246-98f4-bce447cf3149",
        "provider": "d011b895-0766-444a-9fa3-06075775b67d",
        "name": "WA Animaciones CR",
        "description": "Música, dinámicas, juegos, maquina de burbujas, luces, entre otros...",
        "type": "Animación",
        "image": "https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fanimacion.jpeg?alt=media&token=3e27d907-ce4c-4363-a16d-6b777bb53a91",
        "provincia": "Alajuela",
        "canton": "Montes de oca",
        "is_active": true,
        "long_lat": {
            "type": "Point",
            "coordinates": [10.058082883459361, -84.08186609499008]
        }
    }
]
);

//Servicios legales
db.products.insertOne(
    {
        "description": "Servicios de notariado para su boda",
        "image": "http://ghp.cr/wp-content/uploads/2017/03/notarial-img-1170x780.jpg",
        "is_active": true,
        "name": "Notariado para boda",
        "price": 100000,
        "rate_type": "Absoluto",
        "service": "e48f265f-85aa-4b7d-a62c-c79b6201f53c",
        "uuid": "3bcf7eb2-574a-4c9c-8ede-2374fe9b75bd"
    }
);
//Luces y escenografía
db.products.insertMany([
    {
        "description": "Luces para exteriores",
        "image": "https://cdn.christmaslightsetc.com/images/CategoryDetail/63642/backyard_deck_patio_string_lights_5540.jpg",
        "is_active": true,
        "name": "Luces para exteriores",
        "price": 1000000,
        "rate_type": "Por hora",
        "service": "1ae4376b-55cd-49d7-bed8-9260305151a2",
        "uuid": "9dbb3c25-f9f0-4e06-aef1-a749e29d5459"
    },
    {
        "description": "Pinocho, actuado por profesionales.",
        "image": "https://edm.com/.image/c_limit%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTUyOTU2NzQ2MDExMjU1ODE1/markusschulz-laser-lightshow.webp",
        "is_active": true,
        "name": "Pinocho, actuado por profesionales.",
        "price": 1000000,
        "rate_type": "Absoluto",
        "service": "1ae4376b-55cd-49d7-bed8-9260305151a2",
        "uuid": "8886dcc3-ea27-4930-be0a-69769fbe6896"
    },
    {
        "description": "Luces y pantallas de humo para todos sus eventos",
        "image": "https://edm.com/.image/c_limit%2Ccs_srgb%2Cq_auto:good%2Cw_1200/MTUyOTU2NzQ2MDExMjU1ODE1/markusschulz-laser-lightshow.webp",
        "is_active": true,
        "name": "Luces de baile",
        "price": 1000000,
        "rate_type": "Por persona",
        "service": "1ae4376b-55cd-49d7-bed8-9260305151a2",
        "uuid": "06a740a9-f74e-4585-82aa-5fdb3f8aced1"
    }
    ]
);
//Animacion
db.products.insertMany([
    {
        "description": "Narrador de juegos de bingo",
        "image": "https://www.newbingosites.biz/wp-content/uploads/2015/02/bingo-caller.jpg",
        "is_active": true,
        "name": "Ricardo Hernandez Llamador de Bingo",
        "price": 1000000,
        "rate_type": "Por hora",
        "service": "7b83aa1b-4b47-4246-98f4-bce447cf3149",
        "uuid": "482b1cb2-f2e3-4956-8639-bee12151544a"
    },
    {
        "description": "Payasos para sus fiestas infantiles",
        "image": "https://www.tedxpuravida.org/wp-content/uploads/2017/01/hernan-jimenez-200x200.jpg",
        "is_active": true,
        "name": "Payasos Pirulos",
        "price": 150000,
        "rate_type": "Por hora",
        "service": "7b83aa1b-4b47-4246-98f4-bce447cf3149",
        "uuid": "05b4eb75-0426-4e2d-a236-d5a7eee502e8"
    },
    {
        "description": "Reir por montones",
        "image": "https://www.tedxpuravida.org/wp-content/uploads/2017/01/hernan-jimenez-200x200.jpg",
        "is_active": true,
        "name": "Hernan Jimenez Stand-up Comedy",
        "price": 1000000,
        "rate_type": "Absoluto",
        "service": "7b83aa1b-4b47-4246-98f4-bce447cf3149",
        "uuid": "241f7b0a-40b5-496b-90f8-e98334465c2c"
    }
]
);

//Decoración
db.products.insertMany([
	{
	  "service": "8a00627e-9c25-43cd-b1b9-81839d5f9d21",
	  "name":"Arreglo Floral Primaveral",
	  "description": "Arreglo de diversas flores frescas",
	  "price": 55000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fprimaveral.jpeg?alt=media&token=aa9b0e29-2180-4e76-aea6-d443bafd457d",
	  "rate_type": "Absoluto",
	  "uuid": "5b592efd-446e-4c55-9772-ed52380adc00"
	},
	{
	  "service": "8a00627e-9c25-43cd-b1b9-81839d5f9d21",
	  "name":"Rosas",
	  "description": "Rosas para arreglos florales",
	  "price": 2000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Frosas.jpeg?alt=media&token=54ea46e2-7506-4f71-ba27-e4a8b37cf379",
	  "rate_type": "Absoluto",
	  "uuid": "66f4f38d-f211-4f3e-82ac-2ed4baedb4bb"
	},
	{
	  "service": "8a00627e-9c25-43cd-b1b9-81839d5f9d21",
	  "name":"Bucket de matrimonio",
	  "description": "Arreglo de flores personalizado para matrimonio",
	  "price": 20000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fbouquet.jpeg?alt=media&token=0719fdc9-112e-4d4c-82e6-df6fd9ab9917",
	  "rate_type": "Absoluto",
	  "uuid": "8425c784-a16c-4050-b33d-99b493505b55"
	}
]);

//Pastelería
db.products.insertMany([
	{
	  "service": "39ead6de-98ac-4519-84b2-2943bad07086",
	  "name": "Cupcakes",
	  "description": "Cupcake de sabor vainilla con relleno de dulce de leche y buttercream",
	  "price": 2000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fcupcakes.jpeg?alt=media&token=085d532c-c6a2-47e5-8169-581d906bdacd",
	  "rate_type": "Absoluto",
	  "uuid": "f49f591f-e8eb-4864-8a57-8f495d971d1e"
	},
	{
	  "service": "39ead6de-98ac-4519-84b2-2943bad07086",
	  "name":"Bocadillos para fiesta",
	  "description": "Paquete de 2 bocadillos salados y 2 bocadillos dulces ",
	  "price": 2000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fbocadillos.jpeg?alt=media&token=3fdcece8-b81a-40c2-af52-28e597ee8524",
	  "rate_type": "Persona",
	  "uuid": "6ecf2c64-4758-4397-a15a-ec72954b2eb7"
	},
	{
	  "service": "39ead6de-98ac-4519-84b2-2943bad07086",
	  "name":"Pastel de cumpleaños",
	  "description": "Pastel de cumpleaños con base de vainilla y buttercream",
	  "price": 30000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fcumple_cake.jpeg?alt=media&token=3b479ee8-f815-4812-a33e-51d0109e804b",
	  "rate_type": "Absoluto",
	  "uuid": "6d131552-ce1b-4fee-bd30-1e47830f14c6"
	}
]);

//Alimentos y bebidas
db.products.insertMany([
	{
	  "service": "e820e561-2225-426b-ac66-be4b8a254470",
	  "name":"Cena navideña familiar",
	  "description": "Paquete familiar que incluye plato fuerte, postre y bebida",
	  "price": 15000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fcenanavi.jpeg?alt=media&token=46bc0fc0-f3b6-42a8-b17e-0e0432b8a7de",
	  "rate_type": "Por Persona",
	  "uuid": "6c7a7b50-3beb-4b37-81eb-ac2992c2922b"
	},
	{
	  "service": "e820e561-2225-426b-ac66-be4b8a254470",
	  "name":"Desayuno Deluxe",
	  "description": "Incluye waffles, salsa de caramelo, frutos rojos, tocineta, queso, huevos",
	  "price": 10000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fdesayuno.jpeg?alt=media&token=9f752f64-3c10-498e-bf75-2ed87b0b657a",
	  "rate_type": "Por Persona",
	  "uuid": "bdec7ea7-1d36-40b2-bdbc-29eda5bf5635"
	},
	{
	  "service": "e820e561-2225-426b-ac66-be4b8a254470",
	  "name":"Cocteles de verano",
	  "description": "Paquete de 5 margaritas, 2 piñas coladas y 1 mojito",
	  "price": 35000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fcocteles.jpeg?alt=media&token=44372ffe-8a7a-458f-a425-f2d63f08345a",
	  "rate_type": "Por persona",
	  "uuid": "18ac645a-9615-496c-925f-e20ac5d93b20"
	}
]);

//Musica
db.products.insertMany([
	{
	  "service": "fc513f4c-eef8-4863-8ee7-e73d044f287b",
	  "name":"Grupo acústico",
	  "description": "Set de 15 canciones acústicas elegidas a gusto del cliente",
	  "price": 100000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Facust.jpeg?alt=media&token=5cb35577-a94a-408e-8977-2360298cc8ae",
	  "rate_type": "Por Hora",
	  "uuid": "e8b4e77b-4f93-4d9c-88d0-17405f81f001"
	},
	{
	  "service": "fc513f4c-eef8-4863-8ee7-e73d044f287b",
	  "name":"Música bailable para fiesta",
	  "description": "Mix de música elegida por el cliente",
	  "price": 75000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fmusicabailable.jpeg?alt=media&token=0c242e33-b3fd-4bd8-8d85-fdbfd72c8a96",
	  "rate_type": "Por Hora",
	  "uuid": "3da3130c-8c9d-4af9-8e88-f82576f94fee"
	},
	{
	  "service": "fc513f4c-eef8-4863-8ee7-e73d044f287b",
	  "name":"Mariachi",
	  "description": "10 Canciones clásicas de mariachis a elección del cliente",
	  "price": 120000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fmariachi.jpeg?alt=media&token=d15412f0-89d9-42fe-a637-645f764c0277",
	  "rate_type": "Por Hora",
	  "uuid": "b7b635e7-3a3a-4811-91ba-561e07c0139b"
	}
]);

//Fotografía
db.products.insertMany([
	{
	  "service": "41363596-b24b-409d-88b0-4ae12a628d21",
	  "name":"Sesión recién nacido",
	  "description": "Paquete de 20 fotos con traje y set decorativo incluido",
	  "price": 90000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fbabyphoto.jpeg?alt=media&token=c62a41e6-a237-41f4-8957-396f3dcfe447",
	  "rate_type": "Absoluto",
	  "uuid": "88ca910d-b693-4eb8-8364-5793124c097d"
	},
	{
	  "service": "41363596-b24b-409d-88b0-4ae12a628d21",
	  "name":"Paquete de fotos de boda",
	  "description": "Paquete de fotos incluye 25 fotos de novios y los familiares",
	  "price": 150000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fboda.jpeg?alt=media&token=3b73b781-d8b4-496c-8a07-75a0a2cf7ce2",
	  "rate_type": "Absoluto",
	  "uuid": "f092e50a-ab2c-4865-9b7a-c55315c39099"
	},
	{
	  "service": "41363596-b24b-409d-88b0-4ae12a628d21",
	  "name":"Sesión de cumpleaños infantil",
	  "description": "Paquete de 20 fotos que incluye vestuario y smash cake ",
	  "price": 110000,
	  "is_active":true,
	  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fkidpar.jpeg?alt=media&token=50c5076a-6e21-470f-a305-8c4b573330b0",
	  "rate_type": "Absoluto",
	  "uuid": "ffe1a990-103f-412f-b0b0-1cbe39d2f86c"
	}
]);

//Eventos
db.events.insertMany([
    {
    "area": [],
    "canton": [],
    "description": "Boda de Arturo y Angie",
    "finish_time": "2021-12-15T00:00:00.00000000",
    "guest_count": 300,
    "image": "@drawable/otros",
    "is_active": true,
    "long_lat": {
        "coordinates": [
            9.9141811,
            -84.2422125
        ],
        "type": "Point"
    },
    "name": "Boda de Arturo y Angie",
    "provincia": [
        "Heredia"
    ],
    "services": [
        {
            "products": [
                {
                    "rate_quantity": 1,
                    "uuid": "241f7b0a-40b5-496b-90f8-e98334465c2c"
                }
            ],
            "provider": "d011b895-0766-444a-9fa3-06075775b67d",
            "uuid": "7b83aa1b-4b47-4246-98f4-bce447cf3149"
        },
        {
            "provider": "d011b895-0766-444a-9fa3-06075775b67d",
            "uuid": "1ae4376b-55cd-49d7-bed8-9260305151a2",
            "products": [
                {
                    "rate_quantity": 300,
                    "uuid": "06a740a9-f74e-4585-82aa-5fdb3f8aced1"
                },
                {
                    "rate_quantity": 5,
                    "uuid": "9dbb3c25-f9f0-4e06-aef1-a749e29d5459"
                }
            ]
        },
        {
            "provider": "d011b895-0766-444a-9fa3-06075775b67d",
            "uuid": "e48f265f-85aa-4b7d-a62c-c79b6201f53c",
            "products": [
                {
                    "rate_quantity": 1,
                    "uuid": "3bcf7eb2-574a-4c9c-8ede-2374fe9b75bd"
                }
            ]
        }
    ],
    "start_time": "2021-12-15T00:00:00.00000000",
    "type": "Otro",
    "user": "a11d39d6-bdbd-4f08-92cd-0dce38ddbd27",
    "uuid": "f4924ac6-f31c-4a4b-bbdf-df3459b89980"
},
    {
        "area": [],
        "canton": [],
        "description": "Cumpleaños de Izahir",
        "finish_time": "2021-12-15T00:00:00.00000000",
        "guest_count": 15,
        "image": "@drawable/otros",
        "is_active": true,
        "long_lat": {
            "coordinates": [
                9.9141811,
                -84.2422125
            ],
            "type": "Point"
        },
        "name": "Cumpleaños de Izahir",
        "provincia": [
            "San José"
        ],
        "services": [
            {
                "amount": 15,
                "payment_due_date": "2021/12/01",
                "payment_status": "PAID",
                "payment_uuid": null,
                "products": [
                {
                  "service": "39ead6de-98ac-4519-84b2-2943bad07086",
                  "name": "Cupcakes",
                  "description": "Cupcake de sabor vainilla con relleno de dulce de leche y buttercream",
                  "price": 2000,
                  "is_active":true,
                  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fcupcakes.jpeg?alt=media&token=085d532c-c6a2-47e5-8169-581d906bdacd",
                  "rate_type": "Absoluto",
                  "uuid": "f49f591f-e8eb-4864-8a57-8f495d971d1e"
                },
                {
                  "service": "e820e561-2225-426b-ac66-be4b8a254470",
                  "name":"Cocteles de verano",
                  "description": "Paquete de 5 margaritas, 2 piñas coladas y 1 mojito",
                  "price": 35000,
                  "is_active":true,
                  "image":"https://firebasestorage.googleapis.com/v0/b/planeador-eventos-47653.appspot.com/o/profileImages%2Fcocteles.jpeg?alt=media&token=44372ffe-8a7a-458f-a425-f2d63f08345a",
                  "rate_type": "Por persona",
                  "uuid": "18ac645a-9615-496c-925f-e20ac5d93b20"
                }
                ],
                "provider": "d011b895-0766-444a-9fa3-06075775b67d",
                "uuid": "a11acc47-dc69-48f8-ae9f-743d4fd1e643"
            }
        ],
        "start_time": "2021-12-15T00:00:00.00000000",
        "type": "Otro",
        "user": "a11d39d6-bdbd-4f08-92cd-0dce38ddbd27",
        "uuid": "f4924ac6-f31c-4a4b-bbdf-df3459b89980"
    }
    ]
);
