"""2020-11-05 migration"""

name = "20201105_initial"
dependencies = []


def upgrade(db):
    db.create_collection('test')
    db.tours.insert([
        {
            "image": "https://boliviamia.net/Images/Attractionphotos/atop-deathroad-01.jpg",
            "title": "El mejor recorrido en Bici hasta Incachaca",
            "brief": "Hermoso paisaje tienes la oportunidad de hacer actividades variadas desde un vertiginoso descenso",
            "description": "Cochabamba es una ciudad boliviana, capital del departamento homónimo y de la provincia de Cercado. Se encuentra situada en el centro del país, en el valle del mismo nombre.Tiene una población de 1 113 474 habitantes en el área metropolitana (Censo 2012)1​ y pertenece a la Región metropolitana de Kanata junto a los municipios de Sacaba, Quillacollo, Colcapirhua, Tiquipaya, Vinto y Sipe Sipe.Cochabamba se encuentra en un valle de tierra fértil y productiva a 2558 m de altura. La ciudad, rodeada por campos de cultivos y valiosos vestigios preincaicos e incaicos, conserva su personalidad virreinal.",
            "duration": "1 hour",
            "transportType": "Car",
            "location": "Cochabamba",
            "rating": 4.59,
            "ratingCount": 233
        },
        {
            "image": "https://i.ytimg.com/vi/C7-N9Kc9lEc/maxresdefault.jpg",
            "title": "Camino a la piedra de Guatapé",
            "brief": "Conoce la historia del Peñol de Guatapé, todas las anécdotas mientras viajas a la piedra.",
            "description": "Son 740 escalones que te llevan a la cima del imponente monolito Peñón de Guatapé o piedra del Peñol de 220 metros de altura, un sitio que por su singularidad se ha convertido en uno de los destinos imperdibles de Antioquia, para quienes desean conocer además de este atractivo, un auténtico pueblito paisa. Este atractivo se encuentra ubicado entre el Peñol y Guatapé, un lugar estratégico para quienes suben a su cumbre, ya que logran obtener la mejor panorámica de la región y del embalse de más de 2 200 hectáreas de extensión, que conforman un paisaje de varios lagos, color verde esmeralda, que surcan diversas montañas e islas. Pero antes de que subas y si eres curioso, encontrarás escrita la historia y datos relevantes de esta roca y durante el ascenso vas a poder saber en qué escalón te encuentras, porque todos están enumerados",
            "duration": "2 hours",
            "transportType": "Car",
            "location": "Guatapé",
            "rating": 4.8,
            "ratingCount": 234
        },
        {
            "image": "https://webimages.trailfinders.com/image/fetch/dpr_auto,q_auto,f_auto,w_960,c_limit/https://images.trailfinders.com/asset/196de2/TF1666529/bigstock-HAVANA-CUBA-APRIL-------126913997_960x960.jpg",
            "title": "Historia de las playas de Bahia a pie",
            "brief": "Hace 50 años unos 1.500 exiliados cubanos entrenados y financiados por la CIA",
            "description": "Situado en el Archipiélago de Tinharé, a 240 Km de Salvador, la capital de Bahía, Ilha de Boipeba fue elegida por Trip Advisor en 2013 como la segunda mejor isla en América del Sur. La Isla de Boipeba es el hogar de una densa selva atlántica, con marismas, dunas y extensos manglares, y con frondosos cocoteros enmarcando las playas. Hay muchas playas hermosas en Boipeba, pero Moreré no sólo es la más bella de la isla, sino de toda Bahia. Famosa por sus claras piscinas de aguas calientes cristalinas y arrecifes de coral, Praia de Moreré es perfecta para bucear y nadar. Hay muchas piscinas en esta playa, pero las mejores se encuentran en alto mar y sólo se puede accederlas en barco durante la marea baja.",
            "duration": "3 hours",
            "transportType": "Street View",
            "location": "Bahia",
            "rating": 4.49,
            "ratingCount": 234
        },
        {
            "image": "https://www.afd.fr/sites/afd/files/styles/visuel_principal/public/2018-12-03-13-21/cuba-la-havane-rue-pedro-szekely-flickr.jpg?itok=QUVxvTZJ",
            "title": "Cuba en bus, conociendo la Revolución Cubana",
            "brief": "Conoce los mejores de Cuba y la verdadera vida de los cubanos sigue esta ruta.",
            "description": "A partir de la fundación de la Villa de San Cristóbal de La Habana en el año 1519, se dice que los agasajos fundacionales coincidían con los de Santiago Apóstol el 25 de julio, por lo que el Obispo no podía asistir a las celebraciones de La Habana. Un buen día, no determinado, la ciudad jó sus festejos para el 16 de noviembre, y por fuerza de la tradición, los habaneros acuden al Templete, sitio fundacional, para darle tres vueltas a una legendaria ceiba y pedir igual número de deseos al santo patrono.",
            "duration": "2 hours",
            "transportType": "Bus",
            "location": "Bahia",
            "rating": 4.59,
            "ratingCount": 234
        },
        {
            "image": "https://cdn.semanariolacalle.com/2018/10/bogota_eje_cafetero_cartagena-1024x683.jpg",
            "title": "Ruta del tintico, lo mejor del café de Colombia",
            "brief": "Paisaje de montañas, cafetales, guayacanes, yarumos, guaduales y platanales, así es Colombia",
            "description": "En Cultor solo sirven cafés 100 % sostenibles. Eso quiere decir que hacen todo un estudio del origen, los cultivadores, el mercado y las condiciones medioambientales en las que crece la mata. La idea es que usted vaya, se ‘culturice‘ —ya va siendo hora— y deje que le echen el cuento que hay detrás del producto que escoja, pues cada café está bautizado con el nombre de la persona que lo sembró. En esta casa se toma el tintico —literalmente— recién hecho, pues la gente de Varietale cuenta con su propia tostadora. Le ofrecen cafés de origen de Santander, Huila, Nariño, la Sierra Nevada de Santa Marta... y nueve métodos de filtrado (tranquilo que allá le explican las propiedades de cada uno). Si le gusta mucho el café, inscríbase en los talleres quincenales que organizan para entusiastas; si no, vaya también, pues la carta tiene 20 variedades de té.",
            "duration": "3 hours",
            "transportType": "Car",
            "location": "Eje Cafetero",
            "rating": 4.16,
            "ratingCount": 234
        },
        {
            "image": "https://blogapi.uber.com/wp-content/uploads/2018/05/BO_Disfruta-de-la-noche-en-estos-X-boliches-de-La-Paz.jpg",
            "title": "Tour de Boliches en la Ciudad Maravilla",
            "brief": "Como toda ciudad con una vida nocturna “que se respeta,” La Paz cuenta con su propio bar irlandés.",
            "description": "También ubicado en la misma zona de Sopocachi, desde hace más de 25 años Equinoccio es sinónimo de rock boliviano y un símbolo de la vida nocturna de La Paz. Algunas de las mejores bandas, tanto locales como de otras latitudes de Bolivia, han pasado por el escenario del Equi. Es un lugar en el que los amantes del rock se sienten siempre como en casa.",
            "duration": "2 hours",
            "transportType": "Bus",
            "location": "La Paz",
            "rating": 4.69,
            "ratingCount": 234
        },
        {
            "image": "https://www.renfe-sncf.com/es-es/blog/PublishingImages/paris-en-bici-capital/paris_en_bici_capital.jpg",
            "title": "Conoce París en Bici",
            "brief": "Ahora puedes escoger la bicicleta como compañera de viaje para conocer París",
            "description": "París es una ciudad que parece diseñada para el disfrute del viajero. Sus calles, plazas, edificios, jardines y monumentos parecen ideados para que cualquier persona que visite París desee volver. Visitar la Torre Eiffel, el Arco del Triunfo o la Catedral de Notre Dame, acudir a un espectáculo de cabaret en el mítico Moulin Rouge, o bien pasear por algunos de los barrios más pintorescos de la ciudad como Montmartre o Montparnasse, son algunas de las experiencias que todo el mundo debería tener la ocasión de disfrutar.",
            "duration": "3 hours",
            "transportType": "Bicycle",
            "location": "Paris",
            "rating": 4.69,
            "ratingCount": 234
        },
        {
            "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Metro_de_Medell%C3%ADn%2C_Colombia.jpg/1200px-Metro_de_Medell%C3%ADn%2C_Colombia.jpg",
            "title": "Recorre Medellin en Metro y conoce su historia",
            "brief": "El Metro de Medellín es un sistema de transporte masivo que sirve directamente no sólo a Medellin",
            "description": "Medellín es una ciudad cautivadora, no solo por su clima agradable (ronda los 24 °C durante todo el año); también por la amabilidad de su gente, su deliciosa comida y ese encanto paisa que enamora a los visitantes. El humor campesino de los habitantes de Medellín, que se refleja en las trovas antioqueñas, los bailes típicos y en general en la cultura paisa, se mezcla con la vida agitada de la metrópoli. No hay montañas ni ríos que puedan amilanar a estas personas, quienes tienen uno de los territorios más prolíficos del país, con grandes empresas y crecimiento en todos los sectores. De hecho, el ingen io es una característica de los antioqueños, por lo que no es extraño que en 2013 Medellín haya sido nombrada la Ciudad más Innovadora del Mundo en el concurso City of the Year del Wall Street Journal. ",
            "duration": "3 hours",
            "transportType": "Train",
            "location": "Medellin",
            "rating": 4.2,
            "ratingCount": 234
        },
        {
            "image": "https://lp-cms-production.imgix.net/2019-06/GettyImages-184886622_medium.jpg?fit=crop&q=40&sharp=10&vib=20&auto=format&ixlib=react-8.6.4",
            "title": "Recorre parque tayrona y disfruta sus playas",
            "brief": "Es considerado un Santuario de la Naturaleza por lo rico en fauna y flora y hace parte de la Sierra Nevada de Santa Marta.",
            "description": "Las estribaciones de la Sierra Nevada de Santa Marta, la montaña costera más alta del mundo, se hunden en el mar como los dedos de una mano gigantesca entre los que se forman bahías y ensenadas de belleza singular: Chengue, Gayraca, Cinto, Neguanje, Concha, Guachaquita, con sus playas de arenas blancas delimitadas por, manglares, matorrales o bosques, y bañadas todas por las aguas cristalinas del mar Caribe, hacen parte de los muchos atractivos que ofrece el Parque Nacional Natural Tayrona. Para quienes buscan la contemplación y el descanso, el Parque ofrece magníficas playas y el relajante panorama de un mar intensamente azul. Quienes se sienten atraídos por actividades más emocionantes podrán disfrutar de caminatas, careteo y buceo autónomo.",
            "duration": "2 hours",
            "transportType": "Bus",
            "location": "Tayrona",
            "rating": 4.7,
            "ratingCount": 379.0
        },
        {
            "image": "https://rtvc-assets-radionacional-v2.s3.amazonaws.com/s3fs-public/senalradio/articulo-noticia/galeriaimagen/valle_del_cocora_salento_quindio_consulta_minera_0.jpg",
            "title": "Salento tierra amable",
            "brief": "Salento es sin duda alguna y con permiso de los otros municipios, el más importante en lo que a turismo en el departamento del Quindío",
            "description": "Salento es un lindo pueblo de Colombia ubicado en el departamento del Quindío. Un pequeño lugar de casas coloridas que reflejan la pujanza del Eje cafetero y la belleza del Valle del Cocora. Salento es el típico pueblo cafetero de gente amable y calles coloridas. Un pequeño lugar considerado el «Municipio Padre del Quindío», por ser el más antiguo de los tres departamentos que conforman el Eje cafetero. Salento está a 1.895 metros sobre el nivel del mar, su clima es templado y su temperatura promedio suele ubicarse entre los 20°C y 10°C. En Salento encontrarás una variada oferta de hospedajes, hoteles de lujo, hostales, zonas de acampar y glampings en medio de la naturaleza.",
            "duration": "2 hours",
            "transportType": "Bus",
            "location": "Salento",
            "rating": 4.5,
            "ratingCount": 381.0
        },
        {
            "image": "https://www.ecured.cu/images/0/02/Parque_nacional_tuparro.jpg",
            "title": "Parque Nacional Natural El Tuparro",
            "brief": "El parque nacional natural El Tuparro se encuentra ubicado en la Orinoquía en Colombia. Su superficie hace parte del departamento de Vichada.",
            "description": "El Parque Nacional Natural El Tuparro es una reserva natural de gran extensión en el departamento de Vichada que ofrece al visitante hermosos ríos, gran variedad de vegetación, la posibilidad de ver jaguares, tapires y animales de la región, además de cientos de especies de aves. Sobresalen los \tRaudales de Maipures sobre el Río Orinoco y en la desembocadura del Río Tuparro. El cauce del Orinoco se estrecha por esta zona y su corriente fluye estruendosamente entre rocas gigantes que se extienden hasta 5 km.",
            "duration": "4 hours",
            "transportType": "Bus",
            "location": "Vichada",
            "rating": 4.3,
            "ratingCount": 361.0
        },
        {
            "image": "https://caribeconforthostal.com/wp-content/uploads/2019/11/tour-a-punta-gallinas-desde-santa-marta.jpg",
            "title": "Punta Gallinas",
            "brief": "Visitar el extremo norte del país y del continente suramericano es una experiencia inigualable.",
            "description": "La punta Gallinas es el extremo más septentrional de la placa continental de América del Sur, ubicada al extremo norte de la península de La Guajira, en el departamento homónimo de la República de Colombia, sobre las aguas meridionales del mar Caribe. Se trata de un extremo de tierra que se adentra en dirección noroeste al mar y que cierra un conjunto de accidentes que conforman una bahía de la península que va desde punta Gallinas hasta el cabo de la Vela o Jepirra (en wayúu).",
            "duration": "3 hours",
            "transportType": "Bus",
            "location": "La Guajira",
            "rating": 4.4,
            "ratingCount": 386.0
        },
        {
            "image": "https://cdnuploads.aa.com.tr/uploads/Contents/2017/09/28/thumbs_b_c_b7cdd7b91b9a6f9bd8443426f43e127e.jpg?v=015116",
            "title": "Caño Cristales",
            "brief": "Caño Cristales (La Macarena, Meta, Colombia) es considerado por muchos como el “Río más Hermoso del Mundo”.",
            "description": "Ubicado en la sierra de la Macarena en el Meta, se encuentra Caño Cristales, llamado por muchos portales de turismo a nivel internacional como el “río más hermoso del mundo”. Esto es debido a los diversos colores que se pueden observar en el fondo gracias a la presencia de plantas acuáticas que le dan esas tonalidades característica. En la Serranía de la Macarena son muchas las corrientes de agua que se pueden encontrar. Sin embargo, ninguna es tan majestuosa como Caño Cristales, espacio que ni siquiera se puede comparar con algún lugar por sus características. ",
            "duration": "3 hours",
            "transportType": "Bus",
            "location": "Meta",
            "rating": 4.4,
            "ratingCount": 386.0
        },
        {
            "image": "https://m.eltiempo.com/files/image_640_428/uploads/2018/10/03/5bb522c3aa254.jpeg",
            "title": "Desierto de la Tatacoa",
            "brief": "Estar en el desierto de la Tatacoa es una experiencia inolvidable. A pocas horas de Neiva.",
            "description": "El Desierto de la Tatacoa es la segunda zona árida más extensa de Colombia después de la Península de La Guajira. Es uno de los escenarios naturales más atractivos de Colombia, de tierra de color ocre y gris con pincelazos del verde de los cactus. La Tatacoa o el Valle de las Tristezas, como lo llamó en 1538 el conquistador Gonzalo Jiménez de Quesada, por los rastros de deterioro que notó en su territorio, no es justamente un desierto, sino un bosque seco tropical. Su nombre “Tatacoa” también se lo atribuyeron los españoles, refiriéndose a la serpiente cascabel y no, como se podría pensar, a las culebras inofensivas de color negro. Como lo revelan los científicos, La Tatacoa, durante el Período terciario, fue un jardín con miles de flores y árboles que poco a poco se fue secando hasta convertirse en un desierto.",
            "duration": "5 hours",
            "transportType": "Bus",
            "location": "Huila",
            "rating": 4.1,
            "ratingCount": 356.0
        },
        {
            "image": "https://fincaenmanizales.files.wordpress.com/2016/05/utria-parquesnacionales-choco-altomira.jpg?w=863&h=1&crop=1",
            "title": "Parque Nacional Natural Utría",
            "brief": "Una de las experiencias más increíbles para los amantes del ecoturismo es la posibilidad de ver ballenas jorobadas",
            "description": "Con el fin de ofrecer una mejor experiencia al visitante durante su estadía en el Parque Nacional Natural Utría, varias entidades, alcaldías de la zona, consejos comunitarios y las comunidades aunaron esfuerzos para mejorar la infraestructura y dotar de nuevos espacios para la educación ambiental y el ecoturismo en esta área protegida. En un evento que contó con la participación del Viceministerio de Turismo y Parques Nacionales de Colombia, se inauguró el Sendero Estero Grande y el Auditorio del Parque, para ofrecer espacios de educación y sensibilización a los visitantes.",
            "duration": "2 hours",
            "transportType": "Bus",
            "location": "Choco",
            "rating": 4.2,
            "ratingCount": 268.0
        },
        {
            "image": "https://www.elespectador.com/resizer/_GceCGshRrOr1kNrKup-XUPsJLs=/657x431/arc-anglerfish-arc2-prod-elespectador.s3.amazonaws.com/public/IKTOHOOZJZGJLLCQMABUTZNEVY.jpg",
            "title": "Disfruta de la Reserva Río Claro y sus cristalinas aguas",
            "brief": "A tres horas de la capital antioqueña se encuentra Río Claro, una hermosa reserva donde se observa el paso del río en medio de un cañón.",
            "description": "El río Claro nace en la parte alta del municipio de Sonsón, en las montañas del alto del Tigre y de la Osa, a 40 Kms de distancia de la Reserva. Durante su recorrido se suma al cuadal del río Cocorná, hasta desembocar en el río Magdalena a 57Kms de la Reserva. Visitar Río Claro, es un plan imperdible si estás en Bogotá o Medellín, o si vas de una ciudad a otra, en este lugar puedes hacer una parada de la cual no te vas a arrepentir, pues a pesar de lo increíble que es, encontrar un lugar selvático en medio de Bogotá y Medellín, la Reserva Natural Río Claro es uno de los ríos más bonitos de Colombia, después de Caño Cristales.",
            "duration": "3 hours",
            "transportType": "Car",
            "location": "Antioquia",
            "rating": 3.7,
            "ratingCount": 341.0
        },
        {
            "image": "https://i1.wp.com/padondenosvamos.com/wp-content/uploads/2017/10/Playa-El-Rodadero.jpg?resize=768%2C422&ssl=1",
            "title": "Playa El Rodadero",
            "brief": "La playa de El Rodadero se ubica aproximadamente a 8 km de la ciudad de Santa Marta.",
            "description": "Es uno de los lugares turísticos de Colombia más populares y no solo de Colombia sino  del Caribe. Sus aguas y arena blanca son propicias para practicar todo tipo de deportes acuáticos. Además, cuenta con una gran variedad de alojamientos. En las noches también es un lugar turístico excelente por la calidad de sus tiendas, bares, discotecas y ambiente festivo. El Rodadero es un balneario de la ciudad de Santa Marta, a orillas del mar Caribe en Colombia. Se encuentra en la comuna de Gaira - Rodadero.",
            "duration": "1 hours",
            "transportType": "Car",
            "location": "Santa Marta",
            "rating": 4.2,
            "ratingCount": 359.0
        },
        {
            "image": "https://i1.wp.com/padondenosvamos.com/wp-content/uploads/2017/10/Nuqu%C3%AD.jpg?resize=768%2C576&ssl=1",
            "title": "Nuquí, naturaleza exótica y relajante donde aislarte",
            "brief": "Es un municipio ubicado a 120 kilómetros de la capital del Departamento de Chocó.",
            "description": "Sus playas hermosas y su clima cálido hacen que este sea uno de los lugares turísticos de Colombia más visitados en la región del pacifico. Si te gusta la aventura aquí podrás hacer buceo autónomo y a pulmón, pesca deportiva (de mayo a junio), pesca artesanal, canotaje, kayak y surf. Nuquí fue inicialmente un corregimiento de El Valle. Con la llegada de don Roberto Walt y su matrimonio con la niquiseña Olimpia Moreno, se inicia el proceso de crecimiento de Nuquí. Roberto Walt fue nombrado alcalde de El Valle, y es entonces cuando se dirige al intendente Jorge Valencia Lozano, a quien le expresa que aceptaría el cargo sólo si se trasladaba la cabecera municipal a Nuquí, la tierra de su esposa. La petición fue aceptada, y el traslado fue efectuado en 1915.",
            "duration": "1 hours",
            "transportType": "Car",
            "location": "Choco",
            "rating": 4.0,
            "ratingCount": 322.0
        }

    ])


def downgrade():
    pass
