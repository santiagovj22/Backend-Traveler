"""2020-08-07 migration"""

name = "20200807_landmarks_collection"
dependencies = ['20200406_users_collection']


def upgrade(db):
    db.create_collection('landmarks')
    db.landmarks.insert([
        {
            "tourId": "5f068e0cd4e3ebcf661f8733",
            "landmarks": [
                {
                    "category": "marker",
                    "description": "El Parque Principal donde todos se juntan para charlar es un sitio muy concurrido y realmente hermosa la fuente que abarca toda la plaza, está situada en el centro de una gran represa alrededor encontrarás lugares para tomarse un café o simplemente disfrutar la vista de un bello atardecer con agradable clima, descubrir tiendas llenas de artesanías y otros negocios de abarrotes. Las construcciones a su alrededor son llamativas. Desde allí prestan el servicio de transporte de mototaxis y jeep para dirigirte a la piedra o al municipio del Peñol.",
                    "distance": 1.5,
                    "idMarker": 78214557,
                    "location": {
                        "latitude": "6.234260",
                        "longitude": "-75.161704"
                    },
                    "name": "Parque Principal",
                    "number": 1,
                    "resources": [
                        {
                            "name": "parque principal",
                            "type": "image",
                            "source": "https://i1.wp.com/elturismoencolombia.com/wp-content/uploads/2018/07/guatape-plaza-principal-colombia-travel.jpg?w=900&ssl=1"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Su construcción inicio en el año 2010. Se comenzó un proyecto el cual consistió en que cada de las personas se apropiaran más de las raíces de su pueblo, haciendo que se formaran convites en pro de la zocalizacion logrando que los Guatapenses día a día se fueran identificando más con los zócalos y los colores que engalanan esta región, mostrando en el frontis de sus hogares figuras que cuentan historia yendo desde el primer zocalo (el cordero)  hasta figuras que muestran la identidad de las familias.",
                    "distance": 2.5,
                    "idMarker": 78214558,
                    "location": {
                        "latitude": "6.233753",
                        "longitude": "-75.160320"
                    },
                    "name": "Plazoleta Zocalos",
                    "number": 2,
                    "resources": []
                },
                {
                    "category": "info circle",
                    "description": "El museo histórico de Guatapé esta ubicado en la calle del recuerdo. en el se da a conocer la historia del municipio. La apertura del museo abre otra perspectiva cultural a Guatapé, porque se enfoca también en la recuperación de la memoria y la cultura histórica del municipio. ",
                    "distance": 3.2,
                    "idMarker": 78214559,
                    "location": {
                        "latitude": "6.233364",
                        "longitude": "-75.160926"
                    },
                    "name": "Museo Historico Guatapé",
                    "number": 0,
                    "resources": []
                },
                {
                    "category": "marker",
                    "description": "La piedra de El Peñol es una masa granítica, compuesta por cuarzo, feldespato y mica, fue escalada por primera vez en 16 de julio de 1954 por un habitante de la zona, Luis Eduardo Villegas López. Hasta ahora la piedra sigue perteneciendo a la familia Villegas. Son 740 escalones que te llevan a la cima del imponente monolito Peñón de Guatapé o piedra del Peñol de 220 metros de altura, un sitio que por su singularidad se ha convertido en uno de los destinos imperdibles de Antioquia, para quienes desean conocer además de este atractivo, un auténtico pueblito paisa.",
                    "distance": 6.8,
                    "idMarker": 78214560,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Piedra el peñol",
                    "number": 3,
                    "resources": [
                        {
                            "name": "piedra del peñol",
                            "type": "image",
                            "source": "https://cr00.epimg.net/radio/imagenes/2019/03/14/medellin/1552578455_582628_1552578644_noticia_normal_recorte1.jpg"
                        },
                        {
                            "name": "piedra del peñol",
                            "type": "video",
                            "source": "https://www.youtube.com/embed/tVmQJMwqj5s"
                        }
                    ]
                }
            ]
        },
        {
            "tourId": "5f068e0cd4e3ebcf661f8741",
            "landmarks": [
                {
                    "category": "marker",
                    "description": "Caminando por nuestro sendero, a 10 minutos de la plazoleta central, frente a las cabañas de El Refugio, se encuentra la llamada Playa de Mármol, nombrada así por el majestuoso basamento de mármol milenario que constituye el fondo y la ribera del río. Aquí, la roca ha sido maravillosamente pulida por el constante trabajo del río a lo largo del tiempo. En este lugar se forma una amplia y profunda piscina, donde se puede apreciar claramente el fantástico lecho de este mármol. Es uno de los sitios preferidos por los visitantes para disfrutar un refrescante baño. Se toma conciencia del privilegio inusual de estar sumergido en aguas naturales, en un paraje único conformado por un bosque tropical sobre rocas kársticas milenarias.",
                    "distance": 1.5,
                    "idMarker": 88214557,
                    "location": {
                        "latitude": "6.234260",
                        "longitude": "-75.161704"
                    },
                    "name": "Playa de Mármol",
                    "number": 1,
                    "resources": [
                        {
                            "name": "playa de marmol",
                            "type": "image",
                            "source": "http://www.rioclaroreservanatural.com/wp-content/uploads/2016/01/marmol001.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Por el sendero, a 20 minutos de la plazoleta central, se encuentra una caverna fósil milenaria, fantásticamente oradada por múltiples precipitaciones geológicas que continuamente van formando estalactitas y estalagmitas. Estas configuraciones creadas por el agua y sus minerales; han tardado aproximadamente un millón de años en formarse. Este es un lugar se pueden percibir las texturas de la roca y dejar que la imaginación juegue hasta encontrar figuras como ‘el mamut’, que se descubre entre sombras y relieves, en un rincón este templo.",
                    "distance": 2.5,
                    "idMarker": 88214558,
                    "location": {
                        "latitude": "6.233753",
                        "longitude": "-75.160320"
                    },
                    "name": "Templo del Tiempo",
                    "number": 2,
                    "resources": [
                        {
                            "name": "templo del tiempo",
                            "type": "image",
                            "source": "http://www.rioclaroreservanatural.com/wp-content/uploads/2016/02/templo.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Lugar característico por sus gigantescas piedras marmóreas, talladas por el agua y ancladas quizás por un derrumbe geológico en medio del río. Megalitos que parecen emerger para dejarse moldear por la fuerza de las corrientes, y nos invitan a escuchar el dialogo que se establece entre ellas y el río. Este lugar recibe su nombre porque allí se encuentra la desembocadura de la quebrada “Las Dantas”. Se llega por un camino de trocha, a 60 minutos de la plazoleta central. Requiere un nivel de esfuerzo medio alto. ",
                    "distance": 3.2,
                    "idMarker": 88214559,
                    "location": {
                        "latitude": "6.233364",
                        "longitude": "-75.160926"
                    },
                    "name": "Las Dantas",
                    "number": 3,
                    "resources": [
                        {
                            "name": "las dantas",
                            "type": "image",
                            "source": "http://www.rioclaroreservanatural.com/wp-content/uploads/2015/12/rioclaro002.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Cavada por el río, en su vera encontramos esta majestuosa cornisa, bautizada “Boca Caimán”: hileras de estalactitas y estalagmitas parecen ser los dientes de un lagarto antediluviano. En este lugar se puede apreciar la real magnitud del cañón, patrimonio geológico del país. Se llega por un camino de trocha, a 50 minutos de la plazoleta central, y se requiere un nivel de esfuerzo medio alto.",
                    "distance": 6.8,
                    "idMarker": 88214560,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Boca Caimán",
                    "number": 4,
                    "resources": [
                        {
                            "name": "boca caiman",
                            "type": "image",
                            "source": "http://www.rioclaroreservanatural.com/wp-content/uploads/2016/01/boca001.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Por el sendero, a 40 minutos de la plazoleta central, se encuentra esta playa, delimitada por el paisaje exuberante del cañón de mármol labrado por el río, forrado por cortinajes de bosques y realzado por un manantial que marca el sitio de salida de la Caverna de mármol de ‘Los Guácharos’ y la quebrada Bornego (hasta aquí ciega escultora de la caverna), se derrama sobre el río Claro para festejar su encuentro con la luz. Aquí se encuentra un pozo profundo, donde también se puede gozar de un energizante baño en el río.",
                    "distance": 6.8,
                    "idMarker": 88214561,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Playa Manantial",
                    "number": 5,
                    "resources": [
                        {
                            "name": "playa manantial",
                            "type": "image",
                            "source": "http://www.rioclaroreservanatural.com/wp-content/uploads/2016/01/playa005.jpg"
                        }
                    ]
                },
            ]
        },
        {
            "tourId": "5f068e0cd4e3ebcf661f8734",
            "landmarks": [
                {
                    "category": "info circle",
                    "description": "Cuba destaca por la belleza de sus finas arenas blancas y aguas transparentes y, por supuesto, deberías conocer cuáles son las mejores playas. Está situada entre el mar Caribe y el Océano Atlántico, por eso no es casualidad que las playas de Cuba estén consideradas como las mejores del mundo. ",
                    "distance": 0,
                    "idMarker": 98214557,
                    "location": {
                        "latitude": "6.234260",
                        "longitude": "-75.161704"
                    },
                    "name": "Comencemos el viaje",
                    "number": 1,
                    "resources": []
                },
                {
                    "category": "marker",
                    "description": "Posiblemente la Playa de Varadero se encuentra entre las playas de Cuba más conocidas y demandadas en España. Situado en la península de Hicacos, en la provincia de Matanzas. Con 20 kilómetros de hermosa arena blanca en una de las mejores playas que alberga la isla, Varadero es una atracción turística en si misma. La excelente combinación de arena fina y blanca, además de sus aguas claras y trasparentes, entretenimiento nocturno, posibilidad de practicar deportes acuáticos, hace que creas en el paraíso.",
                    "distance": 6.5,
                    "idMarker": 98214558,
                    "location": {
                        "latitude": "6.233753",
                        "longitude": "-75.160320"
                    },
                    "name": "Playa Varadero",
                    "number": 1,
                    "resources": [
                        {
                            "name": "playa varadero",
                            "type": "image",
                            "source": "https://img.chavetas.es/albums/cuba08/playascuba02.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Para muchos es la playa más bonita de todo el Caribe cubano y no seríamos nosotros los que diríamos lo contrario. Arenas blancas, tonos azules y verdes dignos de fotografiar, preciosos atardeceres y que apenas está a 12 km de Trinidad. Y recalcamos la cercanía con Trinidad, porque Playa Ancón se puede combinar con una de las joyas arquitectónicas coloniales que alberga Cuba, declarada Patrimonio de la Humanidad por la UNESCO y que bien merece una visita (o una noche de fiesta) ",
                    "distance": 12,
                    "idMarker": 98214559,
                    "location": {
                        "latitude": "6.233364",
                        "longitude": "-75.160926"
                    },
                    "name": "Playa Ancón",
                    "number": 2,
                    "resources": [
                        {
                            "name": "playa ancon",
                            "type": "image",
                            "source": "https://img.chavetas.es/albums/cuba08/playascuba04.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Situado al noreste de Cuba, posee cerca de 13 km2 y se está convirtiendo cada vez más en un destino con muchos turistas, lo que le hace perder algo de autenticidad. Aún así, según los lugareños, la mejor playa de Cayo Guillermo es El Pilar, que ha sido visitada por numerosos novelistas estadounidenses, entre ellos el famoso novelista Ernest Hemingway. No es casualidad, los amantes de la naturaleza disfrutarán especialmente de su entorno. Grandes dunas de arena, que se elevan hasta los 16 metros sobre el nivel del mar, la más alta del Caribe y la mejor alternativa para disfrutar de una pesca en tierra firme, son algunos de sus atractivos principales. ",
                    "distance": 21.3,
                    "idMarker": 88214560,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Cayo Guillermo",
                    "number": 3,
                    "resources": [
                        {
                            "name": "cayo guillermo",
                            "type": "image",
                            "source": "https://img.chavetas.es/albums/cuba08/playascuba07.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "La mayor congregación de playas y enclaves privilegiados de Cuba que hemos disfrutado de esta lista. Playa Sirena o Playa Tortuga dan acceso a verdaderas piscinas naturales a una decena de privilegiados complejos que se han instalado en los últimos tiempos. Más de 20 km de arena blanca, aguas turquesa y hasta iguanas. ",
                    "distance": 36.8,
                    "idMarker": 88214561,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Playas de Cayo Largo, la piscina natural",
                    "number": 4,
                    "resources": [
                        {
                            "name": "playa cayo",
                            "type": "image",
                            "source": "http://www.rioclaroreservanatural.com/wp-content/uploads/2016/01/playa005.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Estamos en una isla ubicada en la Provincia de Holguín, conocida como la “ciudad de los parques”, donde encontraremos una de las mejoress playas de Cuba, la playa Holguín. Además el Cayo Saetía te da un valor añadido, la posibilidad de explorar la naturaleza tropical exótica además de practicar muchos deportes acuáticos, con lo que le estamos ante la combinación perfecta hermosas playas, naturaleza y un impresionante paisaje natural. Es también una alternativa económica que agradecerá cualquier bolsillo en una de las islas más exclusivas del Caribe. ",
                    "distance": 46.8,
                    "idMarker": 88214561,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Cayo Saetía para amantes de la naturaleza",
                    "number": 5,
                    "resources": [
                        {
                            "name": "cayo saetia",
                            "type": "image",
                            "source": "https://img.chavetas.es/albums/cuba08/playascuba10.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Se encuentra al norte de Camagüey [ver en mapa] y se extiende a lo largo de 21 kilómetros de longitud en una excelente playa de Cuba una gran variedad de patos migratorios, flamencos, coloridos peces tropicales y otras especies marinas, lo que lo hace un principal de interés en la zona. También es un lugar ideal para los amantes del buceo y observación marina, ya que es famosa por tener uno de los arrecifes de coral más importantes del mundo. Un dato.. Playa Santa Lucía, se ha convertido en uno de los destinos preferidos para recién casados a la hora de elegir unas vacaciones de luna de miel inolvidable.",
                    "distance": 46.8,
                    "idMarker": 88214561,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Playa Santa Lucía y su arrecife de coral",
                    "number": 6,
                    "resources": [
                        {
                            "name": "playa santa lucia",
                            "type": "image",
                            "source": "https://img.chavetas.es/albums/cuba08/playascuba13.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Ubicado en la zona norte de la occidental provincia de Pinar del Río en el archipiélago de los Colorados [ver en mapa], también llamado archipiélago de Santa Isabel, está sólo a 2h 30 por carretera de La Habana (y 30 más en ferry), contando con 3 kilómetros de excelentes playas, arena blanca, y sólo un hotel que consta de 40 habitaciones. Cayo Levisa es ideal si deseas estar alejado de las cadenas hoteleras. Además sólo es posible su ingreso mediante embarcaciones que salen de la costa norte de Pinar del Río y puede ser combinada con la zona de Viñales. ",
                    "distance": 68.9,
                    "idMarker": 88214561,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Cayo Levisa, ideal para el buceo",
                    "number": 7,
                    "resources": [
                        {
                            "name": "cayo levisa",
                            "type": "image",
                            "source": "https://img.chavetas.es/albums/cuba08/playascuba15.jpg"
                        }
                    ]
                },
            ]
        },
        {
            "tourId": "5f068e0cd4e3ebcf661f8735",
            "landmarks": [
                {
                    "category": "marker",
                    "description": "Una de las cinco principales plazas de La Habana, en la considerada “La Habana Vieja”. Destaca su arquitectura barroca, a la cual acompañan las edificaciones que la rodean, incluida la maravillosa catedral.",
                    "distance": 6.5,
                    "idMarker": 18214558,
                    "location": {
                        "latitude": "6.233753",
                        "longitude": "-75.160320"
                    },
                    "name": "Plaza de la Catedral",
                    "number": 1,
                    "resources": [
                        {
                            "name": "plaza de la catedral",
                            "type": "image",
                            "source": "https://viajarparacontar.com/wp-content/uploads/foto-2-768x427.jpg"
                        }
                    ]
                },
                {
                    "category": "info circle",
                    "description": "Sin duda, Cuba es un país que se disfruta nada más llegar, pero se necesita un largo proceso de maduración al terminar el viaje. Esto es debido a su potente y muy marcada personalidad y al espíritu de su gente. Como es lógico, su historia y actual situación gubernamental definen en muchos casos como es la vida de sus ciudadanos. No perdáis la oportunidad, siempre desde el respeto, de escuchar a todo aquel que os quiera contar como es la vida allí, algo que resulta sencillo dada la cordialidad y elocuencia de los cubanos. Con una buena charla pasaréis un rato muy agradable y aprenderéis mucho. Es muy recomendable viajar durante la estación seca, desde noviembre a abril, ya que las temperaturas serán un poco más suaves y sobre todo la humedad es menor (¡puede resultar mortal el calor unido a la humedad en verano!). ",
                    "distance": 0,
                    "idMarker": 18214557,
                    "location": {
                        "latitude": "6.234260",
                        "longitude": "-75.161704"
                    },
                    "name": "Conociendo Cuba",
                    "number": 0,
                    "resources": [
                        {
                            "name": "conociendo cuba",
                            "type": "image",
                            "source": "https://viajarparacontar.com/wp-content/uploads/foto-1-768x427.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Data de 1519, poco después de la fundación de la ciudad, siendo la más antigua de las plazas de La Habana. Aunque actualmente es sede de un mercado de libros de segunda mano, en el pasado era el centro administrativo de la ciudad. Destaca, una vez más, la arquitectura barroca y la gran cantidad de cafeterías, bares y negocios locales, lo que hace de ella un punto muy vivo de la ciudad. ",
                    "distance": 12,
                    "idMarker": 18214559,
                    "location": {
                        "latitude": "6.233364",
                        "longitude": "-75.160926"
                    },
                    "name": "Plaza de Armas",
                    "number": 2,
                    "resources": [
                        {
                            "name": "plaza de armas",
                            "type": "image",
                            "source": "https://viajarparacontar.com/wp-content/uploads/foto-3-768x427.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Ubicado en el imponente Palacio de los Capitanes Generales, en el lado oeste de la Plaza de Armas, es una visita obligada. Su gran patio central tiene una estatua, de mármol blanco, de Cristóbal Colón que data de 1862. Su interior también resulta interesante, ya que hay una gran cantidad de carruajes, mobiliario, uniformes militares… del siglo XIX, así como fotografías y documentación relativa a la historia de la ciudad. ",
                    "distance": 21.3,
                    "idMarker": 18214560,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Museo de la Ciudad",
                    "number": 3,
                    "resources": []
                },
                {
                    "category": "marker",
                    "description": "Este castillo es uno de los más antiguos de toda América. Se encuentra rodeado de un gran foso que lo separa de la Plaza de Armas y en el que hoy nos encontramos el Museo de la Navegación. En el interior de la fortaleza se encuentra el Museo de la Fortaleza, el cual refleja la vida del castillo a lo largo del tiempo a través de una gran maqueta y una colección de objetos datados a partir del siglo XVI. ",
                    "distance": 36.8,
                    "idMarker": 18214561,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Castillo de la Real Fuerza",
                    "number": 4,
                    "resources": []
                },
                {
                    "category": "marker",
                    "description": "Una plaza adoquinada de un modo irregular, imagen muy particular fruto de una reforma de los años 90. En su centro está la Fuente de los Leones de mármol blanco. También destaca la estatua de “El Caballero de París” un personaje popular de la ciudad, de la década de los 50, conocido por ir por la calle entreteniendo a los vecinos con sus historias y opiniones siempre con un tono extravagante pero entrañable.",
                    "distance": 46.8,
                    "idMarker": 18214561,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Plaza de San Francisco de Asís",
                    "number": 5,
                    "resources": [
                        {
                            "name": "plaza de san francisco de asis",
                            "type": "image",
                            "source": "https://viajarparacontar.com/wp-content/uploads/foto-4-768x427.jpg"
                        }
                    ]
                },
            ]
        },
        {
            "tourId": "5f068e0cd4e3ebcf661f8740",
            "landmarks": [
                {
                    "category": "marker",
                    "description": "Una de las experiencias turísticas que desde hace años se roba el corazón de colombianos y extranjeros es el avistamiento de ballenas jorobadas en El Pacífico. Y es que si bien Colombia es muy conocida por sus espectaculares playas en el mar Caribe, no hay que olvidar que el país es privilegiado por ser bañado por dos océanos, y en el Pacífico hay enormes tesoros que no te querrás perder. El impresionante espectáculo que ofrecen las ballenas jorobadas, que pueden tener hasta 16 metros de largo, transcurre entre los meses de julio y noviembre, cuando cientos de estos imponentes cetáceos arriban a las cálidas aguas colombianas para dar a luz a sus crías, culminando así un viaje que empieza ni más ni menos que en la Antártida. Dos de los mejores lugares para que vivas esta experiencia son Nuquí y Bahía Solano, destinos que se ubican en el departamento del Chocó.",
                    "distance": 6.5,
                    "idMarker": 2214558,
                    "location": {
                        "latitude": "6.233753",
                        "longitude": "-75.160320"
                    },
                    "name": "Contempla las hermosas ballenas jorobadas",
                    "number": 1,
                    "resources": [
                        {
                            "name": "plaza de la catedral",
                            "type": "image",
                            "source": "https://viajarparacontar.com/wp-content/uploads/foto-2-768x427.jpg"
                        }
                    ]
                },
                {
                    "category": "info circle",
                    "description": "El Parque Nacional Natural Utría es una especie de ‘sala de partos’ de las ballenas jorobadas, que allí están protegidas del oleaje del Pacífico en la ensenada de Utría. Su principal ecosistema es el de selva húmeda tropical, donde se encuentra una gran diversidad de fauna y flora. Allí es posible hacer senderismo submarino, acuático y terrestre, y observar ballenas entre julio y noviembre.",
                    "distance": 0,
                    "idMarker": 28214557,
                    "location": {
                        "latitude": "6.234260",
                        "longitude": "-75.161704"
                    },
                    "name": "Parque Nacional Utría",
                    "number": 0,
                    "resources": []
                },
                {
                    "category": "marker",
                    "description": "Manglares, árboles y cascadas conforman el paisaje que se aprecia cuando se percibe el contraste entre la frondosidad de la selva y la serenidad de las aguas del Pacífico, sobre la arena oscura de la ensenada del Parque Nacional Natural Utría y las playas del Golfo de Tribugá. En el Chocó también es posible practicar snorkel, bucear, montar en kayak y hacer caminatas.",
                    "distance": 12,
                    "idMarker": 28214559,
                    "location": {
                        "latitude": "6.233364",
                        "longitude": "-75.160926"
                    },
                    "name": "Entre manglares y el mar en Chocó",
                    "number": 2,
                    "resources": [
                        {
                            "name": "manglares choco",
                            "type": "image",
                            "source": "https://colombia.travel/sites/default/files/styles/super_banner/public/actividades/21entre_manglares_y_el_mar_en_choco.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Ornitólogos y turistas de todo el mundo llegan al Chocó con la esperanza de ver algunas de las 650 especies de aves que habitan en el Pacífico colombiano, y no se devuelven decepcionados. Un buen sitio para llevar a cabo esta actividad es la reserva natural de El Almejal, en Bahía Solano, que además de contar con varias especies endémicas es un corredor migratorio importante.",
                    "distance": 21.3,
                    "idMarker": 28214560,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Avistamiento de aves en Chocó",
                    "number": 3,
                    "resources": [
                        {
                            "name": "avistamiento aves choco",
                            "type": "image",
                            "source": "https://colombia.travel/sites/default/files/styles/imagen_650x450_escala_y_recorte/public/actividades/10Avistamiento-de-aves-en-Choco.jpg"
                        }
                    ]
                },
                {
                    "category": "info circle",
                    "description": "Probar platos auténticos de la gastronomía local, compartir su tiempo con las culturas nativas y afrodescendientes y aprender sobre sus costumbres es posible en el Chocó porque en este departamento se han creado programas que les permiten a los viajeros entrar en contacto con personas de comunidades como embera, waunana y tule.",
                    "distance": 46.8,
                    "idMarker": 28214561,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Etnoturismo en Chocó",
                    "number": 0,
                    "resources": [
                        {
                            "name": "etnoturismo choco",
                            "type": "image",
                            "source": "https://viajarparacontar.com/wp-content/uploads/foto-4-768x427.jpg"
                        }
                    ]
                },
            ]
        },
        {
            "tourId": "5f068e0cd4e3ebcf661f8743",
            "landmarks": [
                {
                    "category": "info circle",
                    "description": "Nuquí es selva y es mar. Playa, población y montañas hijas del Pacífico colombiano. Entre sus laberintos de roca en las playas, sus manglares fértiles y llenos de vida, y sus montes húmedos rebosantes de vida, se encuentran parajes paradisiacos para recorrer. Las poblaciones de Nuquí se caracterizan por ser pequeñas. Llenas de casitas de madera y de niños que corretean en medio de angostas calles por donde difícilmente pasa un carro, (sólo en la cabecera municipal, junto al aeropuerto, hay vehículos) es un área perfecta para encontrarse con lo que hace de Nuquí un lugar especial: su gente.",
                    "distance": 1.2,
                    "idMarker": 38214557,
                    "location": {
                        "latitude": "6.234260",
                        "longitude": "-75.161704"
                    },
                    "name": "Comencemos el viaje",
                    "number": 0,
                    "resources": []
                },
                {
                    "category": "marker",
                    "description": "Es el lugar para abastecerse antes de dirigirse al hotel en la playa. Ahí se consiguen las artesanías más representativas de la región, como vasijas y bandejas en wérregue, utensilios en totumo, y collares en Tagua.",
                    "distance": 6.5,
                    "idMarker": 38214558,
                    "location": {
                        "latitude": "6.233753",
                        "longitude": "-75.160320"
                    },
                    "name": "Nuquí, cabecera municipal",
                    "number": 1,
                    "resources": [
                        {
                            "name": "municipio nuqui",
                            "type": "image",
                            "source": "https://i.pinimg.com/originals/a0/37/59/a03759b1d809888e99968d90767cdcba.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Es una caminata de 20 minutos en medio de la selva junto al río. Bajo la caída de agua, hay un pozo de 2 metros de profundidad.",
                    "distance": 2.5,
                    "idMarker": 38214559,
                    "location": {
                        "latitude": "6.233364",
                        "longitude": "-75.160926"
                    },
                    "name": "Cascada del Amor",
                    "number": 2,
                    "resources": [
                        {
                            "name": "cascada del amor",
                            "type": "image",
                            "source": "https://elturismoencolombia.com/wp-content/uploads/2018/10/nuqui_cascada_amor_choco_turismo_colombia_travel.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Frente a una playa sin límites, se encuentra una población que lleva dicho nombre. En una caminata de 5 minutos hacia el interior del pueblito, se llega a un yacimiento natura de aguas termales de color turquesa, ideal para tomar un baño relajante.",
                    "distance": 21.3,
                    "idMarker": 38214560,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Los Termales",
                    "number": 3,
                    "resources": [
                        {
                            "name": "termales",
                            "type": "image",
                            "source": "https://www.andando.co/andando/img/1553707534311/1555609840231-1535702665497Termales4.jpg"
                        }
                    ]
                },
            ]
        },
        {
            "tourId": "5f068e0cd4e3ebcf661f8732",
            "landmarks": [
                {
                    "category": "info circle",
                    "description": "Palabra quechua cuya traducción es “Puente del inca”. Por tanto ese lugar es una parte del camino que los incas utilizaban en el sector tropical, lo mismo que las laderas de los cerros y algunas planicies. Ubicado a 88 km de Cochabamba, Incachaca se encuentra en la zona de transición entre los andes y el trópico. El clima generalmente cálido y húmedo da lugar a una exuberante vegetación que alberga una gran variedad de flora y fauna. Incachaca se destaca por su belleza natural con impresionantes cascadas y pozas de aguas cristalinas.",
                    "distance": 1.2,
                    "idMarker": 48214557,
                    "location": {
                        "latitude": "6.234260",
                        "longitude": "-75.161704"
                    },
                    "name": "Puente del Inca",
                    "number": 0,
                    "resources": [
                        {
                            "name": "puente de los incas",
                            "type": "image",
                            "source": "https://www.lostiempos.com/sites/default/files/styles/noticia_detalle/public/media_imagen/2017/6/3/4_b_1_lopezzzzzzz.jpg?itok=tSfGxNb9"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Antes de llegar al lugar, normalmente se pasa por el Parque Ecoturístico San Isidro, que pertenece al   municipio de Sacaba y es parte del tour por Incachaca. Esta zona es conocida por el templo que lleva el mismo nombre, un patrimonio que data de hace un siglo y es el centro de la Festividad de San Isidro Labrador, el patrono de la producción agrícola. Además, cuenta con un barco pirata a las orillas de la laguna donde la gente aprovecha para tomar fotos. Según explica Gregorio Cusicanqui, guardabosques del lugar, en el parque se puede realizar camping y diferentes eventos como cumpleaños, sin costo alguno. Actualmente, trabajan en la implementación de actividades como la tirolesa y el rápel para convertir la zona en un destino turístico para pasar un fin de semana divertido en familia y amigos.",
                    "distance": 40.5,
                    "idMarker": 48214558,
                    "location": {
                        "latitude": "6.233753",
                        "longitude": "-75.160320"
                    },
                    "name": "San Isidro, parte del recorrido",
                    "number": 1,
                    "resources": [
                        {
                            "name": "barco mirador",
                            "type": "image",
                            "source": "https://sacaba.gob.bo/images/wsacaba/turismo/isidro/san-isidro-sacaba6.jpg"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Ubicado a 80 kilómetros de la ciudad de Cochabamba, en el municipio de Colomi, Incachaca se encuentra          en la zona de transición entre los Andes y el Trópico “Puente del Inca” es la traducción que se hizo del quechua al español. Se cree que ese lugar era parte del camino que recorrían los incas por la zona tropical de Bolivia, al igual que las laderas y planicies cercanas. Al ser un sitio arqueológico existen varios fuertes, puentes y escalones que quedaron como ruinas de aquel tiempo Incachaca posee un clima cálido húmedo, con temperaturas que varían desde los 16 grados centígrados hasta los 30. La neblina es parte de la decoración natural del paisaje. Las lluvias en el lugar son constantes por lo que se recomienda llevar varios cambios de ropa para disfrutar la estadía. Para aquellos aficionados por las áreas verdes y la historia nacional, Incachaca es la ruta perfecta.",
                    "distance": 55,
                    "idMarker": 48214559,
                    "location": {
                        "latitude": "6.233364",
                        "longitude": "-75.160926"
                    },
                    "name": "El Camino de los Incas",
                    "number": 2,
                    "resources": []
                },
                {
                    "category": "marker",
                    "description": "Una vez que se culmina el paseo por San Isidro, se sigue por la carretera al oriente del país hasta llegar al kilómetro 93, donde se desvía cinco kilómetros por un camino secundario de ripio hasta llegar a las puertas del parque. La ruta principal por Incachaca tiene ocho puntos centrales distribuidos en unos dos kilómetros de distancia. El primero es la laguna artificial que está rodeada de bosques naturales de pinos y árboles endémicos de la zona, además de una gran presencia de aves rapaces. En el lugar se practica tirolesa, paseo a caballo y canotaje. También tiene áreas para hacer camping y actividades de recreación familiar. Luego, se retorna la entrada la comunidad donde está el sendero para iniciar el recorrido. Los caminos son angostos, pedregosos y rodeados de maleza. Una vez que comienza el descenso, la primera parada es el Velo de la Novia, una cascada de aguas cristalinas que lleva ese nombre por la blancura de su corriente. El sonido de su caída es estrepitoso  y llama la atención de los visitantes. Luego, siguiendo el camino, se llega a la Casa de Máquinas, la primera hidroeléctrica de Bolivia que data de 1940 y fue mandada a construir por Simón I. Patiño. La imponente estructura está hecha de piedra y conserva en su interior diferentes máquinas de hierro que muestran cómo se trabajaba en el pasado para generar energía eléctrica. Volviendo a la ruta principal se llega a la Ventana del Diablo, una formación rocosa que da lugar a un mirador desde donde se observa la Garganta del Diablo, una cascada que desciende por unas rocas en forma de circular simulando una garganta. Ambas fueron bautizadas así por los comunarios de la zona. Finalmente, se llega al Baño de las Ñustas que es parte del río Incachaca. Este lugar posee aguas cristalinas a bajas temperaturas. Las plantas aledañas decoran el paisaje. Se dice que la zona lleva ese nombre porque era donde las mujeres de los incas se bañaban debido a la pureza de sus aguas.",
                    "distance": 93,
                    "idMarker": 38214560,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "El Sendero Natural",
                    "number": 3,
                    "resources": [
                        {
                            "name": "sendero natural",
                            "type": "image",
                            "source": "https://i1.wp.com/elcalderoviajero.com/wp-content/uploads/2018/04/bolivia-cochabamba-incachaca-17.jpg?w=750&ssl=1"
                        }
                    ]
                },
                {
                    "category": "marker",
                    "description": "Una vez que finaliza el sendero por Incachaca, la última parada reglamentaria antes de volver a Cochabamba es el Criadero de Truchas Paraíso. Este lugar posee un circuito de filtración de agua que pasa por varias piscinas que albergan cientos de truchas de todo tamaño. Además, el Paraíso es un restaurante que vende este pez hecho a la plancha y en chicharrón, una delicia culinaria infaltable para degustar. La garantía del criadero es la frescura de sus pescados y el buen sabor de cada platillo. El restaurante está en medio del bosque de la zona, por lo que ofrece una vista de la naturaleza llena de árboles, agua y neblina.",
                    "distance": 93,
                    "idMarker": 48214860,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "Criadero de Truchas",
                    "number": 4,
                    "resources": [
                        {
                            "name": "sendero natural",
                            "type": "image",
                            "source": "https://i1.wp.com/elcalderoviajero.com/wp-content/uploads/2018/04/bolivia-cochabamba-incachaca-17.jpg?w=750&ssl=1"
                        }
                    ]
                },
                {
                    "category": "info circle",
                    "description": "El enfoque principal de esta zona es manejar un turismo comunitario. Allí habitan 50 familias del Sindicato Agrario de Incachaca, quienes son los encargados de administrar el lugar, que, dicho sea, se halla protegido por la  Ley 2410/2003 y la ordenanza 25/2003.3. Además, Incachaca fue declarado Patrimonio Cultural de Bolivia el año 2003 durante la presidencia de Carlos Mesa. Aunque la zona conserva su belleza natural, varios comunarios fueron alertando sobre la intensificación de la depredación y deforestación del lugar debido a varios factores, entre los que saltan a la vista la construcción  de casas. Más allá de este hecho, se ha convertido en un destino turístico de gran belleza y singularidad. Tanto así que cada vez más empresas se animan a crear tours para visitar el lugar, ofreciendo el servicio completo que implica el recorrido",
                    "distance": 93,
                    "idMarker": 48214890,
                    "location": {
                        "latitude": "6.220566",
                        "longitude": "-75.179353"
                    },
                    "name": "El Patrimonio Cultural crece",
                    "number": 0,
                    "resources": []
                },
            ]
        },
    ])


def downgrade():
    pass
