// import React, { useState, useEffect } from "react";
// import"./Home.css"
// import { Card, Icon, Image } from 'semantic-ui-react'
// import { Carousel } from 'react-responsive-carousel'
// import "react-responsive-carousel/lib/styles/carousel.min.css";
// import axios from 'axios'

// const Carrousel = () => {

//   const [tours,setTours] = useState([])
//   async function fetchData(){
    
//     const res = await axios.get('http://localhost:8000/api/v1/tours')
//     setTours(res.data)
//   }
//   useEffect(() => {
//     fetchData()
//   },[])

//   return(
//   <div id="carrousel">
//     <Carousel>
//         {tours.map((tour) => (
//                 <div className="hola">
//                   <Card id="tour-pack" extra={false}>
//                        <Image src={tour.image_tour}  id="image_tour"/>
//                       <Card.Content className="contenido" extra={false}>
//                           <Card.Header>{tour.tour_title}</Card.Header>
//                       <Card.Description>
//                           {tour.short_description}
//                       </Card.Description>
//                       </Card.Content>
//                       <Card.Content extra>
//                         <a>
//                           <Icon name='map marker' />
//                           {tour.location}
//                         </a>
//                       </Card.Content>
//                     </Card>
//                 </div>
//         ))}
//         </Carousel>
//         </div>
//   )
//   }
// export default Carrousel;